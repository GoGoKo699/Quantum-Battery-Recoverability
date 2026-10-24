# Reproduction and finite verification

The written proofs establish the universal control converse and asymptotic resource criteria. These calculations check finite channel representations, numerical optimization, boundary conventions, and illustrative native-gate behavior.

## Environment and commands

The recorded environment uses Python 3.12.14 with NumPy 2.3.5, SciPy 1.17.0, and Matplotlib 3.10.8. Install the pinned libraries in your preferred environment, then run from the repository root:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_checks.py
python3 verification/generate_figures.py
```

The calculations are deterministic and use no sampled trajectories or random seeds. They require no GPU. The figure script uses a temporary Matplotlib cache outside the repository and writes its final SVG and numerical data into the paths below.

## What each calculation establishes

| Calculation | Method and evidence | Limitation |
|---|---|---|
| Passive channel | Complete finite binomial affinity sum; normalization and positive-semidefiniteness checks. | Finite cases do not prove an asymptotic limit. |
| Passive optimum | Convex simplex minimization, active-support polish, and supporting-plane optimization-gap certificate. | The certificate is evaluated in floating-point arithmetic, not interval arithmetic. |
| Independent native dynamics | Full register–oscillator Lindblad generator compared with the flagged target-block equations, including all loss sectors for $`n=2,N=8`$. | One small case checks the representation and depleted-sector boundaries. |
| Native gate bounds | Reference-input trace distance checked below the proved full-channel upper bounds in both operating regimes. | A chosen input cannot certify an optimized diamond norm. |
| Scaling illustration | Exact target-block evolution across increasing $`n,N`$, with an analytic loss-count truncation bound. | Plotted entanglement infidelity is for one input and the canonical decoder. |

The finite verification suite contains **13 cases**. Its independent full-Lindblad and loss-sector output matrices agree to approximately $`4.4\times10^{-16}`$ in the recorded environment. The passive convex-program gap is checked below $`2\times10^{-8}`$; actual values are in the committed output. Normalization, positivity, and physical upper-bound comparisons use the explicit tolerances in the runner.

## Files and output conventions

- [channel_models.py](channel_models.py) contains the finite models and the independent tensor-product calculation.
- [run_checks.py](run_checks.py) writes [results/finite_checks.json](results/finite_checks.json).
- [generate_figures.py](generate_figures.py) writes [results/native_gate_sweeps.json](results/native_gate_sweeps.json) and [figures/native_gate_scaling.svg](figures/native_gate_scaling.svg).
- [requirements.txt](requirements.txt) records the library versions.

For the native gate, the input is

```math
\frac{|0\rangle_{\mathrm{ref}}|0^n\rangle
+|1\rangle_{\mathrm{ref}}|1^n\rangle}{\sqrt2}.
```

The target is the same state after $`X_j`$ on the addressed qubit. The output is obtained after the canonical loss-sector decoder. `reference_input_trace_error` is half its trace distance from that ideal pure output; `reference_input_entanglement_infidelity` is one minus the ideal-state overlap. The trace error lower-bounds the diamond error of this particular decoded channel. It need not lower-bound the error of an alternative optimized decoder.

The fixed-bare-coupling sweep uses $`\kappa/g=0.2`$, $`n\in\{32,128,512,2048,8192\}`$, and budgets rounded up from $`4n`$, $`4n^{4/3}`$, and $`4n^{3/2}`$. The calibrated fixed-enhanced-rate sweep uses $`\kappa/\Omega=0.05`$, $`n\in\{4,8,16,32\}`$, and budgets rounded up from $`8n^2`$ and $`2n^{5/2}`$. The script records actual pulse durations, coupling strengths, emitted counts, no-emission probabilities, and upper bounds along with each error.

## Truncation and independent representation

The flagged simulator retains photon-loss sectors up to a chosen count. The conditional emission intensity never exceeds $`\kappa N`$, so the probability beyond the cutoff is bounded by the upper tail of a Poisson random variable with mean $`\kappa NT`$. The code requires this bound to be below $`10^{-11}`$. If all $`N+1`$ sectors are retained, the truncation probability is exactly zero. The count-tail bound, output trace, and minimum output eigenvalue are included in the results.

Absent logical states in highly depleted sectors are padded with zero. The independent small calculation instead evolves the full tensor-product register–Fock space, with a different vectorization convention, and applies the sector decoder explicitly afterwards. Agreement checks the transition amplitudes, phases, jump indexing, and padded boundary treatment without assuming the flagged equations in both implementations.

The SVG is generated directly from these numerical data. It contains no manually edited data points and no generated imagery.
