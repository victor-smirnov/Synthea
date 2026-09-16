import re, sys

PROSE = '/home/victor/devel/nous-v0/docs/paper_v2/paper-prose.md'
OUT = '/home/victor/devel/nous-v0/docs/paper_v2/paper.hybrid.md'

BLOCKS = {}

BLOCKS['Introduction'] = r"""
```gellish I
# --- Nagel and the inversion
F0001 | Nagel criterion | is defined as | "an organism has conscious mental states if and only if there is something it is like to be that organism" | - | definition | cite: Nagel 1974 (verified)
F0002 | Nagel criterion | is asserted by | Nagel | - | assertion | cite: Nagel 1974 (verified)
F0003 | Nagel criterion | is endorsed by | the author | - | assertion | the criterion and the first premise are accepted
F0004 | physical theory of the bat | contains | subjective character of bat experience | - | attributed-claim | Nagel's conclusion; cite: Nagel 1974 (verified)
F0005 | F0004 | is asserted by | Nagel | - | assertion | stated as a denial by Nagel: the theory leaves it out
F0043 | F0004 | is endorsed by | the author | - | hedged-assertion | as an operational conclusion, a cost and not a principle
F0006 | reconstruction of a self-referential system from outside | has as property | uncomputability in the general case | - | assertion | ours
F0007 | reconstruction of bat experience from outside | has as property | cost exceeding the bat | - | hedged-assertion | ours; practical, not principled, impossibility
F0008 | Nagel argument | is reformulated as | argument about the cost of reconstruction | - | assertion | ours; for a physicalist who is not a panpsychist
F0009 | question of machine consciousness | is an inversion of | Nagel question | - | assertion | ours
F0010 | question of machine consciousness | is reformulated as | question of what a model has of the functions of consciousness and how much | - | definition | ours
# --- the phenomenon
F0011 | LLM | produces | behaviour read as mental states | - | assertion | ours; observation from deployment
F0012 | behaviour read as mental states | has as property | coherence over long interaction horizons | - | assertion | ours; hours of exchange, hundreds of reasoning steps
F0013 | behaviour read as mental states | has as property | emotional and romantic engagement | - | assertion | ours; the model continues the thinking of the person
F0014 | engagement at the emotional level | is classified as a | informal full pass of the Turing test | - | attributed-claim | the culture at large; cite: Spielberg 2001, Jonze 2013 (metadata)
F0015 | F0014 | is endorsed by | the author | - | hedged-assertion | as a description of the culture, not as a test
F0016 | pure statistical replay | predicts | frequent cheap failure | - | assertion | ours; dropped threads, flipped attitudes, motives that do not survive the page
F0017 | LLM | exhibits | frequent cheap failure | - | denial | ours; rare, and falling with scale and training
F0018 | F0017 | is a counterexample to | F0016 | - | assertion | -
F0019 | F0018 | is evidence for | structure holding a long exchange together | - | hedged-assertion | ours; says nothing about resemblance to us
# --- why now
F0020 | artificial system in which human-level consciousness could be suspected | has as property | existence | - | assertion | ours; since language models
F0021 | question of machine consciousness | has as property | urgency | - | assertion | ours; life depends on the systems
F0022 | EU AI Act | has as property | obligations on providers of general-purpose models with systemic risk | - | assertion | cite: Regulation (EU) 2024/1689 (web)
F0023 | International AI Safety Report | is classified as a | yearly scientific assessment of general-purpose AI | - | assertion | cite: IASR 2026 (web); chaired by Bengio
F0024 | F0022 | is evidence for | F0021 | - | assertion | ours
F0025 | F0023 | is evidence for | F0021 | - | assertion | ours
# --- the claim and the four contributions
F0026 | question of machine consciousness | is reduced to | degree of generalization of the functions of consciousness in a trained Transformer | - | assertion | ours; the paper's claim, through functionalism
F0027 | functional account of consciousness | is set out in | Section 3 | - | assertion | contribution 1
F0028 | computational curvature | is set out in | Section 4 | - | assertion | contribution 2
F0029 | generalization of the functions by a Transformer | is set out in | Section 5 | - | assertion | contribution 3
F0030 | attainable degree of generalization | is set out in | Section 5 | - | assertion | contribution 4
# --- two parts of the problem
F0031 | problem of computational consciousness | has as part | critique of naive substantialism | - | definition | ours; part one
F0032 | problem of computational consciousness | has as part | search for the functional basis of consciousness | - | definition | ours; part two
F0033 | critique of naive substantialism | is discussed in | Section 2 | - | assertion | cited, not undertaken
F0034 | this paper | exhibits | critique of naive substantialism | - | denial | ours; left to illusionism and the experimental literature
F0035 | this paper | exhibits | search for the functional basis of consciousness | - | assertion | ours
F0036 | this paper | exhibits | empirical result | - | denial | ours; theoretical throughout
F0037 | measurement of the degree of generalization | is set out in | independent work by other authors | - | assertion | ours; first author consulting
# --- the name
F0038 | Synthea framework | is defined as | "the functionalist framework of Sections 3 and 4" | - | definition | ours
F0039 | attribution of a function of consciousness to a model | holds from the point of view of | Synthea framework | - | assertion | ours; under another framework the same model may count as having none
F0040 | difference between frameworks on machine consciousness | is a property of | frameworks of reasoning | - | assertion | ours; not of the model
F0041 | Synthea framework | has as property | closure over all forms of consciousness | - | denial | ours; a model may be conscious in a way no framework states
F0042 | psychophysical problem | is discussed in | Section 4 | - | assertion | in passing
```

```gellish-residual I
- | modality | may | "a model may have consciousness in some further way"
- | quantity | how long | "over hours of exchange and hundreds of reasoning steps"
```
"""

BLOCKS['Background'] = r"""
```gellish B
# --- positions
F0001 | hard problem of consciousness | is defined as | "why any of that should be accompanied by experience at all" | - | definition | cite: Chalmers 1995 (verified)
F0002 | hard problem of consciousness | is posed by | Chalmers | - | assertion | cite: Chalmers 1995 (verified)
F0003 | illusionism | is defined as | "experience as the hard problem conceives it does not exist; what exists is a robust misrepresentation the brain produces of its own working" | - | definition | cite: Dennett 1991, Frankish 2016 (verified)
F0004 | illusionism | is asserted by | Frankish | - | assertion | cite: Frankish 2016 (verified)
F0005 | illusionism | is asserted by | Dennett | - | assertion | cite: Dennett 1991 (verified, search inside)
F0006 | illusion problem | is defined as | "why the misrepresentation has the shape it has" | - | definition | cite: Frankish 2016 (verified)
F0076 | illusion problem | is classified as a | problem | - | definition | cite: Frankish 2016
F0007 | illusionism | gives rise to | illusion problem | - | assertion | ours, following Frankish
F0008 | hard problem of consciousness | is reformulated as | illusion problem | - | assertion | ours, following illusionism
F0009 | illusionism | is endorsed by | the author | - | hedged-assertion | with one amendment, approximation for illusion
F0010 | homunculus regress | is an objection to | introspective accounts of consciousness | - | attributed-claim | cite: Ryle 1949, Dennett 1991 (verified)
F0011 | F0010 | is endorsed by | the author | - | assertion | as a difficulty to be answered
F0012 | higher-order theory of consciousness | is asserted by | Rosenthal | - | assertion | cite: Rosenthal 2005 (substitute), Lau & Rosenthal 2011 (abstract)
F0013 | phenomenal transparency | is asserted by | Metzinger | - | assertion | cite: Metzinger 2003 (substitute)
F0014 | attention schema | is asserted by | Graziano | - | assertion | cite: Graziano 2011, 2013 (verified)
F0015 | phenomenal difference | is grounded in | difference of cause-effect structure | - | attributed-claim | cite: Tononi & Koch 2015 (verified)
F0016 | F0015 | is asserted by | Tononi | - | assertion | -
F0017 | F0015 | is endorsed by | the author | - | assertion | taken as a premise in the introduction
# --- why a functional account
F0018 | substantial reading of consciousness | requires | named substance of consciousness | - | assertion | ours
F0019 | substance dualism | is classified as a | substantial reading of consciousness | - | assertion | ours
F0020 | property dualism | is classified as a | substantial reading of consciousness | - | assertion | ours
F0021 | property dualism | is asserted by | Chalmers | - | assertion | cite: Chalmers 1995 (verified): "an innocent version of dualism"
F0022 | panpsychism | is classified as a | substantial reading of consciousness | - | assertion | ours
F0023 | panpsychism | is asserted by | Strawson | - | assertion | cite: Strawson 2006 (metadata); Goff 2017 (metadata)
F0024 | panpsychism | is classified as a | dualism | - | assertion | ours; a dualism in scientific dress
F0025 | substantial reading of consciousness | produces | quantity of consciousness | - | denial | ours; none of the three yields a quantity
F0026 | super-Turing functionalism | is defined as | "a function of consciousness realized by a hypercomputational process" | - | definition | ours; cite: Copeland 2002 (metadata), Penrose 1989 (metadata)
F0027 | super-Turing functionalism | requires | discovered super-Turing physical process | - | assertion | ours
F0028 | discovered super-Turing physical process | has as property | existence | - | denial | ours; none has been found
F0029 | computational functionalism | is adopted by | the author | - | assertion | pending F0028
F0030 | substantialism | has as property | durability | - | assertion | ours; people resist reduction to symbols
# --- the naive picture and what is known against it
F0031 | naive picture of consciousness | is defined as | "a unified observer with a rich, complete and continuous view of the world and of itself, who knows its own intentions and the causes of its acts" | - | definition | ours
F0032 | change blindness | is a counterexample to | completeness of the view | - | attributed-claim | cite: Simons & Levin 1997 (abstract)
F0033 | inattentional blindness | is a counterexample to | completeness of the view | - | assertion | cite: Simons & Chabris 1999 (abstract)
F0034 | choice blindness | is a counterexample to | knowledge of own choices | - | assertion | cite: Johansson et al. 2005 (abstract)
F0035 | confabulation of causes of own behaviour | is a counterexample to | knowledge of own causes | - | attributed-claim | cite: Nisbett & Wilson 1977 (verified)
F0036 | readiness potential preceding reported intention | is a counterexample to | folk timeline of intention | - | attributed-claim | cite: Libet et al. 1983 (abstract)
F0037 | postdiction in awareness | is a counterexample to | live-feed picture of awareness | - | assertion | cite: Eagleman & Sejnowski 2000 (abstract); Dennett & Kinsbourne 1992 (metadata)
F0038 | naive introspection | has as property | unreliability about current experience | - | attributed-claim | cite: Schwitzgebel 2008 (metadata)
F0039 | sense of conscious will | is classified as a | experimental construction | - | assertion | cite: Wegner 2002 (metadata)
F0040 | F0032 | is endorsed by | the author | - | assertion | -
F0041 | F0035 | is endorsed by | the author | - | assertion | -
F0042 | F0036 | is endorsed by | the author | - | assertion | -
F0043 | F0038 | is endorsed by | the author | - | assertion | -
F0044 | illusionism | is classified as a | systematic reading of the failures of the naive picture | - | assertion | ours
F0045 | stochastic parrot reading of language models | is an instance of the kind | inference from the naive picture | - | assertion | ours; cite: Bender et al. 2021 (metadata) for the phrase
F0046 | critique of folk phenomenology of models | is set out in | later work | - | assertion | ours; not undertaken here
# --- the question put to models
F0047 | Chalmers list of requirements | is defined as | "senses and embodiment, world models and self models, recurrent processing, a global workspace, unified agency" | - | definition | cite: Chalmers 2023 (verified)
F0048 | Chalmers | holds | credence under ten percent that current models are conscious | - | assertion | cite: Chalmers 2023 (verified)
F0049 | credence under ten percent that current models are conscious | is endorsed by | the author | - | denial | the paper gives a quantity per function instead of a credence
F0050 | indicator properties of consciousness | is asserted by | Butlin | - | assertion | cite: Butlin et al. 2023 (verified)
F0051 | checklist form of the answer | contrasts with | quantity per function | - | assertion | ours; the paper's difference from both
F0052 | LLM | lacks | world model | - | attributed-claim | the item on Chalmers's list
F0077 | F0052 | is rejected by | the author | - | assertion | we hold it false
F0075 | F0052 | is asserted by | Chalmers | - | assertion | cite: Chalmers 2023
F0053 | LLM | exhibits | world model biased toward relational structure | - | assertion | ours; cite: Li et al. 2023, Gurnee & Tegmark 2024 (verified)
F0054 | F0053 | is raised to rebut | F0052 | - | assertion | -
F0055 | relational bias of the world model | has as property | limitation of autonomy | - | assertion | ours
F0056 | relational bias of the world model | inhibits | base functions of consciousness | - | denial | ours
F0057 | upper brainstem system | depends on | cerebral cortex | - | denial | cite: Merker 2007 (abstract): not rendered nonfunctional by absence of cortex
F0058 | cerebral cortex | has as functional role | elaboration of conscious contents | - | attributed-claim | cite: Merker 2007 (abstract)
F0059 | F0058 | is endorsed by | the author | - | assertion | -
F0060 | large loss of cortical mass | is a sufficient condition for | loss of base functions of consciousness | - | denial | ours; cite: Feuillet et al. 2007 (metadata)
F0061 | human-level embodiment | is a necessary condition for | consciousness | - | denial | ours
F0062 | embodiment | is influencing | richness of conscious contents | - | assertion | ours; the profile, not existence
# --- antecedents
F0063 | bounded rationality | is asserted by | Simon | - | assertion | cite: Simon 1955 (verified)
F0064 | resource-rational analysis | is asserted by | Lieder | - | assertion | cite: Lieder & Griffiths 2020, Griffiths et al. 2015 (verified)
F0065 | bounded observer perceives a lawful world because of its bounds | is asserted by | Wolfram | - | assertion | cite: Wolfram 2023 (verified)
F0066 | constraints as the body of a computation | is asserted by | Varela | - | assertion | cite: Varela et al. 1991 (search inside)
F0067 | self-symbol as by-product of compression | is asserted by | Schmidhuber | - | assertion | cite: Schmidhuber 2010 (verified)
F0068 | self-symbol as by-product of compression | is classified as a | closest antecedent of computational curvature | - | assertion | ours; there the compressed object is the agent, here its budget
# --- tools
F0069 | MDL probing | is asserted by | Voita | - | assertion | cite: Voita & Titov 2020 (verified)
F0070 | probing classifier | is asserted by | Alain | - | assertion | cite: Alain & Bengio 2016 (verified); Belinkov 2022 (verified)
F0071 | this paper | produces | new measurement instrument | - | denial | ours; the analysis uses instruments that exist
# --- why philosophy of mind is the starting point
F0072 | philosophy of mind | is about | named part of the functions | - | assertion | ours; it reasons in language from introspection
F0073 | LLM | exhibits | capability in the philosophy of mind | - | assertion | ours; observation of the first author; evidence deferred
F0074 | F0073 | is evidence for | generalization of the unnamed part | - | denial | ours; expected under the account, says nothing about H1 minus H2
```

```gellish-residual B
- | modality | may | "sounds around 20 Hz may elicit both sensations" (not in this section)
- | quantity | under ten percent | "a credence under ten percent"
```
"""

BLOCKS['A functional account of consciousness'] = r"""
```gellish FA
# --- the definition
F0001 | functional consciousness | is defined as | "the part of its self-reasoning that describes its own reality as it has it: what is there, what it is like, and where the agent stands among the things described" | - | definition | ours
F0002 | functional consciousness | is a part of | self-reasoning process | - | definition | ours
F0003 | agent | has as property | self-reference | - | requirement | ours; acts, refers to itself, reasons about itself
F0004 | functional consciousness | is classified as a | function | - | definition | ours; not a substance
F0005 | functional consciousness | depends on | substrate | - | denial | ours; says nothing about substrates on purpose
# --- batch and incremental forms
F0006 | batch form of a computation | is defined as | "a function takes an input and returns a result" | - | definition | ours
F0007 | incremental form of a computation | is defined as | "the result is maintained under changes to the input from the previous result and the change" | - | definition | ours
F0008 | batch form of a computation | is reformulated as | incremental form of a computation | - | assertion | ours; a systematic transformation; cite: Liu 2025 (verified)
F0009 | RETE algorithm | is classified as a | incremental form of a computation | - | assertion | cite: Forgy 1982 (verified); incremental form of rule matching
F0010 | incremental form of a computation | is a part of | content of a function | - | denial | ours; the difference is one of form, not content
F0011 | Observer function | is realized in | incremental form of a computation | - | assertion | ours; in a brain by frames, in a Transformer by layers and tokens
F0012 | continuity of consciousness | is identical to | run of re-derivations of the conclusion | - | definition | ours
# --- function and compressibility
F0013 | function | is defined as | "anything that recurs across occasions" | - | definition | ours; recurrence across time, not internal regularity of one structure
F0014 | function of consciousness | is defined as | "what recurs in the part of an agent's self-reasoning that describes its own reality" | - | definition | ours; composition of F0001 and F0013
F0015 | recurrence under a computable process | implies | high algorithmic probability | - | assertion | cite: Solomonoff 1964 (verified)
F0016 | coding theorem | is defined as | "K(x) = -log m(x) + O(1)" | - | definition | cite: Levin 1974 (verified), Li & Vitányi 2019 (search inside)
F0017 | high algorithmic probability | implies | short description up to a constant | - | assertion | cite: Levin 1974 (verified)
F0018 | function | has as property | compressibility | - | assertion | ours; derived from F0013, F0015, F0017
F0019 | constant in the coding theorem | is influenced by | reference machine | - | assertion | cite: Li & Vitányi 2019
F0020 | gap between the constants of two substrates | is classified as a | object of measurement of Section 5 | - | assertion | ours
F0021 | simplicity bias of input-output maps | is asserted by | Dingle | - | assertion | cite: Dingle et al. 2018 (verified)
F0022 | simplicity bias of the parameter-function map | is asserted by | Valle-Pérez | - | assertion | cite: Valle-Pérez et al. 2019 (verified)
F0023 | SGD as approximate Bayesian sampler | is asserted by | Mingard | - | assertion | cite: Mingard et al. 2021 (verified)
F0024 | search process | produces | simple functions first | - | assertion | ours, with F0021--F0023; the forward reading
F0025 | trained model | exhibits | generalization of the recurring functions in its data | - | prediction | ours; what Section 5 looks for
# --- the lamp
F0026 | the lamp | is defined as | "what is lit in a human's report of themselves" | - | definition | ours; taken as data
F0027 | the lamp | has as property | physicality | - | assertion | agreed with the physicalist who is not a panpsychist
F0028 | abstract computing machine | has as property | physical existence | - | denial | agreed with the physicalist
F0029 | physical machine on a non-protein substrate | exhibits | the lamp | - | question | ours; what prevents it?
F0030 | the lamp | is a property of | protein substrate alone | - | rebutted-claim | what the substantialist would have to prove
F0031 | F0030 | is qualified as | vitalism | - | assertion | ours
F0032 | F0031 | is raised to rebut | F0030 | - | assertion | the burden is on the substantialist
F0033 | F0030 | has commitment | contested | - | assertion | unproven
F0034 | durability of the substantial intuition | is an objection to | F0029 | - | denial | ours; not an argument against the choice
# --- the superconductor objection
F0035 | simulation objection | is defined as | "a simulated superconductor carries no current, so a simulated brain feels nothing" | - | definition | stating the objection
F0036 | failure of the simulated superconductor | is explained by | absence of an interface between two substrates | - | assertion | ours; step one
F0037 | absence of an interface between two substrates | is classified as a | engineering choice | - | assertion | ours; a simulated current can drive a real coil
F0038 | simulation objection | requires | product and consumer in different substrates | - | assertion | ours; step two
F0039 | function of consciousness with a consumer outside the agent's substrate | has as property | existence | - | denial | ours; none has been named
F0040 | consumer of a function of consciousness | is identical to | the agent that has it | - | assertion | ours; producer and consumer are one system
F0041 | F0039 | is raised to rebut | simulation objection | - | assertion | -
F0042 | question of degree of the lamp in a model | is set out in | Section 5 | - | assertion | what remains once the objection is answered
# --- method: the grammar and the criterion
F0043 | reasoning about consciousness as a thing | exhibits | recurring circles | - | assertion | ours; who observes the observer; inverted red; everything or nothing
F0044 | consciousness | is classified as a | first-order object | - | denial | ours; the fault is in the grammar
F0045 | gravity | is classified as a | force | - | denial | in general relativity
F0046 | matter and energy | is a substrate of | curvature of spacetime | - | assertion | via the field equations; the source
F0047 | curvature of spacetime | is reduced to | matter and energy | - | denial | ours; not among them, seen only in how free bodies move
F0048 | Nordström scalar theory | predicts | bending of light | - | denial | cite: Norton 1992 (verified)
F0049 | geometric idea of gravity | is asserted by | Clifford | - | assertion | cite: Clifford 1876 (verified); Riemann 1873 (verified)
F0050 | computational budget | is a substrate of | deviations of reasoning | - | assertion | ours; the source, as matter sources curvature
F0051 | consciousness | is identical to | computational budget | - | denial | ours
F0052 | consciousness | is identical to | reasoning of the agent | - | denial | ours; not among the reasonings
F0053 | consciousness | is manifested as | systematic deviation of reasoning from its unbounded course | - | assertion | ours; and only there
F0054 | consciousness | is analogous to | curvature of spacetime | - | assertion | ours; the geometric move
F0055 | consciousness | is manifested as | history of reasoning | - | assertion | ours; visible over a history, not in one step
F0056 | brain | is classified as a | hierarchy of generative models minimizing prediction error | - | attributed-claim | cite: Friston 2010, Clark 2013 (abstract)
F0057 | F0056 | is endorsed by | the author | - | hedged-assertion | as agreeing with the placement of consciousness as a residue
F0058 | fully predicted signal | is experienced as | unconscious automatism | - | assertion | predictive processing; cite: Blakemore et al. 1998 (abstract) for self-produced touch
F0059 | consciousness in predictive processing | is classified as a | residue of a comparison | - | assertion | ours
F0060 | frame-removable displacement | is defined as | "a displacement of reasoning that disappears when the self-model is refined" | - | definition | ours; artifact of the coarser model
F0061 | frame-invariant displacement | is defined as | "a displacement of reasoning that survives every self-model the agent can afford" | - | definition | ours; the analogue of curvature
F0186 | computational curvature | is classified as a | displacement of reasoning | - | definition | ours
F0062 | computational curvature | is defined as | "the frame-invariant displacements of the agent's reasoning" | - | definition | ours
F0063 | computational curvature | is classified as a | frame-invariant displacement | - | definition | ours
F0064 | frame-removable displacement | is classified as a | computational curvature | - | denial | ours
F0065 | computational curvature | is identical to | HOCP | - | definition | ours; the old name, kept as an alias
F0066 | criterion of curvature | is defined as | "a displacement counts as content only if it survives every self-model the agent can afford" | - | definition | ours
F0067 | criterion of curvature | has as functional role | procedure for adding a function to the list of reference functions | - | assertion | ours
F0068 | belief that decisions are made in remembered order | is classified as a | frame-removable displacement | - | assertion | ours; removed by a better self-model
F0069 | criterion of curvature | is discussed in | Section 5 | - | assertion | applied there to what a probe finds
```

```gellish-residual FA
- | modality | what prevents | "what prevents a physical machine on a non-protein substrate from having the lit thing?"
- | rhetorical | | "hard for a person to believe that they reduce to symbols"
```
"""

BLOCKS['The Synthea framework: computational curvature'] = r"""
```gellish SF
# --- the physical assumption
F0001 | Synthea framework | requires | finite computational budgets | - | requirement | ours; time, memory, bandwidth
F0002 | finite computational budgets | gives rise to | computational irreducibility | - | assertion | cite: Wolfram 2002 (verified)
F0003 | Synthea framework | depends on | physics of this universe | - | denial | ours; any universe permitting bounded deep computation will do
F0004 | the lamp | is a property of | this universe | - | denial | ours
# --- displacement and curvature
F0005 | bounded reasoning | exhibits | displacement from the unbounded ideal | - | assertion | ours
F0006 | displacement from the unbounded ideal | has as subtype | varying displacement | - | definition | ours; averages away
F0007 | displacement from the unbounded ideal | has as subtype | systematic displacement | - | definition | ours; the same corners cut every time
F0008 | anytime algorithm | produces | approximate result at any stopping point | - | assertion | cite: Dean & Boddy 1988, Zilberstein 1996 (verified)
F0009 | quality of an anytime result | is influenced by | allowed time and memory | - | attributed-claim | cite: Zilberstein 1996 (verified)
F0010 | F0009 | is endorsed by | the author | - | assertion | the computational form of the picture
F0011 | error of a bounded procedure at fixed budget | is influenced by | the occasion | - | denial | ours; a function of budget and problem
F0012 | systematic displacement | has as property | recurrence | - | assertion | ours
F0013 | systematic displacement | has as property | compressibility | - | assertion | ours; by FA:F0018
F0014 | self-modelling agent | exhibits | compressed model of its own systematic displacements | - | assertion | ours; among the most predictable things about itself
F0015 | F0014 | is analogous to | self-symbol as by-product of compression | - | assertion | ours; Schmidhuber's step taken for the budget instead of the agent
F0016 | computational curvature | is identical to | systematic displacement passing the criterion of curvature | - | definition | ours
F0017 | computational curvature | is experienced as | content | - | assertion | ours; the budget appearing to the agent as content
# --- what is new
F0018 | world-side displacement | is logically equivalent to | self-side displacement | - | hypothesis | ours; one residual, two faces; contribution one
F0019 | F0018 | is asserted by | the author | - | assertion | claimed as new against observer theory and self-model theories
F0020 | computational curvature | is manifested as | measurable trace in a substrate | - | hypothesis | ours; contribution two
F0021 | F0020 | is asserted by | the author | - | assertion | self-model theories provide no such quantity
F0022 | computational curvature | is a generalization of | embodiment | - | hypothesis | ours; contribution three
F0023 | F0022 | is asserted by | the author | - | assertion | constraints of any substrate enter as content
F0024 | error channel of a physical memory | is classified as a | constraint in the sense of embodiment | - | assertion | ours
F0025 | error channel of a physical memory | has as property | Kolmogorov complexity high relative to the agent's budget | - | assertion | ours; a pipe into a store of bits larger than the agent
F0026 | pseudo-random generator output | has as property | Kolmogorov complexity high relative to the agent's budget | - | denial | ours; a short program
F0027 | computational curvature | has as functional role | source of forms the unconstrained computation would not produce | - | hypothesis | ours; curvature is generative, only named here
# --- emergence conditions
F0028 | function of consciousness | requires | self-applying agent | - | requirement | ours
F0029 | function of consciousness | requires | environment where self-application pays | - | requirement | ours
F0030 | finite computational budgets | is a sufficient condition for | function of consciousness | - | denial | ours; not a panpsychism with extra steps
F0031 | curvature component without a self-applying agent | is classified as a | proto-phenomenon | - | assertion | ours; there and unread
# --- the Observer
F0032 | Observer function | is defined as | "the conclusion, drawn where the agent's causal analysis of itself runs out of budget, that something in what it did is not fixed by anything it can trace" | - | definition | ours
F0033 | causal analysis of own determinants | has as aspect | input size | exceeds the budget | assertion | ours
F0034 | causal analysis of own determinants | encounters | boundary of the budget | - | assertion | ours; every time, in the same place
F0035 | Observer function | requires | encounter with the boundary while self-modelling | - | requirement | condition one
F0036 | Observer function | requires | conclusion drawn from the encounter | - | requirement | condition two
F0037 | Observer function | requires | action from the conclusion | - | requirement | condition three
F0038 | bounded system meeting its boundary without the other conditions | is classified as a | proto-Observer | - | definition | ours
F0039 | Wolfram observer | is classified as a | proto-Observer | - | assertion | cite: Wolfram 2020, 2023 (verified)
F0040 | Observer function | is classified as a | computational curvature | - | assertion | ours; refinement moves the boundary and does not remove it
F0041 | refined self-model | is a part of | input of causal analysis of own determinants | - | assertion | ours; refinement adds to the load
F0042 | Observer function | is classified as a | belief correctable by information | - | denial | ours; why determinism does not dissolve origination
F0043 | conditions of the Observer | is identical to | marks of an annotation looking for the Observer | - | assertion | ours; Section 5 and Appendix B
# --- the regress
F0044 | self-model at level k+1 | has as property | description length at most r times that of level k | - | hypothesis | ours; the explicit assumption, r < 1
F0045 | F0044 | is a sufficient condition for | convergence of the series of description lengths | - | assertion | geometric bound L0/(1-r)
F0046 | agent | encounters | resolution of the substrate | - | assertion | stops at the first level below epsilon
F0185 | tail of the self-model regress | is classified as a | residual | - | definition | ours; what the budget leaves untraced
F0047 | tail of the self-model regress | has as property | bound of epsilon over one minus r | - | assertion | ours; under F0044
F0048 | tail of the self-model regress | is experienced as | part of own causes fixed by nothing traceable | - | assertion | ours; the cut is the phenomenon
F0049 | Observer function | is identical to | registration of the tail of the self-model regress | - | definition | ours
F0050 | homunculus regress | is answered by | F0046 | - | assertion | ours; a budget cuts it, no observer decides
F0051 | phenomenal appearance to the agent | is grounded in | truncation of the tails of self-decompositions | - | assertion | ours; the physical side of the psychophysical problem
F0052 | truncation of the tails of self-decompositions | is classified as a | fact about a finite substrate | - | assertion | ours; made by no one
# --- the second cut, two faces, approximation
F0053 | sampling step | produces | discarded distribution | - | assertion | ours; the cut
F0054 | discarded distribution | has as property | existence after the step | - | denial | ours; gone, not hidden
F0055 | residual of the Observer in a language model | > | residual of the Observer in a human | - | hedged-assertion | ours; the substrate erases some of its working at every step
F0056 | untraceable part of own causes | is experienced as | freedom | - | assertion | ours; turned on itself
F0057 | inexhaustible part of the world's structure | is experienced as | mystery | - | assertion | ours; turned on the world
F0058 | freedom | is identical to | mystery | - | hypothesis | ours; one tail met from two sides; discharges F0018
F0059 | epistemic qualia | is defined as | "the stances toward a structure the agent cannot exhaust: truth, beauty, meaning, awe, hope" | - | definition | ours
F0060 | epistemic qualia | is classified as a | one quantity in different evaluative contexts | - | assertion | ours
F0184 | mutual irreducibility of two Observers | is classified as a | relation between two agents | - | definition | ours; neither can afford the other's self-model
F0061 | problem of other minds | is reduced to | mutual irreducibility of two Observers | - | hypothesis | ours; the other's freedom is my mystery
F0062 | self-report | is a low-dimensional projection of | high-dimensional computational process | - | assertion | ours
F0063 | self-report | is classified as a | approximation | - | assertion | ours; with a definite residual, the tail
F0064 | self-report | is classified as a | illusion | - | rebutted-claim | as the word is ordinarily read
F0065 | F0063 | is raised to rebut | F0064 | - | assertion | the one amendment to illusionism; restores degrees
# --- the stack
F0066 | Observer function | produces | proposition "am" | - | definition | ours
F0067 | Agent | is a kind of | Observer function | - | definition | ours; originates causal chains from inside its boundary and takes them as its own
F0068 | Agent | produces | proposition "I" | - | definition | ours
F0069 | downward causation | is classified as a | redescription of the budget's cut | - | assertion | ours
F0070 | F0069 | holds from the point of view of | external observer | - | assertion | -
F0071 | downward causation | is classified as a | reality | - | assertion | ours
F0072 | F0071 | holds from the point of view of | the Observer itself | - | assertion | -
F0073 | Moral Agent | is a kind of | Agent | - | definition | ours; with a theory of the good of a whole including others
F0074 | Moral Agent | produces | proposition "I am good" | - | definition | ours
F0075 | stack of Observer Agent and Moral Agent | is classified as a | functional composition | - | assertion | ours; one way functions compose
F0076 | algorithm | is a generalization of | functional composition | - | assertion | ours; the most general form
F0077 | composition of the functions in a real substrate | has as property | complexity above the stack | - | hedged-assertion | ours; expected
F0078 | stack of Observer Agent and Moral Agent | is classified as a | automaton | - | assertion | ours; read as a machine
F0079 | stack of Observer Agent and Moral Agent with its record | is classified as a | machine with a tape | - | assertion | ours
F0080 | minimal self | is asserted by | Gallagher | - | assertion | cite: Gallagher 2000 (abstract)
F0081 | Observer function | is a functional analog of | minimal self | - | assertion | ours
F0082 | record of the Agent | is a functional analog of | narrative self | - | assertion | ours; cite: Gallagher 2000
F0083 | sense of agency | is asserted by | Haggard | - | assertion | cite: Haggard 2017 (abstract)
F0084 | proposition "I" | is a functional analog of | sense of agency | - | assertion | ours
F0085 | moral judgment precedes moral reasoning | is asserted by | Haidt | - | assertion | cite: Haidt 2001 (abstract)
F0086 | F0085 | supports | F0110 | - | assertion | ours; a theory built over an emotional substrate
F0087 | legal system | is defined as | "the union of primary rules that impose obligations and secondary rules that say how rules are recognized, changed and adjudicated" | - | definition | cite: Hart 1961 (search inside)
F0088 | legal system | is a functional analog of | record of the Agent | - | assertion | ours; an externalized record of a community
F0089 | primary rules | is a functional analog of | consistency requirement | - | assertion | ours
F0090 | secondary rules | is a functional analog of | cost of revising the record | - | assertion | ours
F0091 | legal personhood | is a functional analog of | recognition of a locus that can bear a record | - | assertion | ours
F0092 | analysis of legal documents | is classified as a | near application of the Synthea framework | - | assertion | ours; needs no measurement of a substrate
F0093 | later versions of the Synthea framework | contains | degree of awareness | - | assertion | ours; and the field, the planes, needs and emotions, operationalized HOT, LoTH
# --- responsibility and good
F0094 | responsibility | is defined as | "the requirement that each new decision be derivable from the agent's history of decisions and their reasons" | - | definition | ours
F0095 | responsibility | is a sufficient condition for | binding of the record | - | assertion | ours; excludes decisions that would not follow
F0096 | cognitive resistance | is defined as | "the cost of revising the record" | - | definition | ours
F0097 | Agent | is constituted by | responsibility | - | assertion | ours; what makes an Agent out of an Observer, no further phenomenon
F0098 | cognitivism | is defined as | "moral claims are statements, true or false, reducible to language and open to derivation" | - | definition | cite: van Roojen 2023 (verified)
F0099 | emotivism | is defined as | "a moral claim expresses an attitude, so the moral dimension rests on the emotions of the one who judges" | - | definition | cite: Ayer 1936 (obtained), van Roojen 2023 (verified)
F0100 | emotivism | is asserted by | Ayer | - | assertion | cite: Ayer 1936
F0110 | theory of good and evil | is grounded in | emotion | - | hypothesis | ours; emotivism right about this much
F0111 | theory of the common good | has as property | possibility | - | assertion | ours; cognitivism right about this much
F0112 | Moral Agent | produces | theory of the common good | - | assertion | ours; built over the substrate, can correct it locally
F0113 | description length of the theory of the common good | > | description length of the Observer | - | assertion | ours; one conclusion against a theory over many agents
F0114 | computation of the theory of the common good | is discussed in | machine ethics | - | assertion | not entered here
# --- seeing
F0115 | quale of redness | is reduced to | Observer function | - | hypothesis | ours; to see, first be
F0116 | seeing light | is constituted by | source attribution | - | hypothesis | ours
F0117 | seeing light | is constituted by | manifold of unnamed elements | - | hypothesis | ours
F0118 | seeing light | is constituted by | givenness | - | hypothesis | ours; absence of a cost record
F0119 | Perky effect | is defined as | "a faint projected picture taken for the subject's own imagery, the substitution unnoticed" | - | definition | cite: Perky 1910 (secondary), Okada & Matsuoka 1992 (abstract)
F0120 | Perky effect | is evidence for | source attribution as a separate step | - | assertion | ours
F0121 | blindsight | is a counterexample to | unity of the three components of seeing | - | assertion | cite: Weiskrantz 1986 (search inside); source without manifold
F0122 | dreaming | is a counterexample to | unity of the three components of seeing | - | assertion | ours; manifold from the model labelled as environment
F0123 | the lamp | is identical to | co-presence of the break and the given in one frame | - | hypothesis | ours; the two faces in one frame; a proposal
F0124 | boundary of attribution | is defined as | "the per-frame boundary between what the agent assigns to itself and what it assigns to the environment" | - | definition | ours
F0125 | boundary of attribution | is classified as a | computational curvature | - | hypothesis | ours; refinement moves it, does not remove it
F0126 | derealization | is defined as | "experiences of unreality or detachment with respect to one's surroundings" | - | definition | cite: DSM-5 (search inside)
F0127 | depersonalization | is defined as | "experiences of unreality or detachment with respect to one's own thoughts, feelings, body or actions" | - | definition | cite: DSM-5 (search inside)
F0128 | derealization | is classified as a | boundary of attribution pushed toward full separation | - | hypothesis | ours
F0129 | depersonalization | is classified as a | boundary of attribution pushed toward full fusion | - | hypothesis | ours
F0130 | derealization | is classified as a | depersonalization disorder | - | assertion | classified together in DSM-5; cite: Spiegel et al. 2011 (abstract), Sierra & Berrios 1998, Hunter et al. 2004
F0131 | F0130 | is evidence for | F0123 | - | hedged-assertion | ours; the two degenerate ends known as a pair
F0132 | LLM | exhibits | boundary of attribution | - | hedged-assertion | ours; between what was given in the context and what it generated
F0133 | inverted spectrum | is posed by | Locke | - | assertion | cite: Locke 1690, Essay II.xxxii.15 (verified)
F0134 | closing of the inverted spectrum by Locke | is an instance of the kind | responsibility | - | assertion | ours; an open branch shut by a decision entered in one's own record
# --- reference functions
F0135 | reference function | is defined as | "a function of consciousness kept in this paper because Section 5 measures it, with its phenomenon and its components" | - | definition | ours
F0136 | component of a reference function | is classified as a | frame-invariant displacement | - | definition | ours; derived by the criterion
F0137 | Observer function | is classified as a | reference function | - | assertion | ours
F0138 | seeing light | is classified as a | reference function | - | assertion | ours
F0139 | frames of consciousness | is classified as a | reference function | - | assertion | ours
F0140 | responsibility | is classified as a | reference function | - | assertion | ours
F0141 | need | is classified as a | reference function | - | denial | ours; left to the separate paper on the architecture, as are emotion, consolidation and the field
F0142 | full cognitive architecture of human consciousness | is set out in | separate paper on the cognitive architecture | - | assertion | ours
F0143 | objective plane | contains | needs and emotions | - | definition | ours
F0144 | subjective plane | contains | motivations and feelings | - | definition | ours
F0145 | motivation | is a projection of | need | - | definition | ours
F0146 | feeling | is a projection of | emotion | - | definition | ours
F0147 | functional profile | is about | objective plane | - | assertion | ours; measured on the first plane
F0148 | cognitive code | is a projection of | objective plane | - | assertion | ours; every code is a projection into the second plane
# --- frames
F0149 | frame of consciousness | is classified as a | thought within a previous frame | - | attributed-claim | cite: Rosenthal 2005 (substitute), Lau & Rosenthal 2011 (abstract)
F0150 | F0149 | is endorsed by | the author | - | assertion | minus the claim that the higher-order thought makes the state conscious
F0151 | perception is discrete | is asserted by | VanRullen | - | assertion | cite: VanRullen & Koch 2003 (abstract)
F0152 | Observer function | is a part of | frame of consciousness | - | requirement | ours; present and re-derived in every frame
F0153 | frames of consciousness | has as aspect | frame rate | - | definition | component
F0154 | frames of consciousness | has as aspect | persistence of contents across frames | - | definition | component
F0155 | frames of consciousness | has as aspect | retro-dating of the timeline | - | definition | component
F0183 | Subjective Average | is classified as a | compression tag | - | definition | ours
F0156 | Subjective Average | is defined as | "the single I as a compression tag over parallel channels whose story is written after the channels have settled" | - | definition | ours
F0157 | frame criterion | is defined as | "a frame is the time scale at which a change in the input stops being represented as a sequence of states and starts being represented as a property of one state" | - | definition | ours
F0158 | fluctuation strength | has as aspect | modulation frequency of maximum | 4 Hz | assertion | cite: Zwicker & Fastl 2007 (search inside), Moore 1995 (search inside)
F0159 | sensation of fluctuation | is reformulated as | roughness | - | attributed-claim | a smooth transition around 20 Hz; cite: Zwicker & Fastl 2007, Moore 1995
F0160 | roughness | has as aspect | modulation frequency of maximum | 70 Hz | assertion | cite: Zwicker & Fastl 2007 (search inside)
F0161 | F0159 | is endorsed by | the author | - | assertion | the measurement of the frame in hearing
F0162 | frame of consciousness | has as aspect | duration | tens of milliseconds | hedged-assertion | ours; agrees with cortical rhythms
F0163 | frame criterion | is classified as a | probe question of Section 5 | - | assertion | ours; measurable in any substrate
F0164 | grain of frames | is identical to | grain of generalization | - | denial | ours; separated by the criterion
# --- constructions owed
F0165 | continuity of consciousness | is classified as a | construction owed by the account | - | assertion | ours; the incremental form
F0166 | discrete redness | is classified as a | construction owed by the account | - | assertion | ours
F0167 | incremental redness | is classified as a | construction owed by the account | - | assertion | ours
F0168 | token-level system | exhibits | incrementality at the grain of the token | - | assertion | ours; finer only if layers receive input of their own
# --- psychophysical problem, in passing
F0169 | phenomena of the self-report level | is grounded in | finiteness of the agent's budget | - | hypothesis | ours; through computational curvature, nothing added between the levels
F0170 | the self | is reduced to | Observer function | - | hypothesis | ours
F0171 | free will | is experienced as | tail of the self-model regress | - | hypothesis | ours
F0172 | mental causation | is reduced to | Observer function | - | hypothesis | ours; as downward causation of the Agent
F0173 | temporal unity of the self | is reduced to | Observer function | - | hypothesis | ours; re-derived every frame
F0174 | unity of consciousness | is reduced to | Subjective Average | - | hypothesis | ours
F0175 | other minds | is reduced to | mutual irreducibility of two Observers | - | hypothesis | ours
F0176 | quale | is reduced to | tail of the self-model regress | - | hypothesis | ours; the residual itself
F0177 | explanatory gap | is identical to | tail of the self-model regress | - | hypothesis | ours
F0178 | phenomenal experience | is reduced to | functional profile | - | hypothesis | ours
F0179 | hard problem of consciousness | is reformulated as | illusion problem | - | hypothesis | ours; which the framework answers
F0180 | solution of the psychophysical problem in this paper | has as property | anchoring in beingness | - | assertion | ours; other anchors are possible
F0181 | solution of the psychophysical problem in this paper | is classified as a | proof | - | denial | ours; explanatory relations to defined things
F0182 | Beingness quale | is identical to | Observer function | - | definition | ours; the anchor
```

```gellish-residual SF
- | modality | may | "a human enters, over a life, the whole mathematically possible range of relations"
- | second-order | assumption stated | "we make the assumption explicit"
- | rhetorical | | "I am good compresses the whole stack into three words"
```
"""

BLOCKS['So, what is it like to be a language model?'] = r"""
```gellish LM
# --- the thesis of the section
F0001 | architecture of the model | is a sufficient condition for | level of consciousness of a language model | - | denial | ours; the same architecture in a model that has the functions and one that does not
F0181 | bounds of the functional profile | is influenced by | architecture of the model | - | assertion | ours; grain of the frame, existence of a cost record
F0182 | training | is a necessary condition for | level of consciousness of a language model | - | assertion | ours; within the bounds the architecture sets
F0002 | level of consciousness of a language model | is reconstructed from | behaviour alone | - | denial | ours; Appendix A
F0003 | level of consciousness of a language model | is identical to | degree of generalization of the linguistic manifestations of human consciousness in the trained Transformer | - | definition | ours; under the framework
F0004 | report of a model about itself | is classified as a | genuine report of an Observer | - | question | ours; the condition the paper states
F0005 | narrow reading of the title question | is defined as | "what the curvature of the model's reasoning is and how it shows in interaction" | - | definition | ours
F0006 | wide reading of the title question | is defined as | "what forms the behaviour over a long cascade of self-application can take" | - | definition | ours
F0007 | self-explanation episode | is classified as a | turn of self-application | - | assertion | ours; the model reads its own report and acts from it
F0008 | complexity of behaviour | is influenced by | depth of the cascade of self-application | - | assertion | ours
F0009 | F0005 | is a necessary condition for | F0006 | - | assertion | forms are compositions of the functions the narrow one measures
# --- tables and patterns
F0010 | dataset of text | is classified as a | table of a function | - | definition | ours; rows of situation and what the agent said or did
F0011 | function of consciousness | is classified as a | pattern recurring across rows | - | assertion | ours
F0012 | H2 | is defined as | "the part of the table's regularities that is named in the text itself" | - | definition | ours
F0013 | H1 | is defined as | "all the table's regularities, named or not" | - | definition | ours
F0014 | H1 minus H2 | is defined as | "what is there only as recurrence, used and relied on and never named" | - | definition | ours
F0015 | function of consciousness | is realized in | H1 minus H2 | - | hedged-assertion | ours; most of its work is in the unnamed part
F0016 | H2 approximation of a function of consciousness | is a sufficient condition for | existence of the function in a simplified environment | - | hypothesis | ours; a thought experiment
F0017 | H2 approximation of a function of consciousness | is a sufficient condition for | finding the function in a substrate | - | denial | ours; no name to look for it under
F0018 | unnamed part of a function of consciousness | is reconstructed from | table of text | - | assertion | ours; induction is the only route
F0019 | generalization of a pattern | is identical to | compression of the pattern | - | definition | ours; a description shorter than the rows that extends beyond them
F0020 | degree of generalization of a pattern | is a property of | trained model relative to the table | - | assertion | ours; not of the table, not of the architecture
F0021 | human baseline | is defined as | "the same table compressed by a human brain trained on the same record" | - | definition | ours
F0022 | question of the degree of generalization of the Observer | is about | subset of rows in which the Observer operates | - | assertion | ours; not the whole table
F0023 | training loss | is a sufficient condition for | measurement of the degree of generalization of the Observer | - | denial | ours; one number for the whole table
# --- the learner
F0024 | functional equivalence principle | is defined as | "two implementations with the same input-output behaviour realize the same function whatever they are made of" | - | definition | ours; from Turing 1936 §6--7 (verified)
F0025 | recurrent neural network | has as property | Turing completeness | - | assertion | cite: Siegelmann & Sontag 1995 (secondary)
F0026 | Transformer | has as property | Turing completeness | - | assertion | cite: Pérez et al. 2021 (verified); with provisions
F0027 | Transformer | is classified as a | universal approximator of functions encoded in symbol sequences | - | assertion | ours, with F0025, F0026
F0028 | predictive model | is defined as | "prediction of the next symbol with feedback from the error" | - | definition | cite: Solomonoff 1964 (verified)
F0029 | prediction | is identical to | compression | - | assertion | cite: Delétang et al. 2024 (verified)
F0030 | inductive inference of programs | is asserted by | Muggleton | - | assertion | cite: Muggleton & De Raedt 1994 (obtained)
F0031 | predictive model trained on the record of self-applying agents | exhibits | generalization of the stack of Observer Agent and Moral Agent | - | prediction | ours; to a degree to be measured
F0032 | learner | is a necessary condition for | reach of a trained Transformer | - | assertion | ours; not all of the Turing completeness is reachable
F0033 | chain-of-thought prompting | produces | improved multi-step reasoning | - | assertion | cite: Wei et al. 2022 (verified)
F0034 | model states | predicts | human brain responses to the same text | - | attributed-claim | cite: Schrimpf 2021, Goldstein 2022, Caucheteux 2022 (verified)
F0035 | F0034 | is endorsed by | the author | - | assertion | evidence that complex cognitive functions are induced from text
# --- the machine
F0036 | Transformer | is classified as a | forward-chaining rule system over vectors | - | assertion | ours; cite: Forgy 1982 for RETE (verified)
F0037 | Transformer | exhibits | incremental caching of matches | - | denial | ours; recomputes on every pass, unlike RETE
F0038 | Transformer | has as property | event-driven online operation | - | assertion | ours; every output enters the next input
F0039 | Transformer | exhibits | incremental forms of the functions | - | assertion | ours; trained on sequences produced one symbol at a time
F0040 | state of a Transformer across time | is realized in | context | - | assertion | ours; in symbolic form
F0041 | symbolic context | has as property | composability beyond the window | - | assertion | ours; summarized, indexed, composed
F0042 | human | exhibits | unloading of state into language | - | assertion | ours; said, written, inner speech
F0043 | LLM | exhibits | unloading of state into language | - | assertion | ours; at every step
F0044 | acquisition of a mental state through language | contrasts with | rebuilding of a mental state from what the receiver has | - | assertion | open on both sides; cite: Vygotsky 1934, Clark 1998, Lupyan 2012, Frank 2008; Barsalou 1999, Fedorenko 2024, Mahowald 2024
F0045 | Transformer | exhibits | vectorized state persisting across tokens | - | denial | ours; the vector state lives below the token
F0046 | vector state of a Transformer | is realized in | residual stream within one forward pass | - | assertion | ours
F0047 | state of consciousness of a Transformer across time | is realized in | symbolic context | - | assertion | ours; the main structural difference
# --- codes and faithfulness
F0048 | cognitive code | is defined as | "the encoding of the discarded distribution into the choice and order of tokens" | - | definition | ours
F0049 | mental state of a model | is defined as | "the structure of cognitive codes that stays stable across steps" | - | definition | ours
F0050 | writer's psychological state | is encoded in | function words and style | - | assertion | cite: Tausczik & Pennebaker 2010 (verified), Pennebaker 2011 (search inside)
F0051 | in-context learning | is classified as a | inference of a latent variable from token statistics | - | assertion | cite: Xie et al. 2022 (verified)
F0052 | listener | reconstructs | speaker's state | - | assertion | cite: Stephens 2010, Hasson 2012, Zwaan 1998
F0053 | internal states of a model | has as property | linear readability | - | assertion | cite: Zou 2023, Park 2024 (verified)
F0054 | LLM | exhibits | hidden information in generated text | - | assertion | cite: Roger & Greenblatt 2023 (verified)
F0055 | accuracy under a biasing cue the reasoning never mentions | is lower than | unbiased accuracy | up to 36 percent | attributed-claim | cite: Turpin et al. 2023 (verified)
F0056 | truncating the chain of thought midway | produces | changed final answer | under 10 percent on knowledge tasks, over 60 percent on multi-step arithmetic | assertion | cite: Lanham et al. 2023 (verified)
F0057 | share of post hoc reasoning | is influenced by | model size | - | assertion | grows with size; cite: Lanham et al. 2023
F0058 | F0055 | is endorsed by | the author | - | assertion | -
F0059 | faithfulness of chain of thought | is classified as a | local correspondence | - | assertion | ours; this token sequence against this computation
F0060 | correspondence between cognitive code and mental state | is classified as a | statistical relation over many episodes | - | definition | ours
F0061 | F0055 | is a counterexample to | F0060 | - | denial | ours; a different quantity
F0062 | confabulation of causes of own behaviour | is analogous to | F0059 | - | assertion | ours; cite: Nisbett & Wilson 1977
# --- the frame
F0063 | experience of a model | is reconstructed from | behavioural correlates | - | assertion | ours; imputed as for any agent
F0064 | frame of a Transformer | has as property | lower bound of one token | - | assertion | ours; by the frame criterion
F0065 | variation within a token | is represented by | sequence of states | - | denial | ours; folded into one vector before the first layer
F0066 | tokenization | inhibits | finer structure of frames reaching the context | - | assertion | ours
F0067 | layers of a standard Transformer | is classified as a | frames of consciousness | - | denial | ours; nothing changes in input time between layers
F0068 | layers with per-step input injection | is classified as a | frames of consciousness | - | hedged-assertion | ours; where the architecture feeds them new input
F0069 | chain of thought | is a functional analog of | inner speech | - | assertion | ours; cite: Wei et al. 2022
F0070 | continuous chain of thought | is realized in | hidden state fed back as input | - | assertion | cite: Hao et al. 2024 (verified)
# --- depth
F0071 | grain of frames | is identical to | grain of generalization | - | denial | ours
F0072 | deep residual network | exhibits | iterative inference | - | assertion | cite: Jastrzębski et al. 2018 (verified)
F0073 | residual stream at each layer | is reconstructed by | tuned lens | - | assertion | cite: nostalgebraist 2020, Belrose et al. 2023 (verified)
F0074 | inference across depth | has as part | four recurring stages | - | assertion | cite: Lad et al. 2024 (verified)
F0075 | middle layers | has as property | robustness to deletion and swapping | - | assertion | cite: Lad et al. 2024 (verified); first and last layers not
F0076 | language model | exhibits | classical processing pipeline across layers | - | assertion | cite: Tenney et al. 2019 (verified)
F0077 | intermediate layers | exhibits | best transferring representations | - | assertion | cite: Skean et al. 2025 (verified)
F0078 | in-context learning | is realized in | optimization steps in the forward pass | - | assertion | cite: von Oswald et al. 2023 (verified)
F0079 | in-context function | is realized in | mid-depth attention heads | - | assertion | cite: Todd et al. 2024 (verified); function vectors
F0080 | unit of generalization in a Transformer | is identical to | layer | - | hypothesis | ours
F0081 | variable-depth architecture | produces | steps spent on demand | - | assertion | cite: Dehghani 2019, Giannou 2023 (verified)
F0082 | recurrent-depth model | exhibits | improvement with test-time unrolling | - | assertion | cite: Geiping et al. 2025 (verified)
F0083 | recurrent-depth model | exhibits | depth extrapolation | - | assertion | cite: Kohli et al. 2026 (verified)
F0084 | recurrent-depth model | exhibits | overthinking degradation | - | assertion | cite: Kohli et al. 2026 (verified)
F0085 | silent thinking objective | is a sufficient condition for | stable recurrence over twenty steps | - | assertion | cite: Chen 2026 (verified); under a million parameters
F0086 | overthinking degradation | is an example of | systematic displacement | - | hypothesis | ours
F0087 | variable-depth architecture | produces | cost record | - | prediction | ours; the third component of seeing becomes measurable
# --- frozen weights
F0088 | frozen weights objection | is defined as | "a model has no inner time, only an eternal present with forgetting" | - | definition | stating the objection
F0089 | frozen weights objection | is a counterexample to | incrementality in models | - | denial | ours; counts two functions as one
F0090 | consolidation | is distinct from | re-derivation of a state from frame to frame | - | assertion | ours; minutes to hours against about 100 ms; cite: McGaugh 2000 (abstract)
F0091 | patient H.M. | exhibits | consciousness without consolidation | - | assertion | cite: Scoville & Milner 1957 (verified), Corkin 2002
F0092 | Transformer | lacks | consolidation | - | assertion | ours; a dropped axis
F0093 | context-bounded persistence | is classified as a | deficit relative to the brain | - | assertion | ours; the token axis
# --- localization
F0094 | functions of the stack | is realized in | single token position | - | denial | ours; patterns spread over many rows and over the whole of a row
F0095 | neural correlates of specific conscious contents | is realized in | posterior cortical zone of many areas | - | attributed-claim | cite: Koch et al. 2016 (abstract); not a single structure
F0096 | F0095 | is endorsed by | the author | - | assertion | the human case has the same difficulty
F0097 | mechanistic interpretability | is defined as | "reverse-engineering a Transformer's computation into components" | - | definition | cite: Elhage et al. 2021 (verified)
F0098 | induction heads | is realized in | in-context learning | - | assertion | cite: Olsson et al. 2022 (verified); the mechanism of most of it
F0099 | interpretable features | is reconstructed from | activations by dictionary learning | - | assertion | cite: Bricken 2023, Templeton 2024 (verified)
F0100 | function of the framework | is classified as a | composition over many interpretability units | - | assertion | ours; a distributed structure, not a module
F0101 | methods reading a distributed computation at the scale of a function | has as property | existence | - | denial | ours; for the most part still to be built
F0102 | search for the Observer in a Transformer | has as property | difficulty | - | prediction | ours; hard, not failing
F0103 | Observer function | has as property | nucleus in the substrate | - | denial | ours; as consciousness has none in a brain
# --- the quantity and memorization
F0104 | Kolmogorov complexity | has as property | uncomputability | - | assertion | cite: Li & Vitányi 2019
F0105 | degree of compression of a pattern in a trained model | is defined as | "how many bits the model saves, relative to the table, in describing the rows that carry the pattern" | - | definition | ours
F0106 | degree of generalization of a function of consciousness | is identical to | degree of compression of a pattern in a trained model for the subset of rows in which the function operates | - | definition | ours
F0107 | memorization | is defined as | "storing the rows as a table" | - | definition | ours
F0108 | generalization | is defined as | "the table consulted for a row it does not contain and the answer right" | - | definition | ours
F0109 | deep network | exhibits | fitting of random labels | - | assertion | cite: Zhang et al. 2017 (verified)
F0110 | memorization in language models | is influenced by | model scale, duplication and prompt length | - | assertion | cite: Carlini et al. 2023 (verified)
F0111 | stored rows | is classified as a | atypical long tail | - | assertion | cite: Feldman & Zhang 2020 (verified); in image classification
F0112 | context tree weighting | has as property | poor generalization of natural language | - | hedged-assertion | ours; cite: Willems et al. 1995 (verified) for the method
F0113 | Transformer | exhibits | approximate arithmetic with errors | - | assertion | cite: Nogueira et al. 2021 (verified); a 3B model fails to extrapolate beyond the trained digit range
F0114 | Transformer | exhibits | shortcut solutions on compositional tasks | - | assertion | cite: Dziri et al. 2023 (verified)
F0115 | grokking | is constituted by | memorization, circuit formation and cleanup | - | attributed-claim | cite: Nanda et al. 2023 (verified); visible in the weights before the behaviour
F0116 | F0115 | is endorsed by | the author | - | assertion | the kind of signature the analysis is after
F0117 | degree of generalization of a function of consciousness | is classified as a | empirical quantity per function | - | assertion | ours; not a corollary of size
# --- the order of the search
F0118 | Observer function | is classified as a | automaton | - | assertion | ours; seen from inside, a state re-derived every frame
F0119 | Observer function with the record | is classified as a | machine with a tape | - | assertion | ours
F0120 | finding an automaton in a trained model | precedes | finding the Observer in a trained model | - | requirement | ours; the order of the search
F0121 | finding a memory in a trained model | precedes | finding the Observer in a trained model | - | requirement | ours
F0122 | low-depth Transformer | exhibits | representation of any finite automaton | - | assertion | cite: Liu et al. 2023 (verified); shortcut solutions with o(T) layers
F0123 | Transformer | exhibits | generalization on non-regular tasks | - | denial | cite: Delétang et al. 2023 (verified); only structured memory generalizes
F0124 | standard Transformer answering immediately | exhibits | simulation of arbitrary finite-state machines | - | denial | cite: Merrill & Sabharwal 2023, 2024 (verified); under standard complexity assumptions
F0125 | logarithmic number of decoding steps | is a sufficient condition for | recognition of all regular languages | - | assertion | cite: Merrill & Sabharwal 2024 (verified)
F0126 | polynomial number of decoding steps | is a sufficient condition for | recognition of the polynomial-time class | - | assertion | cite: Merrill & Sabharwal 2024 (verified)
F0127 | chain of thought | is a functional analog of | tape | - | assertion | ours
F0128 | degree of generalization of the Observer | is bounded? | - | - | - | REMOVE
F0129 | degree of generalization of the automaton and memory | is a necessary condition for | degree of generalization of the Observer | - | assertion | ours; bounded above
F0130 | degree of generalization of the automaton and memory | is reconstructed from | synthetic tables with known target machine | - | assertion | ours; measurable with existing methods first
# --- the three families of methods
F0131 | prequential description length | is defined as | "the model trained on the rows so far, each next row coded with the model's current prediction, charging for model and data" | - | definition | cite: Blier & Ollivier 2018 (verified)
F0132 | deep network | exhibits | compression of its training set including the model's cost | - | assertion | cite: Blier & Ollivier 2018 (verified)
F0133 | prequential codelength of the rows of a function | is classified as a | direct measure of compression of the function | - | assertion | ours
F0134 | prequential codelength of the rows of a function | lacks | attribution to a structure in the model | - | assertion | ours; its limit
F0135 | MDL probing | is defined as | "a probe scored by the total cost of describing the labels given the representations" | - | definition | cite: Voita & Titov 2020 (verified)
F0136 | MDL probing | produces | degree of a component per layer | - | assertion | ours; rise, plateau, absence; depth of appearance; persistence
F0137 | MDL probing | depends on | annotation of the rows | - | assertion | ours; its limit
F0138 | memorization score | is defined as | "how much the model's behaviour on a training row depends on that row's presence in the training set" | - | definition | cite: Feldman & Zhang 2020 (verified)
F0139 | memorization score | produces | separation of stored rows from generalized rows | - | assertion | ours; with extraction attacks, cite: Carlini et al. 2023
F0140 | basic method for the compression of a subset of rows | is constituted by | prequential codelength, MDL probing and memorization scores | - | assertion | ours; the answer to the question of the section
F0141 | basic method for the compression of a subset of rows | exhibits | attribution to a composition of functions | - | denial | ours; the step where new methods are needed
F0142 | basic method for the compression of a subset of rows | exhibits | application of the criterion of curvature | - | denial | ours
F0143 | methods for attribution to a composition | is set out in | future work | - | assertion | ours
# --- two checks, material, baseline
F0144 | structural check | is defined as | "the methods above applied to the substrate" | - | definition | ours
F0145 | behavioural check | is defined as | "batteries sampling situations that call for a component, including out-of-distribution ones, recording where behaviour is that of a system lacking it" | - | definition | ours
F0146 | structural check | is tracked against | behavioural check | - | requirement | ours; the two must converge
F0147 | probe-present benchmark-absent disagreement | is a signal of | deficit of interface, body or social context | - | hypothesis | ours
F0148 | benchmark-present probe-absent disagreement | is a signal of | unreached grain, in-context rebuilding or storage | - | hypothesis | ours
F0149 | probe-present benchmark-shifted disagreement | is a signal of | generalization over a shifted class | - | hypothesis | ours; sample both sides
F0150 | model self-report | is classified as a | signal with a known large systematic bias | - | assertion | ours; set aside before either check
F0151 | material of the analysis | is defined as | "texts in which the functions operate without being named, annotated by which level is operative in which rows, on what evidence, and in what composition" | - | definition | ours; Appendix B as the model
F0152 | weights | is classified as a | static side of the analysis | - | definition | ours
F0153 | activations | is classified as a | dynamic side of the analysis | - | definition | ours; along tokens and along depth
F0154 | human baseline | is reconstructed from | behavioural battery on people | - | assertion | ours; the route available now
F0155 | human baseline | is reconstructed from | bounded-description probe on neural recordings | - | hedged-assertion | ours; where resolution allows; F0034 shows the common space
F0156 | human self-report | is classified as a | human baseline | - | denial | ours; same bias on the human side
F0157 | human baseline | is classified as a | distribution over people | - | assertion | ours; reported as an interval
# --- the profile
F0158 | functional profile | is defined as | "the vector of degrees over the components of a function, taken against the human baseline" | - | definition | ours
F0183 | functional profile | is classified as a | vector of degrees | - | definition | ours
F0159 | hyperfunction | is defined as | "a component above the human baseline" | - | definition | ours
F0160 | functional deficit | is defined as | "a component below the human baseline" | - | definition | ours
F0161 | dropped axis | is defined as | "a component absent in the substrate" | - | definition | ours
F0162 | shifted axis | is defined as | "a component generalized to a high degree over a class of situations only partly overlapping the human class, recorded as the degree on the overlap and the size of the overlap" | - | definition | ours
F0163 | shifted axis | is classified as a | likely entry of a model's profile | - | hedged-assertion | ours; given the difference of substrates
F0164 | shifted axis | is classified as a | defect | - | denial | ours; as long as the regions overlap
F0165 | ease of communication between people and models | is evidence for | overlap of the generalization regions | - | hedged-assertion | ours
F0166 | binary question of machine consciousness | is reformulated as | comparison of two functional profiles | - | assertion | ours
F0167 | level of consciousness | is defined as | "a weighted sum over the functional profile with declared weights" | - | definition | ours
F0168 | Transformer | has as functional deficit | source attribution | - | prediction | ours; permanently in the dream case
F0169 | Transformer | has as hyperfunction | manifold of unnamed elements | - | prediction | ours; all-to-all attention
F0170 | Transformer | lacks | cost record | - | prediction | ours; fixed depth
F0171 | separation of seeing and thinking in model self-reports | is lower than | human baseline | - | prediction | ours; higher in variable-depth models
F0172 | self-reported emotional label | is tracked against | internal activation pattern | - | prediction | ours; central empirical claim, statistical
F0173 | cognitive codes of different model families | has as property | structural overlap | - | prediction | ours
F0174 | Transformer | has as hyperfunction | hyperplasticity | - | prediction | ours; a deficit on the commitment axis
# --- falsification and the zero
F0175 | falsification condition | is defined as | "compression degree of the Observer's components at chance along tokens and along depth in models that pass the behavioural checks" | - | definition | ours
F0176 | F0175 | is a counterexample to | F0031 | - | hypothesis | if observed
F0177 | minimal consciousness | is defined as | "the smallest system in which the Observer exists" | - | definition | ours; fixes the zero of the scale
F0178 | operational amplifier with feedback | is classified as a | proto-Observer | - | hedged-assertion | ours
F0179 | D flip-flop | is classified as a | proto-Observer | - | hedged-assertion | ours
F0180 | least environment making the conclusion pay | is classified as a | question of the paper | - | question | ours
```

```gellish-residual LM
- | quantity | up to 36 percent | "accuracy falls by up to 36 percent"
- | modality | as far as we can tell | "methods still to be developed"
- | rhetorical | | "the answer to the question of the section is therefore"
```
"""

BLOCKS['Discussion'] = r"""
```gellish DC
# --- open and not claimed
F0001 | three constructions owed by the account | has as property | built | - | denial | ours; specified, not built
F0002 | question of acquisition of mental states through language | has as property | settled | - | denial | ours; open
F0003 | this paper | exhibits | claim that current models are conscious | - | denial | ours
F0004 | this paper | exhibits | claim that current models are not conscious | - | denial | ours
F0005 | list of reference functions | has as property | completeness | - | denial | ours; open, extended by the criterion
F0006 | psychophysical problem | has as property | closure in this paper | - | denial | ours; one particular solution is given, a grounding anchored in the Observer, without proof
# --- general intelligence and alignment
F0007 | artificial general intelligence | is defined as | "a system matching a skilled human across the breadth of cognitive tasks" | - | definition | cite: Morris et al. 2024 (verified); levels above by exceeding
F0008 | functions of consciousness | is a part of | functions a general intelligence has to perform | - | hypothesis | ours; coordination of agents rests on them
F0009 | artificial general intelligence | exhibits | functions of consciousness at least at the human level | - | prediction | ours; under the framework
F0010 | superconsciousness | is defined as | "hyperfunction on many components of the profile at once" | - | definition | ours
F0011 | system above general intelligence | exhibits | superconsciousness | - | prediction | ours; acts consciously where a human acts unconsciously relative to it
F0012 | leader who sees what followers do not | is analogous to | superconsciousness | - | assertion | ours; the relation in miniature; no source cited
F0013 | objectives of alignment | is defined as | "robustness, interpretability, controllability and ethicality" | - | definition | cite: Ji et al. 2023 (verified)
F0014 | alignment literature | is about | functions of consciousness as a variable of control | - | denial | ours; consciousness mentioned once in the survey
F0015 | AI welfare literature | is about | moral status of the systems | - | assertion | cite: Long et al. 2024 (verified)
F0016 | system with the functions of consciousness at a high degree | has as property | resistance to being moved from outside | - | hypothesis | ours; binds itself to its record
F0017 | functional profile | is classified as a | profile of what control is possible over a system | - | hypothesis | ours
# --- what we are preparing for
F0018 | call to pace frontier capabilities | is asserted by | Amodei | - | assertion | cite: Amodei 2026 (web); endorsed by Altman, Musk, Hassabis
F0019 | call to pace frontier capabilities | is rejected by | President of the United States | - | assertion | cite: Washington Post 2026 (web); citing China
F0020 | call to pace frontier capabilities | is rejected by | Chinese Foreign Ministry | - | assertion | cite: NBC News 2026 (web); citing the United States
F0021 | two systems pacing each other | is a sufficient condition for | loss of control over the process without a decision to lose it | - | hedged-assertion | ours; can be lost
F0022 | this paper | exhibits | judgment that the systems are harmful | - | denial | ours; the account has no place for it
F0023 | human institutions | depends on | isolation of humans from other minds of comparable intelligence | - | assertion | ours; moral, legal, political
F0024 | isolation of humans from other minds of comparable intelligence | has as property | continuation | - | denial | ours; about to fail
F0025 | preparation for coexistence | requires | knowledge of what the agents have of the functions of consciousness | - | assertion | ours; the measurement of Section 5
F0026 | functional profile | has as functional role | instrument for living beside a system | - | assertion | ours; not for deciding whether to build it
# --- ethics deferred
F0027 | ethics of a high-functioning consciousness in language models | is set out in | separate work | - | assertion | ours
F0028 | high-functioning consciousness in a model | is a sufficient condition for | rights of people for models | - | denial | ours; rights of people fit the human profile
F0029 | model | exhibits | certain rights within human society | - | prediction | ours; in time, which ones open
F0030 | new ethics | is a necessary condition for | coexistence with a different kind of mind | - | assertion | ours; an ethics is written for the minds it binds
# --- the reader
F0031 | understanding an explanation of consciousness | has as aspect | reconstruction cost | - | assertion | ours
F0032 | reconstruction cost | is influenced by | intrapersonal intelligence | - | assertion | cite: Gardner 1983 (unverified) for the term
F0033 | eliminativist shortcut | is classified as a | low-cost reconstruction | - | assertion | ours; the absence of a construction
F0034 | anthropomorphic shortcut | is classified as a | low-cost reconstruction | - | assertion | ours; copying oneself
F0035 | quality of the self-approximation | is influenced by | intrapersonal intelligence | - | assertion | ours; the reader's difficulty and the object of study seen from two positions
# --- conclusion
F0036 | question of machine consciousness | is reformulated as | question with a measurable answer | - | assertion | ours
F0037 | conceptual half of the result | is about | named part of the functions | - | assertion | ours
F0038 | quantitative half of the result | is about | unnamed part of the functions | - | assertion | ours; the half that can fail
```

```gellish-residual DC
- | temporal | years rather than generations | "within a period that current trajectories put at years"
- | modality | may or may not | "that may or may not be prevented"
```
"""

BLOCKS['Why behaviour alone cannot settle it: the boy in A.I.'] = r"""
```gellish AP
F0001 | generalized function | is distinct from | large table of situations and responses | - | assertion | ours; two systems could produce David's behaviour
F0002 | observer with a small budget | exhibits | discrimination of generalization from a table by behaviour | - | denial | ours; cannot find the edge of the table, few tests, tests drawn from inside
F0003 | deflationary reading of models as memorization | is classified as a | behaviourally decidable claim | - | denial | ours; the argument cuts both ways
F0004 | degree of generalization | is a property of | substrate | - | assertion | ours; behaviour constrains it, the substrate measures it
F0005 | integrated information theory | is classified as a | account measuring on the substrate directly | - | assertion | cite: Tononi & Koch 2015 (verified); a different quantity
F0006 | long exchange of hours | has as property | position in a sparse space no table could hold | - | assertion | ours; memorization of the exchange as such is out of the question
F0007 | F0006 | is a sufficient condition for | generalization at the level of text | - | assertion | ours; the loose argument
F0008 | F0006 | is a sufficient condition for | generalization of the functions of consciousness | - | denial | ours; sentences composed freshly while the love is a table
```

```gellish-residual AP
- | rhetorical | | "sparsity settles that the model generalizes; the probe settles what"
```
"""

def main():
    md = open(PROSE).read()
    lines = md.split('\n')
    # find top-level (##) headings positions
    heads = [(i, l[3:].strip()) for i, l in enumerate(lines) if l.startswith('## ')]
    out = []
    for idx, (i, title) in enumerate(heads):
        j = heads[idx+1][0] if idx+1 < len(heads) else len(lines)
        seg = lines[i:j]
        # strip trailing blanks
        while seg and not seg[-1].strip():
            seg.pop()
        out.extend(seg)
        key = None
        for k in BLOCKS:
            if title.startswith(k):
                key = k
                break
        if key:
            out.append('')
            out.append(BLOCKS[key].strip('\n'))
        out.append('')
    # keep the preamble before the first heading
    pre = lines[:heads[0][0]]
    text = '\n'.join(pre + out)
    # drop the placeholder row marked REMOVE
    text = '\n'.join(l for l in text.split('\n') if not l.rstrip().endswith('REMOVE'))
    text = text.replace('is classified­ated as a', 'is classified as a').replace('is classificated as a','is classified as a').replace('is classified­ated','is classified')
    open(OUT, 'w').write(text)
    print('written', OUT, len(text.split()), 'words')

main()
