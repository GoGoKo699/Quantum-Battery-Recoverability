# Native control cannot erase the earliest emission record

For the dressed Fock-battery interface, bounded native exchange cannot prevent the emitted field from learning register excitation before the register has time to move appreciably. This section turns that observation into bounds on **optimal recovery**, allowing arbitrary time-dependent native controls, classical randomization known to the recovery, and unrestricted terminal recovery.

The controlling dimensionless parameter is

```math
\mathcal A=\frac{\kappa n^2}{N\Omega},\qquad \Omega=g\sqrt N.
\tag{1}
```

On an interval of order $`1/\Omega`$, diverging $`\mathcal A`$ forces the optimal half-diamond error to approach one, while vanishing error requires $`\mathcal A\to0`$. The finite-size statements and their constants are given below. Combined with the [native gate upper bounds](native-gates.md), they give the fixed-bare-coupling scale $`N\gg n^{4/3}`$. The distinction between a prescribed operation interval and a gate whose duration must itself be justified is treated explicitly in the final corollary.

## Model and operational error

Let $`R`$ contain $`n\ge1`$ qubits, with excitation operators $`n_i=|1\rangle\langle1|_i`$ and $`W=\sum_i n_i`$. Let $`B`$ be a bosonic battery with annihilator $`a`$, and write $`Q=W+a^\dagger a`$. For an integer $`N\ge n`$, the input interface is

```math
V_N|x\rangle=|x\rangle_R|N-w(x)\rangle_B.
\tag{2}
```

This is the fixed-excitation encoding of [Kurman2026](../references/related-work.md). The unknown logical input is encoded by the same $`V_N`$ for every control seed.

During $`[0,T]`$, the physical state evolves according to

```math
\frac{d\rho}{dt}=-i[H(t),\rho]+\kappa\mathcal D[a](\rho),
\qquad
\mathcal D[a](\rho)=a\rho a^\dagger-\frac12\{a^\dagger a,\rho\},
\tag{3}
```

with $`\kappa>0`$ and

```math
H(t)=H_0(t)+\sum_{i=1}^n\left[g_i(t)a\sigma_i^+
+g_i(t)^*a^\dagger\sigma_i^-\right],
\qquad |g_i(t)|\le g,
\qquad [H_0(t),W]=[H_0(t),Q]=0.
\tag{4}
```

Here $`g>0`$, and $`\sigma_i^+=|1\rangle\langle0|_i`$. Controls may be piecewise continuous; more generally it is enough that the resulting evolution is well defined. The bound does not constrain the strength of $`H_0`$: detunings and arbitrarily strong excitation-preserving register interactions are included. There is no other source or sink of $`Q`$ during this interval. The Markov output field is inaccessible and does not return to interact with the processor.

A classical seed $`z`$, independent of the input, may select the entire control schedule. The seed is available to the terminal recovery. In particular, the physical output channel can be written

```math
\mathcal N_T^{\mathsf C}(\rho)
=\sum_z p_z|z\rangle\langle z|_C\otimes
\mathcal N_{T,z}(\rho),
\tag{5}
```

where each $`\mathcal N_{T,z}`$ includes encoding by $`V_N`$. The recovered output is a quantum register of dimension $`2^n`$; the seed may be used and then discarded. For a fixed control protocol $`\mathsf C`$, define

```math
\delta_{\mathsf C}(T)
=\inf_{\mathcal R}\frac12
\left\|\mathcal R\circ\mathcal N_T^{\mathsf C}
-\mathrm{id}_R\right\|_\diamond.
\tag{6}
```

The recovery acts on $`RBC`$ and is an arbitrary deterministic CPTP map. Its energy, ancillas, measurements, locality, and computational complexity are unrestricted. All bounds below hold for every $`\mathsf C`$, and hence after additionally minimizing over the allowed controls. Replacing the identity in (6) by a specified unitary channel leaves the optimum unchanged: composing $`\mathcal R`$ with the inverse unitary is a bijection on the allowed recoveries.

The encoding is part of the premise. A seed-dependent unitary applied before $`V_N`$, a different logical code, a drive exceeding (4), or coherent access to the emitted field defines a different problem.

## Finite-size converse

Set

```math
\Omega=g\sqrt N,\qquad q=\frac{\kappa}{\Omega},\qquad
\mathcal A=\frac{\kappa n^2}{N\Omega}.
\tag{7}
```

### Theorem 1: a critical-scale error floor

For any $`\tau\le T`$ with $`c=\Omega\tau\in(0,1/2]`$, let

```math
b_c=1-\frac23c^2,
\qquad
D_*(\mathcal A,q,c)
=\frac{\mathcal A c\,e^{-2qc}b_c^2}
{8+\frac83\mathcal A c^3+\mathcal A c\,e^{-2qc}b_c^2}.
\tag{8}
```

Every allowed control protocol and terminal recovery obey

```math
\boxed{\displaystyle
\delta_{\mathsf C}(T)
\ge\frac{1-\sqrt{1-D_*(\mathcal A,q,c)^2}}{2}.}
\tag{9}
```

This is an inequality for finite $`n`$. No Gaussian approximation, assumption of a small probability of emission, or adiabatic assumption is used.

### Theorem 2: a distinguishable weight ladder

Choose $`m\in\{2,\ldots,n+1\}`$ computational basis states with excitation weights separated by at least an integer $`d\ge1`$. For $`0<\tau\le T`$, put $`p=1-e^{-\kappa\tau}`$ and

```math
\epsilon_{\mathrm{cnt}}
=\frac{16\kappa N\tau}{d^2p^2}
+\frac{4\kappa n\Omega\tau^2}{dp}.
\tag{10}
```

Whenever $`\epsilon_{\mathrm{cnt}}\le1/2`$,

```math
\boxed{\displaystyle
\delta_{\mathsf C}(T)
\ge 1-\frac1m-
\left(1-\frac1m\right)
2\sqrt{\epsilon_{\mathrm{cnt}}(1-\epsilon_{\mathrm{cnt}})}.}
\tag{11}
```

When (10) exceeds $`1/2`$, the theorem supplies the trivial lower bound zero. The chosen logical basis states can be fixed independently of both the Hamiltonian schedule and the random seed.

### Consequences on a native clock

Consider sequences with $`n\to\infty`$, $`N\ge n`$, and

```math
T\ge\frac{c_0}{\Omega},\qquad c_0>0\ \text{fixed},
\qquad q\le\bar q<\infty.
\tag{12}
```

If $`\mathcal A`$ does not tend to zero, some subsequence satisfies $`\mathcal A\ge a_0>0`$. Fix $`c\in(0,\min\{c_0,1/2\}]`$. The expression in (8) increases with $`\mathcal A`$ and decreases with $`q`$, so (9) gives a strictly positive lower bound along that subsequence. Consequently

```math
\delta_{\mathsf C}(T)\longrightarrow0
\quad\Longrightarrow\quad
\mathcal A\longrightarrow0.
\tag{13}
```

If $`\mathcal A\to\infty`$, choose equally spaced weights with

```math
m=\lfloor\mathcal A^{1/7}\rfloor,
\qquad
c=\mathcal A^{-3/7},
\qquad
\tau=\frac{c}{\Omega}.
\tag{14}
```

Eventually $`2\le m\le n/2`$ and $`\tau\le T`$: indeed $`\mathcal A=q n^2/N\le\bar q n`$. With $`d=\lfloor n/(m-1)\rfloor`$, one has $`d\ge n/(2m)`$. Using $`1-e^{-\kappa\tau}\ge\kappa\tau e^{-\kappa\tau}`$ in (10) gives

```math
\epsilon_{\mathrm{cnt}}
\le\frac{64e^{2qc}m^2}{\mathcal A c}
+8e^{qc}mc
\le C_{\bar q}\mathcal A^{-2/7},
\qquad
C_{\bar q}=64e^{2\bar q}+8e^{\bar q}.
\tag{15}
```

For sufficiently large $`\mathcal A`$, equations (11) and (15) yield

```math
\delta_{\mathsf C}(T)
\ge1-\left(2+2\sqrt{C_{\bar q}}\right)\mathcal A^{-1/7}
\longrightarrow1.
\tag{16}
```

Thus the lower result concerns the full worst-case recovery metric, not only a single fragile coherence. It does not assert that every input or every subcode becomes useless.

For fixed positive $`g`$ and $`\kappa`$, condition (13) becomes $`N/n^{4/3}\to\infty`$, while $`N=o(n^{4/3})`$ implies (16). At fixed positive $`\Omega`$ and $`\kappa`$, the corresponding necessary condition is $`N/n^2\to\infty`$. These different exponents reflect whether increasing battery occupation is allowed to increase the native exchange rate.

## Proof: motion of the register

All states reached from (2) are supported on $`Q\le N`$. On this subspace,

```math
\|a\sigma_i^+\|\le\sqrt N,
\qquad
\|a^\dagger\sigma_i^-\|\le\sqrt N.
\tag{17}
```

These are exact bounds, not $`\sqrt{N+1}`$ estimates. For example,
$`(a^\dagger\sigma_i^-)^\dagger(a^\dagger\sigma_i^-)
=(a^\dagger a+1)n_i\le Nn_i`$, because $`n_i=1`$ implies at most $`N-1`$ battery excitations.

Fix an initial weight $`w`$ and define $`K_w=|W-w|`$. A single exchange changes $`W`$ by one, and the function $`u\mapsto|u-w|`$ changes by at most one between adjacent integers. Thus

```math
\|i[H(t),K_w]\|\le2ng\sqrt N=2n\Omega.
\tag{18}
```

The $`H_0`$ contribution vanishes, and $`\mathcal D[a]^\dagger(K_w)=0`$ because $`a`$ commutes with $`K_w`$. An initial state supported in the subspace of weight $`w`$ therefore satisfies

```math
\mathrm{tr}[K_w\rho(t)]\le2n\Omega t.
\tag{19}
```

The endpoint inputs satisfy a stronger bound. Let $`y(t)=\mathrm{tr}[W\rho(t)]`$ for initial weight zero. From (17) and Cauchy–Schwarz,

```math
\left|\mathrm{tr}[a^\dagger\sigma_i^-\rho]\right|
\le\sqrt{N\mathrm{tr}[n_i\rho]},
\qquad
|y'(t)|\le2\Omega\sum_i\sqrt{\mathrm{tr}[n_i\rho(t)]}
\le2\Omega\sqrt{ny(t)}.
\tag{20}
```

Integrating the differential inequality from $`y(0)=0`$ gives $`y(t)\le n\Omega^2t^2`$. One can regularize $`\sqrt{y}`$ by $`\sqrt{y+\varepsilon}`$ and then let $`\varepsilon\downarrow0`$ to justify the endpoint. Applying the same argument to the number of holes gives

```math
\mathbb E_0 W(t)\le n\Omega^2t^2,
\qquad
\mathbb E_1[n-W(t)]\le n\Omega^2t^2,
\tag{21}
```

where subscripts $`0,1`$ denote initial register weights $`0,n`$. Only $`[H_0,W]=0`$ is needed: the individual populations may change rapidly under $`H_0`$, but their sum has no $`H_0`$ derivative. Bounds (19) and (21) also hold after averaging over the control seed.

## Proof: what the emitted photons reveal

Photon counting of the output field is used as a mathematical observer of the complementary channel, not as a resource granted to the processor. Standard quantum-jump unraveling gives the same unconditional channel as (3); see [DalibardCastinMolmer1992 and WisemanMilburn2010](../references/related-work.md).

Let $`L(t)`$ be the count of photons emitted up to time $`t`$, and let $`\widehat w_t`$ be the conditional expectation of $`W`$ immediately before time $`t`$. The conditioning includes the count history and, when present, the classical seed. Along every trajectory, total excitation is exactly $`N-L(t)`$. The predictable intensity is therefore

```math
\lambda_t=\kappa[N-L(t-)-\widehat w_t],
\qquad 0\le\lambda_t\le\kappa N.
\tag{22}
```

The compensated process

```math
\mathsf M_t=L(t)-\int_0^t\lambda_s\,ds
\tag{23}
```

is a square-integrable martingale with predictable quadratic variation $`\int_0^t\lambda_sds`$. Since $`L(t)\le N`$, integrability causes no difficulty. For a fixed initial weight $`w`$, solve the linear equation for $`L`$ with an integrating factor to obtain

```math
L(\tau)=(N-w)(1-e^{-\kappa\tau})+Z_\tau
-\kappa\int_0^\tau e^{-\kappa(\tau-s)}(\widehat w_s-w)\,ds,
\tag{24}
```

where

```math
Z_\tau=\int_0^\tau e^{-\kappa(\tau-s)}\,d\mathsf M_s,
\qquad
\mathbb E Z_\tau=0,
\qquad
\mathbb E Z_\tau^2
\le\frac N2(1-e^{-2\kappa\tau})\le\kappa N\tau.
\tag{25}
```

The variance estimate is the martingale isometry followed by (22). Identity (24) accounts for depletion exactly. The reference value $`(N-w)(1-e^{-\kappa\tau})`$ need not equal the actual mean when controls change $`W`$.

### Count classification for the weight ladder

For a state of initial weight $`w`$, conditional Jensen and (19) imply

```math
\mathbb E|\widehat w_s-w|
\le\mathrm{tr}[K_w\rho(s)]\le2n\Omega s.
\tag{26}
```

Classify the integer count $`L(\tau)`$ by its nearest reference location $`(N-w_j)p`$, using any rule for ties. Distinct reference locations are separated by at least $`dp`$. A wrong decision implies deviation at least $`dp/2`$ from the correct location. By (24), this requires either $`|Z_\tau|\ge dp/4`$ or an absolute integral drift at least $`dp/4`$.

Chebyshev applied to (25) bounds the first probability by $`16\kappa N\tau/(d^2p^2)`$. The expected absolute drift is at most

```math
\kappa\int_0^\tau\mathbb E|\widehat w_s-w|\,ds
\le\kappa n\Omega\tau^2.
\tag{27}
```

Markov's inequality therefore bounds the second probability by $`4\kappa n\Omega\tau^2/(dp)`$. This proves the uniform per-input classification error (10). The reference locations and decision rule do not depend on the control seed, so the same classification guarantee holds when that seed is averaged out.

### Endpoint mean and variance

For initial weights $`0,n`$, let $`\Delta=\mathbb E_0L(\tau)-\mathbb E_1L(\tau)`$. Taking expectations in the count equation gives

```math
\Delta=\kappa\int_0^\tau e^{-\kappa(\tau-s)}
\left[\mathbb E_1W(s)-\mathbb E_0W(s)\right]ds.
\tag{28}
```

For $`c=\Omega\tau\le1/2`$, equation (21) implies a nonnegative integrand lower bound $`n(1-2\Omega^2s^2)`$. Consequently

```math
\Delta\ge\kappa n\tau e^{-\kappa\tau}
\left(1-\frac23c^2\right)=:\Delta_{\rm lb}.
\tag{29}
```

For either endpoint, conditional Jensen followed by $`W^2\le nW`$, or by the corresponding inequality for $`n-W`$, gives

```math
\mathbb E(\widehat w_s-w)^2\le n^2\Omega^2s^2.
\tag{30}
```

Using (24), (25), $`(u+v)^2\le2(u^2+v^2)`$, and the integral Cauchy–Schwarz inequality, each endpoint count variance is at most

```math
\mathrm{Var}_j L(\tau)
\le\mathbb E_j\left[L(\tau)-(N-w_j)p\right]^2
\le V:=2\kappa N\tau+\frac23\kappa^2n^2\Omega^2\tau^4.
\tag{31}
```

For any two probability distributions on a real variable, with mean difference $`\Delta`$ and variances $`v_0,v_1`$, their total variation distance satisfies

```math
\mathrm{TV}\ge
\frac{\Delta^2}{2(v_0+v_1)+\Delta^2}.
\tag{32}
```

To verify this, center the variable at the midpoint of the means. Cauchy–Schwarz bounds $`\Delta^2`$ by $`(v_0+v_1+\Delta^2/2)`$ times the triangular divergence $`\sum_\ell(P_\ell-Q_\ell)^2/(P_\ell+Q_\ell)`$. The latter is at most $`\sum_\ell|P_\ell-Q_\ell|=2\mathrm{TV}`$. Applying (32) to (29)–(31) yields

```math
\mathrm{TV}(L_0(\tau),L_1(\tau))
\ge\frac{\Delta_{\rm lb}^2}{4V+\Delta_{\rm lb}^2}
=D_*(\mathcal A,q,c).
\tag{33}
```

This proves the classical distinguishability estimate needed for Theorem 1.

## Proof: why terminal recovery cannot undo the record

We use root fidelity

```math
F_{\rm r}(\rho,\sigma)=\|\sqrt\rho\sqrt\sigma\|_1
\tag{34}
```

and trace distance $`D(\rho,\sigma)=\tfrac12\|\rho-\sigma\|_1`$. The required relations are Uhlmann's theorem and $`F_{\rm r}(\rho,\sigma)\le\sqrt{1-D(\rho,\sigma)^2}`$; see [Uhlmann1976, FuchsVanDeGraaf1999, and Watrous2018](../references/related-work.md).

Let $`|\Psi_j\rangle_{SE}`$ be Stinespring output vectors for orthogonal logical inputs $`|x_j\rangle`$, with $`S`$ containing the whole accessible physical output, including the control seed. If the seed is randomized, one valid purification is

```math
|\Psi_j\rangle
=\sum_z\sqrt{p_z}\,|z\rangle_C|z\rangle_{C'}
|\Psi_{j,z}\rangle_{RBF},
\tag{35}
```

where $`C`$ is accessible, $`F`$ is the field environment, and the full complementary output is $`E=C'F`$. Thus the proof never assumes that the recovery is ignorant of its own seed.

For the environmental states $`\rho_E^j`$, the cross-term identity is

```math
\left\|\mathrm{tr}_E|\Psi_j\rangle\langle\Psi_k|\right\|_1
=F_{\rm r}(\rho_E^j,\rho_E^k).
\tag{36}
```

Indeed, the variational expression for the trace norm maximizes the overlap of the two vectors over unitaries on $`S`$, and Uhlmann's theorem identifies that maximum with the root fidelity of their environmental reductions. This also shows directly why arbitrary recovery cannot improve the relevant coherence: append a Stinespring dilation of the recovery, so that the original environment is a subsystem of the enlarged environment. Root fidelity can only increase when the added environmental system is traced out. Every recovered matrix element therefore obeys

```math
\left|\langle x_j|
\mathcal R\mathcal N_T^{\mathsf C}(|x_j\rangle\langle x_k|)
|x_k\rangle\right|
\le F_{\rm r}(\rho_E^j,\rho_E^k).
\tag{37}
```

The emitted field from $`[0,\tau]`$ is part of the final environment for every $`T\ge\tau`$. Counting those early photons is a valid measurement of that environment; later operations on the processor cannot remove the already emitted subsystem. In the ladder construction, the disjoint decision regions identify every $`j`$ with error at most $`\epsilon_{\mathrm{cnt}}`$. Hence, for $`j\ne k`$, the count distributions have total variation at least $`1-2\epsilon_{\mathrm{cnt}}`$. Monotonicity of distinguishability under measurement and (34) give

```math
F_{\rm r}(\rho_E^j,\rho_E^k)
\le2\sqrt{\epsilon_{\mathrm{cnt}}(1-\epsilon_{\mathrm{cnt}})}
\quad\text{if }\epsilon_{\mathrm{cnt}}\le\frac12.
\tag{38}
```

Use the reference-entangled input

```math
|\Phi_m\rangle=\frac1{\sqrt m}\sum_{j=1}^m
|j\rangle_A|x_j\rangle_R.
\tag{39}
```

Its entanglement fidelity after any recovery is at most $`1/m+(1-1/m)f`$ whenever all off-diagonal fidelities in (37) are at most $`f`$: the $`m`$ diagonal terms are each at most one, and the other $`m(m-1)`$ terms are each bounded by $`f`$. Measuring the ideal output projector shows that the half trace distance from the ideal output is at least one minus this entanglement fidelity. Equation (38) therefore proves Theorem 2.

For Theorem 1, use only the two endpoint inputs and (33). Their environmental trace distance is at least $`D_*`$, so their root fidelity is at most $`\sqrt{1-D_*^2}`$. Equation (39) with $`m=2`$ then proves (9). Both conclusions hold after minimizing over all terminal recoveries.

## A native-gate duration corollary

The preceding theorems require that the physical evolution last long enough to contain the witness interval. A target unitary specified only after unrestricted terminal recovery does not impose any duration: at $`T=0`$, the recovery could simply implement that unitary. The following narrower native-gate condition supplies a physical duration without making that assumption.

Fix a target qubit $`j`$ and additionally require

```math
[H_0(t),n_j]=0.
\tag{40}
```

Other qubits may still have active native couplers. Suppose the initial target population is zero and write $`r(t)=\mathrm{tr}[n_j\rho(t)]`$. Since the other native couplers and the loss dissipator commute with $`n_j`$, only the target exchange contributes to its derivative. With $`P_1=n_j`$, $`P_0=I-n_j`$,

```math
\|P_1H(t)P_0\|\le |g_j(t)|\sqrt N.
\tag{41}
```

Purify $`\rho(t)`$ and split the purification into its $`P_0`$ and $`P_1`$ components. Their norms are $`\sqrt{1-r(t)}`$ and $`\sqrt{r(t)}`$. Cauchy–Schwarz applied to the off-diagonal Hamiltonian block gives, even with battery loss present,

```math
|r'(t)|\le2|g_j(t)|\sqrt N\sqrt{r(t)(1-r(t))}.
\tag{42}
```

With the common bound $`g`$, the inequality $`|r'(t)|\le2\Omega\sqrt{r(t)(1-r(t))}`$ also holds for randomized controls by including the classical seed in the accessible state. To integrate through the endpoints, use the regularized primitive

```math
f_\varepsilon(r)=\int_0^r
\frac{du}{2\sqrt{(u+\varepsilon)(1-u+\varepsilon)}}.
```

Its time derivative is at most $`\Omega`$ along the trajectory. Integrating from $`r(0)=0`$ and taking $`\varepsilon\downarrow0`$ proves

```math
\arcsin\sqrt{r(T)}\le\Omega T.
\tag{43}
```

For a deterministic target schedule, the sharper right-hand side $`\sqrt N\int_0^T|g_j(t)|dt`$ follows from (42) by the same argument.

Consequently, if the native physical operation transfers the target population to at least $`1-\varepsilon_{\rm nat}`$ **before arbitrary terminal recovery**, then

```math
T\ge\frac{\arcsin\sqrt{1-\varepsilon_{\rm nat}}}{\Omega}.
\tag{44}
```

There are two direct ways to impose this native performance condition. One can require the actual output, before unrestricted recovery, to achieve that population transfer. Alternatively, one can require that the same native control schedule with $`\kappa=0`$ implement a logical $`X_j`$ to half-diamond error at most $`\varepsilon_{\rm nat}`$ under the canonical identification of the $`Q=N`$ shell with the logical register. Applying that condition to $`|0^n\rangle`$ gives (44) in the lossless evolution and hence constrains the duration of the schedule used in the noisy experiment. The canonical identification preserves target populations and supplies no additional logical gate.

If $`\varepsilon_{\rm nat}\le\bar\varepsilon<1`$ along a sequence, equation (44) supplies (12) with $`c_0=\arcsin\sqrt{1-\bar\varepsilon}>0`$. The control converse then applies while still allowing unrestricted terminal recovery in the noisy experiment. An exact native population inversion requires $`T\ge\pi/(2\Omega)`$. This corollary is not claimed for an arbitrary $`H_0`$ that can rapidly exchange target excitation with other qubits; condition (40) is essential to this particular argument.

## Relation to the constructive bounds and scope

The [native gate construction](native-gates.md) uses one resonant target coupler, switches off the spectators, and satisfies (40). At fixed positive $`g,\kappa`$, its finite-time bound

```math
\delta_X\le\frac{2n}{N}+\frac{7\kappa}{g\sqrt N}
+\frac{\kappa n^2}{gN^{3/2}}
\tag{45}
```

vanishes when $`N/n^{4/3}\to\infty`$. Its duration is of order $`1/\Omega`$, and its actual native target-population transfer tends to one. Equations (13) and (45) therefore provide a matching vanishing-error criterion for this native-clock benchmark. The calibrated construction at fixed $`\Omega`$ in the same file supplies a separate sufficient result in its stated operating range; the converse (9) itself requires no calibration model.

The proof concerns information in the emission record, not the probability that no photon is lost. It permits the expected number of emissions to diverge. It also distinguishes the recoverability of the full dressed interface from quantum capacity or the performance of another encoding: a fixed-weight code, a seed-dependent mask installed before encoding, or a different controller changes the input family being protected. Native masks applied after (2) remain covered by the bounds.

The Markov photon-count representation, Uhlmann and fidelity inequalities, and the original encoding are inherited ingredients. Covariant-QEC and metrological bounds already constrain passive storage; see [ZhouLiuJiang2021](../references/related-work.md). The additional result proved here is the uniform finite-time comparison between bounded native motion and an early emission record, including its growing weight ladder and its recovery-aware critical-scale bound. All claims are within the Jaynes–Cummings control model; allowing $`g\sqrt N`$ to grow with $`N`$ also requires that the physical device remain in the regime where that model and the assumed control bandwidth apply.
