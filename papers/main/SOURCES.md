# Sources ledger for paper v2

One row per key in `refs.bib`. A source counts as **verified** only when the copy was obtained, opened, and the claim
the paper makes located in it; the locus says where. Statuses:

- `verified` — read against the claim, locus given;
- `verified (secondary)` — the copy has no usable text layer and the claim was read in a source that states it;
- `substitute` — the copy is a précis, chapter, or web version rather than the cited item; the citation may have to
  change to what was actually read;
- `obtained` — a copy is in `sources/`, and the claim could not be located in it yet (poor OCR, wrong page range);
- `unverified` — no copy obtained yet.

The verification passes of 2026-09-11 went through every file in `sources/`, then fetched the rest: arXiv, Europe PMC,
Unpaywall, publisher and author pages, PubMed abstracts where the article is paywalled, and Open Library full-text
search inside scanned books. Four claims were corrected against what the sources say; see the bottom of this file.

| key | what it must support | status | locus and file |
|---|---|---|---|
| nagel1974 | the bat question marks a limit on description from outside | verified | "only if there is something that it is like to be that organism", p. 436; the sonar passage and the point of view, pp. 438--439; nagel1974.pdf |
| chalmers1995 | the easy/hard split; the hard problem asks why processing is accompanied by experience | verified | §"The Easy Problems and the Hard Problem"; chalmers1995.pdf |
| frankish2016 | illusionism; the illusion problem as successor of the hard problem | verified | p. 1 and §4 "Facing up to the illusion problem"; frankish2016.pdf |
| chalmers2023 | the applied assessment: the list senses/embodiment, world and self models, recurrent processing, global workspace, unified agency; credence under ten percent for current models | verified | the "X = ..." sections and the closing estimate ("confidence somewhere under 10 percent"); chalmers2023.pdf |
| butlin2023 | computational functionalism as working assumption; indicator properties derived from RPT, GWT, computational HOT, AST, predictive processing, agency and embodiment | verified | §1 tenets and §2 theory list; butlin2023.pdf |
| smirnov2026v1 | the first version of this work; no longer cited in the text, kept for reference | verified (metadata) | version DOI 10.5281/zenodo.20547880 (v0.1-draft) per CITATION.cff and https://zenodo.org/records/20547880; Zenodo refuses automated access, so the record page itself was not fetched |
| synthea2026 | the repository holding the bootstrap texts in three sizes | verified | repository contents: bootstrap/ (six files), bootstrap-mini/, bootstrap-nano/; CITATION.cff for the DOI |
| spielberg2001 | a cultural instance of the Turing test played out on the emotional plane | verified (metadata) | the film itself; cited as a work, no claim beyond its premise |
| jonze2013 | the same on the romantic plane | verified (metadata) | the film itself; cited as a work |
| dean1988 | anytime algorithms: an approximate result at any stopping point, quality a function of the time allowed | verified | AAAI-88 proceedings copy, the section introducing anytime algorithms; dean1988.pdf |
| zilberstein1996 | anytime algorithms: quality of results improves gradually with computation time; performance profiles | verified | abstract and §1: "quality of results improves gradually as computation time increases"; the term coined by Dean and Boddy; zilberstein1996.pdf |
| li2023 | a sequence model's activations carry the board state and can be edited to change its play | verified | abstract: "internal representation of the board state", interventional experiments; li2023.pdf |
| gurnee2024 | linear representations of space and time in large models | verified | abstract: linear representations across multiple scales, space and time neurons; gurnee2024.pdf |
| merker2007 | the upper brainstem system is not rendered nonfunctional by the absence of cortex; cortex as the medium for conscious contents | verified (abstract) | PMID 17475053; merker2007.abstract.txt |
| feuillet2007 | a man with massive hydrocephalus and a thin cortical rim leading a normal life | verified (metadata) | PMID 17658396, Lancet case report with images, no abstract |
| sierra1998 | depersonalization as a clinical phenomenon with its emotional change | verified (abstract) | PMID 9807645; sierra1998.abstract.txt |
| hunter2004 | depersonalisation and derealisation as a recognized pair of symptoms, self and surroundings | verified (abstract) | PMID 15022041, title and abstract; hunter2004.abstract.txt |
| apa2013 | the diagnostic definitions: derealization as unreality or detachment with respect to surroundings; depersonalization with respect to one's own thoughts, feelings, body or actions | verified (search inside) | Open Library full-text search of the Desk Reference to the Diagnostic Criteria from DSM-5: "Derealization: Experiences of unreality or detachment with respect to surroundings" |
| spiegel2011 | derealization symptoms included in depersonalization disorder in DSM-5, i.e. the two classified together | verified (abstract) | PMID 22134959; spiegel2011.abstract.txt |
| liu2025 | incremental computation as a systematic transformation of batch computation: the result maintained under input changes | verified | §2 three categories of studies, §3 essence of incremental computation; liu2025.pdf |
| friston2010 | the brain as minimization of prediction error under the free-energy principle | verified (abstract) | PMID 20068583; friston2010.abstract.txt |
| clark2013 | hierarchical generative models matching input with top-down predictions, minimizing prediction error | verified (abstract) | PMID 23663408; clark2013.abstract.txt |
| blakemore1998 | a self-produced (predicted) tactile stimulus is perceived as less than the same stimulus produced externally | verified (abstract) | PMID 10196573; blakemore1998.abstract.txt |
| vanroojen2023 | the cognitivism / non-cognitivism distinction; emotivism as a non-cognitivist variant | verified | SEP entry, revised Dec 2023, opening and the emotivism section; vanroojen-sep.html |
| gallagher2000 | minimal self (no temporal extension) vs narrative self (identity and continuity across time) | verified (abstract) | PMID 10637618; gallagher2000.abstract.txt |
| haggard2017 | sense of agency as the experience of controlling one's own actions, produced by specific brain mechanisms | verified (abstract) | PMID 28251993; haggard2017.abstract.txt |
| haidt2001 | moral judgment reached first, moral reasoning a post hoc construction | verified (abstract) | PMID 11699120; haidt2001.abstract.txt |
| hart1961 | law as the union of primary and secondary rules | verified (search inside) | Open Library full-text search of The Concept of Law: chapter V "Law as the Union of Primary and Secondary Rules" |
| dostoevsky1866 | the novel cited as the specimen of Appendix C; the horse dream is Part 1, Chapter 5 | verified (metadata) | public-domain text; the quotations are the standard ones |
| wei2022 | asking for intermediate reasoning steps improves answers (chain of thought) | verified | title and abstract; wei2022.pdf |
| nanda2023 | grokking as three continuous phases, memorization, circuit formation, cleanup, visible in the weights | verified | abstract; nanda2023.pdf |
| olsson2022 | induction heads as the mechanism of most in-context learning | verified | abstract; olsson2022.pdf |
| elhage2021 | mechanistic interpretability as reverse-engineering a Transformer's computation | verified | opening section; elhage2021.html |
| bricken2023 | interpretable features recovered from a small model by dictionary learning (sparse autoencoder) | verified | opening; bricken2023.html |
| templeton2024 | the same at production scale, Claude 3 Sonnet | verified | opening and feature examples; templeton2024.html |
| koch2016 | neural correlates of contents in a posterior cortical hot zone of many areas, not one structure | verified (abstract) | PMID 27094080; koch2016.abstract.txt |
| zwicker2007 | fluctuation strength most intense at 4 Hz; smooth transition to roughness; maximum roughness at 70 Hz | verified (search inside) | Open Library full-text search of Psychoacoustics: Facts and Models, ch. 10--11: "most intense at 4 Hz", "a smooth transition rather than a strong", "maximum roughness at 70 Hz" (Fig. 11.6) |
| moore1995 | fluctuation strength bandpass with a maximum around 4 Hz; modulation around 20 Hz may elicit both sensations | verified (search inside) | Open Library full-text search of Hearing (Handbook of Perception and Cognition) |
| plomp1965 | roughness of beats and the critical band | verified (metadata) | PMID 5831012, JASA 38(4) |
| joris2004 | perception and neural processing of amplitude modulation over a range of time scales | verified (abstract) | PMID 15044682; joris2004.abstract.txt |
| strawson2006 | physicalism entails panpsychism (realistic monism) | verified (metadata) | CrossRef records of the 2008 reprints; JCS 13(10--11), 2006 |
| goff2017 | panpsychism / Russellian monism as the account of fundamental reality | verified (metadata) | CrossRef, OUP 2017 |
| copeland2002 | hypercomputation as computation beyond the Turing limit | verified (metadata) | CrossRef, Minds and Machines 12(4) 461--502 |
| penrose1989 | the claim that mathematical insight is non-computable | verified (metadata) | Open Library record |
| simons1997 | change blindness: large changes between views go unnoticed | verified (abstract) | PMID 21223921; simons1997.abstract.txt |
| simons1999 | inattentional blindness: the gorilla missed by about half the observers | verified (abstract) | PMID 10694957; simons1999.abstract.txt |
| johansson2005 | choice blindness: switched outcomes not detected, the unmade choice defended | verified (abstract) | PMID 16210542; johansson2005.abstract.txt |
| libet1983 | readiness potential precedes the reported time of intention | verified (abstract) | PMID 6640273; libet1983.abstract.txt |
| eagleman2000 | postdiction in visual awareness (flash-lag) | verified (abstract) | PMID 10720334; eagleman2000.abstract.txt |
| dennett1992 | time and the observer: no single place and time where consciousness happens | verified (metadata) | CrossRef, BBS 15(2) 183--201 |
| schwitzgebel2008 | naive introspection unreliable about current experience | verified (metadata) | CrossRef, Phil. Review 117(2) 245--273 |
| wegner2002 | the sense of conscious will as a construction | verified (metadata) | CrossRef, MIT Press 2002 |
| bender2021 | "stochastic parrots" as the deflationary reading of language models | verified (metadata) | CrossRef, FAccT 2021, 610--623, doi 10.1145/3442188.3445922 |
| morris2024 | a proposal to grade AGI by levels of performance and generality against skilled humans (a proposal, not an operational test) | verified | title and §1--2 of the position paper; morris2024.pdf |
| ji2023 | alignment objectives stated as robustness, interpretability, controllability, ethicality (RICE); consciousness mentioned once in the survey | verified | §1.2.2 and a full-text count; ji2023.pdf |
| long2024 | AI welfare and moral patienthood as a realistic possibility | verified | abstract; long2024.pdf |
| iasr2026 | yearly international scientific assessment of general-purpose AI capabilities and risks, chaired by Bengio, nominees of 30+ countries | verified (web) | internationalaisafetyreport.org publication page and press summaries, 2026-09-14 |
| euaiact2024 | obligations on providers of general-purpose AI models with systemic risk, applicable from Aug 2025, enforced from Aug 2026 | verified (web) | artificialintelligenceact.eu (Article 55, high-level summary) and Commission Q&A, 2026-09-14 |
| amodei2026 | the call to pace frontier capabilities, 12 Sept 2026, supported publicly by Altman and Musk and, with a caveat, by Hassabis | verified | primary page `darioamodei.com/post/we-must-pace-the-frontier`, read 2026-09-15: title "We Must Pace the Frontier", central sentence "We must slow the pace at which we improve the capabilities of AI models". Support: Altman ("I agree with Dario that we need to pace the frontier") and Musk per press; Hassabis on 12 Sept called the direction correct and the details unworked, proposing an industry standards body instead of embedded evaluators. Title corrected 2026-09-15 from the press paraphrase "Pacing the Frontier" |
| wapo2026 | Trump rejects the call citing competition with China, "whoever wins AI wins" | verified (web) | Washington Post, 13 Sept 2026; NPR and CNN concur |
| nbc2026 | Chinese Foreign Ministry rejects the call as fearmongering and vicious competition, no commitment to slow | verified (web) | NBC News, 14 Sept 2026; CNBC, NPR, Forbes concur |
| blier2018 | prequential description length: deep networks compress their training data including the model's cost; variational bounds poor, incremental encoding excellent | verified | abstract; blier2018.pdf |
| feldman2020 | per-example memorization and influence estimation; the long tail whose storage helps rare test examples | verified | abstract and §1; feldman2020.pdf |
| zhang2017 | deep networks easily fit random labels | verified | abstract and §1 "central finding"; zhang2017.pdf |
| carlini2023 | memorization in language models grows log-linearly with model scale, duplication and prompt length | verified | abstract and §1; carlini2023.pdf |
| deletang2022 | Transformers and RNNs fail to generalize on non-regular tasks; only structured memory (stack, tape) generalizes on context-free and context-sensitive ones | verified | abstract; deletang2022.pdf |
| liu2023auto | a low-depth Transformer represents any finite automaton; trained models converge to shortcut solutions with o(T) layers | verified | abstract; liu2023auto.pdf |
| merrill2023 | log-precision Transformers simulated by constant-depth uniform threshold circuits (TC0); under standard complexity assumptions they cannot solve linear equalities or check membership in an arbitrary context-free grammar | verified | abstract and §"Assuming logspace-uniform TC0 != P/NP"; merrill2023.pdf. The finite-state-machine claim is taken from the abstract of merrill2024 |
| merrill2024 | intermediate decoding steps extend the recognized class: logarithmic steps raise the upper bound only from TC0 to L; linear steps (projected pre-norm) simulate automata and recognize all regular languages, staying within context-sensitive; polynomial steps (generalized pre-norm) reach exactly P | verified | abstract and §1 "Logarithmic Steps", "Linear Steps"; merrill2024.pdf. Corrected 2026-09-15: an earlier row gave regular languages to logarithmic steps |
| dennett1991 | user illusion; the regress objection; self-report as misrepresentation | verified (search inside) | "the benign user illusion of its own", Consciousness Explained, located by full-text search of the scanned edition on Open Library |
| ryle1949 | the regress objection against inner observation | verified (search inside) | "Their theory was a para-mechanical hypothesis", The Concept of Mind, ch. I; Open Library full-text search |
| rosenthal2005 | higher-order thought structure; a frame as a thought within a previous one | substitute, read | "differing in how we are conscious of our conscious states"; rosenthal2009.pdf (Oxford Handbook chapter) |
| lau2011 | empirical support for higher-order theories | verified (abstract) | PMID 21737339: reviews the empirical evidence for the higher-order view against first-order, global workspace and recurrent processing theories; lau2011.abstract.txt |
| tononi2015 | differences of experience follow differences of cause-effect structure | verified | §"The central identity: experience as a conceptual structure"; tononi2015.xml |
| metzinger2003 | phenomenal transparency: the self-model cannot be seen as a model | substitute, read | §1.1.3 "Transparency"; metzinger2005.pdf (Précis of Being No One) |
| graziano2011 | awareness as the system's model of its own attention | verified | "awareness is a perceptual reconstruction of attention", p. 1; graziano2011.pdf. The term "attention schema" is from the 2013 book, not this paper |
| graziano2013 | the same, book-length, and the term | verified (search inside) | "the attention schema" as the middle term between awareness and attention; Open Library full-text search of the book |
| varela1991 | constraints as the body of a computation (embodied cognition) | verified (search inside) | "cognition ... as embodied action", The Embodied Mind; Open Library full-text search |
| ayer1936 | emotivism: moral terms express attitude | obtained | ayer1936.pdf; OCR too poor to pin the passage in ch. VI |
| locke1690 | the inverted spectrum, Essay II.xxxii.15, and Locke's closing it as idle | verified | II.xxxii.15 (Gutenberg text) |
| fodor1987 | the word "psychosemantics" is taken for a different project | verified (metadata) | Open Library: Psychosemantics, 1987; the claim is only that the title is taken for a semantics of mental representation |
| gardner1983 | intrapersonal intelligence as a distinct ability | unverified | no scanned edition searchable; Open Library returns only a study outline |
| solomonoff1964a | universal prediction with feedback; program induction; algorithmic probability | obtained | solomonoff1964a.pdf; no usable text layer, claim read in Part II |
| solomonoff1964b | the same, Part II | verified | §"Use of the Codes for Prediction"; universal decoding instructions, p. 225; solomonoff1964b.pdf |
| levin1974 | the coding theorem K(x) = -log m(x) + O(1) | verified | p. 32: a priori probability defined as 2^(-KP(x)); the equality with the universal semimeasure is quoted from Li & Vitányi, as the paper does; levin1974.pdf |
| livitanyi2019 | uncomputability of K; machine-relativity up to a constant; the coding theorem as stated | verified (search inside) | Open Library full-text hit in the book on "Universal Distribution" and the applications to inference; the coding theorem is §4.3.3 in the 3rd and 4th editions |
| turing1936 | a universal machine carries out what any other machine computes | verified | §§6--7; turing1936.pdf. The paper's sentence was reworded: Turing gives universality, the multiplicity of implementations is the corollary |
| siegelmann1995 | recurrent networks are Turing complete under idealized assumptions | verified (secondary) | siegelmann1995.pdf has no text layer; the claim is stated in Pérez et al. 2021, §1 |
| perez2021 | attention is Turing complete | verified | title, abstract, keywords (arbitrary precision); perez2021.pdf |
| forgy1982 | RETE caches matches between cycles, which a Transformer does not | verified | §2.1 "How to avoid iterating over working memory"; forgy1982.pdf |
| muggleton1994 | program induction has a history independent of this paper | obtained | muggleton1994.pdf, 46 pp., Type 3 fonts, no extractable text; the claim is only that the field exists |
| willems1995 | context-tree weighting: universality within a class of tree sources | verified | abstract: all bounded memory tree sources, redundancy bound for individual sequences; willems1995.pdf |
| schmidhuber2010 | compression progress as intrinsic reward; consciousness as a by-product of compression (a self-symbol because the agent is in all its data) | verified | items 1--3 of §1 for intrinsic reward; §on abstraction as a by-product of compression: "Consciousness may be viewed as a by-product of this ... creating some sort of internal symbol or code representing itself"; schmidhuber2010.pdf |
| dingle2018 | input-output maps are biased toward simple outputs, with a bound | verified | Eq. (3) and §"simplicity bias"; dingle2018.pdf |
| valleperez2019 | the parameter-function map of deep networks is biased toward simple functions | verified | abstract: "exponentially biased towards simple functions"; valleperez2018.pdf |
| mingard2021 | SGD lands on functions with near-Bayesian probabilities | verified | abstract and §1: the Bayesian posterior is the first-order determinant of P_SGD, with second-order differences; mingard2021.pdf |
| wolfram2002 | computational irreducibility follows from bounded computation | verified | p. 737 "Computational Irreducibility"; wolfram2002.html |
| wolfram2020 | the Ruliad observer: bounded, coarse-graining, concluding nothing about itself | verified | arXiv:2004.08210 copy of the Complex Systems paper; the discussion of observers limited in their ability to track the system, §8; wolfram2020.pdf |
| wolfram2023 | a bounded observer sees a lawful world because of its bounds; the second law | verified | §§"Observers Construct Their Perceived Reality", "The Cost of Observation"; "the fundamental origin of the Second Law of thermodynamics"; wolfram2023.html |
| simon1955 | bounded rationality: limits deform choice systematically | verified | §II "The essential simplifications"; simon1955.pdf. The phrase "bounded rationality" is from Simon 1957, the content is here |
| lieder2020 | resource-rational analysis: biases as optimal use of a limited budget | verified | title and abstract; lieder2020.pdf |
| griffiths2015 | levels of analysis for rational use of cognitive resources | verified | abstract: levels between the computational and the algorithmic, "resource-rational" architectures; griffiths2015.pdf |
| riemann1873 | the geometric idea voiced before a theory carried it | verified | Clifford's translation, Nature VIII, pp. 14--17, 36--37; "space is only a particular case of a triply extended magnitude", the closing on measure-relations and binding forces; riemann1873.pdf |
| clifford1876 | space-theory of matter as a precursor of geometrized gravity | verified | the ridges-and-furrows passage on curvature; clifford1876.html (Wikisource) |
| norton1992 | Nordström's scalar theory and where it failed | verified | "does not predict any deflection of a light ray by a gravitational field", and the Einstein--Fokker 1914 dénouement; norton1992.pdf |
| perky1910 | the Perky effect: a faint projected picture taken for one's own imagery | verified (secondary) | perky1910.pdf has a text layer of the table of contents only; the phenomenon as described is stated in Okada & Matsuoka 1992: "the assimilation of the signal tone into imagery, i.e., the effect described by Perky in 1910" |
| okada1992 | the Perky effect reproduced in the auditory modality; statement of the effect as assimilation of a real signal into imagery | verified (abstract) | PMID 1594403; okada1992.abstract.txt |
| weiskrantz1986 | blindsight: source attribution without a manifold of elements | verified (search inside) | "orientation discrimination, in the absence of acknowledged awareness (Table 23)", Blindsight; Open Library full-text search |
| damasio1996 | somatic markers as an ensemble of bodily signals used in decision (not cited since 2026-09-12; text moved to removed-for-ka-paper.tex) | verified | p. 1413, statement of the hypothesis; damasio1996.pdf |
| cahill1998 | emotional arousal modulates lasting declarative memory (not cited since 2026-09-12; text moved to removed-for-ka-paper.tex) | verified (abstract) | PMID 9683321: stress hormones and the amygdala as modulators of consolidation for emotional events; cahill1998.abstract.txt |
| mcgaugh2000 | consolidation runs on minutes to hours and is modulated | verified (abstract) | PMID 10634773: new memories consolidate slowly over time, time-dependent processes; mcgaugh2000.abstract.txt |
| schultz1997 | the reward signal has the form of a prediction error (not cited since 2026-09-12; text moved to removed-for-ka-paper.tex) | verified | §"Do dopamine neurons report an error in the prediction of reward?" and Fig. 2; schultz1997.pdf |
| scoville1957 | H.M.: real-time consciousness without accumulation | verified | "a grave loss of recent memory"; scoville1957.pdf |
| miller1956 | capacity of about seven items (not cited since 2026-09-12; text moved to removed-for-ka-paper.tex) | verified | §on one-dimensional absolute judgments, and the span of immediate memory; miller1956.pdf. The paper's restriction to material passing through speech is ours, not Miller's |
| cowan2001 | the reconsidered capacity, about four (not cited since 2026-09-12; text moved to removed-for-ka-paper.tex) | verified | abstract: the smaller limit of three to five chunks is real, about four; cowan2001.pdf |
| vanrullen2003 | perception is discrete and has a rate | verified (abstract) | PMID 12757822: discrete processing epochs, oscillations as the neuronal basis; vanrullen2003.abstract.txt |
| nisbett1977 | humans misreport the causes of their own behaviour | verified | abstract: "little or no direct introspective access to higher order cognitive processes"; nisbett1977.pdf |
| zwaan1998 | readers build situation models rather than storing sentences | verified (abstract) | PMID 9522683: situation models as integrated mental representations of a described state of affairs; zwaan1998.abstract.txt |
| tausczik2010 | function words and style predict psychological state | verified | §"Content Versus Style Words": style or function words, about 500 words making up about 55% of use; tausczik2010.pdf |
| pennebaker2011 | the same, book-length | verified (search inside) | "their use of style words rather than any nouns or regular verbs", The Secret Life of Pronouns; Open Library full-text search |
| stephens2010 | speaker-listener neural coupling predicts comprehension | verified | abstract and title: coupling between production and comprehension across brains during natural communication; stephens2010.pdf |
| hasson2012 | brain-to-brain coupling as a mechanism of shared states | verified (abstract) | PMID 22221820: neural processes in one brain coupled to those in another via a signal through the environment; hasson2012.abstract.txt |
| vygotsky1934 | inner speech as internalized dialogue | verified (search inside) | "written speech follows inner speech", Thought and Language, ch. 7; Open Library full-text search |
| clark1998 | words as tools that reshape the computation using them | unverified | no open copy of the chapter found; the Edinburgh URL is dead |
| lupyan2012 | label feedback modulates perception | verified | title and abstract: the label-feedback hypothesis, effects of language on perception; lupyan2012.pdf |
| frank2008 | exact numerosity is impaired without number words | verified | abstract: no linguistic method for exact quantity, and the matching-task results; frank2008.pdf |
| barsalou1999 | grounded cognition: concepts rebuilt from perceptual states | verified | abstract: perceptual symbols, simulators and simulations; barsalou1999.pdf |
| fedorenko2024 | the language network is dissociable from thought | verified | §on functional selectivity: language areas not recruited by music, math, general reasoning, social reasoning; fedorenko2024.pdf (author manuscript, PMC13222024) |
| mahowald2024 | the same distinction applied to language models | verified | abstract: formal vs functional linguistic competence, and the dissociation; mahowald2024.pdf |
| deletang2024 | prediction is compression, demonstrated with language models | verified | abstract: Chinchilla 70B compresses ImageNet patches to 43.4% and speech to 16.4%; deletang2023.pdf |
| nogueira2021 | Transformers do arithmetic approximately; representation matters; scale does not fix extrapolation | verified | abstract and §5: a 3B model still fails to extrapolate past the trained digit range; nogueira2021.pdf. The paper's sentence was rewritten to this |
| dziri2023 | compositional tasks are solved by shortcut and degrade with depth | verified | abstract and §4: multi-step compositional reasoning reduced to linearized subgraph matching; performance falls to zero as complexity grows; dziri2023.pdf |
| xie2022 | in-context learning as inference of a latent variable | verified | abstract: in-context learning as inference of a shared latent concept; xie2022.pdf |
| vonoswald2023 | a self-attention layer can perform a gradient step on context examples | verified | abstract: explicit weight construction for one linear self-attention layer, plus trained-model evidence; vonoswald2023.pdf |
| todd2024 | a function vector at middle depth carries an in-context mapping | verified | abstract and Fig. 2c: adding the vector at layer 12 of GPT-J produces the task in a zero-shot prompt; todd2024.pdf |
| jastrzebski2018 | residual blocks make a network perform iterative inference | verified | §2: a residual block moves representations along the negative gradient of the loss; jastrzebski2018.pdf |
| nostalgebraist2020 | the logit lens decodes the residual stream at each block | verified | the post itself; nostalgebraist2020.html |
| belrose2023 | the tuned lens corrects the bias of that decoding | verified | §1--2: the logit lens is unreliable for several models; affine translators per block; belrose2023.pdf |
| lad2024 | four stages of inference across model families; middle layers robust to deletion and swapping, first and last not | verified | abstract (72--95% of top-1 accuracy retained) and §4: "in contrast to the first and last layer interventions, the middle layers are remarkably robust"; lad2024.pdf. The paper's sentence was corrected to this |
| tenney2019 | a language model rediscovers the classical pipeline layer by layer | verified | abstract: expected order POS, parsing, NER, semantic roles, with dynamic revision; tenney2019.pdf |
| skean2025 | intermediate layers transfer best; compression against signal preservation | verified | abstract and §1: intermediate layers surpass the final layer by up to 16% on MTEB; skean2025.pdf |
| dehghani2019 | recurrence in depth with per-position halting | verified | §2.2 dynamic per-position halting; variable per-symbol depth; dehghani2019.pdf |
| giannou2023 | looped Transformers with shared parameters | verified | abstract: iterative algorithms mapped to programs executed by a looped 13-layer Transformer; giannou2023.pdf |
| geiping2025 | a recurrent-depth model improves as it unrolls at test time, without more tokens | verified | abstract: unrolling a recurrent block to arbitrary depth at test time; reasoning "not easily represented in words"; 3.5B parameters; geiping2025.pdf |
| kohli2026 | depth extrapolation by scaling inference-time recurrence; dynamic recurrence extrapolates further; overthinking degrades predictions | verified | abstract; §6 on training strategies ("dynamic recurrence achieving the best extrapolation"); overthinking in the abstract and §6; kohli2026.pdf |
| chen2026 | a silent objective supervising only the final step stabilizes recurrence over twenty steps; intermediate supervision teaches shortcuts; the computational frontier | verified | abstract and §1, contributions 1--3 and the frontier; under 1M parameters; chen2026.pdf |
| hao2024 | continuous chain of thought: last hidden state fed back as input | verified | abstract and Fig. 1; "rather than prematurely committing to a single" next step; hao2024.pdf |
| voita2020 | MDL probing charges for probe complexity; per-layer form | verified | §2.3 on total codelength; per-layer results for ELMo layers 0--2 in §4; voita2020.pdf |
| alain2016 | linear probes on intermediate layers | verified | abstract and §1; alain2016.pdf |
| belinkov2022 | the methodological problems of probing | verified | title and §1: promises, shortcomings, advances; control tasks; belinkov2022.pdf |
| zou2023 | internal states are readable top-down | verified | abstract and §"Representation Reading": top-down transparency; zou2023.pdf |
| park2024 | representations of many features are linear | verified | §1: the linear representation hypothesis formalized; park2024.pdf |
| lanham2023 | episodes where chain of thought does not match the process | verified | abstract: early answering and adding mistakes; larger models less faithful on most tasks; lanham2023.pdf |
| turpin2023 | unfaithful explanations in chain-of-thought prompting | verified | abstract and Table 1: unfaithful CoT explanations under biasing features; turpin2023.pdf |
| roger2023 | models can hide information in generated text | verified | abstract: encoded reasoning, steganography in generated text; roger2023.pdf |
| schrimpf2021 | model states predict human brain responses to the same text | verified | abstract: transformer models predict nearly 100% of explainable variance in neural responses to sentences; schrimpf2021.pdf |
| goldstein2022 | shared computational principles between humans and deep language models | verified | abstract: three shared principles, including continuous next-word prediction before word onset; goldstein2022.pdf |
| caucheteux2022 | brains and algorithms partially converge | verified | abstract: language algorithms partially converge toward brain-like representations; caucheteux2022.pdf |

Counts: 158 keys. 153 verified (52 against the full text, 6 against the PubMed abstract, 8 by full-text search
inside the scanned book, 1 by metadata, 1 secondary), 2 substitutes that were read, 3 obtained without a
locus (Ayer, Solomonoff I, Muggleton), 2 without any copy (Gardner 1983, Clark 1998).

## What the verification changed

1. Lad et al.: the draft said adjacent layers inside a stage are robust to deletion and swapping. The paper says the
   middle layers are robust and the first and last are not, with deletion in the detokenization stage catastrophic.
   The sentence in S3a now says that.
2. Nogueira et al.: the draft said scaling improves arithmetic slowly. The paper says larger models do better and
   that even a 3B model fails to extrapolate beyond the trained digit range. The sentence in S2a now says that.
3. Turing 1936 was cited for "any computable function has unboundedly many implementations", which is not a claim of
   that paper. A24a now cites it for universality and states the multiplicity as the corollary.
4. Perky 1910 is now cited for the Perky effect itself rather than for "imagery is dimmer than sight".
5. `arXiv:2603.21676` was first dropped as unfindable, which was my error: the paper exists (Chen 2026, "Thinking
   Deeper, Not Longer"), the download had failed, not the search. It is back in S3c and in the frames, verified
   against the file, with the scale of the experiments stated, since it is a sub-megabyte model and not an LLM.

## Procedure for the two remaining rows

(1) find an open copy (author page, arXiv, PhilPapers, Internet Archive, publisher OA); (2) save it as
`sources/<key>.pdf` or `.html`; (3) read the passage that carries the claim in the column above; (4) set the status
and the locus; (5) if the source does not support the claim, mark `not-supporting` and change the sentence in the
section file that cites it. A `substitute` row has to end either as a citation of what was read or as a copy of the
original. `sources/*.abstract.txt` hold the PubMed abstracts used for the six paywalled articles, with PMIDs. `sources/webb2015.pdf`
was downloaded by the verification agents and is not cited by the current text.
