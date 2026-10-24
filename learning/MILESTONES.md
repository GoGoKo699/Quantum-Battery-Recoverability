# Project understanding map: 30 milestones

This map follows the scientific argument of quantum-battery recoverability through exactly **30 milestones**. Its targets and order are determined by the project, not by a particular reader’s background. It is common to human readers and LLMs.

The allocation is **14 background/preliminaries milestones** and **16 narrative/innovation milestones**. The preliminary phase gives quantum-channel geometry and photon-count dynamics separate foundations before combining them into the operational question. The narrative then proceeds from the dressed interface and an exactly solved idle channel to the active-control converse, explicit native gates, and the complete resource account. Each phase builds from local objects and steps toward their global scientific meaning.

The single educational anchor is Howard M. Wiseman and Gerard J. Milburn’s *Quantum Measurement and Control* (2010). The [Wiseman–Milburn bridge](WISEMAN_MILBURN_BRIDGE.md) owns the edition, verified section map, notation translation, and mathematical steps supplied locally. Its main reading route uses Chapters 1, 3, and 4 and §7.4. A pointer to an anchor section supplies its stated context; the bridge identifies the channel, probability, and spectral arguments that are developed locally. The linked scientific pages remain authoritative for exact statements, hypotheses, and complete proofs.

Each milestone supplies a central question, an understanding target, earlier prerequisites, its role in the story, a conceptual connection, and canonical sources. The map does not replace the proof files.

## Route through the project

| Phase | Milestones | Connection established |
|---|---|---|
| Background/preliminaries | [M01](#m01-qubit-and-oscillator-states)–[M04](#m04-measurement-outcomes-and-retained-records) | Local systems, coherent exchange, composite states, and measurement records |
| Background/preliminaries | [M05](#m05-quantum-channels-and-their-environments)–[M07](#m07-recovery-error-with-a-reference) | Channels, environments, distinguishability, and recovery with a reference |
| Background/preliminaries | [M08](#m08-markov-loss-and-the-lindblad-generator)–[M11](#m11-moment-bounds-and-count-discrimination) | Markov loss, trajectories, compensated counts, and finite discrimination |
| Background/preliminaries | [M12](#m12-positive-kernels-and-spectral-bounds)–[M14](#m14-the-complete-recoverability-problem) | Spectral and dynamical tools assembled into the full operational question |
| Narrative/innovation | [M15](#m15-the-dressed-interface-and-its-loss-sectors)–[M19](#m19-protected-and-randomized-input-interfaces) | Dressed loss sectors, exact passive recovery, and changes of input interface |
| Narrative/innovation | [M20](#m20-how-quickly-native-control-moves-weight)–[M25](#m25-a-gate-duration-supplied-by-native-dynamics) | Native motion, irreversible early records, the converse, and a justified gate clock |
| Narrative/innovation | [M26](#m26-the-exact-channel-of-an-addressed-pulse)–[M28](#m28-constructive-gates-under-two-speed-conventions) | Exact gate dynamics and attainable bounds in both speed regimes |
| Narrative/innovation | [M29](#m29-attribution-and-the-strength-of-the-evidence)–[M30](#m30-the-complete-energy-and-recoverability-account) | Attribution, verification, and the complete resource account |

## Phase I: background/preliminaries

### M01 Qubit and oscillator states

**Central question.** What are the local quantum systems whose excitations the architecture exchanges?

**Understanding target.** Interpret qubit populations, oscillator number states, and their ladder operators before introducing a controller. Keep the number of register qubits, the oscillator occupation, and the dimension of a state space distinct.

**Prerequisites.** None within this map.

**Story role.** Establishes the local physical objects used throughout both phases.

**Conceptual connection.** An oscillator number is an energy label; it is not a count of independent logical qubits.

**Canonical sources.** W&M §§A.1, A.4, and 1.2; [local dressed-qubit example](WISEMAN_MILBURN_BRIDGE.md#a-dressed-qubit-worked-from-loss-to-logical-error); [register and battery](../science/model.md#1-register-and-battery).

### M02 Coherent exchange and conserved excitation

**Central question.** Which transitions does the native interaction permit, and what do they conserve?

**Understanding target.** Read the two terms of a Jaynes–Cummings exchange as opposite excitation transfers. Identify invariant total-excitation sectors and the occupation dependence of a transition amplitude. Separate a bound on one coupler from a bound on the complete Hamiltonian.

**Prerequisites.** [M01](#m01-qubit-and-oscillator-states).

**Story role.** Connects a local matrix element to the physical control resource.

**Conceptual connection.** A large battery can increase an exchange rate without adding an independently addressable logical degree of freedom.

**Canonical sources.** W&M §§3.2–3.3 for open-system context; [native-control bridge](WISEMAN_MILBURN_BRIDGE.md#bounded-control-and-the-native-clock); [allowed native dynamics](../science/model.md#2-native-dynamics-and-inaccessible-radiation).

### M03 Reduced states and entangled references

**Central question.** What information can disappear from a subsystem while the joint state remains coherent?

**Understanding target.** Use tensor products, partial traces, and purifications to distinguish a subsystem state from its correlations with an inaccessible system. Interpret an inert reference as part of an input specification rather than a control resource.

**Prerequisites.** [M01](#m01-qubit-and-oscillator-states).

**Story role.** Introduces the correlations that a quantum memory must preserve.

**Conceptual connection.** Correct output populations alone do not establish that an unknown quantum state, including its external correlations, has survived.

**Canonical sources.** W&M §§A.2 and 1.2; [channel geometry bridge](WISEMAN_MILBURN_BRIDGE.md#channel-geometry-and-the-recovery-witness); [operational error](../science/model.md#3-what-the-error-measures).

### M04 Measurement outcomes and retained records

**Central question.** How do an outcome probability and a conditional state fit into one physical measurement?

**Understanding target.** Distinguish effects, state-update operators, and a measurement instrument. Track whether an outcome is retained, discarded, or accessible to a later operation. Treat a classical random seed and a physically observed syndrome as different records.

**Prerequisites.** [M01](#m01-qubit-and-oscillator-states), [M03](#m03-reduced-states-and-entangled-references).

**Story role.** Makes the location and availability of information explicit.

**Conceptual connection.** Discarding a label changes a channel; knowing a label does not by itself reverse the disturbance associated with obtaining it.

**Canonical sources.** W&M §§1.3–1.4; [rate and record conventions](WISEMAN_MILBURN_BRIDGE.md#conventions-that-keep-rates-consistent); [accessible seed and recovery](../science/control-converse.md#model-and-operational-error).

### M05 Quantum channels and their environments

**Central question.** How can the same noisy operation be described through Kraus operators or an environment?

**Understanding target.** Relate completely positive trace-preserving maps, isometric dilations, and complementary outputs. Understand why different descriptions of an inaccessible environment must represent the same physical channel, and how a recovery can be appended to a dilation.

**Prerequisites.** [M03](#m03-reduced-states-and-entangled-references), [M04](#m04-measurement-outcomes-and-retained-records).

**Story role.** Supplies the mathematical language for arbitrary terminal recovery.

**Conceptual connection.** A proof using a measurement on a complementary output does not grant the processor access to that output.

**Canonical sources.** W&M §1.4 as measurement context; [local channel and dilation steps](WISEMAN_MILBURN_BRIDGE.md#channel-geometry-and-the-recovery-witness); [environmental recovery proof](../science/control-converse.md#proof-why-terminal-recovery-cannot-undo-the-record).

### M06 Distinguishability and root fidelity

**Central question.** How can distinguishable environmental states constrain surviving coherence?

**Understanding target.** Keep classical total variation, quantum trace distance, and root fidelity separate. Follow their behavior under measurement and partial trace, and identify which direction of each inequality is needed when converting an observed distinction into a fidelity bound.

**Prerequisites.** [M04](#m04-measurement-outcomes-and-retained-records), [M05](#m05-quantum-channels-and-their-environments).

**Story role.** Builds the quantitative link between a field record and quantum coherence.

**Conceptual connection.** An upper bound on environmental overlap has a different operational meaning from an upper bound on a processor's state error.

**Canonical sources.** W&M §§1.3–1.4 for measurement context; [locally supplied channel geometry](WISEMAN_MILBURN_BRIDGE.md#channel-geometry-and-the-recovery-witness); [fidelity conventions and cross terms](../science/control-converse.md#proof-why-terminal-recovery-cannot-undo-the-record).

### M07 Recovery error with a reference

**Central question.** What must a recovery preserve to protect an arbitrary logical input?

**Understanding target.** Define the optimization over deterministic recovery maps and distinguish worst-input channel error from one input's entanglement fidelity. Understand how a reference-entangled state witnesses a channel error and how exact subspace correction imposes conditions on the noise operators.

**Prerequisites.** [M03](#m03-reduced-states-and-entangled-references), [M05](#m05-quantum-channels-and-their-environments), [M06](#m06-distinguishability-and-root-fidelity).

**Story role.** Fixes the operational strength of the statements to be proved.

**Conceptual connection.** A successful basis-state test, a good average, and a uniform recovery guarantee answer different questions.

**Canonical sources.** W&M §7.4; [recovery-witness bridge](WISEMAN_MILBURN_BRIDGE.md#channel-geometry-and-the-recovery-witness); [error convention](../science/model.md#3-what-the-error-measures); [exact-subspace criterion](../science/passive-recovery.md#6-protected-subspaces-and-their-exact-dimension).

### M08 Markov loss and the Lindblad generator

**Central question.** Which physical assumptions turn oscillator emission into the stated master equation?

**Understanding target.** Identify the system, vacuum reservoir, loss rate, and rotating-frame conventions. Relate a jump operator to the corresponding dissipator and its adjoint action on observables. Separate the assumptions behind Markov loss from the assumptions behind the native exchange Hamiltonian.

**Prerequisites.** [M02](#m02-coherent-exchange-and-conserved-excitation), [M05](#m05-quantum-channels-and-their-environments).

**Story role.** Defines the unconditional dynamics that every later calculation must represent.

**Conceptual connection.** An asymptotic increase in a model parameter does not automatically preserve the physical regime used to obtain the generator.

**Canonical sources.** W&M §§3.2, 3.3, and 3.6; [rate conventions](WISEMAN_MILBURN_BRIDGE.md#conventions-that-keep-rates-consistent); [noise and control model](../science/model.md#2-native-dynamics-and-inaccessible-radiation).

### M09 Conditional photon trajectories

**Central question.** How does a counted-emission description reproduce the unconditional open-system channel?

**Understanding target.** Relate jumps, conditional no-jump evolution, and averaging over records. Distinguish a hypothetical observation used to analyze the complementary channel from a measurement or feedback operation actually available to the processor.

**Prerequisites.** [M04](#m04-measurement-outcomes-and-retained-records), [M08](#m08-markov-loss-and-the-lindblad-generator).

**Story role.** Connects the Lindblad equation to the emitted record used in the converse.

**Conceptual connection.** Different representations of the same reduced dynamics need not give the processor different physical resources.

**Canonical sources.** W&M §§4.2–4.3; [dressed-qubit loss example](WISEMAN_MILBURN_BRIDGE.md#a-dressed-qubit-worked-from-loss-to-logical-error); [photon-record proof](../science/control-converse.md#proof-what-the-emitted-photons-reveal).

### M10 Counting intensity and compensated noise

**Central question.** Which part of a photon-count record is predicted by its conditional intensity?

**Understanding target.** Define the predictable intensity and the compensated counting process. Understand the stochastic-integral second-moment identity and the use of an integrating factor when the intensity depends on the count already accumulated.

**Prerequisites.** [M09](#m09-conditional-photon-trajectories).

**Story role.** Provides the controlled fluctuation estimate used in both converse and construction.

**Conceptual connection.** Subtracting a deterministic guess for the mean is not the same operation as compensating a process by its conditional intensity.

**Canonical sources.** W&M §§4.2–4.3 for trajectories; [local count-martingale derivation](WISEMAN_MILBURN_BRIDGE.md#the-count-martingale); [exact count identity](../science/control-converse.md#proof-what-the-emitted-photons-reveal).

### M11 Moment bounds and count discrimination

**Central question.** What distinguishability can be certified without assuming Gaussian count statistics?

**Understanding target.** Use conditional Jensen, Cauchy–Schwarz, Markov, and Chebyshev inequalities with their actual hypotheses. Relate mean separation and variance to total variation, and distinguish an upper bound on classification error from an estimate of a typical fluctuation.

**Prerequisites.** [M06](#m06-distinguishability-and-root-fidelity), [M10](#m10-counting-intensity-and-compensated-noise).

**Story role.** Turns trajectory moments into statements valid for finite parameters.

**Conceptual connection.** A signal-to-noise heuristic suggests a scale; a uniform discrimination inequality is what supports a recovery converse.

**Canonical sources.** W&M §4.3 for the counting setting; [local mathematical tools](WISEMAN_MILBURN_BRIDGE.md#mathematical-tools-supplied-locally); [endpoint moments](../science/control-converse.md#endpoint-mean-and-variance); [count classification](../science/control-converse.md#count-classification-for-the-weight-ladder).

### M12 Positive kernels and spectral bounds

**Central question.** How can positivity simplify the analysis of a channel acting on matrix entries?

**Understanding target.** Recognize Gram matrices, Schur channels, and probability-simplex quadratic forms. Relate rank-one perturbations, eigenvalue signs, and nonnegative eigenvectors to trace-norm bounds. Keep these local algebraic tools distinct from a theorem about optimal recovery.

**Prerequisites.** [M05](#m05-quantum-channels-and-their-environments), [M06](#m06-distinguishability-and-root-fidelity).

**Story role.** Prepares the exact passive benchmark without assuming its conclusion.

**Conceptual connection.** A matrix of classical distribution overlaps can also encode how quantum off-diagonal entries survive.

**Canonical sources.** [Local Schur-channel bridge](WISEMAN_MILBURN_BRIDGE.md#schur-channels-and-the-simplex-minimum), following W&M §1.4 as channel context; [affinity matrix](../science/passive-recovery.md#1-the-loss-syndrome-and-its-surviving-coherence); [spectral attainment argument](../science/passive-recovery.md#diamond-norm-attainment).

### M13 Operator bounds for evolving channels

**Central question.** How can local norm estimates remain valid for a many-body state entangled with a reference?

**Understanding target.** Use commutators to bound observable motion and use an interaction-frame integral to compare two evolutions. Track positive subnormalized states and their traces so that summing conditional contributions preserves a bound on the complete output.

**Prerequisites.** [M02](#m02-coherent-exchange-and-conserved-excitation), [M06](#m06-distinguishability-and-root-fidelity), [M08](#m08-markov-loss-and-the-lindblad-generator).

**Story role.** Supplies the dynamical tools shared by lower and upper bounds.

**Conceptual connection.** An operator inequality controls all allowed inputs; a bound verified only on selected expectations does not have the same scope.

**Canonical sources.** W&M §§3.6 and 3.11; [local mathematical tools](WISEMAN_MILBURN_BRIDGE.md#mathematical-tools-supplied-locally); [motion bounds](../science/control-converse.md#proof-motion-of-the-register); [channel comparison](../science/native-gates.md#a-comparison-bound-that-charges-logical-noise).

### M14 The complete recoverability problem

**Central question.** What exactly is supplied, varied, observed, and optimized in this project?

**Understanding target.** State the already encoded arbitrary input, inaccessible field, allowed Hamiltonians, accessible seed, and terminal recovery output. Keep $`N\ge n`$, the native interval $`T\ge c_0/\Omega`$ with fixed $`c_0>0`$, and bounded $`\kappa/\Omega`$ explicit in the general asymptotic converse. Distinguish a prescribed clock from a gate performed by the native controls.

**Prerequisites.** [M07](#m07-recovery-error-with-a-reference), [M10](#m10-counting-intensity-and-compensated-noise), [M11](#m11-moment-bounds-and-count-discrimination), [M12](#m12-positive-kernels-and-spectral-bounds), [M13](#m13-operator-bounds-for-evolving-channels).

**Story role.** Closes the preliminary phase by assembling its tools into one operational task.

**Conceptual connection.** Changing the input interface, retained output, duration convention, or available rate can change the mathematical question even on the same hardware.

**Canonical sources.** W&M §7.4 as error-correction context; [resource bridge](WISEMAN_MILBURN_BRIDGE.md#physical-resources-and-scope); [complete model](../science/model.md); [converse hypotheses](../science/control-converse.md#model-and-operational-error).

## Phase II: narrative/innovation

### M15 The dressed interface and its loss sectors

**Central question.** How can a register remain coherently encoded while the battery occupation depends on its weight?

**Understanding target.** Construct the fixed-total-excitation isometry and follow one photon loss into a new total-excitation sector. Identify the canonical sector decoder, including its valid support and CPTP extension when heavily depleted sectors lack some logical basis states.

**Prerequisites.** [M02](#m02-coherent-exchange-and-conserved-excitation), [M04](#m04-measurement-outcomes-and-retained-records), [M07](#m07-recovery-error-with-a-reference), [M14](#m14-the-complete-recoverability-problem).

**Story role.** Starts the project narrative from the smallest physical encoding and error event.

**Conceptual connection.** Learning total excitation lost is different from measuring the register weight carried inside a sector.

**Canonical sources.** W&M §§1.3–1.4 and §7.4; [dressed-qubit bridge](WISEMAN_MILBURN_BRIDGE.md#a-dressed-qubit-worked-from-loss-to-logical-error); [encoding](../science/model.md#1-register-and-battery); [decoder and exact sectors](../science/native-gates.md#a-completely-positive-decoder-and-the-exact-loss-sector-equations).

### M16 Idle loss as an affinity channel

**Central question.** What logical disturbance remains after an idle loss syndrome is decoded?

**Understanding target.** Obtain the positive diagonal conditional Kraus operators from bosonic pure loss and construct their affinity Gram matrix. Identify the register coherences to which each matrix entry applies and the distinction between a correctable excitation shift and information left in the environment.

**Prerequisites.** [M05](#m05-quantum-channels-and-their-environments), [M09](#m09-conditional-photon-trajectories), [M12](#m12-positive-kernels-and-spectral-bounds), [M15](#m15-the-dressed-interface-and-its-loss-sectors).

**Story role.** Turns the physical loss mechanism into an exactly tractable channel.

**Conceptual connection.** The environment's ability to distinguish two loss distributions is visible in the surviving overlap between two logical branches.

**Canonical sources.** W&M §§3.3 and 4.2; [Schur-channel bridge](WISEMAN_MILBURN_BRIDGE.md#schur-channels-and-the-simplex-minimum); [loss syndrome and surviving coherence](../science/passive-recovery.md#1-the-loss-syndrome-and-its-surviving-coherence).

### M17 Exact optimal passive recovery

**Central question.** Why is the canonical decoder optimal even when arbitrary terminal recovery is allowed?

**Understanding target.** Follow the separate optimizations over recovery maps and logical input distributions. Connect the conditional Kraus converse to the spectral attainment argument, and account for reference inputs and weight degeneracies when identifying the exact optimum.

**Prerequisites.** [M06](#m06-distinguishability-and-root-fidelity), [M07](#m07-recovery-error-with-a-reference), [M12](#m12-positive-kernels-and-spectral-bounds), [M16](#m16-idle-loss-as-an-affinity-channel).

**Story role.** Establishes a solved benchmark against which the active-control result can be interpreted.

**Conceptual connection.** Showing that one decoder performs well is weaker than proving that no decoder improves the worst-case error.

**Canonical sources.** W&M §7.4 as recovery context; [local simplex argument](WISEMAN_MILBURN_BRIDGE.md#schur-channels-and-the-simplex-minimum); [exact passive theorem and both proofs](../science/passive-recovery.md#2-exact-optimal-recovery-theorem).

### M18 Logical resolution and photon lifetime

**Central question.** Which feature of an emitted photon matters for logical error rather than energy survival?

**Understanding target.** Extract the short-time logical disturbance from the passive affinity channel and compare it with the finite-transmissivity energy bounds. Identify the order of limits and separate the logical resolution rate from the probability that the battery has emitted no photons.

**Prerequisites.** [M08](#m08-markov-loss-and-the-lindblad-generator), [M11](#m11-moment-bounds-and-count-discrimination), [M16](#m16-idle-loss-as-an-affinity-channel), [M17](#m17-exact-optimal-passive-recovery).

**Story role.** Isolates the physical rate that motivates, but does not replace, the active proof.

**Conceptual connection.** Many losses can coexist with weak which-weight information; substituting a gate duration into an idle expansion alone does not prove a controlled-dynamics theorem.

**Canonical sources.** W&M §3.3; [many-emission bridge](WISEMAN_MILBURN_BRIDGE.md#why-many-emissions-can-coexist-with-a-good-gate); [finite passive bounds](../science/passive-recovery.md#3-finite-energy-bounds); [infinitesimal noise](../science/passive-recovery.md#4-infinitesimal-logical-noise).

### M19 Protected and randomized input interfaces

**Central question.** Which changes to the encoded input alter the recovery problem, and why are they not counterexamples?

**Understanding target.** Analyze constant-weight subspaces using the exact correction criterion, including the maximal-dimension argument. Separately follow ideal random masking before encoding, its accessible seed, and its averaged quantum output. Distinguish either interface from a native mask begun after the original encoding.

**Prerequisites.** [M04](#m04-measurement-outcomes-and-retained-records), [M07](#m07-recovery-error-with-a-reference), [M17](#m17-exact-optimal-passive-recovery), [M18](#m18-logical-resolution-and-photon-lifetime).

**Story role.** Locates the assumptions under which full-register fragility is meaningful.

**Conceptual connection.** Failure of one full-dimensional channel is compatible with protected subspaces on the same physical register and with improvements under another encoder.

**Canonical sources.** W&M §7.4; [resource bridge](WISEMAN_MILBURN_BRIDGE.md#physical-resources-and-scope); [ideal input randomization](../science/passive-recovery.md#5-ideal-input-randomization); [protected subspaces and exact dimension](../science/passive-recovery.md#6-protected-subspaces-and-their-exact-dimension).

### M20 How quickly native control moves weight

**Central question.** How much can the register change before its earliest emitted photons leave?

**Understanding target.** Derive the uniform bound on absolute displacement from a definite initial weight and the stronger endpoint-population bound. Use the exact exchange-operator norm on the occupied excitation support, and identify why arbitrary weight-preserving terms in $`H_0`$ do not invalidate the estimates.

**Prerequisites.** [M02](#m02-coherent-exchange-and-conserved-excitation), [M13](#m13-operator-bounds-for-evolving-channels), [M14](#m14-the-complete-recoverability-problem), [M15](#m15-the-dressed-interface-and-its-loss-sectors).

**Story role.** Supplies the control limitation that the passive benchmark alone cannot establish.

**Conceptual connection.** The converse already includes collective contributions from all allowed couplers; it does not assume that the register remains stationary.

**Canonical sources.** W&M §3.11; [bounded-control bridge](WISEMAN_MILBURN_BRIDGE.md#bounded-control-and-the-native-clock); [motion-of-register proof](../science/control-converse.md#proof-motion-of-the-register).

### M21 An early count record during control

**Central question.** How can depletion, control-induced drift, and count fluctuations be separated exactly?

**Understanding target.** Derive the conditional emission intensity from the trajectory's remaining total excitation. Obtain the integrating-factor identity and its variance control, and distinguish its fixed-weight reference count from the actual controlled mean. Track the interval whose output is already beyond the processor's reach.

**Prerequisites.** [M10](#m10-counting-intensity-and-compensated-noise), [M11](#m11-moment-bounds-and-count-discrimination), [M15](#m15-the-dressed-interface-and-its-loss-sectors), [M20](#m20-how-quickly-native-control-moves-weight).

**Story role.** Converts bounded charge motion into a usable record in the emitted field.

**Conceptual connection.** Treating depletion exactly avoids mistaking a large predictable count drift for uncontrollable logical noise.

**Canonical sources.** W&M §§4.2–4.3; [count-martingale bridge](WISEMAN_MILBURN_BRIDGE.md#the-count-martingale); [emission-record proof](../science/control-converse.md#proof-what-the-emitted-photons-reveal).

### M22 From environmental information to failed recovery

**Central question.** Why can no terminal operation erase the quantum damage certified by an emitted record?

**Understanding target.** Use the Stinespring cross-term identity and fidelity monotonicity to constrain every recovered coherence. Construct a reference-entangled witness and include a classical control seed available to recovery, with its purification placed correctly. Preserve the distinction between the proof's observer and the processor.

**Prerequisites.** [M03](#m03-reduced-states-and-entangled-references), [M05](#m05-quantum-channels-and-their-environments), [M06](#m06-distinguishability-and-root-fidelity), [M07](#m07-recovery-error-with-a-reference), [M21](#m21-an-early-count-record-during-control).

**Story role.** Makes the subsequent bounds apply to optimal recovery rather than one decoder.

**Conceptual connection.** Accessible knowledge of a control seed cannot invalidate a record-based bound proved uniformly with seed-independent logical inputs.

**Canonical sources.** W&M §§1.4 and 7.4 as measurement and recovery context; [channel-geometry bridge](WISEMAN_MILBURN_BRIDGE.md#channel-geometry-and-the-recovery-witness); [terminal-recovery obstruction](../science/control-converse.md#proof-why-terminal-recovery-cannot-undo-the-record).

### M23 A finite error floor at the crossover

**Central question.** How can endpoint count moments rule out vanishing error at a nonzero resolution scale?

**Understanding target.** Join the endpoint motion estimates, exact count equation, and mean–variance discrimination inequality into a finite-parameter lower bound. Explain why bounded $`q=\kappa/\Omega`$ and a nonzero native-clock interval are needed when drawing the vanishing-error necessity from that bound.

**Prerequisites.** [M11](#m11-moment-bounds-and-count-discrimination), [M20](#m20-how-quickly-native-control-moves-weight), [M21](#m21-an-early-count-record-during-control), [M22](#m22-from-environmental-information-to-failed-recovery).

**Story role.** Establishes the converse at the crossover, beyond a limiting signal-to-noise argument.

**Conceptual connection.** Ruling out a scale that diverges is not yet enough to prove that a scale must vanish; a positive floor at fixed nonzero scale closes that gap.

**Canonical sources.** W&M §4.3 for the observed process; [local probability tools](WISEMAN_MILBURN_BRIDGE.md#mathematical-tools-supplied-locally); [critical-scale theorem](../science/control-converse.md#theorem-1-a-critical-scale-error-floor); [endpoint mean and variance](../science/control-converse.md#endpoint-mean-and-variance).

### M24 A weight ladder and maximal worst-case error

**Central question.** Why does distinguishing many weights give a stronger obstruction than distinguishing two?

**Understanding target.** Build a family of separated weight labels and a common count classifier. Balance the number of labels, their spacing, and the early observation time while keeping $`q`$ bounded. Track the resulting reference-entangled witness and the uniformity over all allowed native controls.

**Prerequisites.** [M11](#m11-moment-bounds-and-count-discrimination), [M21](#m21-an-early-count-record-during-control), [M22](#m22-from-environmental-information-to-failed-recovery), [M23](#m23-a-finite-error-floor-at-the-crossover).

**Story role.** Upgrades the binary obstruction to full worst-case channel failure below the frontier.

**Conceptual connection.** A half-diamond error approaching its maximum is not a claim that every input fails or that every subcode has zero quantum capacity.

**Canonical sources.** W&M §§4.2–4.3 for trajectory context; [count and witness bridge](WISEMAN_MILBURN_BRIDGE.md#the-count-martingale); [weight-ladder theorem](../science/control-converse.md#theorem-2-a-distinguishable-weight-ladder); [native-clock consequences](../science/control-converse.md#consequences-on-a-native-clock).

### M25 A gate duration supplied by native dynamics

**Central question.** When does a claimed bit flip force a nonzero native operation time?

**Understanding target.** Derive the target-population angle bound in the narrower class with $`[H_0,n_j]=0`$. Distinguish actual native population transfer from a stipulated lossless implementation, and specify where either condition is evaluated relative to arbitrary terminal recovery.

**Prerequisites.** [M02](#m02-coherent-exchange-and-conserved-excitation), [M13](#m13-operator-bounds-for-evolving-channels), [M14](#m14-the-complete-recoverability-problem), [M20](#m20-how-quickly-native-control-moves-weight), [M23](#m23-a-finite-error-floor-at-the-crossover).

**Story role.** Connects the prescribed-clock converse to a precisely defined native gate.

**Conceptual connection.** A target unitary named only after unrestricted recovery does not by itself certify that the native hardware performed any gate.

**Canonical sources.** W&M §3.11; [native-clock bridge](WISEMAN_MILBURN_BRIDGE.md#bounded-control-and-the-native-clock); [duration corollary](../science/control-converse.md#a-native-gate-duration-corollary); [gate and recovery distinction](../science/model.md#5-a-gate-condition-cannot-be-supplied-by-the-recovery).

### M26 The exact channel of an addressed pulse

**Central question.** What logical dynamics does one resonant target coupler generate across every loss sector?

**Understanding target.** Derive the sector Hamiltonians and jump amplitudes with arbitrary spectator coherences and an inert reference. Track jump indexing, subnormalized blocks, and zero padding at depleted boundaries. Keep the assumed ability to switch spectator couplers off explicit.

**Prerequisites.** [M02](#m02-coherent-exchange-and-conserved-excitation), [M08](#m08-markov-loss-and-the-lindblad-generator), [M09](#m09-conditional-photon-trajectories), [M15](#m15-the-dressed-interface-and-its-loss-sectors), [M25](#m25-a-gate-duration-supplied-by-native-dynamics).

**Story role.** Starts the constructive part from an exact physical channel rather than an effective scalar drive.

**Conceptual connection.** Replacing the battery occupation by its mean too early can hide both coherent dispersion and support errors.

**Canonical sources.** W&M §§3.3, 3.6, and 4.2; [many-emission bridge](WISEMAN_MILBURN_BRIDGE.md#why-many-emissions-can-coexist-with-a-good-gate); [exact decoder and sector equations](../science/native-gates.md#a-completely-positive-decoder-and-the-exact-loss-sector-equations).

### M27 Bounding logical noise while allowing many emissions

**Central question.** How can a channel comparison remain accurate without conditioning on zero photon loss?

**Understanding target.** Construct the completely positive comparison that stops only at a severe-depletion boundary. Separate Hamiltonian mismatch from reduced logical dissipation, and use a scalar shift of a Hermitian jump amplitude to identify the part that acts on logical information.

**Prerequisites.** [M07](#m07-recovery-error-with-a-reference), [M10](#m10-counting-intensity-and-compensated-noise), [M13](#m13-operator-bounds-for-evolving-channels), [M26](#m26-the-exact-channel-of-an-addressed-pulse).

**Story role.** Provides the reusable estimate from which both native-gate upper bounds follow.

**Conceptual connection.** The stopping channel is a proof construction, while the large common jump amplitude governs emission statistics without setting the full logical error.

**Canonical sources.** W&M §§3.6 and 4.2; [many-emission bridge](WISEMAN_MILBURN_BRIDGE.md#why-many-emissions-can-coexist-with-a-good-gate); [completely positive comparison and dissipator estimate](../science/native-gates.md#a-comparison-bound-that-charges-logical-noise).

### M28 Constructive gates under two speed conventions

**Central question.** How do the attainable resource criteria change when bare coupling or enhanced rate is fixed?

**Understanding target.** Compare the midpoint-occupation pulse with the pulse calibrated for deterministic depletion. Track each duration, tail estimate, error term, and control assumption. Interpret the calibrated pulse's solvability condition as a condition on that construction rather than a universal impossibility threshold.

**Prerequisites.** [M18](#m18-logical-resolution-and-photon-lifetime), [M21](#m21-an-early-count-record-during-control), [M25](#m25-a-gate-duration-supplied-by-native-dynamics), [M26](#m26-the-exact-channel-of-an-addressed-pulse), [M27](#m27-bounding-logical-noise-while-allowing-many-emissions).

**Story role.** Supplies explicit achievable operations for comparison with the control converse.

**Conceptual connection.** A fixed bare coupling lets increased occupation buy faster dynamics; a fixed enhanced-rate ceiling requires a different calibration and resource accounting.

**Canonical sources.** W&M §§3.3 and 4.3; [physical-resource bridge](WISEMAN_MILBURN_BRIDGE.md#physical-resources-and-scope); [fixed-bare-coupling gate](../science/native-gates.md#theorem-1-a-native-clock-gate-at-fixed-bare-coupling); [calibrated fixed-rate gate](../science/native-gates.md#theorem-2-a-depletion-calibrated-gate-at-a-fixed-rabi-rate-ceiling).

### M29 Attribution and the strength of the evidence

**Central question.** Which parts are inherited theory, which are proved here, and what do the computations verify?

**Understanding target.** Separate established architecture, covariant correction, conditional recovery, and twirling tools from the active-control argument and its matching constructions. Read the finite verification as checks of representations, optimization certificates, and selected inputs, with the distinction between a state error and an optimized diamond error intact.

**Prerequisites.** [M17](#m17-exact-optimal-passive-recovery), [M19](#m19-protected-and-randomized-input-interfaces), [M23](#m23-a-finite-error-floor-at-the-crossover), [M24](#m24-a-weight-ladder-and-maximal-worst-case-error), [M28](#m28-constructive-gates-under-two-speed-conventions).

**Story role.** Places the mathematical results and numerical evidence in their proper scientific context.

**Conceptual connection.** Agreement of independent finite models supports implementation correctness; it neither proves a universal control theorem nor establishes novelty by itself.

**Canonical sources.** W&M anchor boundaries in the [bridge](WISEMAN_MILBURN_BRIDGE.md#physical-resources-and-scope); [related-work comparison](../references/related-work.md); [what each calculation establishes](../verification/README.md#what-each-calculation-establishes); [passive optimization certificate](../science/passive-recovery.md#7-numerical-evaluation).

### M30 The complete energy and recoverability account

**Central question.** What coherent scientific statement remains after the converse, constructions, and resource boundaries are combined?

**Understanding target.** Connect the accepted input interface, emission mechanism, bounded native motion, optimal-recovery obstruction, and explicit gate upper bounds. Reconstruct the distinct fixed-coupling and fixed-rate conclusions with their hypotheses on duration and bounded $`\kappa/\Omega`$. Keep decoder costs, alternative encodings, and the physical validity of the Hamiltonian visible.

**Prerequisites.** [M14](#m14-the-complete-recoverability-problem), [M19](#m19-protected-and-randomized-input-interfaces), [M24](#m24-a-weight-ladder-and-maximal-worst-case-error), [M25](#m25-a-gate-duration-supplied-by-native-dynamics), [M28](#m28-constructive-gates-under-two-speed-conventions), [M29](#m29-attribution-and-the-strength-of-the-evidence).

**Story role.** Closes the narrative by connecting the local mechanism to the complete conditional resource law.

**Conceptual connection.** The result concerns recoverability of a specified already dressed interface; it is neither a complete fault-tolerant architecture nor a hardware-independent energy law.

**Canonical sources.** [Complete Wiseman–Milburn bridge](WISEMAN_MILBURN_BRIDGE.md); [model and result map](../science/model.md); [physical interpretation and limits](../science/interpretation.md); [relation of converse to construction](../science/control-converse.md#relation-to-the-constructive-bounds-and-scope).

