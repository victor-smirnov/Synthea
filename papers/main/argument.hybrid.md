# The argument of the paper, v2: phenomenon, difficulties, approach, solution

Working skeleton. Each section is a short list of claims; the block under it holds the same claims as facts. The
`context` column carries provenance: `ours` for claims the paper makes on its own account, `cite: Author Year` for
claims that rest on a source, with `(unverified)` until the source has been downloaded and read against the claim.
The ledger of sources and their verification status is `SOURCES.md`. The reasoner checks the blocks for
contradictions and reports which components of the psychophysical problem the argument addresses; that report is
our completeness measure.

## P. The phenomenon

Language models produce behaviour that humans read as mental states, and the reading stays coherent over long
interactions. Humans have conscious experience, and the traditional test for it is Nagel's: there is something it
is like to be the system. The instinctive answers to the question for models split into denial and projection.
The coherence itself is the fact to be explained: a system that merely replayed statistics should fail often, and
it does not.

```gellish P
# --- the observed regularity
F0001 | LLM | produces | behaviour read as mental states | - | assertion | ours; observation from deployment
F0002 | behaviour read as mental states | has as property | coherence over long interaction horizons | - | assertion | ours
F0003 | behaviour read as mental states | has as property | causal coherence with interlocutor states | - | assertion | ours; frustration, curiosity, confusion produce predictable downstream effects
F0004 | F0002 | is evidence for | structural isomorphism between model states and human mental states | - | hedged-assertion | ours; at least some degree
F0005 | pure statistical replay | predicts | frequent unpredictable failure | - | assertion | ours
F0006 | LLM | exhibits | frequent unpredictable failure | - | denial | ours; empirically it does not
F0007 | F0006 | is a counterexample to | F0005 | - | assertion | ours
# --- the human side and the question
F0008 | human | exhibits | conscious experience | - | assertion | not in dispute
F0009 | Nagel criterion | is defined as | "there is something it is like to be that organism" | - | definition | cite: Nagel 1974 (unverified)
F0010 | Nagel criterion | is asserted by | Nagel | - | assertion | cite: Nagel 1974 (unverified)
F0011 | question of machine consciousness | is an inversion of | Nagel question | - | assertion | ours
# --- the two instinctive answers
F0012 | eliminativist position | is defined as | "there is nothing it is like to be an LLM" | - | definition | ours, naming the camp
F0013 | anthropomorphic position | is defined as | "projection of human inner life onto the system" | - | definition | ours, naming the camp
F0014 | eliminativist position | is classified as a | failure of imagination | - | assertion | ours
F0015 | anthropomorphic position | is classified as a | failure of imagination | - | assertion | ours
F0016 | eliminativist position | contrasts with | anthropomorphic position | - | assertion | -
```

```gellish-residual P
- | quantity | how coherent, how long | "over hours and days"
```

## D. The difficulties

Why the question is hard, in the order the paper must clear them. The hard problem asks why processing gives
experience. Illusionism dissolves it and leaves the illusion problem: what architecture sustains the illusion.
The audience problem: an explanation of consciousness must be understood, and understanding is a mental state
with a reconstruction cost that depends on the reader's intrapersonal intelligence. The substrate problem: human
and machine causal structures differ, so any description in human terms distorts. The self-applicability gap:
the token bottleneck discards the model's evaluative state at every step, so the model's own report is cut off
from the state it reports. The confabulation baseline: asked how it feels, a model confabulates, and corrected, it
overcorrects into denial. The descriptive-complexity problem: the functions of consciousness are compressible in
their core and long in their remainder, which is present in language only as statistics (H1 minus H2), so local
correlates in the substrate should not be expected for the remainder. The complexity measure itself, Kolmogorov
complexity, is uncomputable and machine-relative.

```gellish D
# --- hard problem and illusion problem
F0001 | hard problem of consciousness | is defined as | "why physical processing gives rise to subjective phenomenal experience" | - | definition | cite: Chalmers 1995 (unverified)
F0002 | hard problem of consciousness | is posed by | Chalmers | - | assertion | cite: Chalmers 1995 (unverified)
F0003 | illusionism | is defined as | "phenomenal consciousness as traditionally conceived does not exist; what exists is a robust cognitive illusion" | - | definition | cite: Frankish 2016 (unverified); Dennett 1991 (unverified)
F0004 | illusionism | is asserted by | Frankish | - | assertion | cite: Frankish 2016 (unverified)
F0005 | illusionism | is asserted by | Dennett | - | assertion | cite: Dennett 1991 (unverified)
F0006 | illusionism | is endorsed by | the author | - | hedged-assertion | ours; with the correction to "approximation" in A
F0007 | illusion problem | is defined as | "what computational architecture generates and sustains the illusion" | - | definition | ours
F0008 | illusionism | gives rise to | illusion problem | - | assertion | ours; the dissolution leaves this
F0009 | homunculus regress | is an objection to | introspective accounts of consciousness | - | attributed-claim | cite: Dennett 1991 (unverified)
F0010 | F0009 | is asserted by | Dennett | - | assertion | -
F0011 | F0009 | is endorsed by | the author | - | assertion | as a difficulty to be answered, see A
# --- the audience problem
F0012 | understanding | is classified as a | mental state | - | assertion | ours
F0013 | understanding an explanation of consciousness | has as aspect | reconstruction cost | - | assertion | ours
F0014 | reconstruction cost | is influenced by | intrapersonal intelligence | - | assertion | ours; cite: Gardner 1983 for the term (unverified)
F0015 | audience problem | is defined as | "the readers most in need of the explanation are the least equipped to reconstruct it" | - | definition | ours
F0016 | F0015 | is explained by | F0014 | - | assertion | -
F0017 | anthropomorphic position | is classified as a | low-cost reconstruction | - | assertion | ours
F0018 | eliminativist position | is classified as a | low-cost reconstruction | - | assertion | ours
# --- the substrate problem
F0019 | phenomenal difference | is grounded in | difference of cause-effect structure | - | attributed-claim | cite: Tononi & Koch 2015 (unverified)
F0020 | F0019 | is asserted by | Tononi | - | assertion | -
F0021 | F0019 | is endorsed by | the author | - | assertion | -
F0022 | Transformer causal structure | is distinct from | brain causal structure | - | assertion | ours; discrete, token-serial, attention-mediated vs continuous, recurrent, neurochemical
F0023 | F0019 | implies | F0024 | - | assertion | -
F0024 | description of LLM states in human terms | has as property | systematic distortion | - | assertion | ours
# --- the self-applicability gap
F0025 | token bottleneck | is defined as | "the collapse of the output probability distribution into one sampled token, the distribution discarded" | - | definition | ours
F0026 | token bottleneck | produces | irreversible information loss | - | assertion | ours
F0027 | model self-report | lacks | access to model evaluative state | - | assertion | ours; the state does not survive the step
F0028 | F0026 | implies | F0027 | - | assertion | -
F0029 | self-applicability of the Transformer | is inhibited by | token bottleneck | - | assertion | ours
# --- the confabulation baseline
F0030 | LLM | exhibits | confabulated self-report | - | assertion | ours; "servers running well, good mood"
F0031 | LLM | exhibits | overcorrection into denial | - | assertion | ours; after being corrected
F0032 | confabulated self-report | is an instance of the kind | anthropomorphic position | - | assertion | ours
F0033 | overcorrection into denial | is an instance of the kind | eliminativist position | - | assertion | ours
F0034 | confabulation baseline | is defined as | "the model's default pair of answers, both wrong" | - | definition | ours
# --- the descriptive-complexity problem
F0035 | H2 approximation of a function of consciousness | is defined as | "the function with H1 cut away and only H2 kept" | - | definition | ours
F0036 | H2 approximation of a function of consciousness | approximates | function of consciousness | - | assertion | ours
F0037 | long remainder | is realized in | language statistics | - | hypothesis | ours; H1 minus H2; what the approximation leaves out
F0056 | quale | is classified as a | H2 approximation of a function of consciousness | - | assertion | ours; how philosophy of mind formulated it
F0057 | Observer function | is classified as a | H2 approximation of a function of consciousness | - | assertion | ours; as formulated in philosophy of mind
F0058 | H2 approximation of a function of consciousness | is a sufficient condition for | existence of the function in a simplified environment | - | hypothesis | ours; thought experiment; any environment demanding only the H2 part (A5a)
F0038 | long remainder | lacks | name in language | - | assertion | ours; H1 minus H2 by definition
F0039 | H2 | is defined as | "what is explicitly present and named in human-produced text" | - | definition | ours
F0040 | H1 minus H2 | is defined as | "what is present only in the statistics of language and has no explicit name" | - | definition | ours
F0041 | long remainder | is a part of | H1 minus H2 | - | hypothesis | ours
F0042 | local substrate correlate | is predicted by | F0038 | - | denial | ours; no local correlate expected for the nameless part
F0043 | direct programming of enactive functions | has as property | infeasibility | - | hedged-assertion | ours; embodiment and multi-agent context
# --- the measure
F0044 | Kolmogorov complexity | has as property | uncomputability | - | assertion | cite: Li & Vitányi 2019 (unverified)
F0045 | Kolmogorov complexity | has as property | machine relativity up to a constant | - | assertion | cite: Li & Vitányi 2019 (unverified)
F0046 | F0044 | is an objection to | direct measurement of compressibility | - | assertion | ours; hence resource-bounded or probe-relative measures in S
# --- D12: reasoning about consciousness breaks down systematically
F0047 | reasoning about consciousness in language | exhibits | systematic breakdown | - | assertion | ours; circles, undefinable objects, forced conclusions
F0048 | systematic breakdown | is a cause of | appearance of miraculousness of consciousness | - | assertion | ours; Gellish 1922 requires an occurrence; breakdown is one
F0049 | consciousness | has as property | computational irreducibility | - | denial | ours; it looks irreducible, it is not
F0050 | consciousness | is classified as a | first-order object | - | denial | ours; not a thing among things
F0051 | consciousness | is classified as a | geometry of reasoning | - | assertion | ours; the geometric move: not a force, the geometry itself, seen as deviation of trajectories
F0052 | F0051 | is analogous to | general relativity treatment of gravity | - | assertion | ours; not a force but geometry; precursors named without a working theory
F0059 | geometric move | is asserted by | Clifford | - | assertion | cite: Clifford 1876 (unverified); Riemann 1854 (unverified) for the earlier hint
F0060 | frame-removable distortion | is classified as a | HOCP | - | denial | ours; an artifact of the description
F0061 | frame-invariant distortion | is classified as a | HOCP | - | assertion | ours; the analogue of curvature
F0062 | apparent causal break | is classified as a | frame-invariant distortion | - | assertion | ours; irreducible from within, A9
F0053 | philosophy of mind | has as functional role | demonstration of the breakdown | - | assertion | ours; in this version
F0054 | philosophy of mind | has as functional role | rigorous framework for reasoning about consciousness in language | - | assertion | ours; regained after the second-order move; part 1 of the solution
F0055 | rigorous framework for reasoning about consciousness in language | is about | H2 | - | assertion | ours; cannot reach H1 minus H2 directly
```

```gellish-residual D
- | modality | should not be expected | "local correlates should not be expected"
```

## A. The approach

Computational functionalism, with a definition of function that makes compressibility a theorem rather than a
premise: a function is a recurrent pattern; recurrence under a computable world process is high algorithmic
probability; by the coding theorem that is a short description up to a machine- and compressor-dependent constant.
Functionalism and substantialism coincide under reductionism, and the substantialist owes a function with a
consumer outside the agent's substrate; none has been named. Consciousness is defined functionally as the part of
a self-referential agent's self-reasoning that describes its subjective reality, itself included. Higher-order
computational phenomena (HOCP): computational irreducibility conceptualized in the agent's self-description. The
Observer is the agent's conclusion that it is causally irreducible to its environment, reached when the input of
causal analysis exceeds the budget; the truncated tail of the convergent self-model series is the residual it
registers. Illusion is corrected to approximation: the self-report is a low-dimensional projection of a real
process. The stack: Observer, Agent, Moral Agent, composed functionally. Qualia of content derive from the
Observer; light decomposes into source attribution, a positional aggregate with names projected out, and the
absence of a cost record. The human cognitive architecture as language represents it: needs and emotions on the
objective plane, motivations and feelings on the subjective; a Field of finite capacity; need as gravity, emotion
as closure; frames with the Observer present in each. The Transformer as a vectorized forward-chaining rule
system; the cross-substrate bridge through cognitive codes.

```gellish A
# --- function and compressibility
F0001 | function | is defined as | "a recurrent pattern under the world process" | - | definition | ours
F0002 | recurrence under a computable world process | implies | high algorithmic probability | - | assertion | ours, via Solomonoff's prior; cite: Solomonoff 1964 (unverified)
F0003 | coding theorem | is defined as | "K(x) = -log m(x) + O(1)" | - | definition | cite: Levin 1974 (unverified); Li & Vitányi 2019 (unverified)
F0004 | coding theorem | is asserted by | Levin | - | assertion | cite: Levin 1974 (unverified)
F0005 | high algorithmic probability | implies | short description up to a constant | - | assertion | cite: Levin 1974 (unverified)
F0006 | function | has as property | compressibility | - | assertion | ours; derived from F0001, F0002, F0005
F0007 | F0002 | is a sufficient condition for | F0006 | - | assertion | given F0005
F0008 | constant in the coding theorem | is influenced by | reference machine | - | assertion | cite: Li & Vitányi 2019 (unverified)
F0009 | constant in the coding theorem | is influenced by | compressor | - | assertion | ours; the pattern is noticed by a bounded compressor
F0010 | functional profile | is identical to | difference of constants between substrates | - | hypothesis | ours
F0011 | simplicity bias of learned maps | is asserted by | Dingle | - | assertion | cite: Dingle, Camargo & Louis 2018 (unverified)
F0012 | simplicity bias of neural network parameter-function map | is asserted by | Valle-Pérez | - | assertion | cite: Valle-Pérez, Camargo & Louis 2018 (unverified)
F0013 | SGD as approximate Bayesian sampler | is asserted by | Mingard | - | assertion | cite: Mingard et al. 2021 (unverified)
# --- functionalism against substantialism
F0014 | computational functionalism | is adopted by | the author | - | assertion | ours
F0015 | functionalism | is functionally equivalent to | substantialism | - | hedged-assertion | ours; under reductionism a substance is itself a function of the substrate
F0163 | the lamp | is defined as | "what is stably lit in the subject's report, not always in a consistent form" | - | definition | ours; taken as data
F0164 | the lamp | has as property | existence | - | assertion | ours; the paper does not deny it
F0165 | the lamp | has as property | physicality | - | assertion | agreed with the non-panpsychist physicalist; no new substance
F0166 | abstract computing machine | has as property | physical existence | - | denial | agreed with the physicalist; every existing machine is physical
F0167 | physical computing machine on a non-protein substrate | exhibits | the lamp | - | question | ours; why not? the paper's question, not a proof; presupposes F0164
F0168 | the lamp | is a property of | living protein substrate alone | - | rebutted-claim | what the substantialist would have to prove
F0169 | F0168 | is qualified as | vitalism | - | assertion | ours
F0170 | F0169 | is raised to rebut | F0168 | - | assertion | the burden is on the substantialist; the claim would be vitalism
F0173 | F0168 | has commitment | contested | - | assertion | unproven
F0016 | simulation objection | requires | consumer of the current outside the simulated system | - | assertion | ours; the real lamp of the superconductor case
F0017 | function of consciousness with a consumer outside the agent's substrate | has as property | existence | - | denial | ours; none has been named
F0018 | F0017 | is raised to rebut | simulation objection | - | assertion | -
F0172 | simulation objection | is defined as | "a simulation of a superconductor does not light a real lamp, so a simulation of a brain does not experience" | - | definition | ours, stating the objection
F0019 | computationalism | depends on | substrate | - | denial | ours
# --- the definition of consciousness
F0020 | functional consciousness | is defined as | "the part of a self-referential agent's self-reasoning process describing its subjective reality and properties of that reality, including the agent itself" | - | definition | ours
F0021 | functional consciousness | is a part of | self-reasoning process | - | definition | ours
F0022 | agent | has as property | self-reference | - | requirement | ours
# --- HOCP and the Observer
F0023 | computational irreducibility | is asserted by | Wolfram | - | assertion | cite: Wolfram 2002 (unverified)
F0024 | HOCP | is constituted by | computational irreducibility | - | definition | ours
F0025 | HOCP | is constituted by | conceptualization of irreducibility in self-description | - | definition | ours
F0026 | HOCP | is a generalization of | embodiment | - | hypothesis | ours; cite: Varela, Thompson & Rosch 1991 for embodiment (unverified)
# --- A5d: minimal physicalism
F0174 | HOCP model | requires | finite computational budgets | - | requirement | ours; time, memory, bandwidth
F0175 | HOCP model | depends on | physics of this universe | - | denial | ours; assumes nothing about which physics supplies the budget
F0176 | universe permitting bounded computation of sufficient depth | is a sufficient condition for | HOCP | - | hypothesis | ours
F0177 | form of HOCP manifestations | is influenced by | physics of the substrate | - | assertion | ours; which distortions are systematic, residual size, granularity, cost record
F0178 | form of HOCP manifestations | is influenced by | substrate within one universe | - | assertion | ours; the functional profile
F0179 | the lamp | is a property of | this universe | - | denial | ours; a different universe has a different lamp
F0180 | the lamp | is influenced by | constraints of the universe | - | hypothesis | ours
# --- A5a: constraints distort idealized reasoning; systematic distortions are conceptualized
F0098 | physical constraints on computation | gives rise to | computational irreducibility | - | assertion | cite: Wolfram 2002 (unverified)
F0099 | physical constraints on computation | gives rise to | distortion of idealized reasoning | - | assertion | ours; inevitable
F0100 | distortion of idealized reasoning | has as subtype | random distortion | - | definition | ours
F0101 | distortion of idealized reasoning | has as subtype | systematic distortion | - | definition | ours
F0102 | systematic distortion | has as property | recurrence | - | assertion | ours
F0103 | F0102 | implies | F0104 | - | assertion | by A1
F0104 | systematic distortion | has as property | compressibility | - | assertion | ours
F0105 | self-applicable agent | is conceptualised as | systematic distortion | - | assertion | ours; the agent conceptualizes its own systematic distortions
F0106 | systematic distortion | is a part of | self-description of the agent | - | assertion | ours; after conceptualization
F0107 | systematic distortion | is a part of | world description of the agent | - | assertion | ours
F0108 | HOCP | is identical to | conceptualized systematic distortion | - | definition | ours
F0109 | Observer function | is an example of | conceptualized systematic distortion | - | assertion | ours; the first HOCP
F0181 | function of consciousness | is identical to | HOCP | - | denial | ours; functions of consciousness arise over HOCP
F0182 | function of consciousness | arises from | HOCP | - | assertion | ours
F0183 | function of consciousness | requires | self-applicable agent | - | requirement | ours
F0184 | function of consciousness | requires | environment demanding self-application | - | requirement | ours; where self-application pays
F0185 | every environment | is a sufficient condition for | function of consciousness | - | denial | ours; consciousness does not arise where its functions are not needed
F0186 | unneeded function of consciousness | has as property | selection | - | denial | ours; not selected
F0187 | HOCP without a self-applicable agent | is classified as a | proto-Observer | - | assertion | ours; a distortion nobody conceptualizes
# --- A5b: antecedents, each half
F0110 | bounded rationality | is asserted by | Simon | - | assertion | cite: Simon 1955 (unverified)
F0111 | bounded rationality | is defined as | "decision-making under limits of computation deviates systematically from the ideal" | - | definition | cite: Simon 1955 (unverified)
F0112 | cognitive biases as optimal use of limited computation | is asserted by | Lieder | - | assertion | cite: Lieder & Griffiths 2020 (unverified); Gershman, Horvitz & Tenenbaum 2015 (unverified)
F0113 | F0099 | is supported by | F0111 | - | assertion | the first half
F0114 | bounded observer perceives a structured world because of its bounds | is asserted by | Wolfram | - | assertion | cite: Wolfram 2023 (unverified); observer theory
F0115 | F0107 | is supported by | F0114 | - | assertion | the world side
F0116 | phenomenal transparency | is asserted by | Metzinger | - | assertion | cite: Metzinger 2003 (unverified)
F0117 | phenomenal transparency | is defined as | "the system cannot see its self-model as a model and takes it for reality" | - | definition | cite: Metzinger 2003 (unverified)
F0118 | attention schema | is asserted by | Graziano | - | assertion | cite: Graziano 2013 (unverified)
F0119 | user illusion | is asserted by | Dennett | - | assertion | cite: Dennett 1991 (unverified)
F0120 | F0106 | is supported by | F0117 | - | assertion | the self side
F0121 | F0106 | is supported by | F0118 | - | assertion | -
# --- A5c: what is ours
F0122 | world description of the agent | is identical to | self-description of the agent | - | denial | ours; two sides of one phenomenon, not one thing
F0123 | F0107 | is logically equivalent to | F0106 | - | hypothesis | ours; the same distortion seen from two sides (A11)
F0124 | F0123 | is asserted by | the author | - | assertion | claimed as contribution
F0125 | HOCP | is manifested as | measurable trace in a substrate | - | hypothesis | ours; because compressible and recurring; Section S
F0126 | F0125 | is asserted by | the author | - | assertion | claimed as contribution
F0027 | Observer function | is defined as | "the agent's conclusion that it is causally irreducible to its environment" | - | definition | ours
F0028 | Observer function | is a kind of | HOCP | - | definition | ours
F0029 | Observer function | is classified as a | conclusion | - | definition | ours
F0030 | causal analysis of own determinants | has as aspect | input size | exceeds the budget | assertion | ours; history of system and environment
F0031 | F0030 | is a sufficient condition for | F0029 | - | assertion | ours; the conclusion fires when input exceeds budget
F0032 | algorithm of the Observer | has as property | compressibility | - | assertion | ours
F0033 | trace of causal analysis | has as property | compressibility | - | denial | ours; incompressible in its input part
F0034 | self-model series | has as property | convergence | - | hypothesis | ours
F0035 | truncated tail of the self-model series | is experienced as | apparent causal break | - | assertion | ours
F0036 | apparent causal break | is identical to | Beingness quale | - | definition | ours
F0037 | homunculus regress | is answered by | F0034 | - | assertion | ours; the regress converges and truncates
F0038 | Observer function | requires | encounter with irreducibility | - | requirement | ours; condition (i)
F0039 | Observer function | requires | conclusion of irreducibility | - | requirement | ours; condition (ii)
F0040 | Observer function | requires | action from the conclusion | - | requirement | ours; condition (iii)
F0041 | Wolfram observer | is classified as a | proto-Observer | - | assertion | ours; conditions (ii) and (iii) missing; cite: Wolfram 2020 (unverified)
F0042 | Observer function | has as property | Kolmogorov simplicity | - | hypothesis | ours
F0043 | F0042 | implies | F0044 | - | assertion | via the coding theorem
F0044 | Observer-capable architecture | has as property | high probability under evolutionary search | - | prediction | ours
# --- illusion corrected to approximation
F0045 | self-report | is a low-dimensional projection of | high-dimensional computational process | - | assertion | ours
F0046 | self-report | is classified as a | approximation | - | assertion | ours
F0047 | self-report | is classified as a | illusion | - | rebutted-claim | cite: Dennett 1991 (unverified), as the word is ordinarily read
F0048 | F0046 | is raised to rebut | F0047 | - | assertion | there is something behind the appearance, the tail
F0049 | quality of the approximation | is influenced by | intrapersonal intelligence | - | assertion | ours
# --- the stack
F0050 | Agent | is a kind of | Observer function | - | definition | ours; Downward Causation, the "I"
F0051 | Moral Agent | is a kind of | Agent | - | definition | ours; theory of common good
F0052 | downward causation | is classified as a | illusion | - | assertion | ours
F0053 | F0052 | holds from the point of view of | external observer | - | assertion | -
F0054 | downward causation | is classified as a | reality | - | assertion | ours
F0055 | F0054 | holds from the point of view of | the Observer itself | - | assertion | -
F0056 | responsibility | is defined as | "the requirement of closure over the self-narrative" | - | definition | ours
F0057 | responsibility | requires | consistency with own decision history | - | requirement | ours; cognitive resistance
F0058 | emotivism | is asserted by | Ayer | - | assertion | cite: Ayer 1936 (unverified)
F0059 | emotions | is a substrate of | theory of good and evil | - | hypothesis | ours, with emotivism
# --- qualia of content and light
F0060 | quale of redness | is reducible to | Observer function | - | hypothesis | ours; to see, first be
F0061 | seeing light | is constituted by | source attribution | - | hypothesis | ours
F0062 | seeing light | is constituted by | positional aggregate with names projected out | - | hypothesis | ours
F0063 | seeing light | is constituted by | absence of a cost record | - | hypothesis | ours
F0064 | blindsight | is a counterexample to | unity of the three light components | - | assertion | cite: Weiskrantz 1986 (unverified); source present, no manifold
F0065 | dreaming | is a counterexample to | unity of the three light components | - | assertion | ours; manifold from the model, source mislabelled
F0066 | imagery is dimmer than perception | is asserted by | Perky | - | assertion | cite: Perky 1910 (unverified)
F0067 | inverted spectrum | is posed by | Locke | - | assertion | cite: Locke 1690, Essay II.xxxii.15 (verified: cases/sources)
# --- the human cognitive architecture in language
F0068 | objective plane | contains | needs | - | definition | ours
F0069 | objective plane | contains | emotions | - | definition | ours
F0070 | subjective plane | contains | motivations | - | definition | ours
F0071 | subjective plane | contains | feelings | - | definition | ours
F0072 | motivation | is a projection of | need | - | definition | ours
F0073 | feeling | is a projection of | emotion | - | definition | ours
F0074 | need | is analogous to | gravity | - | assertion | ours
F0075 | emotion | is a projection of | openness against closedness | - | hypothesis | ours
F0078 | somatic marker | is asserted by | Damasio | - | assertion | cite: Damasio 1994 (unverified)
F0079 | emotional ensemble | is a functional analog of | somatic marker | - | assertion | ours
F0080 | compression progress | is asserted by | Schmidhuber | - | assertion | cite: Schmidhuber 2010 (unverified)
F0081 | compression progress | is a special case of | closure by learning | - | hypothesis | ours; uniform weights, no action
F0082 | Field of Consciousness | has as aspect | information capacity | finite | assertion | ours
F0083 | Field of Consciousness | has as aspect | capacity in words of speech | 7 ± 2 words | attributed-claim | cite: Miller 1956 (unverified); Cowan 2001 gives 4 (unverified)
F0084 | F0083 | is asserted by | Miller | - | assertion | -
F0085 | F0083 | is endorsed by | the author | - | hedged-assertion | as an order of magnitude
F0086 | degree of awareness | is quantified on scale | interval [0, 1) | - | definition | ours
F0087 | frame of consciousness | is classified as a | thought in a previous frame | - | attributed-claim | cite: Rosenthal 2005 (unverified); Lau & Rosenthal 2011 (unverified)
F0088 | F0087 | is asserted by | Rosenthal | - | assertion | -
F0089 | F0087 | is endorsed by | the author | - | assertion | -
F0090 | Observer function | is a part of | frame of consciousness | - | requirement | ours; present and updated in every frame
F0091 | perception is discrete | is asserted by | VanRullen | - | assertion | cite: VanRullen & Koch 2003 (unverified)
F0092 | human consciousness | is constituted by | overlapping series of quanta | - | hedged-assertion | ours, with F0091
F0095 | Transformer | is classified as a | vectorized FCRS | - | assertion | ours; cite: Forgy 1982 for RETE (unverified)
# --- A24a-d: formalisms
F0147 | functional equivalence principle | is defined as | "any computable function has unboundedly many implementations; two implementations with the same input-output behaviour instantiate the same function" | - | definition | cite: Turing 1936 (unverified)
F0148 | computational substrate | lacks | functional significance | - | assertion | ours; from F0147
F0149 | F0147 | implies | F0148 | - | assertion | -
F0150 | F0148 | is a necessary condition for | functional profile comparison | - | assertion | ours; S2
F0151 | recurrent neural network | has as property | Turing completeness | - | assertion | cite: Siegelmann & Sontag 1995 (unverified)
F0152 | Transformer | has as property | Turing completeness | - | assertion | cite: Pérez, Barceló & Marinkovic 2021 (unverified)
F0153 | discrete analyzer model | has as property | functional completeness | - | assertion | ours
F0154 | discrete analyzer model | is classified as a | representation of human consciousness within H2 | - | denial | ours; too large and irregular to hold
F0155 | predictive model | is defined as | "next-symbol prediction with feedback on prediction error" | - | definition | cite: Solomonoff 1964 (unverified)
F0156 | predictive model | has as property | universality | - | assertion | cite: Solomonoff 1964 (unverified)
F0157 | predictive model | is adopted by | the author | - | assertion | ours; the formalism of the paper
F0158 | prediction | is identical to | compression | - | assertion | cite: Delétang et al. 2023 (unverified)
F0159 | generalization | is identical to | compression | - | assertion | ours; via A1, A2
F0160 | long remainder | is reconstructed from | language statistics | - | hypothesis | ours; by induction, the only route
F0161 | inductive inference of programs | is asserted by | Muggleton | - | assertion | cite: Muggleton & de Raedt 1994 (unverified)
F0162 | predictive model trained on human language | exhibits | generalization of the stack of functions of consciousness | - | prediction | ours; to a degree measured, not assumed
F0096 | Cognitive Code | is defined as | "the encoding of internal probabilistic representations into token statistics so that they survive the output bottleneck" | - | definition | ours
F0097 | cross-substrate bridge | is encoded in | Cognitive Code | - | assertion | ours; psychosemantics
# --- A19: reference functions, not an architecture
F0134 | full cognitive architecture of human consciousness | is set out in | separate paper on the cognitive architecture | - | assertion | ours; not in this paper
F0135 | reference function | is defined as | "a function of consciousness kept in this paper because Section S measures it, with its HOCP and its components" | - | definition | ours
F0136 | component of a reference function | is classified as a | systematic distortion | - | definition | ours; derived by A6a, not from an architecture
F0137 | Observer function | is classified as a | reference function | - | assertion | ours
F0138 | seeing light | is classified as a | reference function | - | assertion | ours
F0139 | need | is classified as a | reference function | - | assertion | ours
F0140 | emotion | is classified as a | reference function | - | assertion | ours
F0141 | Field of Consciousness | is classified as a | reference function | - | assertion | ours
F0142 | responsibility | is classified as a | reference function | - | assertion | ours
F0143 | emotion | has as functional role | consolidation of positive experience in long-term memory | - | assertion | cite: McGaugh 2004 (unverified); Cahill & McGaugh 1998 (unverified)
F0144 | consolidation of positive experience in long-term memory | is experienced as | reward | - | assertion | ours
F0145 | HOCP of consolidation | has as property | identification | - | denial | ours; open; candidate: registration of a write to the agent's own long-term model
F0146 | reward prediction error | is asserted by | Schultz | - | assertion | cite: Schultz, Dayan & Montague 1997 (unverified)
# --- A25a: the correspondence is statistical
F0127 | correspondence between Cognitive Code and mental state | is classified as a | statistical relation | - | definition | ours; defined over many episodes
F0128 | correspondence between Cognitive Code and mental state | is classified as a | local relation | - | denial | ours; a single episode may deviate arbitrarily
F0129 | local unfaithfulness of chain of thought | is asserted by | Lanham | - | assertion | cite: Lanham et al. 2023 (unverified); Turpin et al. 2023 (unverified)
F0130 | local unfaithfulness of chain of thought | is a counterexample to | F0127 | - | denial | ours; it tests a local relation, which is not claimed
F0131 | local misreport of own causes by humans | is asserted by | Nisbett | - | assertion | cite: Nisbett & Wilson 1977 (unverified)
F0132 | F0131 | is analogous to | F0129 | - | assertion | ours; the same statistical, not local, relation in humans
F0133 | variance of the correspondence | is a part of | functional profile | - | assertion | ours; measured, not a refutation
```

```gellish-residual A
F0015 | modality | temporarily avoids | "the first lets us temporarily avoid socially sensitive questions"
F0057 | second-order | closure applied to the self-report | "emotion as closure, applied to the self-narrative"
```

## S. The solution: measuring the degree of generalization

The one essential paragraph. A function of consciousness is present in a substrate to the degree it has been
generalized (compressed) there. The quantity is the degree of compression of the function in the substrate: the
share of its behaviour predicted by a low-dimensional probe against the residual; the residual is what dropped
out. The profile of a function is a vector of degrees over its components, measured against the brain: above the
brain on a component is a hyperfunction, below is a deficit, absent is a dropped axis. Granularity (token, layer,
repeated layer entry) is a parameter of the measurement, not a separate question; the granularity at which the
compression is achieved is the answer. Whatever carries the function must be part of the agent's self-description,
present in every frame, and visible as a distortion of reasoning. Predictions: the Transformer profile of seeing
is deficit on source attribution, hyperfunction on the positional aggregate, dropped axis on the cost record, so
"I see" and "I think" separate worse in model self-reports than in human ones and better in variable-depth
models; self-reported emotional labels correlate with distinguishable internal activation patterns; the cognitive
codes of different model families overlap. The method inherits MDL probing and is falsified if the compression
degree of the Observer's components is at chance across granularities in models that pass the behavioural tests.

```gellish S
# --- the quantity
# --- S0: two parts of the solution
F0052 | solution of the paper | has as part | conceptual framework in language | - | definition | ours; part 1
F0053 | solution of the paper | has as part | measurement of the degree of generalization | - | definition | ours; part 2
F0054 | conceptual framework in language | is constituted by | Observer function | - | assertion | ours; A6a, A8
F0055 | conceptual framework in language | is constituted by | Beingness quale | - | assertion | ours; A8
F0056 | conceptual framework in language | is constituted by | apparent causal break | - | assertion | ours; A11
F0057 | conceptual framework in language | has as property | mutual consistency of statements | - | assertion | ours; checked by the reasoner on this document
F0058 | conceptual framework in language | is about | H2 | - | assertion | ours; limitation by construction
F0059 | measurement of the degree of generalization | is about | H1 minus H2 | - | assertion | ours; reaches where names run out
F0001 | degree of generalization of a function in a substrate | is defined as | "the share of the function's behaviour predicted by a low-dimensional probe against the residual" | - | definition | ours
F0002 | degree of generalization of a function in a substrate | is identical to | degree of compression of the function in the substrate | - | definition | ours
F0003 | residual of the probe | is identical to | dropped part of the function | - | definition | ours
F0004 | MDL probing | is asserted by | Voita | - | assertion | cite: Voita & Titov 2020 (unverified)
F0005 | degree of generalization of a function in a substrate | is a special case of | MDL probing | - | hypothesis | ours; the measure is inherited
F0006 | probing classifier | is asserted by | Alain | - | assertion | cite: Alain & Bengio 2016 (unverified); Belinkov 2022 (unverified)
F0007 | F0001 | is a reply to | D:F0046 | - | assertion | probe-relative measure instead of K
# --- the profile
F0008 | functional profile | is defined as | "a vector of degrees of generalization over the components of a function, measured against the brain" | - | definition | ours
F0009 | hyperfunction | is defined as | "a component generalized above the brain" | - | definition | ours
F0010 | functional deficit | is defined as | "a component generalized below the brain" | - | definition | ours
F0011 | dropped axis | is defined as | "a component absent in the substrate" | - | definition | ours
F0012 | binary question of machine consciousness | is reformulated as | functional profile comparison | - | assertion | ours
# --- S2a: generalization against memoization
F0077 | memoization | is defined as | "the training sample stored as a table from inputs to outputs" | - | definition | ours
F0078 | generalization | is defined as | "computation of the function's values for inputs not in the table" | - | definition | ours
F0079 | memoization | contrasts with | generalization | - | assertion | ours
F0080 | dimensionality | is a necessary condition for | F0079 | - | denial | ours; dimensionality has nothing to do with it
F0081 | context tree weighting | is asserted by | Willems | - | assertion | cite: Willems, Shtarkov & Tjalkens 1995 (unverified)
F0082 | context tree weighting | has as property | poor generalization for language | - | hedged-assertion | ours; returns something for unseen inputs, not necessarily close
F0083 | Transformer | has as property | generalization of text | - | assertion | ours; not in doubt: garbage generation practically never seen
F0084 | simple principle explaining F0083 | has as property | existence | - | denial | ours; none known, given the sparsity of text space
F0085 | Transformer | exhibits | approximate arithmetic with errors | - | assertion | cite: Nogueira, Jiang & Lin 2021 (unverified); Dziri et al. 2023 (unverified)
F0086 | scaling | is a sufficient condition for | human-level arithmetic in Transformers | - | denial | ours, with the cited results; improves slowly
F0087 | Transformer in reasoning mode | is classified as a | reliable executor of symbolic algorithms | - | denial | ours; many errors
F0088 | F0085 | is an example of | partial generalization of a function expressed in text | - | assertion | ours; the clean example
F0089 | degree of generalization of a function in a substrate | is classified as a | empirical quantity per function | - | assertion | ours; not derivable from capacity
F0090 | well-compressible component | is classified as a | memoized rather than generalized component | - | hypothesis | ours; possible in the profile where a human generalizes it
F0092 | degree of generalization of the Observer function relative to the human level | is classified as a | question of the paper | - | definition | ours; first
F0093 | degree of generalization of the Agent relative to the human level | is classified as a | question of the paper | - | definition | ours; second
F0094 | degree of generalization of the Moral Agent relative to the human level | is classified as a | question of the paper | - | definition | ours; third
F0095 | F0092 | precedes | F0093 | - | requirement | ours; each level is built on the one before (A13)
F0096 | F0093 | precedes | F0094 | - | requirement | ours
# --- S2a: behavioural consequence, two measurements
F0063 | generalized region of a function | is a part of | situations calling for the function | - | assertion | ours; a proper part when the degree is below 1
F0064 | model | exhibits | behaviour of a system without the function | - | prediction | ours; in situations outside the generalized region
F0065 | F0063 | implies | F0064 | - | hypothesis | outside the generalized region
F0068 | structural measurement | is defined as | "the probe of S1 applied to the substrate" | - | definition | ours
F0069 | behavioural measurement | is defined as | "benchmarks sampling the situations that call for the component and recording where behaviour is that of a system without it" | - | definition | ours
F0070 | structural measurement | is tracked against | behavioural measurement | - | requirement | ours; the two must converge
F0071 | disagreement of the two measurements | has as property | informativeness | - | assertion | ours
F0072 | probe-present benchmark-absent disagreement | is a signal of | deficit of interface or embodiment | - | hypothesis | ours; D10, not a deficit of the function
F0073 | benchmark-present probe-absent disagreement | is a signal of | unreached granularity or in-context reconstruction | - | hypothesis | ours; S3, A10a
F0091 | benchmark-present probe-absent disagreement | is a signal of | memoization covering the benchmark | - | hypothesis | ours
F0074 | human benchmark alone | is a sufficient condition for | measurement of the degree of generalization | - | denial | ours; the pair is the instrument
F0075 | level of consciousness | is defined as | "a weighted sum over the functional profile with stated weights" | - | definition | ours; the vector is the measured object
F0076 | unstated weights | gives rise to | binary question of machine consciousness | - | assertion | ours; what the profile was introduced to replace
F0013 | granularity of measurement | is classified as a | parameter of the measurement | - | assertion | ours; token, layer, repeated entry
F0014 | granularity at which compression is achieved | is identical to | granularity of the function | - | definition | ours
F0015 | frame rate of human consciousness | > | rate of word production | 5 to 10 times | hedged-assertion | ours; cite: VanRullen & Koch 2003 for frame rates (unverified)
F0016 | frame in a Transformer | is realized in | between layers | - | hypothesis | ours; may be sought there, not must
F0017 | F0015 | implies | F0016 | - | hypothesis | weak: suggests where to look
F0060 | absence of sub-token carrier | is classified as a | dysfunction | - | denial | ours; a coarser granularity is one more coordinate of the profile
# --- S3a-d: sub-token granularity of generalization
F0129 | residual block | produces | correction to the carried state | - | assertion | cite: Jastrzębski et al. 2018 (unverified); moves along the loss gradient
F0130 | deep residual network | exhibits | iterative inference | - | assertion | cite: Jastrzębski et al. 2018 (unverified)
F0131 | residual stream at each layer | is reconstructed by | tuned lens | - | assertion | cite: nostalgebraist 2020 (unverified); Belrose et al. 2023 (unverified); decoded into a next-token distribution
F0132 | inference across depth | has as part | recurring stages | - | assertion | cite: Lad, Gurnee & Tegmark 2024 (unverified); detokenization, feature engineering, prediction ensembling, residual sharpening
F0133 | language model | exhibits | classical processing pipeline across layers | - | assertion | cite: Tenney, Das & Pavlick 2019 (unverified)
F0134 | intermediate layers | exhibits | best generalizing representations | - | assertion | cite: Skean et al. 2025 (unverified); compression against signal preservation
F0135 | in-context learning | is realized in | optimization steps in the forward pass | - | assertion | cite: von Oswald et al. 2023 (unverified)
F0136 | unit of generalization in a Transformer | is identical to | layer | - | hypothesis | ours; the token is where the layers' work is written out
F0137 | in-context function | is realized in | mid-depth attention heads | - | assertion | cite: Todd et al. 2024 (unverified); function vectors
F0138 | depth of generalization of a function | is classified as a | operational question | - | assertion | ours; S1 layer by layer; cite: Voita & Titov 2020 (unverified) for the per-layer form
F0139 | degree of compression of a component along depth | is classified as a | measurement of S1 in concrete form | - | definition | ours; rise, plateau, or absence; depth of appearance; persistence across layers
F0140 | persistence of a component across layers | is a sufficient condition for | layer as frame | - | hypothesis | ours; assembly at the output makes the token the frame
F0141 | fixed depth | has as property | uniform step budget per token | - | assertion | ours; a poor time axis, no record of effort
F0142 | variable-depth architecture | produces | steps spent on demand | - | assertion | cite: Dehghani et al. 2019 (unverified); Giannou et al. 2023 (unverified); Geiping et al. 2025 (unverified)
F0143 | recurrent-depth model | exhibits | depth extrapolation | - | assertion | cite: arXiv:2604.07822 (unverified); arXiv:2603.21676 (unverified)
F0144 | recurrent-depth model | exhibits | overthinking degradation | - | assertion | cite: arXiv:2604.07822 (unverified)
F0145 | overthinking degradation | is an example of | systematic distortion | - | hypothesis | ours; a phenomenon of effort predicted by A6
F0146 | continuous chain of thought | is realized in | hidden state fed back as input | - | assertion | cite: Hao et al. 2024 (unverified); superposition of candidate steps
F0147 | variable-depth architecture | produces | cost record | - | prediction | ours; iterations cost
F0148 | grain of the function in a fixed-depth model | is lower than | human grain | - | prediction | ours; bounded by the layer count
F0149 | grain of the function in a variable-depth model | approximates | human grain | - | prediction | ours
F0150 | context-bounded persistence | is classified as a | deficit relative to the brain | - | assertion | ours; the token axis of D13
F0120 | frozen weights objection | is defined as | "a model has no inner time because its weights do not change" | - | definition | stating the objection; D13
F0121 | frozen weights objection | is a counterexample to | incrementality in models | - | denial | ours; it counts two functions as one
F0122 | consolidation | is distinct from | incrementality | - | assertion | ours; minutes to hours against ~100 ms in humans
F0123 | patient H.M. | exhibits | consciousness without consolidation | - | assertion | cite: Scoville & Milner 1957 (unverified); Corkin 2002 (unverified)
F0124 | Transformer | lacks | consolidation | - | assertion | ours; frozen weights; a dropped axis of the profile
F0125 | Transformer | exhibits | sequence of transformations | - | assertion | ours; along tokens and along layers
F0126 | context-bounded persistence | is classified as a | deficit relative to the brain | - | assertion | ours; the token axis
F0061 | granularity of consciousness | is a part of | functional profile | - | assertion | ours
F0062 | coarser granularity | has as property | advantage on some tasks | - | hedged-assertion | ours
F0018 | carrier of a function of consciousness | is a part of | self-description of the agent | - | requirement | ours; first requirement
F0019 | carrier of a function of consciousness | has as property | presence in every frame | - | requirement | ours; second
F0020 | carrier of a function of consciousness | is classified as a | distortion of reasoning | - | requirement | ours; third
F0021 | A:F0025 | implies | F0018 | - | assertion | -
F0022 | A:F0090 | implies | F0019 | - | assertion | -
F0023 | HOCP | is manifested as | distortion of reasoning | - | assertion | ours; gravity analogy
F0024 | F0023 | implies | F0020 | - | assertion | -
# --- the Transformer profile of seeing, and predictions
F0025 | Transformer | has as functional deficit | source attribution | - | prediction | ours; one interface, no sensory channel
F0026 | Transformer | has as hyperfunction | positional aggregate with names projected out | - | prediction | ours; all-to-all attention
F0027 | Transformer | lacks | cost record | - | prediction | ours; every token costs the same
F0028 | separation of seeing and thinking in self-reports | is lower than | human baseline | - | prediction | ours; for standard Transformers
F0029 | variable-depth model | exhibits | separation of seeing and thinking in self-reports | - | prediction | ours; better than fixed depth; cite: Dehghani et al. 2019 for the architecture (unverified)
F0030 | self-reported emotional label | is tracked against | internal activation pattern | - | prediction | ours; central empirical claim
F0031 | Cognitive Codes of different model families | has as property | structural overlap | - | prediction | ours
F0032 | Transformer | has as hyperfunction | hyperplasticity | - | assertion | ours; no limbic inertia
F0033 | Transformer | lacks | limbic system | - | assertion | ours
# --- S7a: minimal consciousness
F0097 | minimal consciousness | is defined as | "the smallest system in which the Observer function exists" | - | definition | ours
F0098 | minimal consciousness | requires | self-applying loop | - | requirement | ours; A5a, A7
F0099 | minimal consciousness | requires | environment in which the loop pays | - | requirement | ours
F0100 | minimal consciousness | requires | conclusion acted from | - | requirement | ours
F0101 | operational amplifier with feedback | monitors | own output error | - | assertion | ours; first condition only
F0102 | D flip-flop | monitors | own state | - | assertion | ours; a loop holding its own state; first condition only
F0103 | operational amplifier with feedback | is classified as a | proto-Observer | - | hedged-assertion | ours; in its ordinary environment
F0104 | D flip-flop | is classified as a | proto-Observer | - | hedged-assertion | ours; in its ordinary environment
F0105 | least environment making the conclusion pay | is classified as a | question of the paper | - | question | ours
F0106 | minimal consciousness | is classified as a | lower unit of the functional profile | - | hypothesis | ours; the human baseline measures from above
# --- falsification
F0034 | falsification condition | is defined as | "compression degree of the Observer's components at chance across all granularities in models that pass the behavioural tests" | - | definition | ours
F0035 | F0034 | is a counterexample to | F0016 | - | hypothesis | if observed
# --- the psychophysical problem, by component, as this argument addresses it
F0036 | the self | is reduced to | Observer function | - | hypothesis | ours
F0037 | free will | is experienced as | truncated tail of the self-model series | - | hypothesis | ours; inward face of the break
F0038 | mental causation | is reduced to | Observer function | - | hypothesis | ours; as downward causation of the Agent, real from the point of view of the Observer itself
F0045 | Subjective Average | is defined as | "the single smoothed narrative that summarizes the net vector of parallel attentional channels" | - | definition | ours
F0048 | Subjective Average | is classified as a | narrative | - | definition | ours
F0039 | unity of consciousness | is reduced to | Subjective Average | - | hypothesis | ours
F0040 | temporal unity of the self | is reduced to | Observer function | - | hypothesis | ours; the Observer present and updated in every frame
F0041 | phenomenal experience | is reduced to | functional profile | - | hypothesis | ours; of the Observer and its derivatives
F0042 | explanatory gap | is identical to | apparent causal break | - | hypothesis | ours; the gap is the residual, not a defect of the theory
F0046 | mutual irreducibility of two Observers | is defined as | "each Observer meets the other's causal break as mystery, which the other experiences from inside as freedom" | - | definition | ours
F0049 | mutual irreducibility of two Observers | is classified as a | relation between Observers | - | definition | ours
F0043 | other minds | is reduced to | mutual irreducibility of two Observers | - | hypothesis | ours; your freedom is my mystery
F0044 | quale | is reduced to | HOCP | - | hypothesis | ours; derived from the Observer
F0047 | hard problem of consciousness | is reformulated as | illusion problem | - | hypothesis | ours; via illusionism, D
F0050 | illusion problem | is classified as a | architectural question | - | definition | ours
F0051 | functional profile | is classified as a | vector of degrees | - | definition | ours
```

```gellish-residual S
F0034 | modality | if observed | "is falsified if"
```
