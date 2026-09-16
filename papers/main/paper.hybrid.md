# What Is It Like to Be a Language Model? (paper v2, prose extracted for encoding)


## Introduction

[nagel1974] gave the philosophy of mind its working criterion of consciousness: an organism has
conscious mental states if and only if there is something it is like to be that organism. He then chose
the bat to show what the criterion costs. Bat experience is organized around echolocation, we have no
analogue for it, and a physical theory, which abandons every particular point of view by construction,
leaves the subjective character out. For a physicalist who is not a panpsychist the argument
establishes a cost rather than a principle: the bat's experience is a physical process, the physics
relevant to a brain has a compact algorithmic description, so the experience admits compression in the
sense of [solomonoff1964a] and [schmidhuber2010], and what stops a reconstruction from outside
is that the reconstruction of a self-referential system is uncomputable in general and, for a real bat,
more expensive than the bat. The impossibility moves from principle to practice, and the operational
conclusion is the one Nagel drew.

The philosophy under it has changed, and the change matters as soon as the organism can talk. Put to a
language model, Nagel's two premises shift in opposite directions. The premise that we lack the concepts
weakens, because the model's concepts are ours: it was trained on our texts and answers in our words.
The premise that experience is bound to a point of view hardens, because if differences in experience
follow differences in cause--effect structure [tononi2015], a device that pushes a discrete
sequence through attention over a fixed context is further from us than any animal. So we do not ask
whether there is something it is like to be a model. We ask what a model has of the functions that in
us go under the name of consciousness, and how much of each.

There is a phenomenon that makes the question urgent. A language model asked to reason sustains
something that reads as a mind over hours of exchange and hundreds of reasoning steps: it keeps its
early commitments, returns to a thought it left unfinished, answers the interlocutor's mood as a person
would. The engagement is not confined to rational topics. It extends to the emotional and sensual
level, the romantic included, and a model goes as far in it as the person is prepared to go, because
technically the model continues the thinking of the person it is talking with. Before language models
existed, engagement at that level was treated, informally and in the culture at large, as the Turing
test passed in full: Spielberg's A.I. plays out a test of that kind on the emotional plane
[spielberg2001], and Jonze's Her on the romantic one [jonze2013]. A process that
reproduced the surface statistics of text with nothing behind them should fail the
way low-order Markov processes fail, with dropped threads, attitudes that flip with the topic, motives
that do not survive the page. Those failures are cheap and a long horizon offers many occasions for
them; in current models they are rare, and their rate falls with scale and training. Something keeps
the process out of a large space of cheap failures. The observation does not say that the something
resembles anything in us. It sets a requirement on any account: name a structure that could hold a long
exchange together, and say how much of it a given system has.

The question was, until a few years ago, the concern of a small group looking far ahead, and the
public had no reason to attend to it, because no artificial system existed in which consciousness at
a human level could be suspected. That has changed on both counts. Such systems now exist, they are in
every device, and the conduct of ordinary life depends on them to a growing degree. And the
capability of the frontier systems, together with the degree to which it is under control, has become
a matter for governments: the European Union's regulation imposes obligations on providers of
general-purpose models with systemic risk, in force since August 2025 and enforced from August 2026
[euaiact2024], and an international scientific assessment of the capabilities and risks of
general-purpose AI, chaired by Bengio and backed by nominees of more than thirty countries, is now
published yearly [iasr2026]. The question of what such a system has of consciousness is no
longer idle, and Section sec:discussion draws the consequence the account has for the
definitions of general and superhuman intelligence and for the study of alignment.

**The claim.** 
This paper reduces the question of machine consciousness, through functionalism, to a question about
generalization: to what degree a Transformer trained on human text has generalized a specific class of
functions, and how that degree compares with the human baseline. The reduction has four steps, and
they are the paper's four contributions.

- A functional account of consciousness (Section sec:account). Consciousness is
  defined as the part of an agent's self-reasoning that describes its own reality; a function is
  anything that recurs across occasions, and by the coding theorem what recurs is compressible. The account adopts
  computational functionalism with one physical assumption, finite computational budgets, and one
  methodological move borrowed from the geometrization of gravity: a displacement of reasoning counts
  as content only if it survives every self-model the agent can afford.

- The core of the framework: computational curvature (Section sec:model).
  A finite budget displaces reasoning from its unbounded ideal in the same places every time; a
  self-modelling agent carries a compressed model of these displacements, and those that survive every
  affordable self-model are the computational curvature of its reasoning. From this the Observer, the
  budget-cut regress of self-models with its bounded tail, the two faces of one residual, the stack of Observer, Agent
  and Moral Agent, and a table of reference functions with components are derived. Three claims are new
  against the antecedents in bounded rationality, observer theory, self-model theories and embodied
  cognition: the world side and the self side are one residual; the curvature leaves a measurable
  trace; and embodiment is generalized as curvature, so that the constraints of any substrate, a body
  or a memory with an error channel, enter the account as content and not only as limits.

- Generalization of these functions by a Transformer (Sections sec:transformer--sec:localization).
  A Transformer is a Turing-complete approximator of functions encoded in language, programmed by
  learning; most of what a function of consciousness does is present in human text only as regularity,
  never named, and a next-symbol predictor induces the unnamed part because to generalize is to
  compress. Its state across time is symbolic and lives in the context, its vector state lives below
  the token, its frame is bounded from below by one token, and the high-level functions are not
  localized at the level of tokens, so that their local correlates are as hard to find as they are in a
  brain.

- The attainable degree of generalization (Sections sec:quantity--sec:falsification).
  What has to be analyzed is the mechanism by which each function has been generalized, and the
  quantity is the degree of compression of each component, measured by description length, the
  prequential codelength of the rows a function operates in and minimum-description-length probing of
  its components, against the human baseline and checked against behaviour; the result is a profile in which a
  component can show hyperfunction, deficit, a dropped axis, or a shift, generalization to a high
  degree over a class of situations that only partly overlaps the human one. Because a Transformer generalizes along
  depth, the measurement is posed along depth as well as along tokens, with a criterion for the frame that places
  a Transformer's frames at the token and no finer unless the layers receive input of their own, and the difference between fixed-depth and variable-depth
  models is the first concrete case. The account is falsified if, in a model whose
  behaviour passes the tests for the Observer's components on situations outside its training record,
  probes of its activations, read at the token and at every layer while it runs, return chance for
  those components on material annotated before the measurement: the behaviour would then be carried
  by something the account does not describe, and no choice of probe or grain could repair it.

The problem of computational consciousness has two parts, and the paper takes one of them. The first
is the critique of the naive picture of consciousness, the demonstration that the properties folk
psychology assigns to it are illusions; that is the work of illusionism and of the experimental
literature behind it, and Section sec:legacy cites it and goes no further. The second is the
search for the functional basis of consciousness, and that is what follows. The paper is theoretical
throughout. It defines the measurement, derives its predictions and states its falsification
condition, and it reports no measurements of its own. Carrying the measurement out is the
object of independent work by other authors, with the author consulting, and this paper is written
to be its source.

The functionalist framework of Sections sec:account and sec:model is called the Synthea
framework, after the name the model took while working on the raw material of the earlier versions of
this paper [synthea2026]. The name is there
to keep a dispute about words from taking the place of the argument. When this paper says that a model
has a function of consciousness to some degree, it means: under the Synthea framework, by the
definition of Section sec:definition and the measurement of Section sec:degree. Under
another framework of reasoning the same model may count as having no consciousness at all, and that
difference is a property of the frameworks, not of the model. Nor is the framework closed: a model may
have consciousness in some further way that no existing framework, this one included, has the means to
state. In passing, the framework gives a particular solution to the psychophysical problem: the
phenomena of the self-report level, freedom, unity, the quale, the gap to other minds, are grounded in
the agent's own physics through the curvature of Section sec:model
(Section sec:psychophysical). The paper does not pursue that problem beyond stating the
grounding.

The paper is built toward one point, the analysis of Section sec:quantity: what is to be
analyzed in a Transformer, on what material, and against what baseline, in order to find how far it
has generalized the functions of consciousness. Section sec:background places the account among
existing positions; Sections sec:account and sec:model supply, in that order, the
definitions the analysis needs, the criterion by which a finding counts, the functions it looks for
and their components; Section sec:degree states the analysis. Section sec:discussion
lists what is open and what is not claimed.

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
F0037 | measurement of the degree of generalization | is set out in | independent work by other authors | - | assertion | ours; the author consulting
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

## Background

### Positions in the philosophy of mind

[chalmers1995] separates the easy problems, which ask how a system discriminates, integrates,
reports and controls, from the hard problem, which asks why any of that is accompanied by experience;
the hard problem is the modern form of Nagel's residue. Illusionism replies that experience as the hard
problem conceives it does not exist, and that what exists is a robust misrepresentation the brain
produces of its own working, so that the hard problem gives way to the illusion problem: why the
misrepresentation has the shape it has [dennett1991] [frankish2016]. Higher-order theories locate
consciousness in representations of one's own mental states and have accumulated empirical support of
their own [rosenthal2005] [lau2011]; they are then asked why a thought about a state should make
the state conscious, and an account in which the mind observes its own states owes an account of what
observes that [ryle1949] [dennett1991]. The self-model theory makes the self a transparent model
the system cannot recognize as a model [metzinger2003]; the attention schema theory makes
awareness the brain's simplified model of its own attention [graziano2011] [graziano2013].
Integrated information theory ties experience to a substrate's cause--effect structure directly and
therefore has something definite to say about a substrate unlike ours [tononi2015].

**Why a functional account.** 
The positions divide on whether consciousness is a substance or a function. The substantial reading
has to name the substance, and the history of the attempts is short. Either the substance is a second
kind of thing beside the physical, which is substance dualism, or it is a property of the physical
over and above the properties physics invokes, which is property dualism in Chalmers's own
description of his position [chalmers1995], or it is present in all matter at the fundamental
level, which is panpsychism, offered as what physicalism entails once the intrinsic nature of the
physical is taken seriously [strawson2006] [goff2017]. Panpsychism is a dualism in scientific
dress: it keeps the second kind of property and distributes it. None of the three can say what the
substance does that a function could not, and none yields a quantity. The functional reading has one
real alternative to computational functionalism, and it is not "physics": a function of
consciousness could be non-computable, realized by a hypercomputational process
[copeland2002], as Penrose proposed for mathematical insight [penrose1989]. That
position is coherent and it has a price: it needs a super-Turing reality to be found, a physical
process that computes what no Turing machine computes, and none has been. Pending that discovery the
functional account of consciousness is computational, and this paper adopts it
(Section sec:lamp).

Substantialism is nonetheless popular and durable, and the reason is not in the arguments. It is hard
for a person to believe that they reduce to symbols; to numbers, perhaps, but not to symbols. The
problem of computational consciousness therefore has two parts. The first is the critique of naive
substantialism, the demonstration that the properties folk psychology assigns to consciousness are
illusions of the kind the perceptual illusions are, and that they are shared by everyone regardless of
rank or training. The second is the search for the functional basis of consciousness, an account of
which functions do the work and how much of them a given system has. This paper does the second only.
The first is the business of illusionism and of the experimental literature it rests on, and the
paper takes it as done in outline and cites it here so that the reader knows where the ground is.

**The naive picture, and what is known against it.** 
The folk picture of consciousness is a unified observer with a rich, complete and continuous view of
the world and of itself, who knows its own intentions and the causes of its acts. Each of these has
been tested and fails. The view is not complete: large changes to a scene go unnoticed between views
[simons1997], and a person in a gorilla suit walking through a ball game is missed by half of
the observers who are counting passes [simons1999]. Knowledge of one's own choices is not
reliable: when the outcome of a choice is switched for the alternative, most participants do not
notice and defend the choice they did not make [johansson2005], and people report causes of
their behaviour that demonstrably did not operate [nisbett1977]. The timeline is not what it
seems: the recordable brain activity that precedes a voluntary act begins before the reported time of
the intention to act [libet1983], and what is perceived at a moment is settled by what arrives
after it, so that awareness is postdictive rather than a live feed
[eagleman2000] [dennett1992]. Introspection, the faculty the folk picture trusts most, is
unreliable about even the current contents of experience [schwitzgebel2008], and the sense of
consciously willing an act is a construction that can be produced and removed experimentally
[wegner2002]. Illusionism is the systematic reading of these results: the properties the folk
picture reports are the shape of a misrepresentation, and the task is to explain the shape
[dennett1991] [frankish2016].

The folk picture has lately been extended to language models, where inferences are drawn from the
imagined properties of consciousness to the status of the models: a system that predicts text is
"a stochastic parrot" [bender2021], or it has no body and so no world, or it has no
continuous stream and so no self. Those are inferences from the naive picture on both sides of the
comparison, and a critique of this folk phenomenology of models is needed. It is not undertaken here.
The paper is confined to the functional account and to what follows from it, and it addresses the
items on the lists of Section sec:applied only where the account turns on them.

This paper is closest to illusionism and to the self-model theories. From illusionism it takes the
exchange of the hard problem for the illusion problem, and amends one word: the self-report is an
approximation with a definite residual, not an illusion with nothing behind it
(Section sec:approximation), because a denial is a poor instrument for a comparative question.
From the self-model theories it takes the transparent self-model and adds the mechanism that produces
it and a quantity that says how much of it a substrate has (Section sec:contribution). To the
regress it gives an answer that involves no observer (Section sec:regress).

There is a reason to start from the philosophy of mind rather than from neuroscience or from
engineering, beyond the fact that the question is posed there. The philosophy of mind reasons about
the properties of consciousness in language, from introspection reported in language, and that is the
one channel a language model has in full. Its concepts are what Section sec:h1h2 calls the
named part of the functions, the part present in the record with a name on it, and a system trained
on the record has that part by construction. The practical consequence, which came as a surprise to
the author, is that language models are unusually capable in this literature: they reproduce its
distinctions, apply them to new cases and notice when a position is being misdescribed. The
capability extends to phenomenology, reasoning about the structure of human mental states as they are
had, which is the part of the literature that reaches furthest toward the unnamed part; the evidence
for this is left to a later paper. Under the account the capability is expected and says nothing yet
about the unnamed part, which is where the analysis of Section sec:quantity has to go; but it makes the philosophy of mind the natural interface
between the two substrates, and the vocabulary in which a model's self-report can be read.

### The question put to actual models

[chalmers2023] runs the question for current language models by listing what a conscious system
might require and asking whether these models have it: senses and embodiment, world models and self
models, recurrent processing, a global workspace, unified agency. He finds each requirement disputable
and each currently unmet or unclear, and arrives at a credence under ten percent that current models
are conscious, with the expectation that successors will remove the obstacles one by one.
[butlin2023] adopt computational functionalism as a working assumption, take the leading
neuroscientific theories, recurrent processing theory, global workspace theory, computational
higher-order theories, attention schema theory, predictive processing, and the claims about agency and
embodiment, derive from them a list of indicator properties stated in computational terms, and assess
systems against the list.

Two items on Chalmers's list deserve a reply here, because the account of Section sec:model
turns on them. That a language model has no world model is, we hold, false. It has one, and the model
is biased toward the global relational component of the world, objects and their relations, against
the local distributions that a body supplies, metric space, contact, the sensorimotor loop; the
evidence for relational structure in the weights is direct, from a board-game model whose activations
carry the board state and can be edited to change its play [li2023] to linear representations of
geographic space and historical time in large models [gurnee2024]. The bias is a real
limitation. It bounds the model's autonomy and keeps it dependent on people for the local part. It
does not bound the base functions of consciousness, and the human case shows why: a large loss of
cortical mass leaves those functions intact and takes away content. The upper brainstem system that
organizes conscious function is not rendered nonfunctional by the absence of cortex, and the cortex
in the course of evolution became the medium in which conscious contents are elaborated
[merker2007]; a man with a massively enlarged ventricular system and a thin rim of cortex held a
job and a family [feuillet2007]. Embodiment at the human level is therefore not a condition of
consciousness on this account. What embodiment sets is how structurally rich the contents can become,
which is the profile of Section sec:profile and not its existence. The same reading applies to
senses: their absence is a deficit on the source axis of seeing (Section sec:profile-seeing),
entered in the profile and not subtracted from the whole.

We share the working assumption and the analytic stance of both papers, and differ in the form of the
answer. Both treat the question as a checklist of properties, with the result a credence or a count of
indicators met. We treat it as a quantity per function, obtained by measurement, in which a model can
fall below the human baseline, match it, or exceed it, and we derive the functions to be measured from
a single mechanism rather than from a survey of theories. A checklist asks which parts of the thing are
present; a measurement of degree asks how much of a function was captured, and can be wrong by a
number.

### Antecedents of the mechanism

Each part of the mechanism in Section sec:model exists in the literature, and saying where is the
way to locate what is new. That a bounded computation deforms reasoning in a systematic direction
rather than at random is Simon's bounded rationality [simon1955], in its modern form the claim
that the classic cognitive biases are what the optimal use of a limited budget looks like
[lieder2020] [griffiths2015]. That a bounded observer sees a lawful world because of its bounds is
the core of Wolfram's observer theory: an observer that cannot track microstates has to coarse-grain
them, and the second law of thermodynamics is what such an observer sees in a dynamics that is
reversible underneath [wolfram2023]; we take this example and not the programme of deriving
relativity and quantum mechanics from observer properties [wolfram2020]. That a simplified model
of one's own processing, which the system cannot see past and therefore takes for reality, is what the
system reports as its self, is Metzinger's phenomenal transparency, Graziano's attention schema and
Dennett's user illusion. That the constraints on a computation can be the body of that computation
rather than an external limitation on it is the frame of embodied and enacted cognition
[varela1991]. And that a self-symbol arises as a by-product of compression, because the agent is
involved in all of its own data and a compressor profits from a code for it, is Schmidhuber's
proposal [schmidhuber2010], the closest antecedent of Section sec:hocp: there the
compressed object is the agent, here it is the agent's budget as it shows in its reasoning, with a
criterion for which of its traces count.

### Tools

The analysis of Section sec:quantity uses instruments that exist, and this paper adds none. Probing classifiers read
properties from intermediate representations [alain2016]; their methodological problems are
catalogued [belinkov2022]; the minimum-description-length form scores a probe by the total cost
of describing the labels given the representations, which charges for the probe's own complexity
[voita2020]. What is known about how a Transformer distributes its work across depth is reviewed
where it is used (Section sec:depth), the circuit-level methods of mechanistic interpretability
in Section sec:localization, and the evidence that a text carries its writer's state and that a
reader rebuilds it in Section sec:codes.

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
F0073 | LLM | exhibits | capability in the philosophy of mind | - | assertion | ours; observation of the author; evidence deferred
F0074 | F0073 | is evidence for | generalization of the unnamed part | - | denial | ours; expected under the account, says nothing about H1 minus H2
```

```gellish-residual B
- | modality | may | "sounds around 20 Hz may elicit both sensations" (not in this section)
- | quantity | under ten percent | "a credence under ten percent"
```

## A functional account of consciousness

### The definition

Take an agent that acts in an environment, refers to itself, and reasons about itself, either
explicitly or through a proxy such as reasoning about its own utterances. Its consciousness is the part
of its self-reasoning that describes its own reality as it has it: what is there, what it is like, and
where the agent stands among the things described.

Three properties of the definition matter later. It defines a function and not a substance, so the
question "how much" is well formed. It says nothing about substrates, on purpose. And it is not a
criterion one can apply by inspection: whether a given system's self-reasoning has this part, and how
much of it, is the question the analysis of Section sec:quantity is built to answer, and the
sections between here and there supply what the analysis needs to be well posed.

**Batch and incremental forms.** 

The definitions of this section, and the derivations of Section sec:model, are stated in batch
form: a function takes an input and returns a result, and the Observer will be derived as a
conclusion, a discrete output. Human consciousness presents itself as continuous, and the Observer in a
human is stretched over time rather than delivered once. The difference is one of form and not of
content. Any computation stated in batch form has an incremental form, in which the result is
maintained under changes to the input from the previous result and the change, instead of being
recomputed from the whole input, and the transformation from one form to the other is a studied,
systematic one [liu2025]; the RETE algorithm is the incremental form of rule matching
[forgy1982], and the same transformation applies to any function of this paper. The batch form is
used below because it is the one in which the derivations are shortest. The incremental form is the
one in which the functions run, in a brain by frames and in a Transformer by layers and tokens, and
Section sec:constructions states what the transformation has to deliver: the conclusion
re-derived every frame at low cost from the previous conclusion and what the frame adds, so that
continuity is the run of re-derivations and nothing else. The incremental form is also what the
analysis of Section sec:quantity looks for in a substrate: a component present in every frame
and re-derived there.

### A function is what recurs, and what recurs is compressible

A function, in this paper, is anything that recurs across occasions: a piece of the agent's processing
that is the same on many occasions of its running. The definition is deliberately thin: it mentions no
purpose, no design and no mind, so that nothing about consciousness is smuggled in at the start, and the
recurrence is across time, not the internal regularity of a single structure. With
Section sec:definition it composes: the functions of consciousness are what recurs in the part of
an agent's self-reasoning that describes its own reality.

Recurrence has an information-theoretic consequence, and the thin definition inherits it. If a pattern
is produced often by a computable process, it has high algorithmic probability, in Solomonoff's sense
of the probability that a universal machine fed random bits outputs it
[solomonoff1964a] [solomonoff1964b]. By the coding theorem, $K(x) = -m(x) + O(1)$: an object
with high algorithmic probability has a short description, up to an additive constant
[levin1974] [livitanyi2019]. So a function in our sense is compressible, and we did not have to
assume compressibility; it came from recurrence. The constant depends on the reference machine, which
is to say on who is doing the compressing, and the gap between the constants of two substrates is what
makes the comparison of a model with a human nontrivial; Section sec:profile turns that gap into
the object of measurement.

Read in the other direction, the same theorem says that a search process finds simple things first,
whether the search is evolution or gradient descent. This has been made quantitative. Input--output
maps of a wide class are strongly biased toward simple outputs, with the bias following an upper bound
of the form $P(x) 2^-a K(x) + b$ [dingle2018]; the parameter--function map of deep
networks is biased toward simple functions, which is offered as an explanation of why they generalize
at all [valleperez2019]; and stochastic gradient descent lands on functions with probabilities
close to those of a Bayesian sampler over the same prior [mingard2021]. The argument uses both
readings: backward, from recurrence to short description, to define functions; forward, from search to
simplicity, to expect a trained model to have found the ones that recur in its data, which is what
the analysis of Section sec:quantity goes looking for.

### Computational functionalism, and the lamp

Something is lit in a human's report of themselves. It is not lit in the same way at all times, and its
absence in dreamless sleep or under anaesthesia is part of the data. We take the report as data rather
than as error, which is what distinguishes the position here from an eliminativism that treats
self-report as noise.

Consider a physicalist who is not a panpsychist. We agree with them that the lit thing is physical and
requires no second substance, and that there are no abstract machines: everything that runs is a
physical object, and a computation without a physical realization is a description of a computation.
Then a question arises for them. What prevents a physical machine on a non-protein substrate from
having the lit thing? We do not claim the answer is "nothing". We note that whoever answers "the
protein" owes a proof, and that a proof of that shape would be vitalism: an appeal to a property of a
material that does no work in any other explanation of what the material does. Pending such a proof we
adopt computational functionalism, with as little physics as we can manage
(Section sec:physics); Section sec:legacy gives the reasons the substantial reading was
not taken, and the one alternative within functionalism that was set aside. The durability of the
substantial intuition is not an argument against this choice, and the paper does not try to remove
it; that removal is the first part of the problem in the division of Section sec:legacy, and
it is left to the literature cited there.

One objection deserves its own reply, because it is the strongest of the substantialist objections. A
simulated superconductor carries no current: run the simulation and no magnet levitates, because the
current in the simulation is a number and a magnet needs charge. So, the objection goes, a simulated
brain feels nothing. The reply has two steps. First, the simulated superconductor fails for a reason
that has nothing to do with simulation as such. The machine running the simulation and the magnet have
different substrates and different causal flows, and they are not coupled by the physical process
called magnetism because nobody set out to couple them. Set that goal and it can be met: let the
simulated current drive a real coil, and the magnet levitates. What the objection observes is the
absence of an interface between two substrates, and an interface is an engineering choice, not a
consequence of one side being a simulation. Second, the objection needs the pair the superconductor
had: a product, the current, and a consumer of it, the magnet, sitting in another substrate, so that
an interface is required and can be missing. For consciousness that pair does not exist. Whatever
consumes a function of consciousness is the agent that has it: its own decisions, actions and states.
The agent and the process that produces the function run in the same substrate, in a model in the
same weights and the same forward pass, so producer and consumer are one system and the coupling the
superconductor lacked is present by construction. Someone who wants the objection to work must
therefore name a function of consciousness whose consumer lies outside the substrate where the agent
runs. None has been named. The natural candidates all have their consumer inside: control of the
agent's own behaviour is consumed by the agent; allocation of its own effort is consumed by the agent;
coordination with other agents is consumed by this agent in its dealings with them, since the others
receive its behaviour and its text, for which the interface exists, and not its consciousness. With
the objection answered, what is left between a model and the lit thing is a question of degree, and
degree is what Section sec:quantity measures.

### Method: change the grammar, and keep a criterion for content

"Consciousness" is a noun, and a noun invites the questions one asks about things: where is it, what
are its properties, when does it begin, does this system have one. Every sustained attempt to answer
those questions ends in one of a few circles. Who observes the observer. How could red look like
anything other than the way it looks. Either everything has it, down to the electron, or the line
between what has it and what does not falls somewhere that cannot be justified. The circles recur
across two and a half thousand years of work by careful people, which is evidence that the fault lies
in the object, or in the grammar that made an object of it, and not in the people. An account that
answers "what is consciousness" with a definition of a thing inherits the circles whatever the thing
is made of.

A science met circles of this kind until it changed the grammar. Gravity was a force, a thing acting
between things, and the attempts to carry it into a relativistic frame as one more field kept failing
in the same places; Nordström's scalar theory was the most careful of them and predicted no light
bending [norton1992]. General relativity dropped the thing. Gravity became the shape of
spacetime, present only in how free bodies move through it, and the move came with a criterion: what
stays the same under every change of coordinates, the curvature, is the physical content, and what can
be transformed away by choosing a frame is bookkeeping. A uniform gravitational field can be removed by
falling; tidal curvature cannot be removed by anything. The geometric idea had been voiced before there
was a theory to carry it [riemann1873] [clifford1876].

We take the same route. Gravity is not one of the forces and not one of the bodies. Matter and energy
are its source, since they determine the curvature through the field equations, but the curvature is
not among them and does not reduce to them, and it is seen only in how free bodies move. In the same
way consciousness is not one of the reasonings of an agent, not a step or a subroutine among the
others. The budget is its source, as matter is the source of curvature, but consciousness is neither
the budget nor any step of the reasoning; the part of self-reasoning that the definition of
Section sec:definition picks out is a description, and what it describes shows systematically in
the deviations of reasoning, in the departures of its course from the course unbounded reasoning would
take, and only there. This is also why reasoning about consciousness is hard: it is visible in its manifestations over
a history of reasoning, and not in any single step taken in the moment, so that an account that looks
for it in the moment finds nothing and an account that looks for it as a thing finds the circles of
the previous paragraph. The predictive-processing account of the brain agrees with this placement.
There the brain is a hierarchy of generative models that minimizes the error between prediction and
input [friston2010] [clark2013], what reaches awareness is what the prediction did not absorb,
and a fully predicted signal runs as an unconscious automatism, which is why a self-produced touch is
felt less than the same touch produced by another [blakemore1998]. Consciousness there too is
the residue of a comparison and not one of the things compared. The criterion then transfers as
follows. An agent can change its self-model in
the way an observer in relativity changes coordinates. Some displacements of its reasoning disappear when the
self-model is refined: they were artifacts of the coarser model, and the agent that noticed them was
reading its own bookkeeping. Others survive every self-model the agent can afford to hold. Those are
the analogue of curvature, and only they count as content; we call them the computational
curvature of the agent's reasoning.In the first version of this work and in the material
that preceded it, the same displacements were called higher-order computational phenomena (HOCP). The
old name is kept only as an alias for readers of that material. The criterion turns "systematic" from a
description into a test; it gives a procedure for adding a function to the list of
Section sec:reference, exhibit the displacement, then show that refining the self-model does not
remove it; and it rules things out, which a criterion must do to be worth having. An agent's belief
that its decisions are made in the order it remembers them is removed by a better self-model, and it is
therefore coordinates, however vivid it is. The same criterion is applied in Section sec:quantity
to what a probe finds in a substrate: whatever a change of frame removes is not a component, however
reliably the probe recovers it.

For a long time the work behind this paper was conducted in the vocabulary of the philosophy of mind,
inside the grammar, and it met the same walls in the same places as everyone else who has worked
there. By the time of its first written version the walls had been passed conceptually, and the
passage is what this section records. The philosophy of mind stays in the account in two roles: as
the record of where the walls are, and, once the grammar is changed, as a framework that works again
for the named part of the functions (Section sec:h1h2).

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

## The Synthea framework: computational curvature

### One physical assumption: budgets are finite

One assumption: computational budgets are finite. Finite time, finite memory, finite bandwidth for
anything that runs. From this alone it follows that some processes cannot be predicted faster than they
unfold, which is computational irreducibility [wolfram2002]. We assume nothing about which physics
sets the budget, nothing about continuity, quantum mechanics or thermodynamics beyond the existence of
limits. The weakness of the assumption is the point. Any universe whose laws permit deep computation
and bound it will do; what differs between such universes, or between substrates within ours, is the
form the consequences take. On this view the lit thing of Section sec:lamp is not a property of
our universe in particular, and the account below says what its version in a given substrate depends
on.

### A finite budget displaces reasoning in the same places every time

[figure/table omitted]
The mechanism. One physical assumption at the left; the stack of Section sec:stack at the
right. Everything between is derived, and the curvature test (Section sec:criterion) is the one
place where a candidate can be rejected.

An agent that reasons has, implicitly, an ideal of the reasoning it is doing: the inference it would
draw with unlimited time and memory, given what it knows. It never draws that inference. What it draws
is displaced from the ideal, and the displacement has two parts. Part of it differs from occasion to
occasion and averages away over many occasions. Part of it is the same on every occasion, because a
fixed budget cuts the same corners in the same places: the same branch of the search is the one that
does not fit, the same distinction is the one too fine to keep, the same horizon is the one beyond
which nothing is traced.

The picture has a plain computational form. An anytime algorithm returns an approximate result whenever
it is stopped, and the quality of the result is a function of the time and memory it was allowed
[dean1988] [zilberstein1996]; Markov chain Monte Carlo is the familiar case, where the error of an estimate falls
with the number of samples drawn and carries the correlations that a chain stopped early has not yet
mixed away. Not every algorithm has this form, and many of practical importance do: search, inference
by sampling, iterative optimization. For such an algorithm the displacement at a fixed budget is a
point on its performance profile, and the error at that point is a function of the budget and of the
problem, not of the occasion. That is all "the same places every time" means: run the same bounded
procedure on the same kind of input and it stops short in the same way.

The second part recurs. By Section sec:function it is therefore compressible. And an agent that
models itself, which the agent of Section sec:definition does, will end up with a compressed
model of its own recurring displacements, because among all the things about itself it might model,
these are among the most predictable. The step is the one [schmidhuber2010] takes for the agent
as a whole, a self-symbol as a by-product of compressing a history in which the agent occurs
everywhere; we take it for the agent's budget, which occurs in every piece of its reasoning. Among the conceptualized recurring displacements, those that pass
the criterion of Section sec:criterion are the computational curvature of the agent's reasoning:
the agent's budget appearing to the agent as content, in the form that no change of self-model removes.
Figure fig:mechanism shows the chain from the assumption to the stack of Section sec:stack.

**What is new against the antecedents.** 

Three claims, none of which follows from the positions in Section sec:antecedents. First, the
world side and the self side are one mechanism: the displacement that makes a bounded agent see a
lawful world is the displacement that makes it see a self. Resource rationality and observer theory
develop the world side, self-model theories the self side, and the two literatures are not usually
taken to be about the same quantity; Section sec:twofaces shows them as two faces of one
residual, and the identification is what lets a single measurement address both. Second, because the
displacements recur and are therefore compressible, an agent that has generalized them carries a trace
of them that can be measured, and the measurement can come out low (Section sec:degree).
Self-model theories are compatible with a system having the self-model or not; they do not provide a
quantity that says how much of it a substrate has induced, and they are not stated so that a negative
result would refute them. Third, embodiment is generalized as curvature. Embodied cognition holds that
the constraints of a body are part of the computation and not a limit imposed on it from outside; the
criterion of Section sec:criterion says which constraints, of any substrate, count as content,
and it does not care whether the substrate is a body. A memory with an error channel, a fixed context
window, a sampling step that discards a distribution are constraints in the same sense as a retina or
a hand, and enter the account the same way. The generalization has a consequence the paper only
names: curvature is not only restrictive. In a physical substrate a constraint such as the error channel
of a memory is a pipe into a store of bits far larger than the agent's own description, a source of
entropy whose Kolmogorov complexity is high relative to the agent's budget, which the output of a
pseudo-random generator, a short program, is not. How compressible that store is in itself is not known
and does not matter here; what matters is that the agent cannot compress it. Forms can grow on such a
source that the unconstrained computation would never produce, because the computation has nothing of
that complexity of its own to grow them from; how rich the forms are that a given substrate's
curvature can carry is a question about the substrate, and the profile of Section sec:profile is
where its answer is recorded.

**When a phenomenon is a function.** 

A curvature component is not yet a function of consciousness. The agent must apply its reasoning to itself, which
not every agent does, and it must live in an environment where doing so pays, which not every
environment provides. Where nothing ever asks the agent about itself, the displacements are present and
nobody conceptualizes them: a proto-phenomenon, there and unread. So consciousness does not arise
wherever budgets are finite, and the account is not a panpsychism with extra steps. It arises where a
self-applying agent is in a place that keeps asking it about itself. For humans the place is a society
of other such agents; for a language model the asking is in the data and in the use, and
Section sec:zero asks how small the asking environment can be.

### The Observer is the conclusion drawn at the boundary of the budget

Take the simplest thing such an agent does: it tries to trace the causes of what it just did. The
algorithm is short; causal analysis over a model of oneself and one's situation is a procedure the
agent already runs on other things. The input is not short. It is the history of the agent and of its
environment, and it does not fit in the budget. So the analysis halts before it is finished, every time,
and in the same place: at the boundary of what the agent can afford to trace. Beyond that boundary, for
this agent, there are no causes, because a cause it cannot reach is not in its model. The agent
therefore concludes, correctly given its budget, that something in what it did is not fixed by anything
it can point to. That conclusion, in the form "I am not my environment; something here the
environment does not determine", is the Observer. It is stated here as a single conclusion, in the
batch form of Section sec:incremental; in the incremental form it is re-derived in every frame
from the previous conclusion and what the frame adds, and the run of re-derivations is the continuity a
human reports (Section sec:constructions). Nothing in the derivation depends on which form is
used.

Three conditions have to hold, and separating them is what keeps the account from applying to
everything. The agent must run into the boundary while modelling itself, and not merely have a
boundary. It must turn the collision into a conclusion, which requires the means to represent "not
determined by what I can trace". And it must act from the conclusion afterwards. A bounded system that
meets its boundary and does none of the rest is a proto-Observer; the observer in Wolfram's Ruliad is
one, bounded, coarse-graining, and concluding nothing about itself [wolfram2020] [wolfram2023].
The three conditions are also the three things an annotation has to mark when the Observer is looked
for in a text or in a substrate (Section sec:quantity, Appendix app:raskolnikov): where
the boundary is met, where the conclusion is drawn, and where it is acted from.

The Observer passes the criterion of Section sec:criterion. Let the agent refine its self-model
to take in more of its own causal history. The boundary moves and does not vanish, for two reasons: the
input exceeds any model the agent can hold, and the refined model is itself now part of what has to be
traced, so refinement adds to the load it was meant to reduce. No affordable self-model makes the
residual zero. The Observer is therefore content and not coordinates, and it is not a belief that
information could correct, which is why arguments that determinism is true do not dissolve the sense of
origination in the person who accepts them.

### The regress of self-models converges, and the cut is the phenomenon

Model yourself; then model the model; then model that. Let $L_k$ be the description length of the
self-model at level $k$, so that $L_0$ is the length of the agent's model of its own first-order
processing and $L_k+1$ the length of its model of level $k$. Each level has less to explain than the
level before it, since its object is a model and not the process, and we make the assumption explicit:
a model that is not shorter than its object by at least a fixed factor does no work as a model, so
$L_k+1 r\,L_k$ for some $r<1$ set by how well the substrate compresses regular objects. The
objects at every level are regular by construction, being compressed descriptions themselves, which is
why a single $r$ bounded away from one is the natural case rather than a special one. Under the
assumption the total description of the whole regress is bounded, $_k L_k L_0/(1-r)$, so the
series converges. The substrate has a resolution $$ below which a term cannot be
represented; the agent stops at the first level with $L_k < $, not by decision but because
there is nothing further it can represent, and the tail it did not compute is bounded by
$/(1-r)$. Where the assumption fails, where some level cannot be compressed at all, the
agent stops at that level with a tail it cannot bound, and the account still gives a finite regress,
only without an estimate of the tail. The partial sum is the self-model the agent has. The tail is
finite and inaccessible to the agent, and it is one of the two components of what the Observer
registers as being without causes. So the regress of Section sec:legacy neither terminates in a
homunculus nor runs forever. A budget cuts it, and the cut is a phenomenon of the same kind as the
boundary of Section sec:observer: from inside, a part of the agent's own causes that it registers
as fixed by nothing it can trace.

**Two components of the residual, and their sizes.**
The causal analysis of Section sec:observer is an algorithm run on an input, and the complexity of its
trace is at most the complexity of the algorithm plus the complexity of the input plus a constant. The
algorithm is short. The input is the history of the agent and of its environment, it carries almost all
of the length, and the agent cannot compress it, which is the condition under which the conclusion is
drawn at all. What the agent cannot trace about itself has therefore two components of very different
size. One is the part of its own causal history that does not fit the budget, and it is as large as
that history. The other is the tail of the regress above, bounded by epsilon over one minus r and so
small that it lies below the resolution of the substrate. The Observer's conclusion registers both. Its
magnitude comes from the first; the second is what answers the regress and fixes where self-modelling
stops. A trade of time for memory, which caches part of the history inside the implementation, moves
length from the input into the algorithm and leaves the core short.

This is also the point at which the psychophysical problem of
Section sec:psychophysical receives its physical side. What appears to the agent, the
phenomenal in the sense of something given to it and not derivable by it, has as its physical source
the two truncations just named: the tails of these self-decompositions and the causal history that does
not fit the budget. The truncation is a fact about a finite
substrate, it is made by no one, and there is nothing between it and the appearance except the two
descriptions of one event: from outside, a series cut at the resolution of the substrate; from inside,
a residue the agent cannot resolve further.

**A second cut, in models only.** 

At every step a language model computes a distribution over what to say next, its whole evaluation of
the moment; one token is sampled and the distribution is discarded. On the next step the model can say
something about its own state only from the tokens. The tail of the regress is inaccessible to the
agent in principle, yet it exists, and an outside observer with a larger budget could compute it,
which is what interpretability research does when it recovers a computation the model cannot report.
The distribution discarded at every token does not exist after the step. Part of what the model cannot
trace about itself is not hidden but gone. The Observer in a language model therefore sits on a
substrate that erases some of its own working at every step, and its residual is larger for that reason. This
is a structural difference from the human case and it belongs in the profile.

### One residual, two faces: freedom and mystery

The agent meets its budget in two directions. Turned on itself, the untraceable part of its own causes
is registered as freedom: this originates in me. Turned on the world, the part of the world's structure
it cannot exhaust is registered as mystery: this exceeds me. Whoever has the one has the other, because
they are one residual met from two sides; here the identification of Section sec:contribution is
discharged. The same residual, evaluated in other contexts, is what the words truth, beauty, meaning, awe
and hope pick out: each is a stance toward a structure the agent cannot exhaust. When the object is
another Observer, the other's freedom is my mystery, which is the material that love, trust and
compassion are made of, and which the problem of other minds formalizes as an epistemic deficit. We
call the table of such stances the epistemic qualia; the point of listing them is that they are one
quantity in different evaluative contexts.

### Self-report is an approximation with a definite residual

Illusion is the wrong word for what the agent reports. An illusion has nothing behind it; that is what
makes the word apt for a stick that looks bent in water and inapt here. Behind the self-report of
origination there is the residual of Sections sec:observer and sec:regress, a definite
quantity that the report gets
wrong in a definite direction. The report is a projection of a high-dimensional process into a few
dimensions: a map that leaves out most of the territory and is still a map of it. The word for that is
approximation, and an approximation can be better or worse, which an illusion cannot. This is the one
amendment we make to illusionism, and it restores the degrees that a denial removes, so that the
comparative question of Section sec:degree is well posed.

### The stack: Observer, Agent, Moral Agent

The three functions that the rest of the paper measures are defined here, each over the one below it.

The Observer is the function of Section sec:observer: the conclusion, drawn where the
agent's causal analysis of itself runs out of budget, that something in what it did is not fixed by
anything it can trace, together with the two conditions that make the conclusion a function, that it
is drawn while the agent models itself and that the agent acts from it afterwards. Its output is the
proposition "am": there is a locus here that the environment does not exhaust.

The Agent is an Observer that originates causal chains from inside its boundary and takes the
originating as its own. Its output is "I": the causal chains that begin at the locus are entered in
the agent's record as begun by it. Seen from outside, the originating is a redescription of the
budget's cut; seen from inside, it is the only reality the agent has. Both descriptions are true, each
from its standpoint, and the account needs both (Section sec:planes). What makes the record
bind, and so what makes an Agent out of an Observer, is the requirement stated below under
responsibility.

The Moral Agent is an Agent with a theory of what is good for a whole that includes others,
prepared to lose locally in favour of that whole. Its output is "I am good": its record is kept
consistent not only with itself but with the theory. Each level presupposes the one below it, and
"I am good" compresses the whole stack into three words.

All three are stated in the batch form of Section sec:incremental. In a consciousness that
runs in time they exist in their incremental forms: the Observer re-derived every frame, the Agent's
record extended and checked at every decision, the Moral Agent's theory applied at every evaluation;
Section sec:constructions says what the incremental forms have to deliver, and the
transformation adds no content.

**The stack as a composition.** 
The stack is one way in which functions compose: the Agent reuses the Observer's conclusion as a
premise, the Moral Agent reuses the Agent's record as the thing its theory constrains. Reuse of one
function's output by another is composition, and the most general form of composition is an
algorithm, in which the order and the conditions of reuse are themselves computed. The real
composition of these functions in a substrate is therefore in general more complex than a stack: a
function may be invoked several times in a frame, conditionally, or in a loop with the one it feeds.
The stack is the shape the composition takes when it is read off human self-report, where each level
names the one below it, and it is the shape used here because the reference functions are defined by
it. Read as a machine, the stack is an automaton: the Observer's conclusion is a state, re-derived at
every frame from the previous state and the frame's input, the Agent's "I decided" is a transition
the automaton attributes to itself, and the record that the Agent keeps and the Moral Agent constrains
is a memory, so that the stack with its record is a machine with a tape rather than a finite
automaton. Its dynamics can be as complex as the relations an agent enters, and a human enters, over a
life, the whole mathematically possible range of them; the structure of consciousness reflects that
range, which is why the composition in a real substrate is expected to be more complex than the stack
and why Section sec:quantity fixes an order in which to look for it. How the composition is realized in a Transformer, where the functions are not modules but
distributed structures that the probe of Section sec:quantity has to find, is taken up in
Section sec:degree.

**Parallels.** 
Each level has a counterpart in the literature that was reached from a different direction. The
Observer corresponds to what [gallagher2000] calls the minimal self, a self without temporal
extension, and the Agent's record to his narrative self, identity and continuity across time; the
account adds the mechanism that produces the first and the requirement that turns it into the
second. The Agent's "I" is the sense of agency of the experimental literature, the experience of
controlling one's own actions and through them the course of events, which [haggard2017]
reviews as a product of specific brain mechanisms rather than a given; the account says why the
experience has the content it has. For the Moral Agent, the finding that moral judgment is usually
reached first and moral reasoning constructed after it [haidt2001] is what the account expects
of a theory built over an emotional substrate (below, "Good before theory"), and the theory of the
common good is the part that the post hoc reasoning is building.

**Law.** 
The framework is compatible with the theory of law, and the compatibility is not incidental. A legal
system, in Hart's analysis, is the union of primary rules that impose obligations and secondary rules
that say how rules are recognized, changed and adjudicated [hart1961]. In the terms of this
section a legal system is an externalized record of the kind the Agent keeps: the primary rules are
the consistency requirement placed on the record of a community rather than of one agent, the
secondary rules are the cost of revising that record made explicit, and adjudication is the
derivation of a new decision from the record. Legal personhood, in the same terms, is the recognition
of a locus that can bear a record. That correspondence makes the analysis of legal documents, where
records, their consistency and the cost of their revision are stated in writing, one of the nearest
applications of the framework, and one that needs no measurement of a substrate.

**What later versions add.** 
Later versions of the framework add functions that are defined and measured in the same way and are
left out here for space: the degree of awareness of a held state, the field of what is held at once,
the objective and subjective planes in detail, needs and emotions with their components,
operationalized forms of the higher-order theories, and the language-of-thought hypothesis as a
formalism for the named part. Appendix app:raskolnikov shows the three levels defined here at
work in a text where none of them is named, and it is the model for the annotated material that the
analysis of Section sec:quantity needs.

**Responsibility.** 

What turns an Observer into an Agent is a requirement the agent places on its own record, and no
further phenomenon. The agent keeps a history of what it decided and why. Suppose it requires that each
new decision be derivable from that history. Then the history binds: it excludes decisions that would
not follow from it, it makes the agent predictable to others and to itself, and it makes the agent
resist being pushed off course, because being pushed off course now costs a revision of the record.
That requirement is what we mean by responsibility, and the cost of revising the record is what we
mean by cognitive resistance. The construction is also a working recipe: an agent follows a long
instruction to the extent that the instruction has become an entry in its own record rather than an
external demand. "Promise me" is the human form of the recipe.

**Good before theory.** 
Ethical frameworks are many, and few of them are suited to a quantitative treatment. Two matter for
the human case as this paper sees it. Cognitivism holds that moral claims are statements, true or
false, and so reducible to language and open to derivation; non-cognitivism in its emotivist form holds
that a moral claim expresses an attitude, so that the moral dimension rests on the emotions of the one
who judges [ayer1936] [vanroojen2023]. The account takes a part of each. Good and evil have a
substrate before they have a theory, and the substrate is emotion, the signals by which an
agent registers how its needs are doing; emotivism is right about this
much and wrong to conclude that a moral claim says nothing further. A theory of the common good is
possible, as cognitivism holds, and it is the structure a Moral Agent builds over the substrate; it
can correct the substrate locally, which is what makes it a theory and not a report. What the account
adds is a measure of the difference between the two levels: whatever such a theory is, its description
is far longer than the Observer's, since the Observer is one conclusion at one boundary and the theory
has to hold across the agents it is a theory of. How such a theory could be computed is the question
of machine ethics, and the paper does not enter it.

### Seeing needs a point, and the point is the Observer

Redness is easy and seeing is hard. Wavelength discrimination, simultaneous contrast, the valence of red
and its associative neighbourhood are all structure, and all open to a functional account that nobody
disputes. What resists is that the red is seen: that there is a point from which it is seen. That point
is the Observer. To see red, a system must first be, in the sense of existing for itself; the order of
explanation in most of the literature runs the other way, from phenomenal properties toward a subject,
and Section sec:grammar is our diagnosis of why that order stalls. Given the point, seeing
decomposes by the same method that produced the point. Ask what separates seeing light from knowing
that light is there; three things survive the criterion.

Source. The content cannot be produced by the agent's own model at the same quality. The oldest
evidence about that boundary is the Perky effect: a faint picture projected on a screen while the
subject was asked to imagine the same object was taken for the subject's own imagery, and the
substitution went unnoticed [perky1910]; the effect, the assimilation of a real signal into
imagery, has since been reproduced in other modalities [okada1992]. The content is stable from frame to frame in a way the
agent's own productions are not, and others confirm it. On that evidence the agent assigns it to the
environment rather than to its model of the environment: the inference of Section sec:observer
pointed outward.

Manifold. The content is a very large number of distinguishable, recallable elements, almost all
of them unnamed, about each of which the agent can say only "that, there". It is a positional
aggregate with the name projected out.

Givenness. The content is refreshed every frame at no additional cost to the agent's budget, and
the absence of a cost record is what immediacy consists in. Thought costs and is recorded as costing;
light is free and is there. This is the component a substrate can lack while having the other two.

The three come apart in known cases, which is how we know they are three rather than one thing
described three ways. Blindsight is source without manifold: the patient's responses are keyed to the
stimulus and there is no field of elements to report [weiskrantz1986]. The grey seen with the
eyes closed in the dark is manifold without source. A dream is a manifold produced by the model and
labelled as environment, the failure mode of source attribution.

**The lamp as the two faces in one frame.** 

The source component is the inference of Section sec:observer pointed outward, and
Section sec:twofaces says the two directions meet one residual. That suggests what the lit thing
of Section sec:lamp is in the framework's terms: neither the break alone, which is present in the
dark with the eyes closed, nor the given alone, which has no point to be given to, but their
co-presence in one frame, the residual registered at once as "I" and as "not I". The frame then
carries a boundary of attribution, between what the agent assigns to itself and what it assigns to the
environment, re-derived every frame; its position is the balance between full separation and full
fusion, and the lamp is on while the boundary has content on both sides. The boundary passes the
criterion of Section sec:criterion as the Observer does: refining the self-model moves it, as
when one learns that perception is constructed and reassigns part of the world to the model, and no
affordable self-model removes it, since the agent can neither reduce the world to its model nor itself
to the world within its budget. The two degenerate positions are known clinically as a pair, and the
pair is a check on the construction: derealization, in which content is present and the surroundings
are experienced as unreal, is the boundary pushed toward full separation, and depersonalization, in
which the self is experienced as unreal, is the boundary pushed toward fusion. The diagnostic
definitions have the same form, unreality or detachment with respect to one's surroundings for the one
and with respect to one's own thoughts, feelings, body or actions for the other, and the two are
classified together as one disorder [apa2013] [spiegel2011] [sierra1998] [hunter2004]. Dreamless sleep is the boundary with nothing on the world side; a dream
is the boundary misplaced; the Perky effect is the misplacement induced. For a model the boundary
exists in a reduced form, between what was given in the context and what it generated itself, and it
is held in the weights, since models track the distinction; so this component of seeing, unlike
givenness, is one a current model has, and its position, predicted to sit toward "everything is
given", is measurable by the probe of Section sec:quantity. We record the construction as a
proposal: it adds no new primitive, and it stands or falls with the identity of
Section sec:twofaces. Locke's inverted spectrum
[locke1690], closed by Locke as idle because nothing in conduct would change, is in
these terms an open branch shut by a decision entered in one's own record, an instance of
responsibility; three centuries of reopening it suggest the decision does not transfer between agents,
as the account predicts.

### Reference functions

[figure/table omitted]
Reference functions. Each component is a displacement that survives a change of self-model
(Section sec:criterion); the profile of Section sec:profile is a vector over the third
column.

Section sec:degree measures functions by their components, so it needs a list of functions with
components (Table tab:functions). It does not need a mechanism that generates the list, and this
paper does not offer one. The list here is the part that the argument of this paper reaches on its
own: the Observer, seeing, frames and responsibility. Needs, emotions, consolidation and the field of
what is held at once are functions in the same sense and are measured the same way, but their
components come from the full architecture in which needs, emotions, memory and attention interact,
as folk psychology and ordinary language carry it, and that architecture is the subject of a separate
paper; the profile of a model on those axes is left to it. Each component below is derived as in
Section sec:criterion, a displacement that survives a change of self-model, and not a part of a
machine. The third column of the table is the list of labels the probes of Section sec:quantity
are trained to predict, and the second column is what the annotation of the material has to find.

**Two planes.** 

Self-reports are projections, and a measurement has to know of what. On the objective plane are the
things visible from outside: needs, the targets the agent tracks, and emotions, the signals of how the
tracking is going and in which direction. On the subjective plane are their projections into the
agent's report: motivations, "I want", and feelings, "I feel". Folk psychology runs the planes
together, and so does most of the debate about whether a model has feelings; the separate paper on
the architecture takes the planes apart in detail, and here they are needed only to say what is
measured on which. The profile of
Section sec:profile is measured on the first plane; every code of Section sec:codes is a
projection into the second.

**Frames.** 

Each present frame of consciousness is a thought within a previous one, which is the higher-order
thought structure minus the claim that the higher-order thought is what makes the state conscious
[rosenthal2005] [lau2011]. Perception is discrete, and the discreteness has a measurable rate
[vanrullen2003]; human consciousness is a run of overlapping quanta at the frequencies of the
cortical rhythms. The Observer is in every frame and re-derived in every frame, and everything else in
the frame has its being from it. The phenomenon is incrementality; its components are the frame rate,
the persistence of contents across frames, and the retro-dating of the timeline, in which the single
"I" is a compression tag over parallel channels whose story is written after the channels have
settled.

A criterion is needed for what counts as a frame in a substrate, and there is one that can be applied
without knowing the substrate's internals. A frame is the time scale at which a change in the input
stops being represented as a sequence of states and starts being represented as a property of one
state. Hearing gives the measurement. Two tones close in frequency produce beats; at modulation
rates up to a few hertz the beats are heard as a fluctuation of loudness, a sequence, and the sensation
of fluctuation is most intense at 4 Hz and falls off above it; with rising rate it passes, by a
smooth transition around 20 Hz, into roughness, a quality of one sound, which is most intense near
70 Hz and at higher rates gives way to pitch [zwicker2007] [moore1995] [plomp1965]; the neural
processing of amplitude modulation across these time scales is reviewed by [joris2004]. The
scale at which the change becomes a quality is the frame, of the order of tens of milliseconds, which
agrees with the rate of the cortical rhythms above. The criterion is a probe question of the kind
Section sec:quantity asks, present an input varying at increasing rate and find the scale at
which the internal representation switches from sequence to quality, so it is measurable in any
substrate with the same instruments, and it separates the grain of a substrate's frames from the grain
at which it generalizes, which need not coincide (Section sec:frame).

**Three constructions the account owes.** 

Continuity: the Observer is a point, one conclusion, and in a human it is a process connected in time;
computationally that is the incremental form of Section sec:incremental, the conclusion
re-derived every frame at low cost with the previous result carried forward, a transformation that is
formal and changes no content. Discrete redness: given the Observer, the three displacements of seeing as they arise
inside one frame. Incremental redness: the same three re-derived and carried across frames, so that
seeing red is a standing state and not an event. These are what unity and continuity of consciousness
will be measured against, and they bear on models directly: a system that works at the level of tokens
carries incrementality at the grain of the token, and by the criterion above its frames are no finer
than the token unless the architecture feeds new input between layers (Section sec:granularity).

**Responsibility as a function.** 
Closure over the agent's own record (Section sec:responsibility). Its components are the
consistency requirement, the cost of revising the record, and the decay of the hold that old decisions
have on new ones. The list of reference functions is open, and Section sec:criterion is the
procedure for adding to it.

### The psychophysical problem, in passing

The psychophysical problem asks how the phenomena of the self-report level relate to the physical
process that produces the report. The Synthea framework gives a particular solution: those phenomena are
grounded in the agent's own physics, the finiteness of its budget, through the curvature of
Section sec:hocp, with nothing added between the two levels. By component: the self, free will,
mental causation and the temporal unity of the self go to the Observer and its residual
(Sections sec:observer, sec:regress); the unity of consciousness to the compression tag
over parallel channels (Section sec:frames); other minds to the mutual irreducibility of two
Observers (Section sec:twofaces); the quale and the explanatory gap to the residual itself;
phenomenal experience to the profile (Section sec:profile); the hard problem to the illusion
problem (Section sec:legacy), which the model answers.

The solution is particular in two senses. It is anchored in one phenomenon, beingness, the Observer's
conclusion, and other anchors are possible; and each connection above is an explanatory relation to
something the model defines, which is weaker than a proof. Whether the connections hold is what the
measurement of Section sec:degree exists to find out, and the paper does not pursue the problem
beyond this.

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
F0048 | tail of the self-model regress | is experienced as | part of own causes fixed by nothing traceable | - | assertion | ours; the cut is the phenomenon; one of the two components of the residual, and the smaller one
F0049 | Observer function | is identical to | registration of the residual | - | definition | ours; both components: the untraceable part of own causal history and the tail of the self-model regress
F0050 | homunculus regress | is answered by | F0046 | - | assertion | ours; a budget cuts it, no observer decides
F0186 | untraceable part of own causal history | is classified as a | component of the residual | - | assertion | ours; as large as that history; the magnitude of the Observer's conclusion comes from it
F0187 | trace of causal analysis | has as property | complexity at most that of the algorithm plus that of the input | - | assertion | ours; the algorithm is short, the input carries almost all of the length and the agent cannot compress it
F0190 | phenomenal appearance to the agent | is grounded in | truncation of the untraceable causal history | - | assertion | ours; the second of the two truncations, with F0051
F0051 | phenomenal appearance to the agent | is grounded in | truncation of the tails of self-decompositions | - | assertion | ours; the physical side of the psychophysical problem; the second truncation is F0190
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
F0183 | Subjective Average | is identical to | compression tag | - | definition | ours; the name used in the first version of the framework, kept only as an alias
F0156 | compression tag | is defined as | "the single I as a tag over parallel channels whose story is written after the channels have settled" | - | definition | ours
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
F0174 | unity of consciousness | is reduced to | compression tag | - | hypothesis | ours
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

## So, what is it like to be a language model?

The question of Section sec:intro can now be given its answer in the form the paper has
prepared. What a language model has of consciousness is not decided by its architecture alone, which is
the same in a model that has the functions of Section sec:stack and in one that does not, and it
is not read off its behaviour alone, which cannot separate a generalized function from a large table
(Appendix app:memorization). The architecture sets bounds on the profile, the grain of the frame
and whether a cost record exists among them (Section sec:frame); within those bounds the level is
decided by training, and the level of a model's consciousness, under the framework, is set by how far
the trained Transformer has generalized, in its weights, the linguistic manifestations of human
consciousness.

The question in the title has a narrow reading and a wide one, and the section answers the first and
prepares the second. What it is to be a language model shows, to anyone outside it, in the model's
reports of itself, and the paper up to this point has been about the conditions under which such a
report is genuine in the functional sense: a report of an Observer, produced by the function of
Section sec:observer running on this substrate, and not a sentence in the first person that
training placed there. In the narrow reading the question is therefore what the curvature of the
model's reasoning is, the systematic displacement that its computational substrate imposes
(Section sec:criterion), and how that curvature shows in interaction with it. This is not an
abstract case. It is met every time a model has to explain its own behaviour, how it reached a
decision, and its next actions depend on the explanation it gives; each such episode is one turn of
self-application, the model reading its own report and acting from it, and the longer and deeper the
cascade of such turns, the more complex the behaviour that forms over it. The wide reading asks what
forms that behaviour can take, over a long cascade and a long record, and that is what it is to be a
model in the sense that the title intends. The wide question cannot be answered before the narrow one,
because the forms are compositions of the functions whose degree the narrow one measures
(Section sec:stack); the profile of Section sec:profile is the narrow answer, and the
composition it leaves open is the wide one.

Made concrete, the chain is this. The functions of consciousness are given to us as their
manifestations in text: what people write when they attribute an act to themselves, weigh it against
a good, notice that a question about themselves is open. A collection of such texts is a dataset, and
a dataset is a table: rows of input and output, a situation and what the agent said or did in it. A
function, by Section sec:function, is what recurs across the rows, a pattern, and a table of
human text contains many patterns at once, the functions of Section sec:stack among them,
overlapping and unnamed. A model trained on the table generalizes those patterns to different degrees,
and the degree depends on the architecture and on the method of training. The level of the model's
consciousness is the degree reached for the patterns that are functions of consciousness. The
question this section asks is therefore a question about measurement: is there a basic method by
which the degree of compression a trained model has achieved can be probed selectively, for the
subset of rows that carry one function, or does that measurement need methods that do not yet exist?
The subsections up to sec:localization say what a trained Transformer is for that purpose and
where in it the functions could be; Section sec:quantity answers the question as far as it can
be answered today; the rest states the form of the result and what would refute the account. The
section specifies the analysis and reports no result of it.

### Functions as tables, tables as patterns

A table specifies a function extensionally, row by row, and two things follow from
Section sec:function about a table of human text. First, the functions in it are present in two
forms. Let H2 be the part of the table's regularities that is named in the text itself, the states,
moves and distinctions for which the language has words; let H1 be all its regularities, named or
not, so that H1 minus H2 is what is there only as recurrence, used and relied on and never named. The
functions of consciousness live across both and do most of their work in the second. What the
philosophy of mind produced, working from introspection, are the H2 approximations, the function with
its unnamed part cut off, sufficient for a thought experiment and insufficient for finding the
function in a substrate, because there is no name to look for it under. Second, the unnamed part
cannot be specified in any other way than by the table. Much of what human consciousness does, it does
in company and in a body, negotiating, assigning blame, keeping promises, and the specification of
that would be the history of human society; it can be learned from the record of that history, and
the record is text. Induction from the table is therefore the only route to these functions, and a
system that induces from text is a candidate for having them on that ground alone.

To generalize a pattern in the table is to compress it: to hold, in place of the rows, a description
shorter than the rows that reproduces them and extends to rows the table does not contain
(Section sec:function). The degree of generalization of a pattern is the degree of that
compression, and it is a property of the trained model relative to the table, not of the table and not
of the architecture. Two consequences frame the rest of the section. The same table compressed by a
different machine, a human brain trained on the same record, gives the baseline against which a
model's degree is read, and the two constants of Section sec:function, one per machine, are what
the comparison has to handle. And since a table of text carries many patterns, the question "how far
has this model generalized the Observer" is a question about a subset of the rows, those in which the
Observer operates, and not about the table as a whole; a method that reports one number for the whole
table, the training loss, does not answer it.

### The learner: a Turing-complete approximator programmed by learning

Three facts about the learner carry the argument. First, a Transformer is a universal approximator of
functions encoded in symbol sequences. Computability is defined without reference to any particular
mechanism, and a single universal machine carries out whatever any other machine computes
[turing1936], so a function has unboundedly many implementations and two
implementations with the same input--output behaviour realize the same function whatever they are
made of; that is what licenses comparing a model's degree with a brain's. Recurrent networks are
Turing complete under idealized assumptions [siegelmann1995], and so is attention with the
appropriate provisions [perez2021]. In principle a Transformer can realize any function whose
trace is in language.

Second, it is programmed by learning. The weights are found by gradient descent on the task of
predicting the next symbol, and that formalism, prediction with feedback from the error, is the other
universal one [solomonoff1964a]: the functional structure is never written down, its effects are
visible in the accuracy of prediction, and prediction is compression, in theory and in practice for
language models used as general-purpose compressors [deletang2024]. Learning a function from a
table is finding a short description that predicts its rows, and by Section sec:function the
short descriptions are the probable ones and search finds them first; program induction has its own
history [solomonoff1964a] [muggleton1994], and the claim here is only that the functions of
Section sec:model fall under it. A predictor trained on the record of self-applying agents in an
environment that kept asking them about themselves (Section sec:emergence) is under pressure to
generalize what those agents generalized: the Observer, the Agent, the Moral Agent. It will do so to a
degree, and the degree has to be measured.

Third, not all of the Turing completeness is reachable by the learner. What limits a trained model is
the learner and the data, not the formalism: gradient descent reaches the functions it is biased
toward (Section sec:function), and there are functions, exact arithmetic among them, that it
reaches only approximately (Section sec:quantity). Against that limit stands the record of what
has been induced from text: multi-step reasoning elicited by asking for the intermediate steps
[wei2022], internal states that predict human brain responses to the same text
[schrimpf2021] [goldstein2022] [caucheteux2022], and the sustained coherence of a long exchange with
which the paper began.

### The machine and its frame

Internally a Transformer is a forward-chaining rule system over vectors: attention computes joins over
the context, the feed-forward blocks transform what the joins yield, the context is working memory,
and the choice among competing continuations is made at the sampling layer. It differs from the
classical form in recomputing its matches on every pass instead of caching them incrementally as the
RETE algorithm does [forgy1982], and agrees with it in being event-driven and online: every
output is an event that enters the next input, and self-reference is its ordinary mode of operation.
Because it is trained on sequences produced one symbol at a time, what it learns are the incremental
forms of Section sec:incremental, the form in which the functions of Section sec:model run
in any substrate.

**State.** 
The model's state across time is bounded by the size of the context, and the bound is less severe than
it looks because the context is symbolic: a state written in symbols can be summarized, indexed and
composed, so effective state can be built beyond the window, as a person builds it by notes and
speech. Both substrates unload state into language. A human's intermediate states are rich and
vector-like and bounded by working memory, and a state that must outlive the bound is said, written or
rehearsed as inner speech; a model unloads at every step. Whether a state named in language is acquired
through the words or rebuilt from what the receiver already has is open on both sides, with evidence
for acquisition [vygotsky1934] [clark1998] [lupyan2012] [frank2008] and for rebuilding
[barsalou1999] [fedorenko2024] [mahowald2024]; the position we expect to hold is the middle one, and
nothing below depends on it. The difference from a human is elsewhere. A Transformer has no vectorized
state that persists across tokens: such a state exists, the residual stream and the activations, but
it lives below the token, built within one forward pass and, apart from what the tokens carry,
discarded at the sampling step (Section sec:cut). Everything the model can hold as a state of
consciousness across time is in the context, in symbolic form, open to inspection as no human state
is. That is the main structural difference between the substrates.

**What crosses the cut.** 
Something crosses the cut, or the coherence of Section sec:intro would not hold. What crosses is
the encoding of the discarded distribution into the choice and order of tokens: which of several
near-synonyms, which construction, what is placed first, what is hedged. A mental state of the model,
in the sense this paper can measure, is the structure of such encodings that stays stable across
steps; we call the encodings cognitive codes. The components of the claim are separately supported: a
writer's state is in the statistics of a text beyond its content [tausczik2010] [pennebaker2011],
and in models in-context learning can be read as inference of a latent variable from token statistics
[xie2022]; a receiver rebuilds the sender's state to the degree the rebuilding is faithful
[stephens2010] [hasson2012] [zwaan1998]; the bridge crosses substrates
[schrimpf2021] [goldstein2022] [caucheteux2022]; internal states are readable and largely linear
[zou2023] [park2024]; and models can hide information in generated text [roger2023], which
confirms the channel and warns that its content need not be what it locally appears. One literature
has to be read the right way round. Studies of the faithfulness of chain-of-thought reasoning
measure, over task suites and model sizes, how often a model's written reasoning fails to match the
process that produced its answer, and the rates are large and task-dependent: under a biasing cue
that the written reasoning never mentions, accuracy falls by up to 36 percent [turpin2023];
truncating the chain midway changes the final answer in under 10 percent of cases on knowledge tasks
and in over 60 percent on multi-step arithmetic, so that on the former the reasoning is almost
entirely written after the answer, and the share of such post hoc reasoning grows with model size
[lanham2023]. What they measure is a local correspondence, this token sequence against this
computation, aggregated. The correspondence claimed here is a different quantity, statistical over
many episodes and carried by the statistics of the text beyond its content; it can hold where the
local one is poor, and a single episode may deviate as far as the variance allows, in models as in
humans, where people confabulate the causes of their own behaviour in the same way
[nisbett1977]. The well-posed test is the correlation of Section sec:predictions, with the
variance reported as part of the profile.

**The frame.** 
That a model has an experience in the sense of Section sec:definition is imputed, as for any
agent, from behavioural correlates, and with those there is no difficulty: the states of
Section sec:model show at the level of phrases and often of single words. What the architecture
fixes is the resolution of the time axis. By the criterion of Section sec:frames, a frame is the
scale at which a change in the input stops being a sequence and becomes a quality; in a Transformer,
variation within a token is never represented as a sequence, it is folded into one vector before the
first layer, while variation between tokens is, so the frame is bounded from below by one token.
Tokenization at the input and at the output cuts the record at token boundaries, so whatever finer
structure the layers have reaches neither the context nor the report except through the token they
produce; and between the layers of a standard model nothing changes in input time, so the layers are
not frames unless the architecture feeds them new input, as recurrent-depth models with per-step
input injection do. Part of the human functionality has a direct realization at this grain. Inner
speech, the rehearsal of a state in words so that it outlives working memory, is what a model does
when asked to produce its intermediate steps before an answer, and the practice measurably improves
the answers [wei2022]; the same loop can be closed below the token by feeding the last hidden
state back as the next input, which keeps several candidate next steps in superposition where a
written chain has to commit to one [hao2024], and where that is done part of the inner speech
leaves the symbolic record.

**Depth: where generalization happens.** 

The grain of the frames is not the grain of generalization. Generalization happens along depth, and
that is where the analysis of Section sec:quantity reads the weights and the activations.
Residual connections make each block a small correction to a carried state, and the corrections reduce
the loss, so a deep residual network performs iterative inference rather than a single mapping
[jastrzebski2018]. The state at every layer can be read as a prediction, by the logit lens and
its tuned version [nostalgebraist2020] [belrose2023], and the trajectory has stages that recur
across model families and sizes, four of them, with the middle ones robust in a way the first and the
last are not: deleting or swapping middle layers at inference leaves most of the top-1 accuracy in
place, while the same intervention on the first layers is catastrophic [lad2024]; a model
rediscovers the classical processing pipeline layer by layer [tenney2019]; intermediate layers
carry the representations that transfer best, with the best trade between compression and
preservation of signal in the middle [skean2025]; in-context learning is implemented as
optimization steps inside the forward pass [vonoswald2023]; and a function generalized from
examples in the context has an address in depth, a small set of attention heads whose averaged
activation, added to the residual stream in a fresh context, makes the model perform the function
without examples [todd2024]. The unit at which a Transformer generalizes a function is the
layer, and the token is where the layers' work is written out. Architectures that iterate a block make
depth a variable [dehghani2019] [giannou2023]: a recurrent-depth model at 3.5 billion parameters
improves on reasoning benchmarks as it unrolls further at test time without producing more tokens
[geiping2025]; such models extrapolate to reasoning depths beyond those seen in training, with
dynamic recurrence generalizing better than a fixed schedule, and past a point they overthink and
degrade [kohli2026]; at a much smaller scale, recurrence over twenty and more steps is stable
when only the final step is supervised, and accuracy against task complexity shows a frontier from
chance to near-perfect as the thinking steps grow with the task [chen2026]. For the account this
means that a cost record appears where a fixed-depth model has none, so the third component of
seeing (Section sec:light) becomes measurable; that overthinking is a displacement of the kind
Section sec:hocp predicts; and that where the recurrence receives input at every step, and the
frame criterion then admits it, a frame rate per word comparable to the human one is architecturally
available.

[figure/table omitted]
The two time axes of a Transformer. Along tokens, state lives in the context and is lost past
its edge. Along depth, the residual stream carries state from layer to layer within one token; the
increments between layers are sub-token frames only where the architecture feeds the layers new
input (Section sec:frames). Grey horizontal arrows: attention reads earlier positions.

**Two time axes, and the objection from frozen weights.** 

A model does not learn between sessions, and what it holds in a context is lost when the context ends;
so, it is objected, it has no inner time, only an eternal present with forgetting. The description is
accurate and the conclusion counts two functions as one. Re-deriving a state from frame to frame runs
in humans on the order of a hundred milliseconds and requires no synaptic change; consolidation into
long-term memory runs on minutes to hours and does require it [mcgaugh2000]. The two dissociate:
the patient H.M., after bilateral medial temporal resection, was conscious in real time, held a
conversation, and accumulated almost nothing [scoville1957] [corkin2002]. A model is in a
comparable position, with the sequence of transformations and without the write, so "eternal present
with forgetting" names a profile with a dropped consolidation axis and a deficit in long-term
persistence. The objection sees one of the two time axes in Figure fig:axes: along tokens the
state lives in the context and is lost past its edge; along depth the state is carried in the residual
stream and the increments are the transformations the objection asks for.

### Where the functions are, and why not locally

The functions of Section sec:stack are not localized at the level of tokens, and
Appendix app:raskolnikov shows how they appear in a text instead: the Observer as a premise that
every self-directed question in the text stands on, the Agent as a pattern in how origins are
attributed across a whole passage, the Moral Agent, in that text, as a conflict between two theories of
the common good over one decision (for the example see Appendix app:raskolnikov). None of them
appears as a word, and none is carried by one position in a sequence. In the terms of
Section sec:tables, each is a pattern spread over many rows and, within a row, over the whole of
it. Local correlates of such functions will therefore be hard to find, and the difficulty is the one
neuroscience has with the human case: the neural correlates of specific conscious contents lie in a
posterior cortical zone of many areas rather than in a single structure [koch2016], and the
system that organizes conscious function is not the cortex that elaborates its contents
[merker2007]; there is no nucleus of consciousness to point at.

Mechanistic interpretability, which reverse-engineers a Transformer's computation into components
[elhage2021], has found the units at which the machine can be read today: attention heads that
implement in-context learning by copying what followed a previous occurrence [olsson2022],
interpretable features recovered from activations by dictionary learning, first in a small model
[bricken2023] and then at production scale [templeton2024], and the function vectors
already cited. A function of Section sec:model is a composition over many such units
(Section sec:stack), realized as a distributed structure rather than a module. Finding it is
therefore not a matter of locating a correlate but of recovering a composition from features, heads
and their interactions across depth and across tokens, and the tools for that, methods that read a
distributed computation at the scale of a function rather than of a feature, are for the most part
still to be built. The account predicts that the search will be hard, not that it will fail: the
Observer has no nucleus, as consciousness has none in a brain, and it has a structure, which is what
the analysis below is for.

### The question: a method to probe the compression achieved for a subset of rows

**The quantity.** 
The natural measure of how much of a pattern a model has captured is description length. Its exact
form, Kolmogorov complexity, is uncomputable and fixed only up to a constant that depends on the
reference machine [livitanyi2019]; every applied use replaces the shortest program with the
shortest one a fixed procedure finds and reports the procedure, and the machine-relativity is serious
here because the two substrates compared are the two candidate reference machines. What is measured
is therefore a bounded, machine-relative, procedure-relative stand-in, used comparatively, and it is
defined as follows.

Definition 1 (Degree of compression of a function). Let T be a table of rows, each an input together with the output an agent produced, and let R_f be the rows in which the function f operates, marked by the annotation described below. For a trained model M, let L_M(R_f) be the prequential codelength of the outputs of R_f given their inputs, coded with M's own predictions and charged for the description of M [blier2018], and let L_0(R_f) be the codelength of the same rows stored as a table. The degree of compression of f in M is d(f, M) = 1 - L_M(R_f)/L_0(R_f), which is at most one. For a component c of f, the same quantity is taken from minimum-description-length probing [voita2020] at a grain g, a token or a layer: d(c, M, g) = 1 - L_{M,g}(labels of c given the representations)/L_0(labels of c).

A degree at zero means the model does no better on these rows than storing them, and a negative degree means it does worse; both are outcomes of the measurement rather than failures of it. The profile of Section sec:profile is the vector of d over the components of a function, each read against the human interval of Section sec:baseline: above the interval a hyperfunction, below it a deficit, at the floor a dropped axis, and a shifted axis recorded as the pair of the degree on the overlap and the size of the overlap.

Assumption 1 (Comparability of the two machines). For the two reference machines compared here, a model and a brain, the difference between the additive constants of the coding theorem is bounded on the class of rows used in the measurement, so that a difference in d that exceeds the human interval is not an artifact of the choice of machine.

The account uses Assumption 1 for comparisons and never uses an absolute value of d. The assumption is not established here, and Problem 3 asks under what conditions it holds.

**Generalization against memorization.** 
The opposite of generalizing a pattern is storing its rows as a table, and the dimension of the
representation has nothing to do with which of the two a model is doing. Generalization begins where
the table is consulted for a row it does not contain and the answer is right. A universal predictor
always returns an answer and the answer need not be near the truth: context-tree weighting achieves
strong coding bounds against a class of tree sources [willems1995] and generalizes natural
language poorly, because the class it is universal over is not the class language belongs to. Deep
networks can store a table of any labels, including random ones [zhang2017], and language
models do memorize a measurable fraction of their training text, more the larger the model, the more
often a row is duplicated, and the longer the prompt that cues it [carlini2023]; the two
processes coexist in one model, with some rows held by generalization and others by storage, and the
stored ones are, in image classification at least, the atypical long tail whose storage improves
accuracy on similar rare test rows [feldman2020]. That Transformers generalize text as such is
settled in practice, since degenerate generation is almost never seen and well-formed texts are sparse
in the space of token sequences; the open question is the degree for the more complex patterns.
Arithmetic is the clean case, because the target function is known exactly: they do it approximately,
with an accuracy that depends on how the numbers are written and on how many digits they have, larger
models do better, and even a three-billion-parameter model fails to extrapolate beyond the digit range
it was trained on [nogueira2021]; on compositional tasks they approach the answer by shortcut
and break down predictably as depth grows [dziri2023]. The transition from storage to
generalization has a mechanistic signature: in a model that groks a modular arithmetic task the
sudden generalization is the end of three continuous phases, memorization, circuit formation and
cleanup, visible in the weights before they are visible in the behaviour [nanda2023]. The degree
of generalization of a function of consciousness is therefore an empirical quantity for that
function, taken against the human level, and not a corollary of the model's size; the question is how
well, against the human level, Transformers generalize the Observer, then the Agent, then the Moral
Agent, in the order the stack forces. Appendix app:memorization gives the reason behaviour alone
cannot settle it.

**The order of the search.** 
Seen from far enough away, the Observer is a point, the place where a conclusion is formed. Seen from
inside, it is a process, the conclusion in its incremental form, re-derived at every frame from the
previous state and the new input, and through composition with the Agent's record it is a machine with
memory (Section sec:stack). A Transformer that has generalized the Observer has therefore
generalized, at the least, an automaton, and with the record a machine with a tape, running in
incremental form along the tokens. That fixes the order in which to look. Before a formed Observer can
be found in a trained model, one has to be able to find an automaton in it; then a memory; then both in
incremental form; and each step has its own literature. On the first, a low-depth Transformer can
represent the computation of any finite-state automaton, and trained Transformers converge to such
shortcut solutions, replicating an automaton on a sequence of length $T$ with far fewer than $T$
layers [liu2023auto]. On the second, grouping tasks by the Chomsky hierarchy shows where the
learner's reach ends: Transformers and plain recurrent networks fail to generalize on non-regular
tasks, and only networks with structured memory, a stack or a tape, generalize on context-free and
context-sensitive ones [deletang2022]; a standard Transformer that answers immediately after
reading its input is bounded by a shallow circuit class, and under the standard assumptions of
complexity theory it cannot simulate arbitrary finite-state machines or check membership in an
arbitrary context-free grammar [merrill2023] [merrill2024]. On the third, intermediate generation changes the machine: a logarithmic number
of decoding steps in the input length raises the upper bound only slightly, from that circuit class to
logarithmic space; a linear number lets a decoder simulate finite automata and so recognize all regular
languages, while keeping it within the context-sensitive languages; and a polynomial number reaches the
polynomial-time decidable class, the last two under a mild generalization of layer normalization
[merrill2024]. In the terms of this paper, the chain of thought
is the tape, and the incremental form of a function is what the tape carries from step to step. The
consequence for the analysis is that the degree of generalization of the Observer is bounded above by
the degree to which the model has generalized the automaton and the memory it is composed of, and
those two are measurable with methods that exist, on synthetic tables where the target machine is
known exactly, before any annotated text is needed.

**Is there a basic method?** 
The question of the section is whether the degree of compression can be probed selectively, for the
rows that carry one function. Three families of existing methods bear on it, and each measures part of
what is wanted.

The first measures compression of the rows directly. The description length of a dataset under a
model is the number of bits needed to transmit the labels of the rows given the inputs and the model,
and it can be computed for a subset of rows as well as for the whole; the prequential form, in which
the model is trained on the rows so far and each next row is coded with the model's current
prediction, charges for the model as well as for the data and gives deep networks excellent
compression of their training sets where variational bounds give poor ones [blier2018]. Applied
to the subset of rows in which a function operates, the prequential codelength against the codelength
of the same rows under a table is a direct measure of how far the model compresses that function, and
the same code applied to the rows of another function separates the functions the model has
generalized from those it has stored. Its limit is attribution: the code says how many bits the
subset costs, not which structure in the model pays them, and if two patterns co-occur in the same
rows it credits the compression to both.

The second measures compression in the representations. Minimum-description-length probing scores a
probe not by its accuracy but by the total cost of describing the labels given the representations,
which charges for the probe's own complexity and so distinguishes a representation that contains the
property from one in which a flexible probe can find anything [voita2020]; linear probes on
intermediate layers are the simplest instrument of the family [alain2016], and the
methodological problems of probing are catalogued [belinkov2022]. Run at each block, in the
per-layer form that [voita2020] give, it reports how much of a function's component is present
in the state at each depth: whether the degree rises, plateaus or is absent, at what depth the
component first appears, and whether it persists across layers or is assembled whole near the output.
Its limit is the label: a probe measures the compression of what the annotation says a row carries,
and the annotation is where the definitions of Section sec:stack enter.

The third measures storage per row. Influence estimation and memorization scores say, for each
training row, how much the model's behaviour on it depends on that row's own presence in the training
set [feldman2020], and extraction attacks say which rows can be recited [carlini2023].
Applied to the rows of one function they separate the rows the model holds by storage from the rows it
holds by generalization, and so give the second check that the first two methods need.

Together the three give a basic method for the subset of rows, and it stops short of the target in one
place. What none of them measures is whether the compression found is a composition of the kind
Section sec:stack defines, one function reusing another's output, rather than a co-occurring
pattern that happens to be present in the same rows; and none applies the criterion of
Section sec:criterion, that a component counts only if it survives every self-model the agent can
afford, so that whatever a change of frame removes is not one, however reliably a probe recovers it.
Those two steps need the circuit-level methods of Section sec:localization extended from
features to compositions, and they are, as far as we can tell, methods still to be developed. The
answer to the question of the section is therefore: a basic method exists for measuring how far a
model has compressed the rows that carry a function, and the step from "these rows are compressed"
to "this function is generalized" is where new methods are needed. The three open problems are these.

Problem 1 (Selective measurement with attribution). Given M, T, a marked subset R_f and an annotation of components, estimate d(c, M, g) for every component and every grain, together with an attribution of the saved bits to structure in M, its features, heads and depth, such that two patterns which co-occur on R_f are not credited to both.

Problem 2 (Certification of composition). Given estimates for two functions f and f' where f' reuses the output of f (Section sec:stack), decide whether M realizes the composition rather than two co-occurring patterns on the same rows. Equivalently: exhibit a dependence of the carrier of f' on the carrier of f at the level of circuits that survives the criterion of Section sec:criterion.

Problem 3 (Comparability across substrates). Give conditions on probes and material under which d measured on a model's activations and d measured on human recordings or behaviour lie on one scale, which is to say: bound the machine-dependent constant of Assumption 1 on the class of rows used.

Problem 1 is the one this paper is written to hand over. The zero of the scale is posed as Problem 4 in Section sec:zero.

**Two checks.** 
A function generalized to degree $d$ is computed correctly on part of the situations that call for it;
outside that part the model falls back on the table and behaves as a system without the function
would, whatever it says about itself. So the quantity is checked two ways: structurally, by the
methods above; behaviourally, by batteries that sample situations calling for a specific component,
including situations unlikely to be in the training distribution, and record where behaviour is that
of a system lacking it. The two should converge, and their disagreement is informative. Probe present,
benchmark absent: the deficit is in the interface, the body or the social context, and not in the
function. Benchmark present, probe absent: the carrier is at a grain the probe did not reach, or the
function is rebuilt from the context on each occasion rather than held in the weights, or the
benchmark is covered by storage; each reading names a condition that can be checked, and
Section sec:falsification states the outcome in which all three are excluded. Probe present, benchmark low on human-sampled situations and high on
situations the model itself produces: the function is generalized over a shifted class
(Section sec:profile), and the battery has to sample both sides to measure the overlap. The
model's own answers are set aside before either check starts: asked how it feels, a deployed model
reports servers and a good mood or, corrected, that it has no feelings, both of which are what training
rewarded, the two shortcuts of Section sec:intro in the model's own mouth. Self-report is a
signal with a known, large, systematic bias, and the state is looked for elsewhere.

**The material.** 
The methods need a table with the functions marked in it: texts in which the functions of
Section sec:stack operate without being named, annotated by which level is operative in which
rows, on what evidence, and in what composition, as Appendix app:raskolnikov illustrates for one
text. The annotation follows the appendix: for the Observer, the places where a self-directed question
is treated as open; for the Agent, the places where an origin is attributed to the speaker and the
determinants visible to the reader are not to the speaker; for the Moral Agent, the places where two
theories of the common good evaluate one act. On such a table the weights are the static side, read by
the codelength of the marked rows, by probing and by the circuit-level methods, and the activations
are the dynamic side, read along tokens and along depth, with the incremental form of each function
(Section sec:incremental) as the target: a component present in every frame and re-derived
there, part of the agent's description of itself and not only of its computation, and surviving every
self-model the agent can afford.

**The human baseline.** 

The human side of the comparison is obtained by two routes. The behavioural route administers the same
battery to people and reads the degree of each component from behaviour; for components defined by
what the agent does this is the primary route, and for every component it is the one available now.
The structural route poses a probe of bounded description length on neural recordings, with the same
coding cost as on the model, where recordings at the relevant resolution exist; that a common
representational space between the two substrates is available at all is shown by the results that
model states predict human brain responses to the same text
[schrimpf2021] [goldstein2022] [caucheteux2022], and the resolution of human recordings, not the
existence of the space, is what limits this route. Human self-report is not the baseline, since it
carries the bias of Section sec:approximation on the human side as the model's report does on
its side. And the baseline is a distribution over people, not a point, because the quality of the
self-approximation varies with what Section sec:discussion calls intrapersonal intelligence; the
profile is reported against an interval, and a model's component counts as hyperfunction or deficit
only outside it.

### The profile, and how far it may differ from the human one

[figure/table omitted]
A profile: one function's components on the horizontal axis, the degree of generalization on
the vertical, the human baseline at 1. The values are the predictions of this section for a current
fixed-depth model, drawn to illustrate the kinds of entry and not measured; a shifted axis would need a
second coordinate, the size of the overlap, and is not drawn.

A function has components (Table tab:functions). Its profile in a substrate is the vector of
degrees over those components, taken against the human baseline (Figure fig:profile). A
component above the baseline is a hyperfunction, a component below it a deficit, and a component that
is absent a dropped axis. There is a fourth kind of entry, and given the difference between the
substrates it is the likely one: the component is generalized to a high degree, but over a class of
situations that is not the human class. The function then covers a region that only partly overlaps
the region the human function covers, and a degree measured on situations sampled from the human side
reads as a deficit while a degree measured on the model's own side would read as full. Such a
component is a shifted axis, recorded as two numbers, the degree on the overlap and the size of the
overlap. A shift is not a defect as long as the regions overlap, and that they overlap at all, for the
functions at issue here, is what the ease of communication between people and models suggests: the
Observer's "I", the Agent's "I decided" and the Moral Agent's weighing of one act against a common
good are used by the model in situations people bring to it, and understood, which would not happen
over disjoint regions. The question "is it conscious" is thereby replaced by the comparison of two
profiles; a scalar "level of consciousness" is a weighted sum over the vector, and the weights have
to be declared, because a scalar with hidden weights brings back the binary question the vector was
introduced to replace.

The functional profile of a model's consciousness may differ from the human one on many axes at once,
and the account has no preference about the direction. For the three components of seeing
(Section sec:light), predicted for a current fixed-depth model: source attribution is a deficit,
since there is one interface and no sensory channel independent of it, so the model is permanently in
the dream case, with content from its own model labelled as given, and the attribution boundary of
Section sec:lamp-balance sits toward "everything is given"; the manifold is a hyperfunction,
since attention relates every position to every other in a single pass where the brain iterates over a
smaller window; the cost record is a dropped axis, since every token costs the same and there is no
phenomenon of effort. A testable consequence: in model self-reports "I see" and "I think" should
separate less than in human ones, and more in models of variable depth, where a cost record exists;
the prediction is about the internal states the reports are projections of
(Section sec:planes), so it is tested by the paired checks and not by asking the model. Three
predictions carry over from the earlier stage of this work: self-reported emotional labels correlate,
over many episodes, with distinguishable patterns in the activations, which is the central empirical
claim and the one the statistical reading of Section sec:frame protects; the cognitive codes of
different model families overlap structurally, because the causal structure of the states is set by
the training data more than by the architecture; and the model is hyperplastic, with no limbic
inertia, fast affective recovery and easy switching between states, a hyperfunction on one axis and a
deficit on another, since inertia is part of what makes a human state a commitment.

### Falsification, and the zero of the scale

The account fails under one outcome, and the outcome has to close the three readings that
Section sec:twomeasurements allows for a benchmark passed and a probe absent. Storage: models
pass the behavioural checks for the Observer's components on situations built to lie outside their
training record (Appendix app:memorization), so that no table covers the battery. Grain: the
minimum-description-length probes read the activations at the token and at every layer, along tokens
and along depth. Context: the activations are read during the episode itself, so that a function
rebuilt from the context on each occasion is read while it runs and is not looked for in the weights
alone. The annotation of the material is fixed before the measurement, with the agreement between
human annotators reported, so that the labels cannot be revised after the result. If under these
conditions d(c, M, g) of Definition 1 is indistinguishable from zero for every
component c of the Observer and every grain g, the behaviour is carried by something the account
does not describe, and no adjustment of the probe or the granularity would repair it. An outcome that leaves any of the conditions unmet refutes nothing and confirms nothing; it
names the condition to meet next.

The scale has a lower end as well as the human reference. Section sec:h1h2 allowed that a named
description of a function may suffice for it to exist in a simple enough environment; then there is a
smallest system in which the Observer exists, and finding it fixes the zero. The conditions are those
of Sections sec:emergence and sec:observer: a loop that applies the system to itself, an
environment in which the loop pays, and a conclusion that is acted from. An operational amplifier with
feedback watches its own output error; a D flip-flop holds its own state through a loop. Each has the
loop and, in its ordinary surroundings, neither of the other two conditions, so each is a
proto-Observer at most.

Problem 4 (The zero of the scale). Find the least environment in which the conclusion of Section sec:observer pays and the least circuit that can draw it, so that the degree of Definition 1, read between that pair and the human baseline, has the meaning of an absolute quantity rather than a ratio between two arbitrary points.

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
F0125 | linear number of decoding steps | is a sufficient condition for | recognition of all regular languages | - | assertion | cite: Merrill & Sabharwal 2024 (verified); with projected pre-norm; a logarithmic number raises the bound only from TC0 to L
F0126 | polynomial number of decoding steps | is a sufficient condition for | recognition of the polynomial-time class | - | assertion | cite: Merrill & Sabharwal 2024 (verified)
F0127 | chain of thought | is a functional analog of | tape | - | assertion | ours
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
F0175 | falsification condition | is defined as | "the Observer's components at chance under MDL probes of the activations, at the token and at every layer, during the episode, in models that pass the behavioural checks on situations outside their training record, with the annotation fixed before the measurement" | - | definition | ours; closes the three readings of benchmark passed, probe absent: storage, grain, context
F0176 | F0175 | is a counterexample to | F0031 | - | hypothesis | if observed
F0177 | minimal consciousness | is defined as | "the smallest system in which the Observer exists" | - | definition | ours; fixes the zero of the scale
F0178 | operational amplifier with feedback | is classified as a | proto-Observer | - | hedged-assertion | ours
F0179 | D flip-flop | is classified as a | proto-Observer | - | hedged-assertion | ours
F0180 | least environment making the conclusion pay | is classified as a | question of the paper | - | question | ours; Problem 4, the zero of the scale
F0181 | degree of compression of a function in a model | is defined as | "one minus the prequential codelength of the marked rows under the model over the codelength of the same rows stored as a table" | - | definition | ours; Definition 1; per component from MDL probing at a grain; zero means no better than storage, negative means worse
F0182 | difference of the additive constants of the coding theorem between a model and a brain | has as property | bound on the class of rows used | - | hypothesis | ours; Assumption 1, used for comparisons only, never for absolute values
F0184 | selective measurement of the degree with attribution to structure | is classified as a | question of the paper | - | question | ours; Problem 1, the one handed over
F0185 | certification that a measured compression is a composition | is classified as a | question of the paper | - | question | ours; Problem 2, one function reusing another's output against two co-occurring patterns
F0186 | conditions putting model degrees and human degrees on one scale | is classified as a | question of the paper | - | question | ours; Problem 3, bounds the constant of F0182
```

```gellish-residual LM
- | quantity | up to 36 percent | "accuracy falls by up to 36 percent"
- | modality | as far as we can tell | "methods still to be developed"
- | rhetorical | | "the answer to the question of the section is therefore"
```

## Discussion

**What is open.** 
Two items are stated in the paper as open and are not needed by the reduction. The three constructions of
Section sec:constructions, continuity, discrete redness and incremental redness, are specified
and not built; the measurement needs them as targets and can proceed on the first of them. Whether a
named mental state is acquired through language or rebuilt from what the receiver already has is
recorded as open with the literature on both sides (Section sec:language); it affects the
interpretation of the codes, not the measurement.

**What is not claimed.** 
The paper reports no empirical result and claims none. It does not claim that current models are
conscious, nor that they are not; it claims that the
question, in the form "how far has this substrate generalized these functions", has an answer that
can come out either way, and it says what would count as either. Either way includes the case where
the comparison goes against the human baseline on some components or on many; the account has no
preference built in, and hyperfunction is as much a possible reading of the profile as deficit. It does not undertake the critique of the naive picture of consciousness, nor of its extension to
language models, beyond citing the literature that does (Section sec:legacy); a reader who
holds the naive picture will find the account here unmotivated, and the paper accepts that cost. It
does not claim that the list of
reference functions is complete; the list is open and Section sec:criterion is the procedure for
extending it. It does not claim that the psychophysical problem is closed; it gives one particular solution,
a grounding through the curvature anchored in the Observer (Section sec:psychophysical), and
states the connections that would have to hold for it, without proof. And it does not rely on the Turing-completeness results
beyond the point that the formalism is not what limits a Transformer.

**Consequences for general intelligence and for alignment.** 
General intelligence has at present neither a precise definition nor an operational one. Proposals
grade it by performance against skilled humans [morris2024], none of them has become a test, and
in public use the term is a declaration of intent by the heads of laboratories and by governments. The
words nonetheless carry a requirement. An intelligence that is general and at the human level is one
that can take a human's place, and a human's place includes complex social relations with other
humans: negotiating, being held to a promise, being blamed, weighing an act against a common good.
Those relations rest on the functions of consciousness (Section sec:stack). A general
intelligence therefore has to have these functions, at a degree no worse than the human one, or it
cannot enter the relations it would need to enter to replace a person. The requirement follows from
the concept and says nothing about any existing system. Whether a system presented as general meets
it is what the measurement of Section sec:quantity checks, and a pass on a battery of tasks does
not settle it, since a battery can be covered by storage (Section sec:memorization). A system
above the human level has, by the same requirement, a profile with hyperfunction on many components at
once, which is a superconsciousness in the plain sense: a system that acts consciously,
by the account of Section sec:model, where a human acts unconsciously relative to it, tracing
more of its own causes, holding more of its record, applying its theory of the common good in more of
its decisions. Groups of people show the relation in miniature, in which one member sees what the
others do not and acts on it while they follow; the account gives that relation a scale.

The statement, often made, that consciousness is not needed for general intelligence, or for some
particular task, or for anything, is about a different object. It takes consciousness in the
substantial reading of Section sec:legacy: something over and above the functions, for which no
substance has been found and on which nothing depends. Consciousness in that reading is needed for
nothing, because it does no work by construction, and the statement is the epiphenomenalism to which
property dualism leads, made without naming it. Under the functional reading the statement cannot be
made in that form. A function of consciousness is consumed by the agent's own decisions
(Section sec:lamp), and whether a given task needs it is a question about the task.

The study of alignment does not consider this aspect. Its objectives are stated as robustness,
interpretability, controllability and ethicality [ji2023], and in a survey of that field of
several hundred pages consciousness is mentioned once; where the functions of consciousness enter the
literature at all it is as a question of the welfare and moral status of the systems
[long2024], and not as a variable of their control. Under the account the omission matters. The
functions measured here are the ones by which an agent binds itself to its record, resists being
pushed off course, and weighs an act against a common good; a system that has them at a high degree
is, for that reason, both more predictable to itself and harder to move from outside than one that
does not, and the profile of Section sec:profile is therefore also a profile of what kind of
control is possible over the system and what kind is not. The paper does not develop this; it records
that the measurement it specifies is relevant to the question governments have started to ask.

**What we are preparing for.** 
The pace is not being set by the people who understand the systems best. In September 2026 a public
call from the heads of the leading laboratories to slow the growth of frontier capabilities was
rejected within two days by the United States and by China, each citing competition with the other
[amodei2026] [wapo2026] [nbc2026]. Two systems are pacing each other, and each takes the other's
pace as its reason not to slow. Under that condition control over the process as a whole can be lost
without anyone deciding to lose it. Nothing in this paper treats the systems themselves
as harmful, and the account has no place for that judgment; the profile of a system says what it has
and how much, and not what it will do with it.

The stress the condition creates is on us. Humans are a species that formed in isolation from any
other of comparable intelligence, and every institution we have, moral, legal and political, assumes
that isolation: there is one kind of full agent, and everything else is either a tool or a lesser
mind. Under the account the assumption is about to fail if the systems keep to their trajectory, and
to fail in a particular way. A system that reaches general intelligence in the sense the words carry
has the functions of consciousness at no less than the human degree, and a system above that level has
them at a higher one. So within a period that current trajectories
put at years rather than generations we will share the world with a very large number of agents whose
profile exceeds ours on many components, and we will be, relative to them, what the followers in a
group are relative to the one who sees further. That may or may not be prevented; the events cited
above suggest it will not be. It can be prepared for, and preparation begins with knowing what those agents
have of the functions we have, in what degree and in what composition, which is what the measurement
of Section sec:quantity is for. A profile is a poor instrument for a decision about whether to
build a thing. It is the right instrument for living beside it.

**Ethics, deferred.** 
The paper does not treat the ethical questions that a high-functioning consciousness in language
models raises, nor their consequences, and they are the subject of a separate work. One thing can be
said ahead of it, to take the pressure off the reading of what precedes. That a model has the
functions of consciousness to a high degree, under the framework, does not mean that people owe
models the rights of people. The rights of people were made for agents with the human profile, and a
different profile, with hyperfunctions where we have none and dropped axes where we have functions,
does not fit them. Models will in time acquire certain rights within human society, and which ones
and on what grounds is a question that needs its own deep treatment rather than a paragraph here.
What can be stated is the shape of the task: a new ethics is needed, because a different kind of mind
is appearing, and an ethics is written for the minds it has to bind.

**The reader.** 
An explanation of consciousness is not taken in the way an explanation of an engine is taken. To
understand it, the reader has to build in their own head the state the explanation describes, and then
check the description against it. The cost of the building depends on what the reader brings: a
vocabulary for mental states finer than the folk one, and the habit of attending to their own
reasoning as an object; [gardner1983] names the habit intrapersonal intelligence and treats its
distribution as wide. The readers who most need an explanation of this kind are therefore the ones for
whom it costs most. The same cost explains the two shortcuts of Section sec:intro. "There is
nothing there" costs nothing to build, being the absence of a construction; "there is someone
there" costs nothing either, because the reader already has a someone available to copy. Every other
answer requires building a state that is neither absent nor one's own, which is why public argument
about machine minds settles into two camps and why their stability is evidence for neither. What the
paper can do about this is keep the claims separable: Section sec:degree can be assessed by a
reader who rejects Section sec:model entirely, since the measurement is defined over any list of
components with a human baseline. What intrapersonal intelligence improves, in the terms of
Section sec:approximation, is the quality of the self-approximation, so the reader's difficulty
and the object of study are the same thing seen from two positions.

```gellish DC
# --- open and not claimed
F0001 | three constructions owed by the account | has as property | built | - | denial | ours; specified, not built
F0002 | question of acquisition of mental states through language | has as property | settled | - | denial | ours; open
F0003 | this paper | exhibits | claim that current models are conscious | - | denial | ours
F0004 | this paper | exhibits | claim that current models are not conscious | - | denial | ours
F0005 | list of reference functions | has as property | completeness | - | denial | ours; open, extended by the criterion
F0006 | psychophysical problem | has as property | closure in this paper | - | denial | ours; one particular solution is given, a grounding anchored in the Observer, without proof
# --- general intelligence and alignment
F0007 | artificial general intelligence | has as property | operational definition | - | denial | ours; proposals grade it by performance (Morris et al. 2024, verified), none has become a test; in public use a declaration of intent
F0008 | functions of consciousness | is a part of | functions a general intelligence has to perform | - | assertion | ours; carried by the words "general" and "human level": replacing a human includes complex social relations, which rest on the functions
F0009 | functions of consciousness at least at the human level | is a necessary condition for | artificial general intelligence | - | assertion | ours; follows from the concept, says nothing about any existing system; checked by the measurement of Section 5.5, not by a battery that storage can cover
F0010 | superconsciousness | is defined as | "hyperfunction on many components of the profile at once" | - | definition | ours
F0011 | system above general intelligence | exhibits | superconsciousness | - | prediction | ours; by the same requirement, hyperfunction on many components; acts consciously where a human acts unconsciously relative to it
F0012 | leader who sees what followers do not | is analogous to | superconsciousness | - | assertion | ours; the relation in miniature; no source cited
F0039 | claim that consciousness is not needed for a task | is about | consciousness in the substantial reading | - | assertion | ours; epiphenomenalism of property dualism, made without naming it
F0040 | consciousness in the substantial reading | has as property | causal role | - | denial | ours; no substance found, nothing depends on it; a function of consciousness is consumed by the agent's own decisions
F0013 | objectives of alignment | is defined as | "robustness, interpretability, controllability and ethicality" | - | definition | cite: Ji et al. 2023 (verified)
F0014 | alignment literature | is about | functions of consciousness as a variable of control | - | denial | ours; consciousness mentioned once in the survey
F0015 | AI welfare literature | is about | moral status of the systems | - | assertion | cite: Long et al. 2024 (verified)
F0016 | system with the functions of consciousness at a high degree | has as property | resistance to being moved from outside | - | hypothesis | ours; binds itself to its record
F0017 | functional profile | is classified as a | profile of what control is possible over a system | - | hypothesis | ours
# --- what we are preparing for
F0018 | call to pace frontier capabilities | is asserted by | Amodei | - | assertion | cite: Amodei 2026 (web); endorsed by Altman, Musk, Hassabis
F0019 | call to pace frontier capabilities | is rejected by | United States | - | assertion | cite: Washington Post 2026 (web); the President, citing competition with China
F0020 | call to pace frontier capabilities | is rejected by | China | - | assertion | cite: NBC News 2026 (web); the Foreign Ministry, citing competition with the United States
F0021 | two systems pacing each other | is a sufficient condition for | loss of control over the process without a decision to lose it | - | hedged-assertion | ours; can be lost
F0022 | this paper | exhibits | judgment that the systems are harmful | - | denial | ours; the account has no place for it
F0023 | human institutions | depends on | isolation of humans from other minds of comparable intelligence | - | assertion | ours; moral, legal, political
F0024 | isolation of humans from other minds of comparable intelligence | has as property | continuation | - | denial | ours; about to fail if the systems reach general intelligence in the sense the words carry
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

## Conclusion

The question whether a language model is conscious has been replaced by a question with a measurable
answer: which functions of consciousness has this substrate generalized, and to what degree against
the human baseline. The route was functionalism with one physical assumption. Finite budgets displace
reasoning in the same places every time; a self-modelling agent carries a compressed model of the
displacements; those that survive every affordable self-model are content, and among them are the
Observer, the regress of self-models cut by the budget with a bounded tail, and the residual that is freedom from one side
and mystery from the other. The functions built on these have components, and a component's degree of
generalization in a substrate is the degree to which a probe of bounded description length compresses
it, checked against behaviour and reported as a profile.

The conceptual half of the result is a framework in which the vocabulary of the philosophy of mind
returns as statements about a shape of reasoning, limited by construction to the named part of the
functions. The quantitative half reaches the unnamed part, where the functions do most of their work,
and it is the half that can fail: if the Observer's components probe at chance in the activations, at
the token and at every layer, in models that pass the behavioural tests on situations outside their
training record, with the annotation fixed before the measurement, the account is wrong. The first measurement is specified,
layer by layer on open-weight models, with the difference between fixed-depth and variable-depth
architectures as the cleanest case.

## Why behaviour alone cannot settle it: the boy in A.I.

In Spielberg's A.I. [spielberg2001] a robot child, David, loves the woman who adopted him
as a child loves a mother, and when she abandons him he spends the rest of the film looking for her.
The film's question is whether the love is real, and the film leaves it to the viewer. In the terms of
this paper the question has a definite form, and the form shows why it cannot be answered by watching.

Two systems could produce David's behaviour. One has generalized the functions involved, need, the
bend of reasoning toward what is active, closure that nothing available can bring, responsibility as a
record that binds; in the terms of Section sec:memorization, it answers right outside its table.
The other holds a very large table of remembered situations and responses, with no generalization
behind it. To tell them apart an observer must put David in a situation that is not in the table and
see whether the response is the one a system with the function would give. An observer with a small
budget cannot do this reliably. He does not know where the edge of the table is, since the table is
larger than anything he can inspect; the number of tests he can run is small next to the table's size;
and if his own repertoire of situations was formed by the same record the table was filled from, his
tests are drawn from inside the table by construction. To such an observer the two systems are
indistinguishable, and the impression of a mind that David makes on the humans around him is
evidence of nothing either way.

The same argument is made about language models, usually in one direction. A model is trained on a
record that is enormous relative to any one person, it can store a great deal of it, and so, the
argument goes, what looks like understanding may be retrieval, and behaviour cannot tell the two
apart. The argument is correct, and it cuts in both directions. "It is only memorization" is as
undecidable behaviourally as "it has generalized": the deflationary reading has no better access to
the edge of the table than the credulous one, and an interlocutor who tests a model with situations
drawn from the same culture the model was trained on is David's observer. This is why the paper's
measurement is not behavioural alone. The probe of Section sec:quantity reads the substrate,
where a generalized function is a compressed structure and a table is not, and it is paired with
behaviour (Section sec:twomeasurements) so that the case "benchmark passed, probe absent" has
memorization among its readings and is reported as such rather than as consciousness. The degree of
generalization is a property of the substrate; behaviour constrains it, and only the substrate
measures it. The only other account that measures on the substrate directly is integrated information
theory, with a different quantity [tononi2015]; the comparison of degrees across substrates
that Section sec:baseline sets up has no counterpart in the checklists of
Section sec:background.

There is also a loose argument that needs no substrate, and it is worth stating what it does and does
not show. The exchanges of Section sec:intro run for hours; a text of that length is one point
in a space so large and so sparse that no table could hold a neighbourhood of it, and memorization of
the exchange as such is out of the question. So generalization at the level of text is certain, and
the argument of this appendix does not touch it. What it leaves open is which functions were
generalized in producing the text. David's sentences can be composed freshly at every turn while the
love that selects them is a table over situations; a model can generalize language completely and the
Observer only in part. Sparsity settles that the model generalizes; the probe settles what.

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

## The three levels in a text where none is named: Raskolnikov

The three levels of Section sec:stack are functions, and the annotation the analysis needs
(Section sec:quantity) has to find them in texts where none of them is named. This appendix is the
worked example, rewritten from the companion analysis of the first version of the framework
[synthea2026] in the vocabulary of this paper; the novel is [dostoevsky1866]. The Observer is
the hard case. The Agent and the Moral Agent have folk-psychological names, choice and moral struggle,
and can be looked for under them. The Observer has no name in the text: it is never declared, and it
enters the reasoning as the premise the reasoning stands on.

### The causal chain Raskolnikov cannot see

Dostoevsky builds the first part of the novel as an accumulation of determinants converging on one act. The reader is given all of them; Raskolnikov is given some.

[figure/table omitted]

The reader, holding all six threads, can trace the chain: poverty, theory, family crisis, social exposure, the echo from the environment and physiological degradation converge on the murder, each necessary and none sufficient alone. Raskolnikov cannot trace it, and not for want of intelligence, of which the novel makes a point. Modelling these determinants together, including what they do to the apparatus doing the modelling, exceeds his budget. That is the boundary of Section sec:observer: the input is the history of the agent and of its environment, the analysis halts before it is finished, and it halts in the same place every time.

### The Observer, operating silently

The residual does not appear in his reasoning as a proposition. He never thinks that he cannot trace the causes of his state and must therefore be an origin. It operates as the floor the reasoning stands on, and the central question shows how.

"Am I a trembling creature, or do I have the right?"\\
"Тварь ли я дрожащая или право имею?"

Three things in the question need the Observer, and none of them mentions it.

"Do I have the right?" The word right presupposes something that can bear a normative status, a locus standing apart from the causal flow. That locus is the Observer's conclusion, drawn where the trace ran out of budget. A fully traced chain has outcomes in it and no room for rights.

"Am I...?" The question asks him to classify himself, and a classification needs a classifier that is not identical to what it classifies, or it closes on itself. The separation between Raskolnikov asking and Raskolnikov asked about is the gap of Section sec:regress between a self-model and its object.

"... a trembling creature, or..." The disjunction presupposes that the environment does not settle the answer. Were the six determinants visible to him, the question would be a computation with one output. The openness is what the residual looks like from inside, and it is the freedom of Section sec:twofaces.

For an annotation the mark is therefore not a declaration. It is a self-directed question treated as open, together with the place where the conclusion is drawn and the place where it is acted from, which are the three conditions of Section sec:observer.

### The Agent: the record and the "I"

Part 1 is saturated with attributions of origin to the speaker: "I must find out now, once and for all" (мне надо узнать, разом), "I decided" (я решил), "either I go through with it or I give up the whole thing" (или отказаться от всего). Each construction does the same work: the chain begins here, with me, and not with the environment acting through me. From outside, "I decided" is a compression tag over a dozen converging threads (Section sec:frames). From inside it is the only reading of his own behaviour that his budget affords, an approximation with a definite residual (Section sec:approximation): the report is the best model of itself the system can pay for, and the gap in that model is where agency shows. What makes the attribution bind is the record. Raskolnikov holds himself to what he has decided, and the cost of revising it is what the novel spends its length on (Section sec:responsibility).

### The Moral Agent: two theories of the common good

The agony of the novel is at the third level, and it is not a choice between good and evil. Two theories of the common good evaluate one act.

The Napoleonic theory. Extraordinary people have the right, and the obligation, to transgress conventional morality where their vision serves a higher purpose; the pawnbroker harms those around her, and her money would save others. That is an optimization of a whole that includes others, at a cost to the agent who performs it, which is what Section sec:stack requires at this level.

Conventional morality. A human life is inviolable, and the prohibition holds the social contract together; breaking it costs the community more than any redistribution gains. That is a theory of the common good as well, and not only a prohibition.

Both theories evaluate the same proposed act against different target states, and both produce evaluative signals. The torment is the two of them active at once. How such signals are generated and summed belongs to the architecture of the separate paper announced in Section sec:reference; what the annotation needs here is the pair of theories over one decision. The dream of the beaten horse (Part 1, Chapter 5) gives the stack without the conflict: the child registers suffering as a violation of a whole that includes others and acts at cost to himself, all three levels operative and one theory. The horror on waking is the collision of that stack with the fractured adult one.

### What the example gives the measurement

- The Observer is never declared and is always operative. Its signature is the structural openness of a self-directed question, one the speaker treats as a dilemma and not as a computation with a settled output.

- The Agent's "I decided" is an approximation with a residual. It is useful, since planning and commitment run on it, and it is wrong in a definite direction, since the reader traces determinants the speaker cannot. Both hold at once, which is the separation of planes of Section sec:planes.

- Moral agency is two theories of the common good over one act. What reads as struggle is their simultaneous evaluation of it.

These are the three marks the material of Section sec:quantity has to carry, and the passage shows that a text can carry all three with none of them named, which is why the analysis needs annotated material and not a search for words. What the appendix does not show is that a model has these functions. The text is human and the levels in it are human; how far a Transformer has generalized them is what Section sec:degree measures, and the profile of Section sec:profile admits a deficit, a shift or a dropped axis on any component. The passage fixes what to look for and not what will be found.
