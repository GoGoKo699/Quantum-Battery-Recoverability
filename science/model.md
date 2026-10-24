# Model, operational question, and results

**When can a shared quantum battery power an operation without irreversibly measuring the register that it powers?** A fixed excitation budget can support arbitrarily deep unitary dynamics in an ideal closed model. In an open device, escaping radiation also carries information. The relevant question is how much logical information remains recoverable after the joint register–battery dynamics, rather than how often the battery loses its first photon.

Kurman et al. introduced the fixed-excitation computational architecture used here and explicitly discussed battery-induced decoherence. This project studies its recoverability with a photon-loss bath and bounded native controls. The attribution and differences from earlier control-energy and covariant-correction bounds are set out in [Related work](../references/related-work.md).

## 1. Register and battery

The register consists of $`n`$ two-level systems. Let $`n_i=|1\rangle\langle1|_i`$, let $`W=\sum_i n_i`$ denote its excitation number, and let $`a`$ annihilate a photon in the shared oscillator. The combined excitation is $`Q=W+a^\dagger a`$. Set $`\hbar=1`$ in Hamiltonians and use the rotating frame of the oscillator.

An integer budget $`N\ge n`$ supplies the full dressed computational interface

```math
V_N|x\rangle=|x\rangle_R|N-w(x)\rangle_B,
\qquad x\in\{0,1\}^n.
```

Here $`w(x)`$ is Hamming weight. $`N`$ counts **total register-plus-battery excitations**; the photon occupation itself ranges from $`N-n`$ to $`N`$. The logical input is an arbitrary density operator on all $`2^n`$ states, and may be entangled with a reference. It is already encoded by $`V_N`$ when the noisy interval starts.

This interface is a substantive assumption. A different code, or a seed-dependent unitary applied before $`V_N`$, defines a different input channel. In particular, [fixed-weight codes](passive-recovery.md#6-protected-subspaces-and-their-exact-dimension) avoid the idle loss mechanism while storing fewer logical states.

## 2. Native dynamics and inaccessible radiation

During $`[0,T]`$, the joint density operator obeys

```math
\dot\rho=-i[H(t),\rho]+\kappa\mathcal D[a](\rho),
\qquad
\mathcal D[L](\rho)=L\rho L^\dagger-\tfrac12\{L^\dagger L,\rho\},
```

with $`\kappa>0`$ and

```math
H(t)=H_0(t)+\sum_{i=1}^n
\left[g_i(t)a\sigma_i^++g_i(t)^*a^\dagger\sigma_i^-\right],
\qquad |g_i(t)|\le g.
```

The broad converse assumes $`[H_0(t),W]=[H_0(t),Q]=0`$. It therefore permits arbitrary detunings and even arbitrarily strong interactions that preserve register weight. Coupler phases, active subsets, and their time dependence are unrestricted. These are prescribed coherent controls; an additional protected quantum memory or an unbounded transverse drive is not part of this model. Fresh classical randomness in the controls is allowed and is independent of the unknown input. Its seed may be available to the final recovery.

Only the oscillator emits into the bath. The bath starts in vacuum, is Markovian, and remains inaccessible to the processor. There is no recharge or other excitation source during the interval. Since the Hamiltonian preserves $`Q`$ and every loss lowers it, all states remain in $`Q\le N`$.

For the constructive native gate, all spectator couplers are switched off and one resonant target coupler has strength $`g`$. This is a specified subset of the allowed control class. A device with always-on spectator couplings and only finite detuning requires an additional crosstalk analysis.

## 3. What the error measures

Let $`\mathcal N_T^H`$ include $`V_N`$, the controlled noisy evolution, and any accessible classical seed. Allow an arbitrary deterministic terminal recovery $`\mathcal R`$ on the surviving register, battery, and seed, with arbitrary ancillary workspace and work supply. It returns only the logical register of dimension $`2^n`$; auxiliary and seed registers can be used internally and are then discarded. It cannot access the emitted field. For a specified control protocol, define

```math
\delta_H(T)=\inf_{\mathcal R}
\frac12\left\|\mathcal R\circ\mathcal N_T^H-\mathrm{id}\right\|_\diamond.
```

Half diamond distance lies in $`[0,1]`$ and includes entangled reference inputs. The converse is uniform in $`H`$, so it also bounds the infimum over the allowed control protocols. Replacing identity by a known target unitary does not change a recoverability converse: its inverse can be composed into the unrestricted recovery.

The gate construction uses a particular recovery, the canonical loss-sector decoder. For each valid basis vector it identifies

```math
|x\rangle_R|N-\ell-w(x)\rangle_B
\longmapsto |x\rangle_L|\ell\rangle_F,
```

and then discards $`F`$. The spaces with different $`\ell`$ are orthogonal total-excitation sectors. This is a well-defined isometry on the noise support, with a CPTP extension elsewhere, even when some logical states are absent from a heavily depleted sector. The decoder need not measure $`W`$.

This is an ideal logical interface, not a claim of an energy-free physical decoder. Its implementation time, locality, and energy cost are outside the upper bound. The construction establishes that information survives the native gate and can be recovered; it does not supply every component of a fault-tolerant device.

## 4. The energy–speed parameter

Write

```math
\Omega=g\sqrt N,
\qquad q=\frac\kappa\Omega,
\qquad A=\frac{\kappa n^2}{N\Omega}
=\frac{\kappa n^2}{gN^{3/2}}.
```

$`\Omega`$ is the enhanced native exchange rate. The broad converse considers a prescribed interval $`T=c_0/\Omega`$, where $`c_0>0`$ is fixed, along scaling sequences with bounded $`q`$. Later processing cannot restore information already retained by the bath during an early subinterval.

| Result | Statement | Assumptions and proof |
|---|---|---|
| **C1: nonzero error floor** | Vanishing recoverability error requires $`A\to0`$. An explicit finite-parameter lower bound is positive at every fixed $`A>0`$. | Full dressed interface, broad native control class, $`T\ge c_0/\Omega`$, bounded $`q`$. [Control converse](control-converse.md). |
| **C2: full-channel collapse** | If $`A\to\infty`$, then $`\delta_H(T)\to1`$, uniformly in the allowed controls and terminal recovery. | Same model; a growing ladder of input weights provides the witness. [Control converse](control-converse.md). |
| **G1: native gate at fixed bare coupling** | A resonant $`X_j`$ gate has error at most $`2n/N+7\kappa/(g\sqrt N)+A`$, for $`N\ge4n`$. | Switchable spectators, canonical decoder, pulse duration $`\pi/[2g\sqrt{N-(n-1)/2}]`$. [Native gates](native-gates.md). |
| **G2: native gate with a fixed enhanced rate** | A depletion-calibrated pulse gives vanishing error when $`N/n^2\to\infty`$, at fixed $`\kappa,\Omega`$ with $`\Omega>\pi\kappa/4`$. | Constant bare coupling $`g=\Omega/\sqrt N`$, explicit calibrated duration and finite bound. [Native gates](native-gates.md). |
| **P1: exact passive benchmark** | Optimal recovery error is $`1-\min_{u\in\Delta_{n+1}}u^\mathsf TB u`$, where $`B`$ is a binomial-affinity Gram matrix. | Idle pure loss of transmissivity $`\eta`$. [Passive recovery](passive-recovery.md). |

At fixed positive $`g`$ and $`\kappa`$, C1 and G1 give the vanishing-error criterion

```math
\frac{N}{n^{4/3}}\longrightarrow\infty.
```

Below this scale, $`N=o(n^{4/3})`$, C2 gives complete worst-case channel failure. At a fixed enhanced rate, C1 and G2 instead identify the criterion $`N/n^2\to\infty`$ in the stated calibrated-gate regime. These are asymptotic vanishing-error statements; the finite bounds, rather than the $`\gg`$ notation, specify sufficient or necessary conditions for a chosen finite accuracy.

The result at fixed $`g`$ is a statement within the Jaynes–Cummings model. Growing $`g\sqrt N`$ must remain within the applicable rotating-wave, oscillator, and control bandwidth regime. It is not a license to extrapolate an ideal Hamiltonian beyond a device's range.

## 5. A gate condition cannot be supplied by the recovery

An unrestricted terminal recovery could itself perform $`X_j`$. Consequently, a target unitary alone does not force any positive native duration in the error definition. The broad theorem prescribes the operation interval explicitly.

There is a separate gate-duration corollary in the narrower class $`[H_0,n_j]=0`$: a native process starting with the target unexcited needs $`\Omega T\ge\arcsin\sqrt{1-\epsilon}`$ to reach target population $`1-\epsilon`$. It applies to a required native gate **before recovery**, including a stipulated lossless implementation. Its precise relation to the converse is proved in [Control converse](control-converse.md). The explicit gate in G1 or G2 meets this operational interpretation.

## 6. Read the connected account

Follow [Control converse](control-converse.md) for the competition between charge motion and photon-count resolution. Then read [Native gates](native-gates.md) for the sector representation and the dissipator cancellation that make the same scale achievable. [Passive recovery](passive-recovery.md) supplies a solvable benchmark and explains protected input interfaces. [Interpretation](interpretation.md) joins the results and their resource boundaries.

The [verification guide](../verification/README.md) distinguishes exact finite checks, numerical optimization certificates, and reference-input simulations from the universal statements proved here. Primary sources and inherited ingredients are collected in [Related work](../references/related-work.md).
