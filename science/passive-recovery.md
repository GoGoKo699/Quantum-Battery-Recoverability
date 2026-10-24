# Exact passive recovery and protected interfaces

The idle channel makes the physical mechanism explicit. Losing a photon shifts total excitation into an orthogonal syndrome sector, which a joint decoder can identify. The remaining logical disturbance comes from the dependence of loss probabilities on register weight. This section solves that recovery problem exactly and separates it from the [native-control converse](control-converse.md).

The initial interface and error convention are those of [Model](model.md). The oscillator undergoes pure loss with transmissivity $0<\eta<1$ and loss probability $p_{\mathrm{loss}}=1-\eta$. Its Stinespring action is

$$
|m\rangle_B\longmapsto
\sum_{\ell=0}^{m}\sqrt{P_m(\ell)}
|m-\ell\rangle_B|\ell\rangle_E,
\qquad
P_m(\ell)=\binom m\ell p_{\mathrm{loss}}^\ell\eta^{m-\ell}.
$$

For a Markov idle interval of duration $t$, $\eta=e^{-\kappa t}$. The count-only environment representation is sufficient for this idle channel. Native control during emission requires the fuller time-resolved argument in the converse.

## 1. The loss syndrome and its surviving coherence

The Kraus component for $\ell$ lost photons lies in total-excitation sector $N-\ell$. The canonical decoder identifies valid vectors with $|x\rangle|\ell\rangle$, as in [Model](model.md#3-what-the-error-measures). After this identification the flagged Kraus operators are positive and diagonal:

$$
D_\ell=\sum_x\sqrt{P_{N-w(x)}(\ell)}|x\rangle\langle x|.
$$

Define the $(n+1)\times(n+1)$ affinity matrix

$$
B_{wv}=\sum_{\ell\ge0}
\sqrt{P_{N-w}(\ell)P_{N-v}(\ell)}.
$$

It is a positive semidefinite Gram matrix, with $B_{ww}=1$ and entries in $[0,1]$. Discarding the syndrome gives the Schur channel

$$
\mathcal C_B(|x\rangle\langle y|)
=B_{w(x),w(y)}|x\rangle\langle y|.
$$

Thus no-loss survival and logical recovery are different quantities. An observed total-excitation shift is correctable; the environmental distinction between weights is not generally reversible.

## 2. Exact optimal recovery theorem

Let $\Delta_{n+1}$ be the probability simplex. Then

$$
\boxed{\displaystyle
\inf_{\mathcal R}\frac12
\|\mathcal R\mathcal N_{\mathrm{pass}}-\mathrm{id}\|_\diamond
=1-\min_{u\in\Delta_{n+1}}u^\mathsf TB u.}
$$

The canonical decoder attains the optimum. The optimal worst-input entanglement fidelity is the complementary quantity $\min_u u^\mathsf TB u$, using squared overlap with the ideal purification as the fidelity convention. Weight degeneracies do not enter this worst-case minimum.

### Recovery converse

Select one orthonormal vector $|w\rangle$ from each weight sector and use the diagonal logical input $\rho_u=\sum_w u_w|w\rangle\langle w|$. The loss output is block diagonal in $\ell$, so any recovery can be represented by conditional Kraus operators $R_{\ell r}$ on these sectors. With $d_{\ell w}=\sqrt{P_{N-w}(\ell)}$, its entanglement fidelity is

$$
F_e=\sum_{\ell,r}
\left|\sum_w u_w d_{\ell w}(R_{\ell r})_{ww}\right|^2.
$$

For fixed $\ell,w$, trace preservation bounds the Euclidean norm of the vector $((R_{\ell r})_{ww})_r$ by one. The triangle inequality therefore gives

$$
F_e\le\sum_\ell\left(\sum_w u_wd_{\ell w}\right)^2=u^\mathsf TB u.
$$

An absent state in a depleted sector has $d_{\ell w}=0$ and contributes nothing. Measuring the ideal output projector bounds half trace distance below by $1-F_e$, establishing the diamond lower bound for every recovery.

This argument extends the conditional polar-recovery structure of Gregoratti–Werner to all diagonal input distributions in this positive-Kraus instrument. Their established maximally mixed-input result must be credited; see [Related work](../references/related-work.md).

### Diamond-norm attainment

A pure input including a reference can be written $\sum_x|x\rangle|v_x\rangle$. The vectors with different $x$ are orthogonal because of the register factor, regardless of their reference overlaps. After normalizing their lengths and combining equal-weight sectors, the trace-norm difference produced by $\mathrm{id}-\mathcal C_B$ is that of

$$
M_u=\operatorname{diag}(\sqrt u)(J-B)\operatorname{diag}(\sqrt u),
$$

where $J$ is the all-ones matrix. This matrix has zero trace and is a rank-one positive matrix minus a positive semidefinite matrix. It has at most one positive eigenvalue, so half its trace norm equals $\lambda_{\max}(M_u)$.

Its entries are nonnegative. Choose a nonnegative unit Perron eigenvector $v$, set $z_w=\sqrt{u_w}v_w$, and put $s=\sum_wz_w\le1$. If $s>0$, set $r=z/s$. Then

$$
\lambda_{\max}(M_u)=s^2(1-r^\mathsf TBr)
\le1-\min_r r^\mathsf TBr.
$$

The zero case is immediate. This proves the required upper bound on every reference input. Conversely, if $u_*$ minimizes the quadratic form, the Rayleigh vector $v=\sqrt{u_*}$ gives $1-u_*^\mathsf TBu_*$. The upper bound is attained. The decoder's entanglement fidelity on any input depends only on its diagonal weight probabilities and equals the same quadratic form.

## 3. Finite energy bounds

Two useful estimates do not require an asymptotic normal approximation.

First, split the two binomial distributions at the midpoint of their means. Hoeffding's inequality and Cauchy–Schwarz give

$$
B_{wv}\le\min\left\{1,
2\exp\left[-\frac{p_{\mathrm{loss}}^2(w-v)^2}{4N}\right]\right\}.
$$

Using the uniform distribution on weights and bounding the Gaussian sum by its integral yields

$$
\delta_{\mathrm{pass}}
\ge\max\left\{0,
1-\frac{1+4\sqrt{\pi N}/p_{\mathrm{loss}}}{n+1}\right\}.
$$

At fixed $\eta$, this proves $\delta_{\mathrm{pass}}\to1$ when $N=o(n^2)$.

For a complementary upper bound, let $K\sim\mathrm{Bin}(m,\eta)$ be the surviving count. The adjacent affinity obeys

$$
B_{m,m-1}=\mathbb E\sqrt{\frac{K}{m\eta}},
\qquad
1-B_{m,m-1}\le\frac{p_{\mathrm{loss}}}{2m\eta}.
$$

Here subscripts denote photon occupations. The estimate follows from $\mathbb EX=1$ and
$1-\mathbb E\sqrt X=\tfrac12\mathbb E(\sqrt X-1)^2\le\tfrac12\mathbb E(X-1)^2$.
Applying the triangle inequality to the square-root probability vectors along adjacent occupations gives

$$
1-B_{wv}\le
\frac{p_{\mathrm{loss}}(w-v)^2}{2\eta(N-n+1)}.
$$

Since $\max\operatorname{Var}(W)=n^2/4$ on $[0,n]$, the exact theorem implies

$$
\delta_{\mathrm{pass}}
\le\min\left\{1,
\frac{p_{\mathrm{loss}}n^2}{4\eta(N-n+1)}\right\}.
$$

Thus $N\gg n^2$ suffices at fixed transmissivity. The passive leading small-error converse, including a sharper coefficient, follows from existing covariant-QEC bounds of Zhou–Liu–Jiang. The dynamic result does not claim priority for that quadratic passive scale.

## 4. Infinitesimal logical noise

For a short idle interval $dt$ at fixed $n,N$,

$$
B_{wv}=1-\frac{\kappa\,dt}{2}
\left(\sqrt{N-w}-\sqrt{N-v}\right)^2+O(dt^2).
$$

The one-jump and no-jump terms give this expansion directly. For a distribution $u$, the first-order loss of $u^\mathsf TBu$ is $\kappa\,dt$ times the variance of $\sqrt{N-W}$. The maximal variance of a quantity in an interval is one quarter of its squared diameter, attained by equal endpoint masses. Hence

$$
\delta_{\mathrm{pass}}(dt)
=\frac{\kappa\,dt}{4}
\left(\sqrt N-\sqrt{N-n}\right)^2+O(dt^2).
$$

For $N\gg n$ the coefficient is asymptotic to $\kappa n^2/(16N)$. This identifies the environmental resolution rate. The [control converse](control-converse.md) proves that bounded native motion cannot immediately remove this vulnerability; it does not merely substitute a gate time into the idle expression.

## 5. Ideal input randomization

Suppose a fresh logical unitary $U_s$ is permitted **before the noisy interval**, with seed independent of the unknown input, a recovery that knows the seed, and only the averaged quantum state delivered at the output. The encoder is now $V_NU_s$, which changes the initial interface. Let

$$
b_w=2^{-n}\binom nw.
$$

The optimum over all such full-dimensional randomized unitary encodings and terminal recoveries is

$$
\delta_{\mathrm{rand}}=1-b^\mathsf TBb.
$$

For the lower bound, the maximally mixed logical input is invariant under the unitary encoder. The best conditional-recovery entanglement fidelity on its purification is $b^\mathsf TBb$, independent of that unitary. Linearity of entanglement fidelity preserves this bound under averaging.

For attainment, choose a uniform bit mask $s\in\{0,1\}^n$, apply $X^s$, decode, and apply $X^s$ again. Averaging makes the Schur kernel depend only on $x\oplus y$. Its Fourier transform on the binary group is nonnegative because the kernel is positive semidefinite, so the resulting channel is a mixture of Pauli $Z$ strings. The identity Pauli has probability $b^\mathsf TBb$. A maximally entangled input distinguishes the Pauli branches, giving half diamond distance exactly one minus that probability. This is an application of established Pauli twirling, not a new general randomization principle.

Since two independent binomial weights satisfy $\mathbb E(W-W')^2=n/2$, the finite affinity estimate gives

$$
\delta_{\mathrm{rand}}
\le\min\left\{1,
\frac{p_{\mathrm{loss}}n}{4\eta(N-n+1)}\right\}.
$$

The mask must physically change the dressed excitation assignment. A software relabeling does not change the photon-loss statistics. A native mask started after $V_N$ is subject to the dynamic converse. The exact randomized optimum above also specifies an averaged quantum output without a retained seed register; other output conventions and seed reuse require their own channel analysis.

## 6. Protected subspaces and their exact dimension

Restricting the logical input to a single weight $w$ fixes the initial photon occupation at $N-w$. Every $D_\ell$ is then scalar on the code. The decoder corrects the idle loss exactly for every transmissivity, including complete loss. The largest weight space has dimension

$$
d_{\max}=\binom n{\lfloor n/2\rfloor}.
$$

This is also the largest possible dimension of an exactly correctable subspace of the full dressed input for any nonzero loss probability. To prove optimality, the distributions $P_{N-w}(\ell)$ are linearly independent as functions of $\ell$: their largest nonzero indices $N-w$ are distinct, so the appropriate submatrix is triangular with nonzero diagonal. The operators $D_\ell^2$ therefore span all weight projectors $\Pi_w$.

The Knill–Laflamme condition for a code projector $P$ consequently requires $P\Pi_wP=\alpha_wP$, with $\alpha_w\ge0$ and $\sum_w\alpha_w=1$. Choose a weight with $\alpha_w>0$. Then $\Pi_w$ is injective on the code, because $\|\Pi_w|\psi\rangle\|^2=\alpha_w\|\psi\|^2$. Therefore

$$
\operatorname{rank}P\le\operatorname{rank}\Pi_w\le d_{\max}.
$$

The central weight sector attains the bound. It stores $\lfloor\log_2d_{\max}\rfloor=n-\tfrac12\log_2n-O(1)$ exact logical qubits. This is the familiar decoherence-free-subspace mechanism in the present interface. Whole-register diamond-error collapse must therefore not be described as vanishing information capacity of the hardware. Gates that move the state out of a protected weight sector require a separate operational analysis.

## 7. Numerical evaluation

The affinity vectors are computed directly from binomial probabilities. The minimization is a convex quadratic program because $B\succeq0$. A feasible candidate $u$ has the rigorous convex supporting-plane lower estimate

$$
\min_v v^\mathsf TBv\ge2\min_w(Bu)_w-u^\mathsf TBu.
$$

Thus $2[u^\mathsf TBu-\min_w(Bu)_w]$ is an optimization-gap certificate in exact arithmetic. The [finite checks](../verification/README.md) report its floating-point evaluation and separately check normalization and matrix positivity. This makes clear what the numerical minimization verifies without using it as a proof of the theorem.
