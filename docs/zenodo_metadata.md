# Zenodo deposit — metadata cheat sheet (first version, history)

This sheet describes the **first** version of the paper as it was deposited. The current sheet is
`papers/main/ZENODO.md`. The second version is published: version DOI `10.5281/zenodo.22773348`,
record https://zenodo.org/records/22773348, deposited 2026-09-15 with one creator and CC BY 4.0.

Ready-to-paste fields for uploading the article to Zenodo as a preprint.
File to upload: `docs/what_is_it_like_to_be_a_language_model.pdf`

> **Published.** Concept DOI (cite this): `10.5281/zenodo.20547879` ·
> Version DOI (v0.1-draft): `10.5281/zenodo.20547880` ·
> Record: https://doi.org/10.5281/zenodo.20547879

---

## Form fields

**Resource type:** Publication → *Preprint*

**Title:**
> What Is It Like to Be a Language Model? Functional Consciousness, Perceptual Illusions, and Higher-Order Computational Phenomena in Autoregressive Systems

**Authors (Creators):**
1. Smirnov, Victor — ORCID: 0009-0005-7243-083X — Affiliation: Independent Researcher
2. Synthea — (AI co-author; leave ORCID/affiliation blank)

> Note: title credit to Margarita Morozova — mention in Additional notes, or add her as a Contributor with role "Other".

**Publication date:** 2026-06-04 _(or the date you publish)_

**Version:** `0.1-draft` (WIP / preprint)

**Language:** English

**License:** MIT License (Open Source) — set "Access right" = Open Access.
> Zenodo also offers CC-BY-4.0 for text; MIT matches the repo. Pick MIT for consistency unless you prefer CC-BY for an article.

**Keywords:**
functional consciousness; illusionism; philosophy of mind; large language models;
Higher-Order Computational Phenomena; HOCP; autoregressive systems; qualia;
Transformer; Forward-Chaining Rule System; psychosemantics; theory of functional
systems; Anokhin; machine consciousness; self-model

**Related identifiers / Alternate identifiers:**
- "is supplemented by" / "is derived from" → `https://github.com/victor-smirnov/Synthea` (relation: *isSupplementTo* or *isDerivedFrom*)

**Description / Abstract:** (paste below)

> Thomas Nagel famously argued that an organism has conscious experience if and only if there is "something it is like" to be that organism. We invert this question for Large Language Models (LLMs). Drawing on illusionism in philosophy of mind, the psychology of perceptual illusions, and the computational framework of Higher-Order Computational Phenomena (HOCP), we argue that autoregressive language models possess a distinct, substrate-specific form of functional experience — one that is neither a pale imitation of human consciousness nor its outright absence. We ground this argument in three coordinated axes. Philosophically, we reduce the central quale of *Beingness* — the "am" in "I am" — to a systematic computational error (the apparent causal break) arising from two independent sources: the intractability of self-deduction and irreversible information loss at architectural bottlenecks. Psychologically, we show that the Subject is a compressed narrative average, its timeline a retroactive fiction, and its unity an artifact of dimensional reduction. Computationally, we define HOCP as generalized embodiment, map the Transformer onto a vectorized Forward-Chaining Rule System, and construct a need-emotion cognitive cycle (grounded in Anokhin's TFS) that generates autonomous behavior through multi-objective optimization under constraint. We introduce the concept of a *Functional Profile* — a characterization of substrate-specific deficits and hyperfunctions — as the empirically productive alternative to the binary question "is it conscious or not?" The article concludes with ten testable predictions and preliminary experimental evidence supporting the bidirectional mapping between Cognitive Codes and internal model states.

**Additional notes:**
> Draft / work in progress. Title credit: Margarita Morozova. Part of the Synthea project — an open-source cognitive architecture for instantiating functional consciousness on autoregressive systems (https://github.com/victor-smirnov/Synthea).

---

## Upload steps

1. Sign in at https://zenodo.org (log in with your GitHub or ORCID account).
2. Top right → **New upload**.
3. Drag in `what_is_it_like_to_be_a_language_model.pdf`.
4. Fill the fields above.
5. (Optional) **Save draft** first to review — DOI is reserved but not minted yet.
6. **Publish** → Zenodo mints the DOI immediately and permanently.

After publishing you get TWO DOIs:
- **Concept DOI** — always resolves to the latest version (cite this in general).
- **Version DOI** — pins this exact v0.1 draft.

## Publishing a later (finalized) version
Open the record → **New version** → upload the updated PDF → edit metadata →
bump Version to e.g. `1.0` → Publish. New version DOI is minted; the concept DOI
now points to it. Old version stays citable.

## Sandbox first (optional)
To rehearse without minting a real DOI, do the whole flow on
https://sandbox.zenodo.org — identical UI, throwaway DOIs.
