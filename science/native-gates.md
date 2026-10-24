# Native resonant gates with a lossy shared battery

An addressed resonant Jaynes–Cummings pulse can implement a logical bit flip on an arbitrary register state even when the shared battery emits many photons. The relevant error is controlled by the variation of the photon-loss amplitude across logical states, rather than by the probability that no photon is emitted.

This note proves two finite-size bounds. At fixed single-qubit coupling $g$ and loss rate $\kappa$, a pulse of duration approximately $\pi/(2g\sqrt N)$ has vanishing recovered error when $N/n^{4/3}\to\infty$. When the available Rabi rate $\Omega=g\sqrt N$ is held fixed instead, a pulse calibrated for deterministic battery depletion has vanishing error when $N/n^2\to\infty$, provided $\Omega>\pi\kappa/4$. Both constructions use a constant bare coupling during the pulse. Their proofs include arbitrary reference entanglement, all loss sectors, and a completely positive terminal decoder.

## Model and operational target

There are $n$ two-level systems, one bosonic battery, and an inert reference of arbitrary dimension. Write

$$
n_i=|1\rangle\langle1|_i,\qquad
W=\sum_{i=1}^n n_i,\qquad
Q=W+a^\dagger a.
$$

For an integer $N\ge n$, the logical input is embedded by the fixed-excitation isometry

$$
V_N|x\rangle=|x\rangle|N-|x|\rangle.
$$

The logical input may be mixed and may be entangled with the reference. The encoding is the fixed-excitation interface of the shared-battery architecture of Kurman and collaborators.[^kurman]

Choose a target qubit $j$. During the pulse its real coupling is $g>0$, every spectator coupling is zero, and all detunings are zero in the battery rotating frame. The physical evolution is

$$
\frac{d\sigma}{dt}
=-i[H,\sigma]+\kappa\mathcal D[a](\sigma),
\qquad
H=g(a\sigma_j^++a^\dagger\sigma_j^-),
$$

$$
\mathcal D[L](\sigma)
=L\sigma L^\dagger-\frac12\{L^\dagger L,\sigma\}.
$$

Here $\sigma_j^+=|1\rangle\langle0|_j$. The loss rate $\kappa$ is a physical rate. The emitted field is inaccessible. There is no measurement, feedback, recharge, or additional energy-changing drive during the pulse. Independently switchable couplers are an explicit control assumption; replacing zero spectator couplings by finite detuning would require an additional crosstalk estimate.

Let $\mathcal G_T$ denote the logical channel obtained by encoding, evolving for time $T$, and applying the canonical decoder defined below. The error is

$$
\delta_X(T)
=\frac12\left\|\mathcal G_T-\mathcal X_j\right\|_\diamond,
\qquad
\mathcal X_j(\rho)=X_j\rho X_j.
$$

The reference is retained when this distance is evaluated.

## A completely positive decoder and the exact loss-sector equations

Let $\mathsf H_{\le N}$ be the physical subspace with total excitation at most $N$. On its computational–Fock basis define

$$
D_N\bigl(|x\rangle|m\rangle\bigr)
=|x\rangle|N-m-|x|\rangle_F,
\qquad m+|x|\le N.
$$

Distinct input basis vectors have distinct output basis vectors, so $D_N$ is an isometry. Its flag is the total excitation lost, $\ell=N-Q$. Tracing the flag gives the canonical logical decoder. It leaves the register label $x$ unchanged.

For completeness, let $P_{\le N}$ project onto $\mathsf H_{\le N}$ and let $\tau_0$ be any fixed logical density operator. A channel on the entire physical Hilbert space is

$$
\mathcal D_N(\sigma)
=\operatorname{Tr}_F\!\left[
D_NP_{\le N}\sigma P_{\le N}D_N^\dagger
\right]
+\operatorname{Tr}\!\left[(I-P_{\le N})\sigma\right]\tau_0.
$$

This map is completely positive and trace preserving. The second term is never used by the evolution considered here: the Hamiltonian preserves $Q$, each loss lowers it by one, and the initial state has $Q=N$.

After tracing the bath, the physical state is block diagonal in $Q$. Identify the block $Q=N-\ell$ with a subnormalized logical state $\rho_\ell$, including its reference. Its support obeys $W\le N-\ell$. Logical basis states outside this support are padded by zero. Define $W_s=W-n_j$ and $z_+=\max\{z,0\}$. On the full padded logical space set

$$
A_\ell=\sqrt{(N-\ell-W)_+},\qquad
H_\ell=g\sqrt{(N-\ell-W_s)_+}\,X_j.
\tag{1}
$$

These operators give an exact representation. For a spectator string of weight $w_s$, the target coupling connects

$$
|0_j,x_s,N-\ell-w_s\rangle
\quad\text{and}\quad
|1_j,x_s,N-\ell-w_s-1\rangle
$$

with matrix element $g\sqrt{N-\ell-w_s}$. If the second state is unavailable, the matrix element is zero. Thus $H_\ell$ preserves the valid support. Likewise $A_\ell$ annihilates its boundary $W=N-\ell$, so a jump has valid support in the next block.

The sector equations are

$$
\dot\rho_\ell
=-i[H_\ell,\rho_\ell]
-\frac\kappa2\{A_\ell^2,\rho_\ell\}
+\kappa A_{\ell-1}\rho_{\ell-1}A_{\ell-1},
\tag{2}
$$

with the last term absent for $\ell=0$. They hold for $0\le\ell\le N$, with all operators tensored with the reference identity. In particular,

$$
\rho_\ell\ge0,\qquad
\sum_{\ell=0}^N\operatorname{Tr}\rho_\ell=1,
\qquad
\mathcal G_t(\rho)=\sum_{\ell=0}^N\rho_\ell(t).
$$

No approximation of $\sqrt{N-W}$ by a scalar has been made.

## A comparison bound that charges logical noise

Choose an integer cutoff $L$ with $N-L>n$. Define an artificial channel that follows (2) through sector $L$. The next jump deposits $\kappa A_L\rho_LA_L$ into an absorbing failure flag. After this jump, the logical state evolves under a chosen ideal Hamiltonian $H_*(t)$ and experiences no further loss. The good sectors retain their exact original dynamics. This is a completely positive, trace-preserving channel on the logical register and flags.

The actual and artificial channels agree until the first jump producing loss count $L+1$. Quantum-jump histories provide a completely positive decomposition according to this first hitting event. Their common prefix has the same trace in both channels; either continuation preserves that trace. Consequently their output half-trace distance is at most

$$
p_{\rm bad}(T)=\Pr\{\ell(T)\ge L+1\}.
\tag{3}
$$

This argument holds with an arbitrary reference. A uniform upper bound on this probability therefore bounds half the diamond distance between the actual and artificial decoded channels. This is a comparison construction, not a measurement or control operation required of the processor.

Let $\widetilde\rho$ be the sum of all good logical blocks and the failure block in the artificial channel. Adding their equations gives

$$
\dot{\widetilde\rho}
=-i[H_*,\widetilde\rho]
+\sum_{\ell=0}^L
\left\{-i[H_\ell-H_*,\rho_\ell]
+\kappa\mathcal D[A_\ell](\rho_\ell)\right\}.
\tag{4}
$$

The large scalar part of the jump amplitude has disappeared from the reduced logical derivative. More precisely, for Hermitian $A$ and real $c$,

$$
\mathcal D[A-cI]=\mathcal D[A].
\tag{5}
$$

On every good sector the full logical space is valid. The eigenvalue diameter of $A_\ell$ is

$$
d_\ell
=\sqrt{N-\ell}-\sqrt{N-\ell-n}
=\frac{n}{\sqrt{N-\ell}+\sqrt{N-\ell-n}}.
\tag{6}
$$

Choose $c$ at the midpoint of this interval. Then $\|A_\ell-cI\|=d_\ell/2$. For every positive subnormalized state, including its reference,

$$
\left\|\mathcal D[A_\ell](\rho_\ell)\right\|_1
\le \frac{d_\ell^2}{2}\operatorname{Tr}\rho_\ell.
\tag{7}
$$

Indeed the sandwich term and the anticommutator together have trace norm at most $2\|A_\ell-cI\|^2\operatorname{Tr}\rho_\ell$. A Hamiltonian commutator similarly obeys

$$
\frac12\|[K,\rho_\ell]\|_1
\le\|K\|\operatorname{Tr}\rho_\ell.
$$

Let $U_*$ be the propagator of $H_*$. Duhamel's formula in its interaction frame, (3), and (7) prove the general bound

$$
\begin{aligned}
\frac12\left\|\mathcal G_T-\mathcal U_*(T)\right\|_\diamond
\le{}&p_{\rm bad}(T)\\
&+\sup_\rho\int_0^T
\sum_{\ell=0}^L\|H_\ell-H_*(t)\|
\operatorname{Tr}\rho_\ell(t)\,dt\\
&+\frac{\kappa n^2T}{16(N-L-n)}.
\end{aligned}
\tag{8}
$$

The supremum includes reference-entangled inputs. The last term follows from $d_\ell^2\le n^2/[4(N-L-n)]$ and $\sum_{\ell=0}^L\operatorname{Tr}\rho_\ell\le1$. Equation (8) bounds the logical effect of all photon losses, including trajectories containing many jumps.

## Theorem 1: a native-clock gate at fixed bare coupling

Assume $N\ge4n$, and define

$$
\nu=N-\frac{n-1}{2},\qquad
T=\frac{\pi}{2g\sqrt\nu},\qquad
L=\lfloor N/2\rfloor.
\tag{9}
$$

The addressed resonant pulse and canonical decoder satisfy

$$
\begin{aligned}
\delta_X(T)\le{}&
\frac{\kappa NT}{L+1}\\
&+\frac{g\bigl[(n-1)T/2+\kappa NT^2/2\bigr]}
{\sqrt\nu+\sqrt{N-L-n+1}}\\
&+\frac{\kappa n^2T}{16(N-L-n)}.
\end{aligned}
\tag{10}
$$

In particular, writing $\Omega=g\sqrt N$,

$$
\boxed{
\delta_X(T)
\le
\frac{2n}{N}
+\frac{7\kappa}{\Omega}
+\frac{\kappa n^2}{N\Omega}.
}
\tag{11}
$$

Every error bound can also be capped at one.

### Proof

The loss-count intensity is at most $\kappa N$, so

$$
\mathbb E\ell(t)\le\kappa Nt,
\qquad
p_{\rm bad}(T)\le\frac{\kappa NT}{L+1}.
\tag{12}
$$

Use the constant comparison Hamiltonian $H_*=g\sqrt\nu X_j$. Rationalizing the square roots in (1), and using $0\le W_s\le n-1$, gives

$$
\|H_\ell-H_*\|
\le
\frac{g[\ell+(n-1)/2]}
{\sqrt\nu+\sqrt{N-L-n+1}}
\quad(\ell\le L).
\tag{13}
$$

The good-sector states of the artificial and original channels coincide. Their weighted good-sector loss count is bounded by the full original expectation in (12). Integrating (13) therefore bounds the Hamiltonian term in (8) by the second term of (10). The chosen duration gives $U_*(T)=-iX_j$. This proves (10).

For the simplified bound, use

$$
N-L-n\ge N/4,\qquad
\sqrt\nu+\sqrt{N-L-n+1}\ge\sqrt N,
$$

$$
T\le\frac{\pi}{g\sqrt{2N}},\qquad
L+1\ge N/2.
$$

The respective coefficients of $n/N$, $\kappa/(g\sqrt N)$, and $\kappa n^2/(gN^{3/2})$ are at most

$$
\frac{\pi}{2\sqrt2}<2,\qquad
\frac{\pi^2}{4}+\sqrt2\pi<7,\qquad
\frac{\pi}{4\sqrt2}<1.
$$

This proves (11).

### Consequences

At fixed $g,\kappa>0$, the choice $N/n^{4/3}\to\infty$ makes every term in (11) vanish. A finite sufficient condition for error at most $\varepsilon>0$ is

$$
N\ge\max\left\{
4n,\frac{6n}{\varepsilon},
\left(\frac{21\kappa}{g\varepsilon}\right)^2,
\left(\frac{3\kappa n^2}{g\varepsilon}\right)^{2/3}
\right\}.
\tag{14}
$$

This upper bound uses one target gate on the full arbitrary register. It does not assume that spectators have known classical weights. Their coherences, and their entanglement with the target and reference, are included in the diamond-norm statement.

## Theorem 2: a depletion-calibrated gate at a fixed Rabi-rate ceiling

Fix $\Omega>0$ and choose the bare target coupling $g=\Omega/\sqrt N$. Then every target transition in every occupied sector has coupling at most $\Omega$. The bare coupling remains constant throughout the pulse.

For $\kappa>0$, assume

$$
\Omega>\frac{\pi\kappa}{4},
$$

and define

$$
T=-\frac2\kappa
\log\left(1-\frac{\pi\kappa}{4\Omega}\right),
\qquad
\eta=e^{-\kappa T}
=\left(1-\frac{\pi\kappa}{4\Omega}\right)^2.
\tag{15}
$$

Assume $N\ge4n/\eta$. The same constant-coupling resonant pulse, now run for the calibrated time (15), satisfies

$$
\boxed{
\begin{aligned}
\delta_X(T)\le{}&
\frac{2(1-\eta^2)}{\eta^2N}
+\frac{2\Omega\sqrt\kappa\,T^{3/2}}
{3\sqrt\eta\sqrt N}\\
&+\frac{\Omega(2n-1)T}{\sqrt\eta N}
+\frac{\kappa n^2T}{4\eta N}.
\end{aligned}
}
\tag{16}
$$

For $\kappa=0$, use the continuous convention $T=\pi/(2\Omega)$ and $\eta=1$; the terms containing loss vanish.

At fixed positive $\kappa,\Omega$ satisfying the displayed solvability condition, $T$ and $\eta$ are constants. Therefore $N/n^2\to\infty$ makes (16) vanish while respecting the fixed Rabi-rate ceiling. The constants worsen as $\Omega$ approaches $\pi\kappa/4$ from above; that dependence is explicit.

### Count fluctuations around deterministic depletion

Photon counting of the emitted field is used only as a mathematical unraveling. It is not accessible to the processor or decoder. Let $\rho_c(t)$ be the normalized conditional state and $w_c(t)=\operatorname{Tr}[W\rho_c(t)]$. The exact identity $Q=N-\ell(t)$ gives intensity

$$
\lambda(t)=\kappa[N-\ell(t)-w_c(t)],
\qquad 0\le\lambda(t)\le\kappa N.
$$

The compensated count

$$
M(t)=\ell(t)-\int_0^t\lambda(s)\,ds
$$

is a martingale with predictable quadratic variation $\int_0^t\lambda(s)\,ds$. Solving the count equation with an integrating factor gives the exact identity

$$
\ell(t)
=N(1-e^{-\kappa t})
-\kappa\int_0^t e^{-\kappa(t-s)}w_c(s)\,ds
+Z(t),
\tag{17}
$$

$$
Z(t)=\int_0^t e^{-\kappa(t-s)}\,dM(s).
$$

The martingale isometry and the intensity bound imply

$$
\mathbb E Z(t)^2
=\mathbb E\int_0^t e^{-2\kappa(t-s)}\lambda(s)\,ds
\le\frac N2(1-e^{-2\kappa t})
\le\kappa Nt.
\tag{18}
$$

Since $0\le w_c\le n$, equations (17)–(18) yield

$$
\mathbb E\left|
\ell(t)-N(1-e^{-\kappa t})
\right|
\le\sqrt{\kappa Nt}+n(1-e^{-\kappa t}).
\tag{19}
$$

These statements hold uniformly over all input states, including reference-entangled inputs.

Choose

$$
L=\left\lfloor N(1-\eta/2)\right\rfloor.
$$

The loss count is monotone. At the final time, the failure event implies

$$
\ell(T)-N(1-\eta)>\eta N/2.
$$

The integral subtracted in (17) is nonnegative, so this event requires $Z(T)>\eta N/2$. Chebyshev's inequality and (18) prove

$$
p_{\rm bad}(T)
\le\frac{2(1-\eta^2)}{\eta^2N}.
\tag{20}
$$

This vanishing tail is needed at fixed $\Omega$. A first-moment bound on the total number of emitted photons would not suffice, because the expected count is of order $N$ over this pulse.

### Calibrated coherent evolution and logical dissipation

Use the comparison Hamiltonian

$$
H_*(t)=\Omega e^{-\kappa t/2}X_j.
\tag{21}
$$

Its pulse area is

$$
\int_0^T\Omega e^{-\kappa t/2}\,dt
=\frac{2\Omega}{\kappa}(1-\sqrt\eta)
=\frac\pi2,
$$

so its final unitary is $-iX_j$. No time-dependent bare coupling is used in the actual protocol; (21) describes the deterministic photon-depletion reference against which the constant-coupling pulse is compared.

Let $m(t)=N(1-e^{-\kappa t})$. On good sectors, rationalizing square roots gives

$$
\|H_\ell-H_*(t)\|
\le
\frac{g[|\ell-m(t)|+n-1]}
{\sqrt{N-L-n+1}+\sqrt{N\eta}}.
\tag{22}
$$

The denominator is at least $\sqrt{N\eta}$. The weighted sum over good-sector states is bounded by the full original expectation in (19), because those good-sector states coincide exactly in the actual and artificial channels. Thus the Hamiltonian term in (8) is at most

$$
\frac{g}{\sqrt{N\eta}}
\left[
\frac23\sqrt{\kappa N}\,T^{3/2}
+n\int_0^T(1-e^{-\kappa t})\,dt
+(n-1)T
\right].
\tag{23}
$$

Using $g=\Omega/\sqrt N$ and bounding the integral by $T$ turns (23) into the second and third terms of (16).

Finally,

$$
N-L-n\ge\frac{\eta N}{2}-n\ge\frac{\eta N}{4}.
$$

The dissipative term of (8) is consequently at most $\kappa n^2T/(4\eta N)$. Combining it with (20) and (23) proves (16).

## Resource interpretation and limits of the claims

The two regimes distinguish photon energy from available operation speed. At fixed bare $g$, increasing $N$ increases the available rate $\Omega=g\sqrt N$ and shortens the pulse. The controlling dissipative term is

$$
\frac{\kappa n^2}{N\Omega}.
$$

At a fixed rate ceiling, the calibrated construction instead uses a smaller bare coupling as $N$ grows and takes a constant physical time. Its error scales as $n^2/N$, up to the explicit lower-order terms and constants in (16). This conclusion does not rely on increasing $g$ as the battery depletes. The condition $\Omega>\pi\kappa/4$ is the finite-time solvability condition for this particular constant-coupling calibrated pulse; no impossibility claim for other protocols is inferred when it fails.

The pulse acts on an arbitrary already dressed register. The decoder is an ideal terminal interface with access to the register and surviving battery. Its physical synthesis time, noise, ancillas, and energy are not included in these bounds. It reads total loss but never receives the emitted field or its emission times. Because it preserves the register basis label, the theorem's small logical error also implies the corresponding target population transfer before decoding.

The results establish one native gate and its recovered error. They do not establish an entire fault-tolerant computation, a universal efficient compiler, or an inexpensive physical decoder. An arbitrary terminal recovery could itself supply a target unitary, so a runtime lower bound must refer to a prescribed native clock or to a gate actually performed before unrestricted recovery. The constructions here specify the physical pulse and use only the canonical terminal identification.

Finally, the Jaynes–Cummings model and its rotating-wave regime are assumptions. In the fixed-$g$ asymptotic regime, the increasing rate $g\sqrt N$ must remain within the physically available carrier and control bandwidth. The fixed-$\Omega$ theorem makes the rate ceiling explicit instead. Neither theorem is an encoding-independent or hardware-independent energy lower bound.

[^kurman]: Y. Kurman, K. Hymas, A. Fedorov, W. J. Munro, and J. Quach, “Powering Quantum Computation with Quantum Batteries,” *Physical Review X* **16**, 011016 (2026), [doi:10.1103/l39v-jwwz](https://doi.org/10.1103/l39v-jwwz), [arXiv:2503.23610](https://arxiv.org/abs/2503.23610). The native-gate bounds and comparison proofs in this note are derived for the explicit control and noise model stated above.
