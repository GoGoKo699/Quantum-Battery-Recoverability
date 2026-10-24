# From Wiseman and Milburn to battery recoverability

The connection between quantum measurement and this battery architecture is concrete: the outgoing field performs an imperfect measurement of register excitation. A logical recovery can use the surviving register and battery, but it cannot erase information already carried away by that field. The central calculation therefore combines conditional emission statistics with a bound on the entire recovered quantum channel.

Wiseman and Milburn supply the measurement, open-system, trajectory, and error-correction vocabulary. This bridge develops the additional channel geometry and architectural estimates explicitly. The [thirty-milestone map](MILESTONES.md) organizes the same connection; the authoritative model and proofs remain in [Model](../science/model.md), [Control converse](../science/control-converse.md), [Native gates](../science/native-gates.md), and [Passive recovery](../science/passive-recovery.md).

## Source and verified reading map

The single book anchor is **Howard M. Wiseman and Gerard J. Milburn, *Quantum Measurement and Control*, Cambridge University Press, 2010**, hardback ISBN **978-0-521-80442-4**, [book DOI](https://doi.org/10.1017/CBO9780511813948).

Cambridge's [official frontmatter PDF](https://assets.cambridge.org/97805218/04424/frontmatter/9780521804424_frontmatter.pdf) identifies 2010 as the copyright and first-publication year and includes the printed contents. The [official contents record](https://www.cambridge.org/core/books/quantum-measurement-and-control/contents/19CEF009846E732E81101600550EACBD) has a separate online-publication date in 2011. The section numbers and starting pages below are verified against those publisher materials. They are navigation pointers, not claims that the complete chapter texts or their equation numbering were checked.

| Book location | Printed starting page | Connection developed here |
|---|---:|---|
| Appendix A, §§A.1, A.2, and A.4 | 398, 404, 410 | Optional review of quantum states, composite systems, and the oscillator. |
| Chapter 1; §§1.2–1.4 | 1; 8, 27, 32 | Outcome operators, conditional states, and averaging outcomes. |
| §§3.2–3.3 | 99, 102 | Markov approximation and radiative damping. |
| §3.6 | 119 | Lindblad generators and positivity. |
| §3.11 | 141 | Heisenberg-picture observable dynamics and the control-speed estimates. |
| §§4.2–4.3 | 149, 154 | Jump trajectories and photon counting. |
| §7.4 | 353 | Errors, syndromes, and quantum correction. |
| Appendix B, especially B.2 and B.6 | 418; 420, 425 | Optional stochastic-calculus context. |

Appendix B is useful for stochastic notation, but the compensated-count identities needed below are supplied locally. A Brownian increment rule cannot be substituted for the photon-count rule. Likewise, the book's correction and feedback topics do not grant this processor access to its emitted field: the model here permits prescribed native controls and terminal recovery, not measurement-based feedback from the bath.

## Conventions that keep rates consistent

The physical register has $`n`$ qubits. Its excitation operator is $`W=\sum_i n_i`$, where $`n_i=|1\rangle\langle1|_i`$. The oscillator annihilator is $`a`$, and $`Q=W+a^\dagger a`$ is total excitation. The input budget $`N\ge n`$ counts total excitations, rather than a photon occupation common to every logical state:

```math
V_N|x\rangle=|x\rangle_R|N-w(x)\rangle_B.
```

The oscillator therefore contains between $`N-n`$ and $`N`$ photons. The full logical input, possibly entangled with an untouched reference, is already encoded when the noisy interval begins. This interface comes from the [shared-battery architecture of Kurman and collaborators](https://doi.org/10.1103/l39v-jwwz).

The rate convention is fixed by the generator, not by the name given to a decay constant:

```math
\dot\rho=-i[H,\rho]+\kappa\mathcal D[a](\rho),
\qquad
\mathcal D[L](\rho)=L\rho L^\dagger-\frac12\{L^\dagger L,\rho\}.
```

The collapse operator is $`\sqrt\kappa\,a`$. During idle loss, photon number decays as $`e^{-\kappa t}`$ and field amplitude as $`e^{-\kappa t/2}`$. Thus $`\eta=e^{-\kappa t}`$ is transmissivity and $`p_{\mathrm{loss}}=1-\eta`$ is a probability.

A resonant exchange has Hamiltonian $`g(a\sigma^++a^\dagger\sigma^-)`$. In a two-state sector with $`m`$ available photons it is $`g\sqrt m\,X`$, giving transition probability $`\sin^2(g\sqrt m\,t)`$. The project defines $`\Omega=g\sqrt N`$; an ideal inversion takes $`\pi/(2\Omega)`$, not $`\pi/\Omega`$. The dimensionless ratio $`q=\kappa/\Omega`$ is distinct from $`p_{\mathrm{loss}}`$.

For states, root fidelity means $`F_{\mathrm r}(\rho,\sigma)=\|\sqrt\rho\sqrt\sigma\|_1`$. For a chosen input purification, entanglement fidelity $`F_e`$ is the overlap of the actual output density operator with the ideal pure state, equivalently the square of their root fidelity. Channel error is half diamond distance, maximized over inputs with a reference. Confusing these three conventions changes both constants and conclusions.

## A dressed qubit worked from loss to logical error

Take one qubit and $`N=1`$. An arbitrary logical state becomes

```math
\alpha|0\rangle+\beta|1\rangle
\quad\longmapsto\quad
\alpha|0,1\rangle_{RB}+\beta|1,0\rangle_{RB},
\qquad |\alpha|^2+|\beta|^2=1.
```

Logical coherence resides jointly in the register and battery. The reduced physical register already has no off-diagonal term, because its two battery states are orthogonal. Tracing out the battery would discard logical information even without loss. The recovery question therefore concerns the joint system.

With an initially empty environment, pure loss gives

```math
|1\rangle_B|0\rangle_E
\longmapsto
\sqrt\eta|1\rangle_B|0\rangle_E
+\sqrt{1-\eta}|0\rangle_B|1\rangle_E,
\qquad
|0\rangle_B|0\rangle_E\longmapsto|0\rangle_B|0\rangle_E.
```

The resulting joint state is

```math
\left(\alpha\sqrt\eta|0,1\rangle+\beta|1,0\rangle\right)|0\rangle_E
+\alpha\sqrt{1-\eta}|0,0\rangle|1\rangle_E.
```

The two terms occupy distinct total-excitation sectors. A canonical joint decoder sends $`|0,1\rangle`$ and $`|1,0\rangle`$ to their logical labels with flag $`\ell=0`$, and sends $`|0,0\rangle`$ to logical zero with flag $`\ell=1`$. After tracing the inaccessible environment, the two flagged logical Kraus operators are

```math
D_0=\begin{pmatrix}\sqrt\eta&0\\0&1\end{pmatrix},
\qquad
D_1=\begin{pmatrix}\sqrt{1-\eta}&0\\0&0\end{pmatrix},
\qquad D_0^\dagger D_0+D_1^\dagger D_1=I.
```

For a general logical density matrix, discarding the flag gives

```math
\mathcal C(\rho)
=D_0\rho D_0+D_1\rho D_1
=\begin{pmatrix}
\rho_{00}&\sqrt\eta\,\rho_{01}\\
\sqrt\eta\,\rho_{10}&\rho_{11}
\end{pmatrix}.
```

Populations are restored exactly; coherence is reduced. This is the phase-flip channel

```math
\mathcal C(\rho)=(1-r)\rho+rZ\rho Z,
\qquad r=\frac{1-\sqrt\eta}{2}.
```

Its half diamond distance from identity is $`r`$. The mixture gives the upper bound $`r`$, and the input $`|+\rangle`$ attains it because $`Z|+\rangle=|-\rangle`$ is orthogonal to the ideal output.

An arbitrary conditional terminal recovery cannot improve this value. For a maximally entangled logical input, the positive diagonal Kraus operators give the bound

```math
F_e\le\frac{(\mathrm{Tr}D_0)^2+(\mathrm{Tr}D_1)^2}{4}
=\frac{(1+\sqrt\eta)^2+(1-\eta)}4
=\frac{1+\sqrt\eta}{2}.
```

The underlying argument bounds each recovery's diagonal Kraus-vector norm by one and applies the triangle inequality; it is given in [Passive recovery](../science/passive-recovery.md#recovery-converse). Testing the ideal pure output implies error at least $`1-F_e=r`$, matching the decoder.

For example, at $`\eta=1/4`$, logical $`|+\rangle`$ becomes

```math
\rho_{\mathrm{out}}=
\begin{pmatrix}1/2&1/4\\1/4&1/2\end{pmatrix},
\qquad \delta_{\mathrm{opt}}=1/4.
```

The probability of one emission is $`(1-\eta)|\alpha|^2`$, which is $`3/8`$ for this input. It is not the logical error probability. An emission reveals that the original logical component was zero, while absence of an emission also changes the relative amplitudes. Knowing the loss flag identifies the sector; it does not deterministically invert this information-bearing filter on an unknown state.

## Channel geometry and the recovery witness

The qubit example generalizes through a complementary-channel argument. Let orthogonal logical inputs produce pure states $`|\Psi_j\rangle_{SE}`$ and $`|\Psi_k\rangle_{SE}`$, with $`S`$ containing every accessible output and $`E`$ the inaccessible environment. Then

```math
\left\|\mathrm{Tr}_E|\Psi_j\rangle\langle\Psi_k|\right\|_1
=F_{\mathrm r}(\rho_E^j,\rho_E^k).
```

This identity follows by maximizing the purification overlap over unitaries on $`S`$, using [Uhlmann's theorem](https://doi.org/10.1016/0034-4877(76)90060-4). Appending any recovery only enlarges the discarded environment, so it cannot increase the coherence available on the recovered logical register.

Suppose a measurement of the emitted field has outcome distributions with total variation distance $`D`$. Measurement cannot increase distinguishability, and the [fidelity–distance inequalities](https://arxiv.org/abs/quant-ph/9712042) give

```math
F_{\mathrm r}(\rho_E^j,\rho_E^k)\le\sqrt{1-D^2}.
```

For a reference entangled equally with these two logical inputs, the diagonal fidelity contributions are at most one and the off-diagonal contributions are at most that root fidelity. Every terminal recovery therefore has

```math
\delta\ge\frac{1-\sqrt{1-D^2}}2.
```

This is a bound on recovered quantum information, rather than an estimate of energy lost. Counting photons is a mathematical witness: the detector need not actually exist. A count measurement can discard some environmental information, but the distinction it does reveal is already enough for the lower bound. A classical control seed remains available to recovery; it is not artificially hidden to strengthen the result.

## The count martingale

The connection from §§4.2–4.3 to this witness begins with a jump unraveling. To first order in $`dt`$, the emission and no-emission operators are

```math
K_1=\sqrt{\kappa\,dt}\,a,
\qquad
K_0=I-\left(iH+\frac\kappa2a^\dagger a\right)dt.
```

Averaging the conditional outcomes produces the Lindblad generator. This trajectory representation is an established tool; an early primary formulation is [Dalibard, Castin and Mølmer](https://doi.org/10.1103/PhysRevLett.68.580).

Let $`L(t)`$ count emitted photons and let $`\widehat w_t`$ be the conditional register weight immediately before time $`t`$. Conservation gives $`Q=N-L(t)`$, so the predictable intensity is

```math
\lambda_t=\kappa[N-L(t-)-\widehat w_t],
\qquad 0\le\lambda_t\le\kappa N.
```

An infinitesimal count has conditional mean $`\lambda_tdt`$ and obeys $`(dL)^2=dL`$. Consequently the compensated count

```math
M_t=L(t)-\int_0^t\lambda_s\,ds
```

has zero conditional mean increments. Its second moment is $`\mathbb E M_t^2=\mathbb E\int_0^t\lambda_sds`$. These are the counting-process facts required here; no Gaussian approximation is being made.

For initial register weight $`w`$, multiplying the count equation by an integrating factor gives

```math
L(\tau)=(N-w)(1-e^{-\kappa\tau})+Z_\tau
-\kappa\int_0^\tau e^{-\kappa(\tau-s)}(\widehat w_s-w)\,ds,
```

```math
Z_\tau=\int_0^\tau e^{-\kappa(\tau-s)}\,dM_s,
\qquad
\mathbb E Z_\tau^2\le\frac N2(1-e^{-2\kappa\tau}).
```

The three terms separate a reference loss count, centered fluctuations, and the effect of control changing register weight. The reference count need not equal the actual controlled mean. The displayed variance follows directly from the martingale isometry and $`\lambda_t\le\kappa N`$. This local derivation is why Appendix B is supporting context, rather than a purported source of the project's particular probability bound.

## Bounded control and the native clock

The allowed Hamiltonian is

```math
H(t)=H_0(t)+\sum_i[g_i(t)a\sigma_i^++g_i(t)^*a^\dagger\sigma_i^-],
\qquad |g_i(t)|\le g,
\qquad [H_0,W]=[H_0,Q]=0.
```

The strength of $`H_0`$ is unrestricted, but it cannot move total register weight. On the reachable space $`Q\le N`$, each exchange operator has norm at most $`\sqrt N`$. Commutator bounds therefore give

```math
\mathbb E|W(t)-w|\le2n\Omega t.
```

For initial weights zero and $`n`$, Cauchy–Schwarz yields the stronger endpoint estimates

```math
\mathbb E_0W(t)\le n\Omega^2t^2,
\qquad
\mathbb E_1[n-W(t)]\le n\Omega^2t^2.
```

These bounds limit how quickly a native mask can change the emission statistics. At short times the endpoint count means separate by order $`\kappa n\tau`$, whereas count fluctuations have scale $`\sqrt{\kappa N\tau}`$. Their squared ratio suggests

```math
\frac{\kappa n^2\tau}{N},
\qquad
A=\frac{\kappa n^2}{N\Omega}
\quad\text{when }\tau\text{ is of order }1/\Omega.
```

That estimate explains the scale; the [control converse](../science/control-converse.md) proves it without assuming that control leaves the weights fixed. Controlled counts are not assumed to be a Poisson process with a fixed rate. The proof combines the count identity, movement bounds, elementary probability inequalities, and the recovery witness. Along sequences with $`n\to\infty`$, $`N\ge n`$, intervals $`T\ge c_0/\Omega`$ with fixed $`c_0>0`$, and bounded $`\kappa/\Omega`$, vanishing error requires $`A\to0`$. If $`A\to\infty`$, a growing ladder of distinguishable weights makes the worst-case recovery error tend to one.

A prescribed clock is essential. An unrestricted recovery could perform a desired unitary at zero native time. A separate duration bound applies when the native operation itself transfers a target population before recovery and $`[H_0,n_j]=0`$: reaching population $`1-\varepsilon`$ from zero requires

```math
\Omega T\ge\arcsin\sqrt{1-\varepsilon}.
```

The explicit gate constructions satisfy this narrower operational condition.

## Why many emissions can coexist with a good gate

For one resonant target and disconnected spectators, the exact decoded sector operators are

```math
H_\ell=g\sqrt{(N-\ell-W_s)_+}\,X_j,
\qquad
A_\ell=\sqrt{(N-\ell-W)_+},
\qquad W_s=W-n_j.
```

The positive-part notation handles missing states in depleted sectors. Summing the sector equations leaves logical dissipators $`\kappa\mathcal D[A_\ell]`$. Since $`A_\ell`$ is Hermitian,

```math
\mathcal D[A_\ell-cI]=\mathcal D[A_\ell]
\quad\text{for real }c.
```

This identity concerns the decoded Hermitian amplitudes; it is not a scalar-shift rule for an arbitrary physical annihilator. The logical disturbance depends on their eigenvalue diameter,

```math
\sqrt{N-\ell}-\sqrt{N-\ell-n},
```

whose square is of order $`n^2/(N-\ell)`$ when enough excitation remains. The much larger common amplitude mostly changes flag statistics.

The rigorous upper proof stops a comparison process before severely depleted sectors, bounds their total probability, and integrates the coherent and dissipative deviations on the remaining sectors. It does not declare every jump a failure. In the calibrated regime below, a nonzero fraction of the battery can be emitted while logical error vanishes.

## Two matched energy scales

At fixed positive $`g,\kappa`$, a target pulse of duration

```math
T=\frac{\pi}{2g\sqrt{N-(n-1)/2}}
```

obeys, for $`N\ge4n`$,

```math
\delta_X\le\frac{2n}{N}+\frac{7\kappa}{g\sqrt N}
+\frac{\kappa n^2}{gN^{3/2}}.
```

Together with the converse, this makes $`N/n^{4/3}\to\infty`$ a necessary and achievable vanishing-error scale for the stated native-clock benchmark. Sufficiency is supplied by this gate, not asserted for every allowed control schedule.

If the enhanced rate $`\Omega`$ is fixed instead, the bare coupling is $`g=\Omega/\sqrt N`$. A constant-coupling pulse can compensate for deterministic depletion by taking

```math
T=-\frac2\kappa\log\left(1-\frac{\pi\kappa}{4\Omega}\right),
\qquad
\eta=e^{-\kappa T},
\qquad \Omega>\frac{\pi\kappa}{4}.
```

Its reference Hamiltonian is $`\Omega e^{-\kappa t/2}X_j`$, whose integrated angle is $`\pi/2`$. The actual bare coupling is not increased during depletion. For $`N\ge4n/\eta`$, the [finite upper bound](../science/native-gates.md#theorem-2-a-depletion-calibrated-gate-at-a-fixed-rabi-rate-ceiling) is of order

```math
\frac{n^2}{N}+\frac nN+\frac1{\sqrt N}
```

at fixed $`\kappa,\Omega`$. Thus $`N/n^2\to\infty`$ is necessary and achievable in this calibrated-gate regime. The condition $`\Omega>\pi\kappa/4`$ is specific to that pulse, not a universal impossibility threshold. The two energy exponents differ because the first regime also buys a faster clock as $`N`$ grows.

## Schur channels and the simplex minimum

For idle pure loss, emitted counts from $`m`$ photons have probabilities

```math
P_m(\ell)=\binom m\ell(1-\eta)^\ell\eta^{m-\ell}.
```

Joint decoding leaves a channel that multiplies each matrix element by

```math
B_{wv}=\sum_\ell\sqrt{P_{N-w}(\ell)P_{N-v}(\ell)}.
```

This affinity is a Gram matrix of square-root probability vectors. The exact recovery error is

```math
\delta_{\mathrm{pass}}=1-\min_{u\in\Delta_{n+1}}u^\mathsf TBu.
```

Here $`u`$ is an input distribution over register weights. For a weight-diagonal logical input with probabilities $`u`$ and its reference purification, positive diagonal Kraus amplitudes bound every conditional recovery's entanglement fidelity by $`u^\mathsf TBu`$. For attainment, the reference-input channel difference reduces to

```math
\mathrm{diag}(\sqrt u)(J-B)\mathrm{diag}(\sqrt u),
```

where $`J`$ is the all-ones matrix. It has trace zero, is rank one minus a positive semidefinite matrix, and has nonnegative entries. Its half trace norm is therefore its largest eigenvalue, with a nonnegative Perron eigenvector. For a nonnegative unit vector $`z`$, set $`v_w=\sqrt{u_w}z_w`$. Cauchy–Schwarz gives $`\sum_wv_w\le1`$, while every simplex vector $`v`$ can be attained by choosing $`u=v`$ and $`z_w=\sqrt{v_w}`$. Maximizing the resulting quadratic form $`v^\mathsf T(J-B)v`$ yields $`1-\min_v v^\mathsf TBv`$. The complete channel-norm argument is supplied in [Passive recovery](../science/passive-recovery.md#diamond-norm-attainment), not attributed to a book theorem.

At fixed $`0<\eta<1`$, the finite estimate

```math
\delta_{\mathrm{pass}}\le
\min\left\{1,\frac{(1-\eta)n^2}{4\eta(N-n+1)}\right\}
```

shows quadratic energy sufficiency; below that scale, $`N=o(n^2)`$, the error tends to one. This passive regime has a duration independent of the improving native rate. Its quadratic scale has prior covariant-correction foundations, including [Zhou, Liu and Jiang](https://doi.org/10.22331/q-2021-08-09-521).

The same section explains why full-register collapse is not loss of all storage capacity. A fixed-weight code makes the battery occupation independent of the logical state. The [Knill–Laflamme condition](https://doi.org/10.1103/PhysRevA.55.900), applied to the span of the loss effects, gives maximum exact code dimension $`\binom n{\lfloor n/2\rfloor}`$ for nonzero idle loss. A random unitary installed before encoding also changes the input interface: uniform bit masks, chosen independently of the input, attain error $`1-b^\mathsf TBb`$ with $`b_w=2^{-n}\binom nw`$, when the recovery knows the seed and the final output discards it. Neither option is a free native mask after an arbitrary state has already arrived through $`V_N`$.

## Mathematical tools supplied locally

The book pointers identify the physical language. The following project-specific mathematical connections have explicit local derivations.

| Tool | Role and local location |
|---|---|
| Purification geometry and half diamond distance | Converts environmental distinguishability into a bound against arbitrary recovery; [control converse](../science/control-converse.md#proof-why-terminal-recovery-cannot-undo-the-record). |
| Compensated counts and integrating factors | Separates photon fluctuations from controlled weight motion; [emission-record proof](../science/control-converse.md#proof-what-the-emitted-photons-reveal). |
| Cauchy–Schwarz, Jensen, Markov, and Chebyshev inequalities | Supply finite bounds without a normal approximation or a no-emission assumption. |
| Schur-matrix geometry and convex optimization | Establishes the exact passive minimum and a numerical optimization-gap certificate; [passive analysis](../science/passive-recovery.md). |
| Completely positive stopping and Duhamel bounds | Controls bad sectors and accumulates coherent and dissipative errors with a reference; [native comparison proof](../science/native-gates.md#a-comparison-bound-that-charges-logical-noise). |

The [primary-source account](../references/related-work.md) retains the provenance of the encoding, polar recovery, Pauli twirling, fidelity inequalities, and exact-correction criterion. Those research citations supplement the single book anchor rather than replacing it with several competing textbooks.

## Physical resources and scope

All conclusions depend on an already dressed arbitrary input, a vacuum Markov loss bath that does not return, and bounded native exchange. The broad lower bound allows arbitrary excitation-preserving terms and an arbitrary deterministic terminal recovery. Fresh control randomness is independent of the input, can be used by recovery, and is discarded from the final logical output. The generic asymptotic statements require a fixed lower bound on $`\Omega T`$ and bounded $`\kappa/\Omega`$.

The constructive gate additionally needs switchable spectator couplers and an ideal joint decoder. Its decoder synthesis, locality, energy, and noise are not priced. One recoverable operation does not establish unlimited circuit depth at fixed error. Different encodings, protected memories, external transverse drives, or coherent recovery of the emitted field change the resources and therefore the question.

Finally, increasing $`g\sqrt N`$ at fixed $`g`$ must remain consistent with the rotating-wave model and available hardware bandwidth. The result at fixed $`\Omega`$ makes that rate constraint explicit. The common organizing quantity is the information left in the emitted field during the time that the specified native controls need to act.
