"""Finite channel calculations for the shared Fock-battery interface.

These routines evaluate finite models. Universal converse and asymptotic
statements are proved in science/, not inferred from this code.
"""
from __future__ import annotations

import math
import numpy as np
from scipy.optimize import minimize
from scipy.sparse import coo_matrix, csr_matrix, eye, kron
from scipy.sparse.linalg import expm_multiply
from scipy.stats import binom, poisson


def affinity_matrix(n: int, N: int, eta: float) -> np.ndarray:
    """Full finite binomial sum, without count truncation."""
    if not (N >= n >= 1 and 0 < eta < 1):
        raise ValueError("Require N >= n >= 1 and 0 < eta < 1")
    m = N - np.arange(n + 1)
    counts = np.arange(N + 1)
    amplitudes = np.exp(0.5 * binom.logpmf(counts[None, :], m[:, None], 1 - eta))
    return amplitudes @ amplitudes.T


def passive_optimum(B: np.ndarray) -> dict:
    """Convex simplex minimization, with a supporting-plane gap certificate."""
    size = B.shape[0]
    result = minimize(
        lambda u: float(u @ B @ u), np.full(size, 1 / size),
        jac=lambda u: 2 * B @ u, method="SLSQP",
        bounds=[(0, 1)] * size,
        constraints=[{"type": "eq", "fun": lambda u: u.sum() - 1,
                      "jac": lambda u: np.ones_like(u)}],
        options={"ftol": 1e-13, "maxiter": 2000},
    )
    if not result.success:
        raise RuntimeError(result.message)
    u = np.maximum(result.x, 0)
    u /= u.sum()
    # SLSQP's objective stopping rule can leave a visible first-order gap.
    # Solve the equality-constrained problem on its active support, then
    # retain the polish only when it is feasible and does not raise the cost.
    support = np.flatnonzero(u > 1e-8)
    block = B[np.ix_(support, support)]
    kkt = np.block([[block, np.ones((len(support), 1))],
                    [np.ones((1, len(support))), np.zeros((1, 1))]])
    rhs = np.r_[np.zeros(len(support)), 1.0]
    stationary = np.linalg.lstsq(kkt, rhs, rcond=None)[0][:-1]
    if stationary.min() >= -1e-12:
        candidate = np.zeros(size)
        candidate[support] = np.maximum(stationary, 0)
        candidate /= candidate.sum()
        if candidate @ B @ candidate <= u @ B @ u + 1e-13:
            u = candidate
    objective = float(u @ B @ u)
    lower = float(2 * (B @ u).min() - objective)
    return {"probabilities": u.tolist(), "fidelity_objective": objective,
            "fidelity_lower_certificate": lower,
            "optimization_gap": max(0.0, objective - lower),
            "delta_lower": 1 - objective,
            "delta_upper": min(1.0, 1 - lower)}


def _flag_block(N, kappa, g, a, b, initial, T, cutoff):
    """Evolve one 2x2 target block between spectator weights a and b.

    Row-major vectorization is used here. Zero padding includes physically
    absent states in depleted sectors; their populations stay zero.
    """
    rows, cols, data = [], [], []
    for ell in range(cutoff + 1):
        ha = g * math.sqrt(max(0, N - ell - a))
        hb = g * math.sqrt(max(0, N - ell - b))
        for s in range(2):
            for t in range(2):
                i = 4 * ell + 2 * s + t
                na = max(0, N - ell - a - s)
                nb = max(0, N - ell - b - t)
                rows.extend([i, i, i])
                cols.extend([i, 4 * ell + 2 * (1 - s) + t,
                             4 * ell + 2 * s + 1 - t])
                data.extend([-kappa * (na + nb) / 2, -1j * ha, 1j * hb])
                if ell:
                    prev_a = max(0, N - ell + 1 - a - s)
                    prev_b = max(0, N - ell + 1 - b - t)
                    rows.append(i)
                    cols.append(i - 4)
                    data.append(kappa * math.sqrt(prev_a * prev_b))
    dim = 4 * (cutoff + 1)
    generator = coo_matrix((data, (rows, cols)), shape=(dim, dim)).tocsr() * T
    start = np.zeros(dim, dtype=complex)
    start[:4] = np.asarray(initial).reshape(4)
    result = expm_multiply(generator, start, traceA=generator.diagonal().sum())
    return result.reshape(cutoff + 1, 2, 2)


def endpoint_output(n, N, kappa, g, T, cutoff=None):
    """Decoded output for (|0>_ref|0^n>+|1>_ref|1^n>)/sqrt(2).

    Returns a 4x4 matrix in the support ordered as
    (ref0,target0),(ref0,target1),(ref1,target0),(ref1,target1),
    with spectator labels implicitly 0 and n-1 respectively.
    """
    if N < n or n < 2:
        raise ValueError("Require N >= n >= 2 for the two spectator labels")
    mean_bound = kappa * N * T
    if cutoff is None:
        cutoff = min(N, math.ceil(mean_bound + 14 * math.sqrt(mean_bound + 1) + 40))
    tail = 0.0 if cutoff == N else float(poisson.sf(cutoff, mean_bound))
    if tail > 1e-11:
        raise ValueError(f"Loss-count truncation bound {tail} exceeds tolerance")
    aa = _flag_block(N, kappa, g, 0, 0, [[1, 0], [0, 0]], T, cutoff)
    bb = _flag_block(N, kappa, g, n - 1, n - 1, [[0, 0], [0, 1]], T, cutoff)
    ab = _flag_block(N, kappa, g, 0, n - 1, [[0, 1], [0, 0]], T, cutoff)
    output = np.block([[aa.sum(axis=0), ab.sum(axis=0)],
                       [ab.sum(axis=0).conj().T, bb.sum(axis=0)]]) / 2
    weights = np.real(np.trace(aa, axis1=1, axis2=2)
                      + np.trace(bb, axis1=1, axis2=2)) / 2
    return output, {"loss_mean_upper": mean_bound,
                    "mean_emitted_count": float(np.arange(cutoff + 1) @ weights),
                    "no_emission_probability": float(weights[0]),
                    "loss_cutoff": cutoff,
                    "truncation_probability_upper": tail}


def native_case(n, N, kappa=0.2, g=1.0, calibrated=False):
    Omega = g * math.sqrt(N)
    if calibrated:
        if Omega <= math.pi * kappa / 4:
            raise ValueError("Calibrated constant-coupling pulse needs Omega > pi*kappa/4")
        T = -2 / kappa * math.log1p(-math.pi * kappa / (4 * Omega))
    else:
        T = math.pi / (2 * g * math.sqrt(N - (n - 1) / 2))
    output, stats = endpoint_output(n, N, kappa, g, T)
    target = np.array([0, 1, 1, 0], dtype=complex) / math.sqrt(2)
    ideal = np.outer(target, target.conj())
    A = kappa * n * n / (N * Omega)
    result = {"n": int(n), "N": int(N), "kappa": kappa, "g": g,
              "Omega": Omega, "T": T, "A": A, "calibrated": calibrated,
              "output_trace": float(np.real(np.trace(output))),
              "min_output_eigenvalue": float(np.linalg.eigvalsh(output).min()),
              "reference_input_trace_error": float(np.abs(np.linalg.eigvalsh(ideal - output)).sum() / 2),
              "reference_input_entanglement_infidelity": float(1 - np.real(target.conj() @ output @ target)),
              **stats}
    if not calibrated and N >= 4 * n:
        result["proved_diamond_upper"] = min(1, 2 * n / N + 7 * kappa / Omega + A)
    if calibrated:
        eta = math.exp(-kappa * T)
        result["eta_at_end"] = eta
        if N >= 4 * n / eta:
            bound = (2 * (1 - eta * eta) / (eta * eta * N)
                     + 2 * Omega * math.sqrt(kappa) * T ** 1.5 / (3 * math.sqrt(eta * N))
                     + Omega * (2 * n - 1) * T / (math.sqrt(eta) * N)
                     + kappa * n * n * T / (4 * eta * N))
            result["proved_diamond_upper"] = min(1, bound)
    return result


def full_physical_endpoint_output(n, N, kappa, g, T):
    """Independent full RB Lindblad calculation for small instances.

    Uses a tensor-product Fock basis and column-major vectorization, then
    explicitly applies the canonical decoder. No loss-count representation
    is used in the dynamics. Intended to check boundary/index conventions.
    """
    d_reg, d_bat = 2 ** n, N + 1
    plus = np.zeros((d_reg, d_reg))
    for x in range(d_reg):
        if not (x & 1):
            plus[x + 1, x] = 1
    annihilator = np.diag(np.sqrt(np.arange(1, N + 1)), 1)
    exchange = kron(csr_matrix(plus), csr_matrix(annihilator), format="csr")
    H = g * (exchange + exchange.conj().T)
    jump = kron(eye(d_reg, format="csr"), csr_matrix(annihilator), format="csr")
    dim = d_reg * d_bat
    ident = eye(dim, format="csr")
    number = jump.conj().T @ jump
    generator = (-1j * (kron(ident, H) - kron(H.T, ident))
                 + kappa * (kron(jump.conj(), jump)
                            - (kron(ident, number) + kron(number.T, ident)) / 2)).tocsr() * T
    x0, x1 = 0, d_reg - 1
    k0, k1 = x0 * d_bat + N, x1 * d_bat + N - n
    starts = np.zeros((dim * dim, 3), dtype=complex)
    for col, (i, j) in enumerate([(k0, k0), (k1, k1), (k0, k1)]):
        starts[i + dim * j, col] = 1
    result = expm_multiply(generator, starts, traceA=generator.diagonal().sum())
    decoded = []
    for col in range(3):
        physical = result[:, col].reshape((dim, dim), order="F")
        logical = np.zeros((d_reg, d_reg), dtype=complex)
        for ell in range(N + 1):
            valid = [(x, N - ell - x.bit_count()) for x in range(d_reg)
                     if N - ell >= x.bit_count()]
            for x, bx in valid:
                for y, by in valid:
                    logical[x, y] += physical[x * d_bat + bx, y * d_bat + by]
        decoded.append(logical)
    a_idx, b_idx = [0, 1], [d_reg - 2, d_reg - 1]
    aa = decoded[0][np.ix_(a_idx, a_idx)]
    bb = decoded[1][np.ix_(b_idx, b_idx)]
    ab = decoded[2][np.ix_(a_idx, b_idx)]
    return np.block([[aa, ab], [ab.conj().T, bb]]) / 2
