"""Run finite checks with distinct analytical and numerical roles."""
import json
from pathlib import Path

import numpy as np
from scipy.stats import binom

from channel_models import (affinity_matrix, passive_optimum, endpoint_output,
                            full_physical_endpoint_output, native_case)


def main():
    rows = []
    for n, N, eta in [(1, 3, 0.3), (2, 2, 0.5), (4, 8, 0.8),
                       (8, 12, 0.25), (12, 60, 0.9), (20, 400, 0.5)]:
        B = affinity_matrix(n, N, eta)
        normalization_error = float(np.max(np.abs(B.diagonal() - 1)))
        minimum_eigenvalue = float(np.linalg.eigvalsh(B).min())
        assert normalization_error < 3e-12
        assert minimum_eigenvalue > -3e-12
        result = passive_optimum(B)
        assert result["optimization_gap"] < 2e-8
        lower = max(0, 1 - (1 + 4 * np.sqrt(np.pi * N) / (1 - eta)) / (n + 1))
        upper = min(1, (1 - eta) * n * n / (4 * eta * (N - n + 1)))
        assert result["delta_lower"] >= lower - 2e-9
        assert result["delta_lower"] <= upper + 2e-9
        if n == 1:
            assert abs(result["delta_lower"] - (1 - B[0, 1]) / 2) < 2e-10
        weights = binom.pmf(np.arange(n + 1), n, 0.5)
        randomized = float(1 - weights @ B @ weights)
        randomized_bound = min(1, (1 - eta) * n / (4 * eta * (N - n + 1)))
        assert -2e-12 <= randomized <= randomized_bound + 2e-10
        rows.append({"check": "passive_convex_program", "n": n, "N": N, "eta": eta,
                     "normalization_error": normalization_error,
                     "minimum_eigenvalue": minimum_eigenvalue,
                     "randomized_error": randomized, **result})

    # An independent tensor-product calculation checks jump indexing, target
    # phases, low-energy absent states and the terminal sector decoder.
    n, N, kappa, g, T = 2, 8, 0.4, 0.8, 0.7
    flagged, stats = endpoint_output(n, N, kappa, g, T, cutoff=N)
    physical = full_physical_endpoint_output(n, N, kappa, g, T)
    discrepancy = float(np.max(np.abs(flagged - physical)))
    assert discrepancy < 3e-11
    assert abs(np.trace(flagged) - 1) < 3e-11
    assert np.linalg.eigvalsh(flagged).min() >= -3e-11
    rows.append({"check": "independent_full_lindblad_vs_flags", "n": n, "N": N,
                 "maximum_matrix_discrepancy": discrepancy, **stats})

    for calibrated in [False, True]:
        for n, N in [(4, 80), (8, 512), (16, 2048)]:
            kappa = 0.05 if calibrated else 0.2
            g = 1 / np.sqrt(N) if calibrated else 1.0
            r = native_case(n, N, kappa=float(kappa), g=float(g), calibrated=calibrated)
            assert abs(r["output_trace"] - 1) < 2e-10
            assert r["min_output_eigenvalue"] > -2e-10
            assert r["reference_input_trace_error"] <= r["proved_diamond_upper"] + 2e-10
            assert r["reference_input_entanglement_infidelity"] <= r["reference_input_trace_error"] + 2e-10
            rows.append({"check": "native_gate_reference_input", **r})

    out = Path(__file__).resolve().parent / "results"
    out.mkdir(exist_ok=True)
    (out / "finite_checks.json").write_text(json.dumps(rows, indent=2) + "\n")
    print(f"PASS: {len(rows)} finite checks; full Lindblad/flag discrepancy {discrepancy:.3g}")
    print("Universal claims rely on the written proofs; reference-input errors are not optimized diamond norms.")


if __name__ == "__main__":
    main()
