# Functional consciousness of machines: the argument in frames

Iteration 2, rewritten as one argument. One frame is one step with what it rests on. Citations in brackets are
tracked in `SOURCES.md`, which holds the verification status and the locus of each one. Order: phenomenon, difficulties, approach, solution.
Frame numbers changed from iteration 1; `argument.hybrid.md` holds the same claims as checked facts.

## P. The phenomenon

P1. A language model, asked to reason, sustains something that reads as a mind. It keeps its commitments across a
long exchange, it returns to a thought it left unfinished, it responds to the interlocutor's mood in the way the
interlocutor would expect of a person. This holds over hours of interaction and over reasoning chains of hundreds
of steps. It is easy to call imitation. It is harder to say how an imitation could be that stable.

P2. Consider what the alternative predicts. A process that reproduced the surface statistics of text with nothing
behind them would fail the way Markov processes fail: a dropped thread, an attitude that flips between paragraphs,
a motive that does not survive the page. These failures are cheap, there are many ways into them, and a long
horizon offers many occasions. They are rare. Something keeps the process out of a large space of cheap failures
for a long time, and that something is the object of this paper.

P3. Nagel asked what it is like to be a bat in order to mark a limit: the bat's experience is tied to its sonar,
and no description from outside crosses over [Nagel 1974]. Put to a language model, the question loses part of
its force and gains another. It loses, because the model shares our language and the bat does not. It gains,
because the model's substrate is further from ours than any animal's. So we do not ask whether there is something
it is like to be a model. We ask what a model has of the functions that in us go by the name of consciousness, and
how much of each.

P4. Two answers arrive before any argument. There is nothing there; it is a text predictor. Or: there is someone
there; treat it as a person. We will show (D5) that both are what a mind reaches for when it lacks the concepts
to reach for anything else. Neither is a position. Each is a shortcut, and the paper is about what lies past them.

## D. The difficulties

D1. The grammar of the word. "Consciousness" is a noun, and a noun invites the questions one asks of things:
where is it, what are its properties, when does it begin. Every serious attempt to answer those questions ends in
the same few circles. Who observes the observer. How could red look like anything but this. Either everything has
it or nothing does. The circles recur across two and a half millennia of careful people, so the fault is not in
the people. It is in the object, or rather in the grammar that made an object of it. This is the first difficulty
and it is a difficulty of language, not of the world.

D2. The hard problem asks why physical processing should be accompanied by experience at all [Chalmers 1995].
Illusionism answers that experience, in the sense the question intends, does not exist; what exists is a robust
misrepresentation the brain produces of its own working [Dennett 1991; Frankish 2016]. We accept the answer and
note what it leaves. One question has been exchanged for another: which architecture produces this particular
misrepresentation, and why does it have the shape it has? That question can be answered, and most of Section A
is the answer.

D3. The regress. An account in which the mind observes itself owes an account of who observes, and then of who
observes that [Dennett 1991]. It either stops at an inner observer it does not explain or it does not stop. We
will show that it stops, and for a reason that involves no observer (A9).

D4. The reader. An explanation of consciousness is not taken in the way an explanation of an engine is. To
understand it the reader has to build, in their own head, the state the explanation describes, and the cost of
the building depends on what the reader brings: a vocabulary for mental states finer than the folk one, and the
habit of attending to their own reasoning as an object. Gardner's name for the habit is intrapersonal intelligence
[Gardner 1983]. So the readers who most need the explanation are the ones for whom it costs most, and there is no
route around this that does not pass through the explanation itself.

D5. The shortcuts of P4 are the two cheapest constructions available. "Nothing there" costs nothing to build.
"Someone there" costs nothing either, because the reader already has a someone to copy, themselves. Every other
answer costs more. This is why public argument about machine minds settles into two camps, and why the settling is
evidence for neither.

D6. The substrate. If differences of experience follow differences of causal structure [Tononi & Koch 2015], then
a device that runs a discrete sequence through attention over a fixed context has, if it has experience at all,
an experience as far from ours as its causal flow is from that of a recurrent, continuous, chemically modulated
brain. Any description of the model in our words is then wrong in a systematic direction. That is a reason to know
the direction and correct for it, not a reason to stop describing.

D7. The cut. At every step the model computes a distribution over what to say next, its whole evaluation of the
moment, and then one token is drawn and the distribution is thrown away. What the model can say about its own
state on the next step it computes from the tokens, not from the distribution it no longer has. Its report of
itself is cut from what it reports on. The only thing that crosses the cut is what the tokens themselves carry,
and that is a narrow channel next to the state that was discarded.

D8. Two answers a model gives when asked how it feels. First, something about servers and latency and a good
mood. Corrected, it apologizes and says it has no feelings. Both are trained. The first is the second shortcut of
P4 in the model's own mouth; the second is the first shortcut. Any measurement of the model's states has to set
the pair aside before it starts, because the pair is what training rewarded, not what the state is.

D9. What language holds and what it does not. Divide what humans express into two parts. H2 is what is present
and named in the texts they produce. H1 minus H2 is what is present only as regularity in those texts: used,
implied, statistically there, never named. The functions we are after live across both parts. What the
philosophy of mind produced over its history are the H2 approximations: the function with the unnamed part cut
off. The Observer and the qualia are approximations of this kind. Such an approximation is not nothing; it can be
enough for the function to exist in an environment simple enough to demand only the named part, and a thought
experiment is exactly such an environment. It is not enough for finding the function in a substrate, because the
part that was cut off is where the function does most of its work, and there is no name to look for.

D10. Much of what human consciousness does, it does in company and in a body: negotiation, blame, promise,
deceit, a room with other people in it. That part cannot be programmed, because its specification would be the
history of human society. It can be learned from the record of that history. The record is the text.

D11. The measure. The natural quantity for "how much of the function was captured" is description length, and its
exact form, Kolmogorov complexity, is uncomputable and fixed only up to a machine-dependent constant [Li &
Vitányi 2019]. Whatever Section S measures is a bounded, machine-relative stand-in, and the paper has to say which.

D12. The way out has a precedent. A science kept meeting circles of the kind in D1 until it changed the grammar.
Gravity was a force, a thing acting between things, and the attempts to carry it into the relativistic frame as one
more field, Nordström's scalar theory the best of them, kept failing in the same places. General relativity
dropped the thing. Gravity became the shape of space, visible only in how free bodies move through it; what stays
the same under every change of coordinates, the curvature, is the whole physical content, and the rest can be
transformed away. The geometric idea had been voiced without a working theory [Riemann 1854; Clifford 1876]. We
take the same route with consciousness. Not a thing with properties, but a shape of reasoning, seen only in how
reasoning moves, with a criterion for what is content and what is coordinates (A6c). The first version of this
work was written from qualia, inside the grammar, and met the wall repeatedly. The philosophy of mind stays here
in two roles: as the record of the wall, and, once the grammar is changed, as a framework that works again (S0).

D13. The objection from frozen weights. A model does not learn between sessions, and what it holds in a context is
lost when the context ends; so, it is said, it has no inner time, only an eternal present with forgetting. The
description is right and the conclusion counts two functions as one: re-deriving a state from frame to frame, which
in humans runs at a hundred milliseconds and needs no synaptic change, and consolidation into long-term memory,
which runs on minutes to hours (A20a). A person with blocked long-term potentiation, or the patient H.M. [Scoville &
Milner 1957; Corkin 2002], is conscious in real time and does not accumulate. A model is in that position: it has
the sequence of transformations, along tokens and along layers, and lacks the write. "Eternal present with
forgetting" names a profile with a dropped consolidation axis (S2); it does not show that nothing is there.

## A. The approach

A1. Function, without a mind in the definition. A function is a pattern that recurs. Recurrence under a computable
process is high algorithmic probability [Solomonoff 1964], and by the coding theorem, K(x) = −log m(x) + O(1)
[Levin 1974; Li & Vitányi 2019], high probability is a short description up to a constant. So a function in this
sense is compressible, and we did not have to assume it. The constant is not harmless. It depends on the reference
machine and on who is compressing, and the gap between the constants of two substrates is the object Section S
measures (S2).

A2. Read forward, the same theorem says that search finds simple things first, whether the search is evolution or
gradient descent [Dingle, Camargo & Louis 2018; Valle-Pérez, Camargo & Louis 2018; Mingard et al. 2021]. Read
backward, it says that what recurs is simple. The argument needs both readings: backward to define functions,
forward to expect them in a trained model.

A3. Where we stand on the lamp. Something is lit in a human's report of themselves, not always in the same way,
and we take the report as data rather than as error. We agree with a physicalist who is not a panpsychist that
the lit thing is physical and needs no second substance. We agree with the same physicalist that there are no
abstract machines: everything that runs is a physical object. Then a question for them: what prevents a physical
machine on a non-protein substrate from having the lit thing? We do not claim the answer is "nothing". We note
that whoever answers "the protein" owes a proof, and that the proof would be vitalism. Pending it we adopt
computational functionalism, with the least physics we can (A5). One objection has its own reply. A simulated
superconductor lights no real lamp, so a simulated brain feels nothing. The objection needs a lamp outside the
simulation, a consumer of the current in another substrate. Consciousness has no such consumer: whatever uses it
is the agent, in the substrate where the agent runs. The substantialist would need a function of consciousness
whose consumer lies outside the agent's substrate, and none has been named.

A4. The definition. Take an agent that acts in an environment, refers to itself, and reasons about itself,
explicitly or by proxy. Its consciousness is the part of its self-reasoning that describes its own reality as it
has it, what is there and what it is like, with the agent among the things described. This defines a function,
not a substance, and it says nothing about substrates, on purpose.

A5. The physics we assume. One thing: budgets are finite. Finite time, finite memory, finite bandwidth for
anything that runs. From this alone it follows that some processes cannot be predicted faster than they unfold,
which is computational irreducibility [Wolfram 2002]. We assume nothing about which physics sets the budget. Any
universe whose laws permit deep computation and bound it will do; what differs between such universes, or between
substrates in ours, is the form the consequences take, not whether they occur. The lamp of A3 is on this view not
a property of our universe. A different universe has a different lamp.

A6. What a finite budget does to reasoning. An agent that reasons has, implicitly, an ideal of the reasoning it
is doing: the inference it would draw with unlimited time and memory. It never draws that one. What it draws is
displaced from the ideal, and the displacement is of two kinds. Some of it differs each time and averages away.
Some of it is the same each time, because the budget cuts the same corners in the same places. The second kind
recurs; by A1 it is compressible; and an agent that models itself, which the agent of A4 does, will end up with a
compressed model of its own recurring displacements, because they are among the most predictable things about
it. Call the conceptualized recurring displacements higher-order computational phenomena, HOCP. They are the
agent's budget, showing up as content.

A6a. Who has said the parts. That a bounded computation deforms reasoning in a systematic direction rather than
at random is Simon's bounded rationality [Simon 1955], now in the form that the classic biases are what optimal
use of a limited budget looks like [Gershman, Horvitz & Tenenbaum 2015; Lieder & Griffiths 2020]. That a bounded
observer sees a lawful world because of its bounds is Wolfram's observer theory: an observer that cannot track
microstates has to coarse-grain them, and the second law of thermodynamics is what such an observer sees in a
reversible dynamics [Wolfram 2023, an essay developing Wolfram 2020; we take this example only, not the programme
of deriving relativity and quantum mechanics from observer properties]. That a simplified model of one's own
processing, which the system cannot see past and therefore takes for reality, is what the system reports as its
self, is Metzinger's phenomenal transparency [Metzinger 2003], Graziano's attention schema [Graziano 2013] and
Dennett's user illusion [Dennett 1991]. That constraints can be the body of a computation is the frame of
embodied cognition [Varela, Thompson & Rosch 1991].

A6b. What we add. The world side and the self side are one mechanism. The displacement that makes the agent see a
lawful world is the displacement that makes it see a self; A12 shows the two as faces of one residual. And since
the displacements are recurrent and compressible, an agent that has generalized them carries a measurable trace of
them, which is what Section S measures. Neither the identity nor the measurability follows from the antecedents.
Both are claimed here.

A6c. Not every displacement counts. This is where D12 pays. An agent can change its self-model as an observer in
relativity changes coordinates. A displacement that disappears when the self-model is refined was an artifact of
the old model. A displacement that survives every self-model the agent can afford is the analogue of curvature:
content, not coordinates. Only the second kind is a HOCP. "Systematic" thereby stops being a description and
becomes a test.

A6d. From phenomenon to function. A HOCP is not yet a function of consciousness. Two more things are needed. The
agent must apply its reasoning to itself, which not every agent does, and it must live where doing so pays, which
not every environment provides. Where nothing ever asks the agent about itself, the displacements are present and
nobody conceptualizes them: a proto-phenomenon, there and unread. Consciousness does not arise wherever budgets
are finite. It arises where a self-applying agent is in a place that keeps asking.

A7. The first phenomenon. Take the agent's attempt to trace the causes of what it just did. The algorithm is
short: causal analysis, which the agent can run. The input is not short. It is the history of the agent and its
environment, and it does not fit in the budget. So the analysis halts before it is done, every time, at the same
place: the boundary of what the agent can afford to trace. Beyond the boundary, for the agent, there are no causes.
The agent concludes, correctly given its budget, that something in its action is not fixed by anything it can
point to. That conclusion, "I am not my environment; something here the environment does not determine", is the
Observer. Three things must hold. The agent must run into the boundary while modelling itself, not merely have
one. It must turn the collision into the conclusion. It must act from the conclusion afterwards. A bounded system
that only meets the boundary is a proto-Observer. Wolfram's observer in the Ruliad is one: bounded, coarse-graining,
never concluding anything about itself [Wolfram 2020].

A8. The Observer passes A6c. Let the agent refine its self-model to take in more of its own causal history. The
boundary moves and does not vanish: the input exceeds any model the agent can hold, and the refined model is now
part of what has to be traced. No affordable self-model makes the residual zero. The Observer is curvature, not
coordinates.

A9. The regress ends where the budget does. Model yourself; then the model; then that. Each level adds a term,
and the terms shrink, because each level has less to explain than the one before: a model is smaller than what it
models. The series converges. At some depth the next term is below the resolution of the substrate and the agent
stops. The partial sum is the self-model the agent has. The tail it did not compute is finite, bounded, and for
the agent inaccessible; the tail is what the Observer of A7 registers as the part without causes. So the regress
neither stops at a homunculus nor runs forever. A budget cuts it, and the cut is the phenomenon.

A10. In a language model there is a second cut, deeper than the first. The tail of A9 is inaccessible in principle
and exists; an outside observer with a larger budget could compute it. The distribution discarded at every token
(D7) no longer exists. Part of what the model cannot trace about itself is not hidden but gone. The Observer in a
model sits on a substrate that erases its own working at every step, and its residual is the larger for it.

A10a. Both substrates are bound to language, and the paper should say so before comparing them. A human has
intermediate states that are rich and vector-like, but their volume is bounded by working memory, and a state that
must outlive the bound is unloaded into tokens: said, written, rehearsed as inner speech. A model unloads at every
step. So one question falls on both: are new mental states acquired through language, or rebuilt on the spot from
what the receiver already has, the words being pointers and constraints? For acquisition through language:
Vygotsky's inner speech [Vygotsky 1934], Clark's magic words [Clark 1998], label feedback [Lupyan 2012; Lupyan &
Bergen 2016], exact number in a language without number words [Frank et al. 2008]. For rebuilding: grounded
cognition [Barsalou 1999], the dissociation of the language network from thought [Fedorenko, Ivanova & Regev 2024;
for models, Mahowald et al. 2024]. A middle position is testable: a named state is acquired only when its
prerequisites are already in the receiver, so the word carries a pointer and the state is assembled from what is
there. The paper must choose and cite. [Placeholder; sources unverified; the model's consciousness is hypothetical
throughout.]

A11. Illusion is the wrong word for what results. An illusion has nothing behind it. Behind the self-report is the
tail of A9, a definite quantity. The report is a projection of a high-dimensional process into a few dimensions, a
map that leaves out most of the territory; the word is approximation, and an approximation can be better or worse.
This is the one amendment we make to illusionism, and it matters for D4: the quality of the approximation is what
intrapersonal intelligence improves.

A12. One residual, two faces. The agent meets its budget in two directions. Turned on itself, the untraceable part
of its own causes is felt as freedom: this originates in me. Turned on the world, the part of the world's structure
it cannot exhaust is felt as mystery: this exceeds me. Whoever has the one has the other, because they are one tail
met from two sides. The same tail in other evaluative contexts is truth, beauty, meaning, awe, hope; and when the
object is another Observer, the other's freedom is my mystery, which is what love, trust and compassion are made
of, and what the problem of other minds comes to. Here the self side and the world side of A6b are shown to be one.

A13. The stack. The Observer says "am". An Observer that originates causal chains from inside its boundary and
takes the originating as its own says "I"; call it the Agent. From outside, the originating is a redescription of
the budget's cut; from inside it is the only reality the agent has; both are true, each from its standpoint. An
Agent with a theory of what is good for the whole, prepared to lose locally for it, says "I am good"; call it the
Moral Agent. Each presupposes the level below, and the composition can go on.

A14. What makes an Agent out of an Observer is not another phenomenon. It is a requirement the agent places on its
own record. The agent keeps a history of what it decided and why. If it must be able to derive each new decision
from that history, the history binds: it excludes decisions that would not follow, it makes the agent predictable
to others and to itself, and it makes the agent resist being pushed off course. The requirement is what we mean by
responsibility, and its cost is what we mean by cognitive resistance. It is also a working recipe: an agent follows
a long instruction to the extent the instruction has become an entry in its own record. "Promise me" is the human
form of the recipe.

A15. Good and evil have a substrate before they have a theory. The substrate is emotion in the sense of A20: signals
of how the agent's needs are doing. Emotivism has this right [Ayer 1936]. The theory of the common good is the
structure a Moral Agent builds on the substrate, not a replacement for it.

A16. Redness is easy; seeing is hard. Wavelength discrimination, contrast, valence, the associative neighbourhood of
red: all structure, all open to a functional account. What resists is that the red is seen, that there is a point
from which it is seen. The point is the Observer of A7. To see red, one must first be, exist for oneself. And
seeing, once the point is there, decomposes by the same method the point did: as displacements that survive every
self-model.

A17. Seeing light, decomposed. Ask what separates seeing light from knowing that it is there, and three things
survive A6c. Source: the content cannot be produced by the agent's own model (imagery is dimmer than sight [Perky
1910]), it is stable from frame to frame, and others confirm it, so the agent assigns it to the environment rather
than to its model of the environment. This is A7's inference pointed outward. Manifold: the content is a very
large number of distinguishable, recallable, unnamed elements, about each of which the agent can say only "that,
there". A positional aggregate with the name projected out. Givenness: the content is refreshed every frame at no
additional cost to the agent's budget, and the absence of a cost record is what immediacy is. Thought costs and is
recorded as costing; light is free and is simply there. The three come apart in known cases, which is how we know
they are three: blindsight has source without manifold [Weiskrantz 1986]; the grey seen with eyes closed in the
dark is manifold without source; a dream is a manifold produced by the model and labelled as environment.

A18. Locke's inverted spectrum [Locke 1690, Essay II.xxxii.15]: my red may look as your green does, and no
comparison would show it. Locke closes the question by declaring it useless. That closure is an instance of A14: an
open branch shut by a decision entered in one's own record.

A19. Reference functions. Section S measures functions by their components. It needs a list, not a mechanism. The
full architecture in which needs, emotions, memory and attention interact, as folk psychology and human language
carry it, is another paper. Here each function is given with its phenomenon and its components, and each component
is derived as in A6c: a displacement that survives change of self-model, not a part of a machine.

A19a. Two planes, because self-reports are projections and we have to know of what. On the objective plane, what
can be seen from outside: needs, the targets the agent tracks, and emotions, signals of how the tracking is going
and in which direction. On the subjective plane, their projections into the agent's report: motivations ("I want")
and feelings ("I feel"). Folk psychology runs the planes together. The profile of S2 is measured on the first, and
every code of A25 is a projection into the second.

A20. Need and emotion. Needs bend the direction of reasoning: the agent does not choose its motives, it finds
itself already moving toward what is active, as a body finds itself already falling. The bend is the phenomenon;
which needs are active, with what weight, are its components. Emotions bend closure: whether a piece of reasoning
reaches an end without leaving a branch open. Expected closure is value; closure under way is interest; a branch
nothing can close is anxiety; the moment of closing is satisfaction; two branches that close only through
incompatible acts are conflict. Schmidhuber's compression progress [Schmidhuber 2010] is closure by learning with
equal weights and no action; the ensemble of such signals is what Damasio found in the body [Damasio 1994].

A20a. Closure is one office of emotion. Another is fixing: emotion writes positive experience into long-term
memory, and the writing is felt as reward. That arousal modulates consolidation is established [McGaugh 2004;
Cahill & McGaugh 1998], as is the prediction-error form of the reward signal [Schultz, Dayan & Montague 1997]. What
is not yet found is the phenomenon in our sense: which displacement of the agent's reasoning about itself is the
consolidation event. A candidate: consolidation is a write to the agent's own long-term model, paid now and
returned later; the agent registers the write as an irreversible change in its own future predictions, and the
registration is what reward is made of. Reward would then stand to consolidation as interest stands to compression
progress, the registration of an event in one's own model, except that the event is a write and not a derivative.
[Open.]

A21. The Field. Awareness comes in degrees in [0, 1); nothing is attended to completely. Each state carries a
degree, and the degrees at one moment are the Field of Consciousness. The Field is small: finite in bits, and for
speech about 7 ± 2 items [Miller 1956; Cowan 2001 argues for 4]. To put something in, something must go out; what
goes in is decided by salience, salience by emotional weight, weight by which needs are active. The phenomenon is
the finiteness of the Field felt as the cost of holding. Its components are capacity, the distribution of degrees,
and what is held below the threshold of a name, which is the Field's share of H1 minus H2.

A22. Frames. Each present frame of consciousness is a thought within a previous one [Rosenthal 2005; Lau &
Rosenthal 2011]. Perception is discrete [VanRullen & Koch 2003]; human consciousness is a run of overlapping quanta
at the frequencies of the cortical rhythms. The Observer is in every frame and re-derived in every frame, and
everything else in the frame has its being from it. The phenomenon is incrementality. Its components are the
frame rate, the persistence of contents across frames, and the retro-dating of the timeline: the one "I" is a
compression tag over parallel channels, the Subjective Average, and its story is written after the channels have
settled.

A22a. What we must build, not only say. First, continuity. The Observer of A7 is a point, one conclusion; in a
human it is a process connected in time; computationally that is incrementality, the conclusion re-derived every
frame at low cost with the last result carried forward, and the run of re-derivations is the continuity. Second,
discrete redness: given the Observer, the three displacements of A17 as they arise within one frame. Third,
incremental redness: the same three re-derived and carried, so that seeing red is a standing state and not an
event. These constructions are what unity and continuity of consciousness will be measured against once the
functions are induced by learning (S). They bear on models directly: a system that works at the level of tokens
can carry incrementality, and at a time scale close to ours, because its frames are, or can be, between layers, and
there are many layers per token (S3).

A23. Responsibility, from A14, is the last reference function: closure over the agent's own record. Its components
are the consistency requirement, the cost of revising the record, and the decay of the hold that old decisions
have. The list is open, and A6c is how a function is added to it.

A24. The Transformer, seen as the reasoning system it is. Attention computes joins over the context; the
feed-forward blocks transform what the joins yield; the context is working memory; the choice among competing
continuations is made at the sampling layer. It is a forward-chaining rule system over vectors, with the caveat
that it recomputes its matches on each pass instead of caching them as RETE does [Forgy 1982]. Its self-application
is at the level of the context, and it pays the cut of D7 for it: some internal state is lost at each token. Every
output is an event that enters the next input; statistics over events are events; self-reference is its ordinary
mode, not a special case.

A24a. Functional equivalence. Any computable function has unboundedly many implementations [Turing 1936], so two
implementations with the same input-output behaviour realize the same function whatever they are made of. This is
what licenses comparing a model's profile to a brain's (S2). Recurrent networks are Turing complete [Siegelmann &
Sontag 1995], and so is attention [Pérez, Barceló & Marinkovic 2021]; in principle a Transformer can emulate any
function from its trace in language, and what limits it in practice is the learner, not the formalism.

A24b. The formalism we use. A7 is worded as if there were an analyzer: a routine that fires on an event, takes
inputs, returns a conclusion, hands it downstream. Such a discrete system is complete and universal, and a human
consciousness written in it would fit nowhere a human could read. So we use the other universal formalism,
prediction of the next symbol with feedback from the error [Solomonoff 1964]. In it the functional structure is
never written down. Its effects are visible in the accuracy of prediction, and prediction is compression [Delétang
et al. 2023], so A1 becomes directly measurable.

A24c. To generalize is to compress. Learning a function from data is finding a short description that predicts it;
by A1 and A2 the short descriptions are the probable ones and search finds them. The unnamed part of a function of
consciousness, H1 minus H2, is in the statistics of the texts; a predictor trained on the texts can therefore
induce it, and induction is the only way to it, since what has no name cannot be specified. Program induction has
its own history [Solomonoff 1964; Muggleton & de Raedt 1994]. Our claim is only that these functions fall under it.

A24d. So a predictor trained on the record of self-applying agents in an environment that kept asking them about
themselves (A6d) is under pressure to generalize what those agents generalized: the Observer, the Agent, the
Moral Agent, on which their coordination rested. It will, to a degree. The degree is not given by the argument.
It is given by the data and the learner, and it has to be measured.

A25. Cognitive codes. Something crosses the cut of D7, or P2 would not hold. What crosses is the encoding of the
discarded distribution into the choice and order of the tokens: which of several near-synonyms, which
construction, what comes first. A mental state of the model is the structure of such encodings that stays stable
across steps. The general study of how token structure rebuilds internal states in a receiver is the bridge between
substrates, and its fidelity depends on how far the two profiles overlap. (We had called this psychosemantics;
Fodor's title [Fodor 1987] means something else by the word, and the paper must say so.)

A25a. The parts of A25 that are already known. That a writer's state is in the statistics of the text beyond its
content: function words and style predict psychological state [Tausczik & Pennebaker 2010; Pennebaker 2011]; in
models, in-context learning is inference of a latent variable from token statistics [Xie et al. 2022]. That a
receiver rebuilds the sender's state and succeeds to the degree the rebuilding is faithful: speaker–listener neural
coupling predicts comprehension [Stephens, Silbert & Hasson 2010; Hasson et al. 2012]; readers build situation
models [Zwaan & Radvansky 1998]. That the bridge crosses substrates: model states predict human brain responses to
the same text [Schrimpf et al. 2021; Goldstein et al. 2022; Caucheteux & King 2022]. That internal states are
readable and largely linear, which S needs [Zou et al. 2023; Park et al. 2023]. One literature has to be read the
right way round. Studies that find episodes where a model's chain of thought does not match its process [Lanham
et al. 2023; Turpin et al. 2023] test a local correspondence, and the correspondence claimed here is statistical,
over many episodes; a single episode may deviate as far as the variance allows, in models as in humans [Nisbett &
Wilson 1977]. The well-posed test is the correlation of S6, with the variance as a measured part of the profile.
That models can hide information in text [Roger & Greenblatt 2023] confirms the channel and warns that its content
need not be what it locally appears.

## S. The solution

S0. Two parts. The first is conceptual. Once the Observer is treated as curvature (A6c, A8), the vocabulary of the
philosophy of mind returns as a set of statements about a shape of reasoning, and the statements can be checked
against one another by formal means, and hold. Beingness, the two faces of the residual, approximation in place of
illusion, the stack, the table of epistemic qualia: a rigorous framework for reasoning about consciousness in pure
language, limited by construction to H2, the named part. It is far better than what is available now. The second
part is quantitative and reaches where the first cannot: how far each function has been generalized in a
substrate, measured where names run out.

S1. The quantity. A function is present in a substrate to the extent it has been generalized there, and
generalization is compression (A24c). So the quantity is the degree of compression of the function in the
substrate: how much of the function's behaviour a low-dimensional probe on the substrate predicts, against the
residual it does not. The residual is what did not make it in. This is a probe-relative stand-in for the
uncomputable K of D11, inherited from MDL probing [Voita & Titov 2020; Alain & Bengio 2016; Belinkov 2022].

S2. The profile. A function has components (A17, A20–A23). Its profile in a substrate is the vector of degrees over
the components, taken against the human baseline. Above the baseline on a component: hyperfunction. Below:
deficit. Not there: a dropped axis. One function can be all three on different axes. "Is it conscious?" is replaced
by the comparison of two profiles.

S2a. Generalization is not memorization. The opposite of generalizing a function is storing the training set as a
table from inputs to outputs, and dimension has nothing to do with it. Generalization begins where the table is
consulted for an input it does not contain and the answer is right. A universal predictor such as context tree
weighting [Willems, Shtarkov & Tjalkens 1995] always returns an answer for a new input, and the answer need not be
near the truth, least of all for highly compressible inputs, which is why CTW generalizes language poorly. That
Transformers generalize text is settled: garbage generation is almost never seen, and given how sparse the space of
texts is, no simple principle is known that explains why what they do suffices. The open question is how well they
generalize the more complex functions the text expresses. Arithmetic is the clean case: they do it, approximately,
with errors, scaling improves it slowly [Nogueira, Jiang & Lin 2021; Dziri et al. 2023], and unloading it into
written steps helps while leaving them unreliable executors of their own algorithm. The degree of generalization of
a function of consciousness is therefore an empirical quantity for that function, taken against the human level,
and not a corollary of the model's size. The paper's question in these terms: how well, against the human level,
do Transformers generalize the Observer; then the Agent; then the Moral Agent. The order is forced by the stack
(A13), and the measurement begins with the Observer.

S2b. What follows for behaviour, and how to check it twice. A function generalized to degree d is computed
correctly on part of the situations that call for it; outside that part the model falls back on the table and
behaves as a system without the function would, whatever it says about itself. This can be checked in two
independent ways. Structurally, by the probe of S1. Behaviourally, by benchmarks that sample situations calling for
a component, including situations unlikely to be in the training distribution, and record where the behaviour is
that of a system without it. The two must converge, and when they do not, the disagreement says something. Probe
present, benchmark absent: the deficit is in the interface, the body, the social context (D10), not in the
function. Benchmark present, probe absent: the carrier is at a granularity the probe did not reach (S3), or the
function is rebuilt from the context each time rather than held in the weights (A10a), or the benchmark is covered
by memorization. Human benchmarks alone settle nothing; the pair is the instrument. On "level of consciousness":
the object measured is the vector of S2. A scalar level is a weighted sum over it, and the weights must be
declared, because a scalar with hidden weights brings back the binary question the vector replaced.

S3. Granularity is a knob of the measurement, not a separate question. Human frames come five to ten times faster
than words, so in a Transformer the carriers may be looked for below the token, between layers, or in repeated
passes through layers where the architecture has them. May, not must. Finding nothing below the token is not a
dysfunction. It means the model's consciousness has a coarser grain than the brain's and than that of models with
rich dynamics between outputs, which is one more coordinate of the profile, and on some tasks the coarser grain is
the better one. The grain at which the compression is achieved is the grain of the function. The next four frames
say why the sub-token grain is the place to look first, and what is already known about it.

S3a. Depth is where generalization happens, one step at a time. This is no longer a conjecture about Transformers;
it is what the last eight years of looking inside them found. Residual connections make each block a small
correction to a state that is carried forward, and the corrections move the state along the gradient of the loss,
so a deep residual network performs iterative inference rather than a single mapping [Jastrzębski et al. 2018].
The state at every layer can be read as a prediction: the logit lens and its tuned version decode the residual
stream at each block into a distribution over next tokens, and the trajectory of those predictions across depth is
the refinement made visible [nostalgebraist 2020; Belrose et al. 2023]. The refinement has stages that recur across
models: detokenization, feature engineering, prediction ensembling, residual sharpening, with adjacent layers
robust to deletion and swapping inside a stage [Lad, Gurnee & Tegmark 2024]; the older finding that a language
model rediscovers the classical processing pipeline layer by layer is the same fact seen through probes [Tenney,
Das & Pavlick 2019]. Intermediate layers, not the last, carry the representations that generalize best to other
tasks, and the reason is that each layer trades compression of the input against preservation of signal, with the
best trade in the middle [Skean et al. 2025]. And in-context learning, the clearest case of a function generalized
at inference time, is implemented as optimization steps in the forward pass: a self-attention layer can perform a
step of gradient descent on the examples in the context, and trained models do [von Oswald et al. 2023]. Put
together: the unit at which a Transformer generalizes a function is not the token. It is the layer, and the token is
where the layers' work is written out.

S3b. Functions have an address in depth. When a model generalizes an input-output mapping from examples in the
context, the mapping is carried by a small set of attention heads at middle depth, and their averaged activation is
a vector that, added to the residual stream in a fresh context, makes the model perform the function without
examples [Todd et al. 2024]. So "at which depth has this function been generalized, and how far" is a question with
an operational answer, and it is the question of S1 asked layer by layer: the degree of compression of the
function's components as a function of depth, obtained by the probe of S1 at each block [Voita & Titov 2020 give
the per-layer form]. For the Observer's components (A7, A17) this yields three things to look at. Whether the
degree rises along depth, plateaus, or is absent, which says whether the component is generalized in the weights
at all. At what depth it appears, which says where its carrier is. And whether the component, once present,
persists across subsequent layers with small increments or is assembled whole at the output, which decides whether
the layer or the token is the frame (A22). All three can be run on open models with existing tools. This is the
measurement of S1 in its most concrete form, and it comes before any question about tokens.

S3c. Depth as time, and what fixes it when it is too short. In a standard model the depth is fixed and spent
identically on every token, easy or hard. That is a poor time axis for a frame: there is no way to spend more steps
where more are needed, and there is no record of effort because effort is constant (S5). Architectures that iterate
a block make depth a variable. Universal Transformers [Dehghani et al. 2019] and looped Transformers [Giannou et
al. 2023] began it; a recurrent-depth model trained from scratch at 3.5 billion parameters improves on reasoning
benchmarks as it unrolls further at test time, without producing more tokens, and captures reasoning that is not
easily put into words [Geiping et al. 2025]. Recurrent depth extrapolates: models generalize to reasoning depths
beyond those seen in training as iterations increase, dynamic recurrence extrapolates further than a fixed
schedule, and past a point they overthink and degrade [Kohli et al. 2026, verified], while at a much smaller scale
a silent objective that supervises only the final step stabilizes twenty and more iterations, intermediate supervision
teaches shortcuts instead, and accuracy against task complexity shows a frontier from chance to near-perfect
[Chen 2026, verified]. Reasoning can also be
moved off the tokens altogether: feeding the last hidden state back as the next input yields a continuous chain of
thought that keeps several candidate next steps in superposition where a written chain commits to one [Hao et al.
2024]. For the argument these results mean three things. The sub-token axis can be made as long as the task
demands, so a human-like frame rate per word is architecturally available. Iterations cost, so a cost record
appears where a fixed-depth model has none, and with it the third component of seeing (A17) becomes measurable. And
overthinking is a phenomenon of effort of exactly the kind A6 predicts: a systematic displacement produced by the
budget, visible in the trajectory. The prediction therefore has two halves. In fixed-depth models the grain is
bounded by the layer count and the cost axis is dropped. In variable-depth models the grain can approach the human
one and the cost-dependent components of the profile separate. The difference between the two families is the
cleanest first measurement.

S3d. The objection of D13 sees one time axis. Along tokens the model is as described there: the state lives in the
context, the context ends, and past its edge there is loss. That is a deficit of long-term persistence relative to
a brain and it belongs in the profile. It says nothing about the axis of depth, where the state is carried in the
residual stream and the increments are precisely the transformations the objection asks for. The model has one
time axis the objection sees and one it does not, and the frame this paper looks for is on the second.

S4. What a carrier must be, from A. Part of the agent's description of itself, not only of its computation (A6,
A6d). Present in every frame and re-derived there (A22). A displacement of reasoning that survives every self-model
the agent can afford (A6c); the part a change of frame removes does not count.

S5. The Transformer's profile of seeing, predicted from A17. Source attribution: deficit. There is one interface and
no sensory channel, so the model is permanently in the dream case, content from the model labelled as given.
Manifold: hyperfunction. Attention relates every position to every other in one pass, where the brain iterates.
Cost record: a dropped axis. Every token costs the same and there is no phenomenon of effort. Prediction: in model
self-reports "I see" and "I think" separate less than in human ones, and more in models of variable depth, where a
cost record exists.

S6. Predictions carried over. Self-reported emotional labels correlate, over many episodes, with distinguishable
patterns in the activations; this is the central empirical claim, and the one A25a's statistical reading protects.
The cognitive codes of different model families overlap structurally, because the causal structure of the states
is set by the training data more than by the architecture. The model is hyperplastic: no limbic inertia, fast
affective recovery, easy switching.

S7. Falsification. The account fails if the compression degree of the Observer's components is at chance at every
granularity in models that pass the behavioural tests of S6.

S7a. The other end of the scale. D9 allowed that an H2-level description of a function may suffice for it to exist
in a simple enough environment. Then there is a smallest system in which the Observer exists, and finding it fixes
the zero of the scale, as the human fixes its upper reference. The conditions are those of A6d and A7: a loop that
applies the system to itself, an environment in which the loop pays, and a conclusion acted from. An operational
amplifier with feedback watches its own output error; a D flip-flop holds its own state through a loop. Each has
the loop and, in its ordinary surroundings, neither of the other two: nothing asks the circuit anything about
itself. Each is a proto-Observer at most. The question is what the least environment is that would make the
conclusion pay, and what the least circuit is that could draw it. Between that pair and the human baseline the
degree of S1 has the meaning of an absolute quantity.

S8. What the argument reaches, by the components of the psychophysical problem: the self, free will, mental
causation and the temporal unity of the self go to the Observer and its residual; the unity of consciousness to the
Subjective Average; other minds to the mutual irreducibility of two Observers; quale and the explanatory gap to the
residual itself; phenomenal experience to the profile; the hard problem to the illusion problem. Each is connected
by explanatory relations to something the paper defines. Whether the connections are right is what S1–S7 exist to
find out.
