# Related work and attribution

## The question addressed here

This project studies the recoverability of an arbitrary register encoded in a shared Fock battery through

```math
V_N|x\rangle=|x\rangle_R|N-|x|\rangle_B,
\qquad N\ge n.
```

Its central question concerns loss **during bounded native control**: can exchange between the battery and the register prevent the emitted field from learning the initial register charge? The model permits time-dependent Jaynes--Cummings couplings $`|g_i(t)|\le g`$, terms preserving register and total excitation, and arbitrary terminal recovery. On an interval of order $`1/(g\sqrt N)`$, the controlling parameter is

```math
A=\frac{\kappa n^2}{gN^{3/2}}.
```

The converse is uniform over those controls. For fixed $`\kappa/g>0`$, vanishing worst-case recovery error, measured by half the diamond norm distance, requires $`A\to0`$; when $`A\to\infty`$, that error tends to one. An addressed resonant gate with a canonical terminal decoder supplies a matching vanishing-error construction. The [model](../science/model.md) and [control converse](../science/control-converse.md) give the precise definitions and proof. The original interface and several ingredients of the passive benchmark are established prior work. The comparisons below identify those dependencies and the additional content of the active-control analysis. Citation keys refer to [references.bib](references.bib).

## Closest comparisons

| Work | Established result relevant here | Relationship to this project |
|---|---|---|
| [Kurman et al. (2026)](https://doi.org/10.1103/l39v-jwwz) | A Fock battery shared by a qubit register; computation within a fixed total-excitation shell; control through qubit detunings. | Supplies the architecture and dressed interface. This project analyzes recoverable logical noise caused by battery loss. |
| [Zhou, Liu and Jiang (2021)](https://doi.org/10.22331/q-2021-08-09-521) | Quantitative lower bounds on covariant error correction, expressed through channel quantum Fisher information. | Already implies the passive quadratic energy law, including its leading converse coefficient. Native exchange during loss requires a further argument. |
| [Gregoratti and Werner (2004)](https://doi.org/10.1063/1.1758320) | Optimal conditional recovery for a fixed Kraus instrument using polar decomposition. | Supplies the recovery principle behind the loss-syndrome decoder and its Choi-fidelity optimum. |
| [Wallman and Emerson (2016)](https://doi.org/10.1103/PhysRevA.94.052325) | Randomized compiling tailors noise into stochastic Pauli errors and improves worst-case error behavior. | Explains the ideal randomized-mask improvement. A physical excitation mask must be implemented before it protects the register. |
| [Gea-Banacloche and Ozawa (2006)](https://doi.org/10.1103/PhysRevA.74.060301) | A shared coherent pulse can produce worst-case register error proportional to register size squared divided by mean photon number. | Establishes an earlier shared-control energy penalty, from atom--field entanglement in a different interface. |
| [Pratapsi, Buffoni and Gherardini (2024)](https://doi.org/10.1103/PhysRevResearch.6.023296) | Combines Jaynes--Cummings speed with entanglement-induced reduced-qubit error to obtain an inverse-energy law. | The closest speed-versus-decoherence comparison; its closed evolution and discarded drive differ from a lossy dressed register with joint recovery. |

## Architecture and the physical meaning of loss

Kurman et al. introduce the fixed-excitation dressed representation and demonstrate gates powered by a battery that remains correlated with its register. Their published discussion recognizes that photon loss can decohere the register and discusses the decreasing lifetime of highly occupied Fock states. The present analysis therefore does not attribute the discovery of battery--register entanglement, the encoding, or the existence of loss-induced decoherence to this project. See the published [PRX article](https://doi.org/10.1103/l39v-jwwz), available as [arXiv:2503.23610v4](https://arxiv.org/abs/2503.23610v4) (`Kurman2026`).

The distinction is between survival of the original Fock state and survival of its encoded quantum information. A lost photon moves the joint state to another total-excitation shell. Its logical effect depends on how strongly the emission probability varies across register weights. Many losses can be compatible with small recoverable error when the large common component of the jump amplitude carries little information about the logical state.

This physical mechanism has an optical-metrology precedent. Huver, Wildfeuer and Dowling analyze path-entangled number states whose populated background makes coherence more resistant to photon loss. Their beam-splitter treatment already contains overlaps of loss-conditioned amplitudes and the use of background photons to reduce environmental distinguishability. The battery's passive two-weight coherence is closely related to that mechanism; it is not a new general principle of loss protection. The full-register optimization and bounded-control interval are different tasks. See [PRA 78, 063828](https://doi.org/10.1103/PhysRevA.78.063828) and [arXiv:0805.0296](https://arxiv.org/abs/0805.0296) (`HuverWildfeuerDowling2008`).

## What the passive benchmark inherits

### Covariant quantum error correction

For a passive pure-loss interval of transmissivity $`\eta`$, write $`q=1-\eta`$. The code is covariant under the physical generator $`H_S=-a^\dagger a`$ and logical generator $`H_L=W`$, up to an irrelevant scalar phase. The physical space can be truncated to battery occupations $`0,\ldots,N`$, which pure loss preserves. Thus the finite-dimensional theorem of Zhou, Liu and Jiang applies directly.

Their error measure is worst-case entanglement **infidelity**, $`1-f_{\rm wc}^2`$, with $`f`$ the root fidelity; it is not the purified distance. Theorem 1 and Eqs. (12)--(14) of [arXiv:2005.11918v3](https://arxiv.org/abs/2005.11918v3) relate this error to regularized channel quantum Fisher information (`ZhouLiuJiang2021`).

For this channel, the Kraus gauge $`h_k=-k/q`$ gives $`\beta=0`$ and $`\alpha=(\eta/q)a^\dagger a`$. Substituting $`\|\alpha\|=\eta N/q`$ and $`\Delta H_L=n`$ into that theorem yields

```math
\epsilon\ge
\ell_1\!\left(\frac{qn^2}{16\eta N}\right),
\qquad
\ell_1(z)=\frac{1+4z-\sqrt{1+4z}}{2(1+4z)}
=z+O(z^2).
```

Consequently, the passive quadratic scaling and its small-error converse coefficient are inherited. The exact finite-size recovery formula, saturation, and worst-case error tending to one provide additional characterization of this particular channel. They should be presented as a solvable benchmark for the dynamic problem. Since native exchange changes $`W`$ and battery occupation during the interval, the passive covariance argument does not directly establish the active-control converse.

### Polar recovery and a physically accessible syndrome

Gregoratti and Werner's Proposition 4, Eqs. (18)--(20), establishes the optimal Choi entanglement fidelity for a fixed, flagged Kraus instrument $`t_k`$:

```math
F_{e,\max}=\frac{1}{d^2}\sum_k
\bigl(\mathrm{Tr}|t_k|\bigr)^2.
```

Undoing the unitary factor in each polar decomposition attains this value. See [arXiv:quant-ph/0403092](https://arxiv.org/abs/quant-ph/0403092) (`GregorattiWerner2004`). For the passive battery channel, distinct loss counts occupy orthogonal total-excitation sectors, so the relevant flag is available from the joint register--battery system. Applying this established recovery principle leaves positive diagonal amplitudes $`\sqrt{p_k(w)}`$, with

```math
p_k(w)=\binom{N-w}{k}q^k\eta^{N-w-k}.
```

The worst-case optimization over register weights and the comparison with half-diamond distance are additional channel-specific steps. Neither the use of polar recovery nor optimality for a maximally mixed logical input should be described as a new general recovery theorem.

### Randomization

For the corrected diagonal channel, a uniform conjugation by products of $`X`$ operators averages over excitation assignments and produces a stochastic Pauli channel of $`Z`$ strings. Its half-diamond error equals its Choi entanglement infidelity. This is a special case of Pauli noise tailoring, as developed in [Wallman and Emerson](https://arxiv.org/abs/1512.01098) (`WallmanEmerson2016`). It replaces sensitivity to the full weight range by sensitivity to the binomial weight variance and can reduce the ideal passive energy scaling.

The distinction relevant to the active theorem is temporal and physical. A mask already applied before the noisy interval changes the initial interface. A software frame update alone does not change battery occupation. A mask implemented after the specified dressed input arrives is subject to the native charge-motion bound, and cannot erase a photon record that has already escaped.

### Protected subspaces

Exact correction on a restricted code is governed by the Knill--Laflamme criterion; see [PRA 55, 900](https://doi.org/10.1103/PhysRevA.55.900) and [quant-ph/9604034](https://arxiv.org/abs/quant-ph/9604034) (`KnillLaflamme1997`). A fixed-weight register sector makes every passive, decoded Kraus operator scalar on that sector. This is the established decoherence-free-subspace mechanism, represented by [Lidar, Chuang and Whaley](https://doi.org/10.1103/PhysRevLett.81.2594) (`LidarChuangWhaley1998`).

For the present passive channel, the loss probabilities span all weight projectors. Applying the standard exact-correction criterion then proves that the largest correctable code has dimension

```math
d_{\max}=\max_w\binom nw=\binom n{\lfloor n/2\rfloor}.
```

The [passive-recovery analysis](../science/passive-recovery.md#6-protected-subspaces-and-their-exact-dimension) gives the channel-specific dimension proof. Its asymptotic count of $`n-\tfrac12\log_2n-O(1)`$ exactly stored qubits concerns an idle code. Universal gates, encoding cost, and protection during operations require separate analysis. The unrestricted-register converse therefore coexists with a large protected subspace.

## Energy, speed, and recoverable information

Gea-Banacloche and Ozawa derive a quadratic register-size penalty when a coherent control pulse is shared among atoms. Their result concerns entanglement generated between the atoms and a quantized pulse, including simultaneous and sequential use. The earlier existence of a shared-control energy penalty should therefore be explicit. The present fixed-total-excitation interface permits access to the battery during recovery and locates the irreversible information in an additional emitted field. See [quant-ph/0611137](https://arxiv.org/abs/quant-ph/0611137) (`GeaBanaclocheOzawa2006`).

Ikonen, Salmilehto and Möttönen analyze energy-efficient control by reusing and correcting itinerant pulses. Their protocol demonstrates why an energy bound must name the controller preparation, reuse, correction, and dissipation resources. It does not impose the initial fixed-excitation interface or the inaccessible photon-loss bath used here. See [npj Quantum Information 3, 17](https://doi.org/10.1038/s41534-017-0015-5) (`IkonenSalmilehtoMottonen2017`).

Pratapsi, Buffoni and Gherardini explicitly combine a Jaynes--Cummings speed scale with decoherence. Their model uses closed evolution of a logical qubit and an initially separate drive; the reduced-qubit error arises when the drive is discarded. They recover an inverse-mean-photon-number scaling. That work supplies a close conceptual precedent for combining speed and error, but does not bound recoverability of an arbitrary dressed register under photon loss and all allowed native controls. See [arXiv:2305.05019v3](https://arxiv.org/abs/2305.05019v3) (`PratapsiBuffoniGherardini2024`).

Vu, Kuwahara and Saito give finite-time relations between average gate fidelity and thermodynamic dissipation, including time-dependent Markovian dynamics and more general environments. Those relations compare different quantities from the worst-case recoverable logical channel considered here. In particular, a large emission count need not cause a large logical error if the photons carry little information about the input. See [arXiv:2311.15762v3](https://arxiv.org/abs/2311.15762v3) (`VuKuwaharaSaito2024`).

## Established tools and the added argument

Quantum-jump unraveling is standard: [Dalibard, Castin and Mølmer](https://doi.org/10.1103/PhysRevLett.68.580) give an early wave-function formulation (`DalibardCastinMolmer1992`). The textbooks `WisemanMilburn2010` and `BreuerPetruccione2002` develop its measurement interpretation and stochastic dynamics. Purification fidelity, its relation to distinguishability, and channel norms are established quantum-information tools; see [Uhlmann](https://doi.org/10.1016/0034-4877(76)90060-4), [Fuchs and van de Graaf](https://arxiv.org/abs/quant-ph/9712042), and [Watrous](https://jhwatrous.github.io/books-and-courses.html) (`Uhlmann1976`, `FuchsVanDeGraaf1999`, `Watrous2018`).

The additional argument links these tools through this architecture's conservation law. Along a photon-count trajectory, $`Q=N-L(t)`$, so the emission intensity is

```math
\lambda(t)=\kappa\bigl[N-L(t)-\langle W\rangle_c(t)\bigr].
```

Bounds on charge motion hold uniformly over the allowed controls. They limit how quickly distinct initial weights can change their count statistics. A distinguishable early record bounds coherence of the entire accessible output and therefore defeats every terminal recovery. A growing set of weights strengthens this to worst-case error approaching one. The construction uses the exact loss-sector dynamics and cancellation of the scalar part of a Hermitian jump operator, rather than classifying every emitted photon as a failed gate.

## Scope of the comparison

The result is a frontier for the stated dressed interface and operation interval. It does not bound the capacity of all protected subspaces, rule out constant-weight encodings, or constrain a register masked before the interval begins. The broad converse permits arbitrary excitation-preserving interactions; a universal gate-duration claim would need an additional speed bound. The achieved gate upper bound uses switchable couplers and an ideal terminal decoder.

The fractional exponent also uses the growth $`\Omega_N=g\sqrt N`$. A physical ceiling on the allowed Rabi frequency must be included separately; the corresponding energy--speed parameter is $`\kappa n^2/(N\Omega_N)`$. Finally, a single-operation result does not imply error independent of circuit depth, or a complete fault-tolerant architecture with free encoding, decoding, reset, and recharge.

The cited works identify the closest direct dependencies and comparisons. The bounded-control recovery frontier is the project's central contribution; passive scaling, polar recovery, Pauli twirling, and the general use of quantum trajectories remain attributed to their established sources.
