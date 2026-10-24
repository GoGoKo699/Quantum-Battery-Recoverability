# Physical meaning and resource boundaries

The joint battery–register encoding lets energy move coherently without requiring the battery to be disentangled from the computation after every operation. That advantage changes the relevant noise question. A lost photon can reveal information about the register even when its energy could be replaced, while a large number of lost photons can be compatible with excellent logical recovery.

The [model](model.md), [control converse](control-converse.md), and [native gate construction](native-gates.md) make this statement quantitative. The [passive solution](passive-recovery.md) isolates its information-theoretic origin.

## 1. Loss is a measurement of register charge

In the dressed interface, register weight $`w`$ corresponds to photon occupation $`N-w`$. The photon-count intensity is therefore sensitive to the logical weight. Along a conditional trajectory it is

```math
\lambda(t)=\kappa\bigl[N-L(t)-w_c(t)\bigr].
```

Measuring the emitted field is only a proof device: the processor is not given that field. If the field distinguishes several logical inputs, the surviving system cannot preserve their arbitrary coherent superpositions. Uhlmann's cross-term identity and an entangled reference turn this statement into a bound that survives every terminal recovery.

In a short interval, an extreme charge separation $`n`$ creates a count separation of order $`\kappa n t`$, against shot noise of order $`\sqrt{\kappa Nt}`$. The resulting squared resolution scale is $`\kappa n^2t/N`$. At the same time, bounded native exchange changes a definite initial weight by at most $`2n\Omega t`$ in expected absolute displacement, with a stronger quadratic bound at the endpoint weights. These estimates lead to

```math
A=\frac{\kappa n^2}{N\Omega}
```

on a time of order $`1/\Omega`$. The proof controls the full dynamics, including changing couplings, rather than treating the register as stationary during a gate.

The growing-weight-ladder argument is especially consequential. Below the frontier the environment can distinguish an increasing number of charge labels before native control moves them sufficiently. The worst-case error then tends to one; the conclusion is stronger than the loss of a single two-branch coherence.

## 2. Why first-photon lifetime gives a different design criterion

A Fock state with $`m`$ photons has no-emission probability $`e^{-\kappa mt}`$ during an idle interval, so its first-emission lifetime decreases with occupation. This familiar quantity is not a measure of decoded logical error. Kurman et al. discuss the raw-lifetime issue in the motivating architecture; see [the source comparison](../references/related-work.md).

For the logical channel, the informative part of the jump amplitude is the variation of $`\sqrt{N-W}`$ across possible logical states. A large common scalar part mostly determines how many photons are emitted. In the native-gate proof it cancels because

```math
\mathcal D[A-cI]=\mathcal D[A]
\quad\text{for Hermitian }A\text{ and real }c.
```

The resulting logical dissipative estimate scales as $`\kappa n^2/N`$, even though the raw photon-loss rate scales as $`\kappa N`$. At fixed bare coupling, the operation also becomes faster as $`1/(g\sqrt N)`$. A larger budget can therefore reduce the decoded error while increasing the number of emitted photons.

This statement does not make the lost energy free. Emission, eventual recharge, detuning work, and decoder implementation remain physical costs. The theorem separates surviving quantum information from energy accounting; it does not establish a net refrigeration or thermodynamic advantage for a complete processor.

## 3. Two different ways to scale the hardware

| Resource convention | Native timescale | Vanishing-error condition | Constructive operation |
|---|---|---|---|
| Fixed positive bare $`g`$ and loss rate $`\kappa`$ | $`T\sim1/(g\sqrt N)`$ | $`N/n^{4/3}\to\infty`$ | Constant resonant pulse at the midpoint occupation. |
| Fixed positive enhanced rate $`\Omega`$ and $`\kappa`$, with $`\Omega>\pi\kappa/4`$ | A fixed depletion-calibrated duration | $`N/n^2\to\infty`$ | Constant $`g=\Omega/\sqrt N`$ with a duration calibrated for the decaying mean occupation. |

The lower bound is uniform over the stated control class; sufficiency is demonstrated by the listed gates. It is not a claim that every allowed control performs well above the scale. For fixed $`\Omega`$, the condition $`\Omega>\pi\kappa/4`$ belongs to this particular constant-coupling construction and is not asserted as an impossibility threshold for every protocol.

With fixed $`g`$, the expected number of emitted photons during a gate is of order $`\sqrt N`$ when $`N\gg n`$, whereas their fraction is of order $`N^{-1/2}`$. With fixed $`\Omega`$, the calibrated interval has a fixed loss fraction and the mean count can be of order $`N`$. Both statements follow from the exact count identity and the bounds $`0\le W\le n`$; neither prevents the corresponding decoded error from vanishing.

The $`4/3`$ exponent is consequently tied to increasing enhanced speed. A finite device cannot increase $`g\sqrt N`$ indefinitely while keeping every other physical assumption unchanged. Its rotating-wave validity, spectral range, oscillator nonlinearity, and control bandwidth determine the applicable regime. The energy–speed parameter $`A`$ exposes this dependency explicitly.

## 4. What recovery contributes

The converse gives the processor arbitrary terminal CPTP recovery. It therefore cannot be evaded by a better final decoder within the same interface. Its obstruction is information in an inaccessible environment.

The upper bound uses a mathematically explicit sector decoder. Different total-excitation losses are orthogonal, so the decoder can identify the syndrome without distinguishing computational configurations within a sector. This establishes recoverability of the gate's logical action, including inputs entangled with external references.

The decoder's locality, circuit complexity, energy supply, and noisy execution are not included in the gate-duration budget. A complete hardware implementation must price those operations. The result is therefore a recoverability frontier with a native-operation construction, rather than a complete fault-tolerant architecture or a free-energy computation protocol.

The prescribed-time convention is equally necessary. If arbitrary terminal recovery were allowed to count as the implementation of the target gate, it could simply execute that gate itself. The separate native population-transfer condition in the [converse](control-converse.md) prevents that interpretation.

## 5. Protected encodings change the input interface

The full-register theorem requires preserving every logical state in a space of dimension $`2^n`$. It includes superpositions spanning widely separated register weights. A constant-weight subspace eliminates this source of which-state information during idle battery loss. The largest exactly correctable idle subspace has dimension $`\binom n{\lfloor n/2\rfloor}`$, as proved in [Passive recovery](passive-recovery.md).

Thus nearly $`n`$ qubits of protected information can coexist with worst-case failure of the specified full-register channel. These are compatible operational statements. The theorem must not be presented as a vanishing-capacity result for every encoding on the same hardware.

Ideal random masking before the noisy input interface also changes the problem. Ordinary Pauli twirling can reduce the passive averaged error to a binomially weighted affinity. A native mask begun after the original interface has been accepted is covered by the dynamic converse and cannot erase the earliest emitted record. A processor initialized and kept in another code or random frame throughout its entire computation needs a corresponding analysis of gates, preparation, reset, and output.

## 6. What the result adds to prior work

The passive energy scale is closely related to covariant quantum error correction and loss-sensitive number-state metrology. Conditional polar recovery and Pauli twirling are established tools. Combining quantum speed with control-induced decoherence also has clear precedents.

The central contribution here is the explicit bound during active, bounded native control of the dressed register, the finite error floor at the crossover, the growing-ladder full-channel failure theorem, and the matching lossy native gates. These conclusions use an inaccessible emitted record and joint terminal recovery, which distinguish the operational model from a closed product-drive calculation. [Related work](../references/related-work.md) records the precise comparison and its limits.

The finite computations support the channel representation, constants, and physical interpretation. They do not establish the universal control converse or certify novelty. Those claims rest respectively on the written proofs and a bounded, current comparison with primary literature.
