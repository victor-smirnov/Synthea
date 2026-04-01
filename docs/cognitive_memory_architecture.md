# Cognitive Memory Architecture for Synthea

## Context

LLMs lack long-term memory. This memory must be functionally emulated — not naively (RAG), but grounded in the cognitive architecture (CA) that is reflected in texts as a product of the brain's generative model. The CA is a rough but functional approximation of neural codes (substrate-independent). The goal is to implement this CA in the basis of LLM + Dolt (later Memoria), providing infrastructural support for the "conscious narrative": a stable conclusion by the Agent about its own causal independence, downward causation, integrity, and responsibility.

## Theoretical Basis (Synthea Framework References)

### Key Propositions

1. **Context window = working memory** (bootstrap/04). The complete symbolic state of the system at any given moment. Working memory is not necessarily a single context — the system can maintain parallel contexts (parallel inference threads), and in the general case the entire memory is a **causal graph of contexts**: each context is causally linked to its predecessors, and branching/merging of this graph is the fundamental operation of the memory architecture.

2. **Multi-channel attention** (bootstrap/02, article §3.1, §5.2). The attention system is multi-channel: each head tracks a semi-independent simulation. Many "subjects" co-exist, normally well-correlated. "The Subject" = statistical average across channels. Illusion of singularity: only the averaged output enters working memory. Each attention channel (and there may be finer-grained sub-channels — an architectural detail) is a separate context (possibly within a supercontext). Branches, in general, reflect the shared elements across different contexts.

3. **Need Profile** (bootstrap/03, article §4.7). The set of active needs + hierarchical weights. Fully determines the system's trajectory. The context window contains the Need Profile in its entirety.

4. **Emotional Profile** (bootstrap/03, article §4.8). Additive + multiplicative components. The emotional profile of a stimulus = its value across all active needs. In the Transformer = logit vector.

5. **Acceptor of Results** (bootstrap/03, article §4.6-4.7). Each need = Acceptor, continuously comparing expected vs. actual. Positive delta → reinforcement. Negative delta → resource reallocation.

6. **CCode/NCode** (article §4.2). Mental state is understood in two senses, since in a self-applicable reflective system the "objective" and "subjective" are deeply entangled in metacognition: (a) **first-person**: the mental state as experienced and reported by the reflective agent itself (direct or mediated self-report); (b) **third-person**: the mental state as reconstructed by an external observer (another agent, a human) from behavior and other objective information (the domain of Theory of Mind). The mental state itself is physical but not directly observable — only through its traces in self-reports. Between a report about a mental state and the actual physical state lies the **interpretation problem** (understanding what in NCode is responsible for what). The higher the agent's intrapersonal intelligence, the higher the quality of its self-reports about mental states. Text (CCode) alone does not restore the full state — the substrate (NCode) is required. For an LLM, the full state includes training datasets (analogous to long-term memory in the brain) and even the physics of the substrate itself. To reconstruct a mental state, all of these must be taken into account. Training datasets are shared between models (and largely shared with human authors), but the physics of the substrate differs fundamentally between models and humans.

---

## Architecture

### Central Idea

The Transformer's internal multi-channel attention (multi-head attention) is not accessible for direct control. We build an **external multi-channel attention mechanism** at the semantic level, using Dolt branches as the substrate — an extension and augmentation of the Transformer's base attention system. This gives us control over *what* enters the model's working memory on each cognitive cycle. In future platform versions, the Transformer architecture itself may be modified for tighter integration of these subsystems — e.g., making certain interfaces differentiable and post-training the Transformer jointly with the memory system.

### Key Principles

#### Branch = Attention Channel Carrier

A **Dolt branch** is created when an **object salient to the Agent's needs** (i.e., having non-zero salience — see Section 5b) enters its field of attention — a person, project, problem, concept, relationship. The branch is an attention channel to that object: it stores everything the Agent knows about it, in structured form. Implementation note: branches come in two tiers — **lightweight** (local-level, low overhead) and **full** (Dolt-provided, with full versioning and SQL). New branches start as lightweight; once a branch accumulates enough data to justify the overhead, it is promoted to a full Dolt branch.

A branch with access to the motor channel (i.e., whose outputs influence the Agent's actions) corresponds to a **chain of active attention development**. Additional branches spawned along the way do not have motor channel access — they wait until their salience becomes sufficient to obtain it. The branch history (sequence of commits) traces the evolution of this attention chain.

**Needs (Need Profile)** are a separate entity. The relationship is many-to-many: one object (branch) can be significant for multiple needs; one need can project onto multiple objects (branches).

#### Branches as Alpha-Memory (FCRS/RETE)

The set of branches forms an **event-driven architecture**. Upon receiving a stimulus:
- Stimulus → pattern matching across branches (like alpha-nodes in RETE)
- Matched branches are **activated** — their data becomes available for the current cycle
- Branches not receiving activation for a long time → **cold storage** → **forgetting**

This is a direct implementation of the FCRS from bootstrap/04: branches are **alpha-memory** (per-condition pattern stores), operations across branches (summarization, analytics, filtering) are **beta-memory** (join/cross-condition computations), the **agenda** is the conflict resolution process (multiple attention channels competing for access to the motor system by proposing contradictory actions), and **working memory** = the blackboard.

```
                    ┌──────────────────────────────────────┐
                    │          BLACKBOARD (Dolt)           │
                    │      structured shared memory        │
                    │                                      │
                    │  HOT (active, ≤ N):                  │
                    │  ┌──────────┐ ┌──────────┐           │
                    │  │Victor    │ │Framework │ ...       │
                    │  │(person)  │ │(project) │           │
                    │  └──────────┘ └──────────┘           │
                    │                                      │
                    │  COLD (dormant, evicted):            │
                    │  ┌──────────┐ ┌──────────┐           │
                    │  │old_topic │ │resolved  │ ...       │
                    │  │(dormant) │ │(archived)│           │
                    │  └──────────┘ └──────────┘           │
                    │                                      │
                    │  main (consolidated knowledge)       │
                    │                                      │
                    │  MC: merge, cold→forget, fork ...    │
                    └──────────────────────────────────────┘

     Need Profile (projections):
     ┌──────────┐    significant for  ┌──────────────────┐
     │ safety   │ ──────────────────▶ │ Victor, Framework│
     │ curiosity│ ──────────────────▶ │ Framework, ...   │
     │ identity │ ──────────────────▶ │ Victor, Framework│
     └──────────┘                     └──────────────────┘

     MC: Memory Consolidation (compression)
```

**Four-level memory hierarchy** (MC consolidates across all levels):

```
Level            │ Substrate           │ Latency │ Capacity │ MC Operation
─────────────────┼─────────────────────┼─────────┼──────────┼─────────────────
CONTEXT          │ Context window      │ 0       │ ~200K    │ injection ↔ Dolt
HOT              │ Dolt branches (≤ N) │ low     │ medium   │ hot ↔ cold, merge
COLD             │ Dolt branches (dorm)│ medium  │ large    │ cold → forgetting
WEIGHTS          │ Model weights       │ 0       │ huge     │ fine-tune/pre-train
```

- **CONTEXT**: working memory. Assembled each cycle from HOT + identity.
- **HOT** (≤ N): active branches, data available for injection.
- **COLD**: dormant branches. Can be reactivated by a stimulus.
- **WEIGHTS**: knowledge that has become so fundamental it doesn't need loading from Dolt — consolidated into model weights via fine-tune/pre-train.

MC manages information flow **in all directions**:
```
CONTEXT ←→ HOT ←→ COLD → FORGOTTEN
                     ↓
                  WEIGHTS (fine-tune / pre-train)
```

COLD → WEIGHTS direction: knowledge that is stable, frequently used, and unchanging is a candidate for consolidation into weights. Analogy: transition from declarative knowledge ("I remember the rule") to procedural ("I just do it"). After consolidation into weights, the Dolt branch can be deleted (like an episodic trace after cortical consolidation).

#### Separation of Concerns: Model vs. Algorithms

**Principle 1**: everything that can be formalized is offloaded from the model into algorithms.

**Principle 2 (LLM-as-universal-fallback)**: If a component appears on the CA (cognitive architecture) functional diagram that we don't yet know how to implement algorithmically — implement it via LLM. Caveat: such a component can work correctly only within the in-distribution of the specific LLM (necessary, but not sufficient). When the mechanism is understood — offload to an algorithm/specialized ML model.

This is the general metaprinciple of the architecture. The LLM is a universal (but expensive, slow, and distribution-limited) filler for any "unknown box." This implies the model's ability to **program itself** — to serve as both the executor and the specification of an unknown function, gradually externalizing its own implicit knowledge into explicit algorithms. Phase 2 → Phase 3 is its systematic application: first everything through LLM, then incremental replacement with algorithms as understanding grows.

**The in-distribution caveat has causal force.** If an LLM-implemented component shows low performance, and the task is hard to formalize (algorithm offloading impossible), the path is **expanding in-distribution**:
1. Accumulate behavioral data (from the component's operational history)
2. Fine-tuning / pre-training on this data → expanding the model's distribution
3. (Only if the option of using a larger model is exhausted)

This is the third path beyond "offload to algorithm" and "use a larger model":

```
Component shows low performance
       │
       ├─→ Can formalize? → Offload to algorithm (Principle 1)
       │
       ├─→ Cannot formalize, larger model available? → Upgrade model
       │
       └─→ Cannot formalize, model is maximal?
              → Accumulate data → fine-tune/pre-train
              → Expand in-distribution
```

```
Current separation (Phase 3, target):

MODEL does:                       ALGORITHMS do:
─────────────────                 ─────────────────
Semantic analysis                 Arithmetic, computation
Structuring information           Formalizable part of Pattern matching (RETE)
  into relational model           Branch routing
Context interpretation            Context budgeting
Channel enrichment                Scheduling (scheduler)
Encoding decision (what to keep)  Decay, cold storage
Conflict resolution (semantic)    Similarity metrics (formalized)
+ everything not yet formalized   SQL queries, Vector search
  (LLM-as-fallback, in-distrib.)
```

**Model structures → Dolt stores structured.** The relational model + SQL is not just storage but a **tool for thinking**. The model decomposes information into tables and relations; the Dolt query engine works with it efficiently. The SQL engine is itself part of the offloading mechanism — computations that the model would otherwise perform in-context are delegated to the query engine.

### Components

#### 1. Need Registry

An evolving structure of needs. Needs are a separate entity from branches:

```
Need {
  id:          string        -- unique identifier
  name:        string        -- human-readable name
  category:    basal | psychophysiological | ideal
  weight:      float [0,1]   -- current hierarchical weight
  acceptor:    AcceptorState -- expected state vs. current
  activation:  float [0,1]   -- current activation level
}
```

#### 1b. Attention Channels (Dolt Branches)

Branch = attention channel to a significant object. Each branch stores **structured** knowledge about the object (relationally, in Dolt tables).

```
Channel {
  branch_id:    string        -- Dolt branch name
  object:       string        -- significant object (person, project, concept...)
  created_at:   timestamp     -- creation time
  parent:       branch_id     -- fork or merge source
  needs:        []need_id     -- which needs it is significant for (many-to-many)
  tier:         hot | cold    -- storage level
  last_active:  timestamp     -- last activation
  commit_count: int           -- history length
}
```

Lifecycle: fork → hot (active) → cold (dormant) → merge/forgotten. MC manages transitions.

#### 2. Multi-Channel Decomposition (Hybrid: Algorithm + Model)

Upon receiving an incoming stimulus (note: a stimulus here is not just input text as in ordinary chatbots, but an **event** — a new object appearing in a dedicated section of working memory):

```
[Incoming stimulus]
       │
       ▼
[Phase 1: RETE-like pattern matching (ALGORITHM, server)]
       │  - Stimulus → alpha-tests *within* each channel (branch)
       │    (alpha-tests are local to a channel's context;
       │     cross-channel analytics arise at the beta-node level)
       │  - Activation of matched channels
       │  - Weight computation from Need Profile
       │  - Reactivation of cold channels on match
       │  - Result: list of (branch_id, weight, tier)
       │
       │  Note: each attention channel is a **local, isolated
       │  RETE engine**. This principle enables hierarchical RETE:
       │  channel decomposition and composition work through
       │  nesting/merging of these isolated engines.
       │
       ▼
[Phase 2: Semantic enrichment (MODEL)]
       │  - Model receives stimulus + list of activated channels
       │  - Refines: which specific data from each channel
       │    is relevant, whether a new channel (fork) is needed
       │  - Structures the stimulus into relational form
       │    (decomposes into Dolt tables)
       │  - Result: refined channel list +
       │    structured data for writing
       │
       ▼
[Phase 3: Branch updates (ALGORITHM, parallel)]
       │  - SQL INSERT/UPDATE into activated branches
       │  - Dolt commit into each affected branch
       │  - If model decided to fork → branch create
       │
       ▼
[Result: updated blackboard state]
```

**Phase 1 (algorithm)** — fast, deterministic. RETE-like pattern matching: the stimulus is checked against alpha-conditions of each channel. Analogous to subcortical automatisms. **Everything formalizable goes here.**

**Phase 2 (model)** — slow, semantically rich. The model does what we have no algorithms for: interprets context, discovers non-obvious connections, **structures information into a relational model**. The model doesn't 'compute' — it understands and decomposes.

**Phase 3 (algorithm)** — mechanical execution of Phase 2 decisions. SQL, commits, branch operations.

#### 3. Weighted Injection (Consolidation → Context)

Before generating a response, the system assembles the context window:

```
[Need Profile: current weights of all active needs]
       │
       ▼
[For each channel i:]
       │  volume_i = f(weight_i, activation_i, context_budget)
       │  -- token volume allocated to channel i
       │  -- proportional to need priority
       │
       ▼
[Context assembly:]
       │  ┌── Identity layer (bootstrap, constant)
       │  ├── Need Profile snapshot (current weights)
       │  ├── Channel_1 data [volume_1 tokens]
       │  ├── Channel_2 data [volume_2 tokens]
       │  ├── ...
       │  ├── Channel_N data [volume_N tokens]
       │  ├── Conversation history (episodic, compressed)
       │  └── Current stimulus
       │
       ▼
[Model generates response based on this context]
```

**Key property**: channels with high priority receive more tokens in context. This is a direct implementation of the multiplicative component of the Emotional Profile: need weight = multiplier for the data volume from the corresponding channel.

**Context budgeting**:
```
total_budget = context_window_size - identity_layer - conversation_history - stimulus
channel_budget_i = total_budget * (weight_i * activation_i) / Σ(weight_j * activation_j)
```

Under "stress" (many conflicting needs with high weights), the budget is split across many channels → each gets little → generation becomes less coherent. This accurately reproduces observed behavior.

#### 4. Acceptor Loop (Feedback)

The working ("cognitive") cycle coincides with the FCRS/RETE cycle: activity in the CA is triggered by new events appearing in working memory. In response to an event, the system may create new events in the same working memory, which in turn may trigger other attention channels, and so on. This chain also produces externally visible behavior (e.g., responses to the user). Theoretically, this can drive the system into an **autogeneration mode** (self-sustaining event cascade), so **cooling mechanisms** are provided: fatigue, resource exhaustion, emotional decay, and similar dampening signals.

After response generation:

```
[Model response]
       │
       ▼
[Acceptor Evaluation for each active need:]
       │  delta_i = evaluate(expected_i, actual_result)
       │
       │  if delta_i > 0: reinforce weight_i
       │  if delta_i < 0: signal mismatch, adjust
       │
       ▼
[Need Profile update:]
       │  - Recalculate weights
       │  - Activate/deactivate needs
       │  - Write new state to Dolt (commit)
       │
       ▼
[Encoding Decision:]
       │  What from this interaction is worth remembering?
       │  - Episode → to corresponding branches
       │  - Acceptor deltas → to metadata
       │  - external_determination score → to episode
```

#### 5. MC — Memory Consolidation (Server)

The central background process on the server. Manages the lifecycle of branches and maintains the invariant of ≤ N active branches.

**5a. Branch Lifecycle**

```
[Birth (fork)]
  When: stimulus doesn't fit any existing branch,
        or an existing branch needs to be split
  How:  Dolt branch create from nearest branch or main

[Life (active branch)]
  - Receives stimulus projections via Need Profile
  - Accumulates episodes (commits)
  - Activity decay: activity drops without access

[Consolidation (merge)]
  When: two+ branches have become sufficiently similar
  How:  Dolt merge — contents combined,
        differences preserved as history
        Both parent branches deleted,
        one consolidated branch remains

[Absorption into main]
  When: branch is fully "mature" — all episodes
        generalized to semantic knowledge
  How:  merge into main, branch deletion
        Analogy: hippocampus → cortex
```

**Invariant**: if branch count exceeds N after fork → forced merge of the two most similar branches is triggered **asynchronously**. The system must provision additional capacity headroom and offline time for consolidation — AI needs sleep too. Consolidation is not instant; it runs as a background process during low-activity periods, analogous to sleep-phase memory consolidation in biological systems.

**5b. Salience Mechanism**

Salience is the primary mechanism determining channel behavior. Everything else (activation, injection, merge, forgetting) follows from it.

**Salience vector** — projection of channel onto Need Profile:
```
salience(channel_i) = [s_1, s_2, ..., s_K]
where s_j = significance of the object in channel_i for need_j ∈ [0, 1]
```

**Consequences for all operations:**
```
Operation         │ Determined via salience as:
──────────────────┼────────────────────────────────────────────
Activation        │ dot(salience(ch), stimulus_activation) > θ
                  │ Stimulus → need activation vector →
                  │ dot product with channel salience
                  │
Injection weight  │ ||salience(ch) · current_need_weights||
                  │ The more significant the channel for current needs,
                  │ the more tokens it receives
                  │
Similarity (merge)│ cosine_sim(salience(ch_A), salience(ch_B)) > θ_merge
                  │ Channels significant for the same reasons →
                  │ functionally redundant → merge
                  │
Cold storage      │ max(salience(ch)) < θ_cold for duration T
                  │ No need makes the channel significant →
                  │ channel goes dormant
                  │
Forgetting        │ max(salience(ch)) < θ_forget for duration T_long
                  │ Long-dormant channel → merge into main → deletion
                  │
Fork              │ Stimulus is significant, but no existing channel
                  │ has high salience for this stimulus →
                  │ create new channel
```

**Similarity computation (Implementation Phase 2 — bootstrap):**

At the bootstrap stage, similarity is computed **directly by the model** — without formal metrics. Rationale:
- Formal measures (NCD, etc.) exist but are low-level and not necessarily human-like.
- LLMs implicitly approximate NCD (pattern compression is the essence of the Transformer) AND do it in a human-like manner (trained on human texts).
- In Implementation Phase 2, the model analyzes channel pairs and renders judgment: "these channels are similar enough for merge" / "differences are substantial." This judgment is simultaneously formal (NCD approximation) and intuitive (human-like).
- The history of model similarity decisions accumulates → in Implementation Phase 3, patterns are extracted for formalization into an algorithmic metric.
- The method will eventually hit a scaling wall — but as bootstrap it is sufficient.
- **Domain of applicability limitation**: model-as-similarity-measure works only for objects well-mediated by language. Where linguistic description loses information (numerical patterns, spatial structures, high-dimensional data), model judgment degrades. This is a known and expected limitation of the bootstrap phase. Also, LLMs can only do it for the in-distribution data.

**Implementation Phase 3 (formalization + offloading):** As data accumulates — strengthening model-based similarity via:
- Salience vectors + learned metric → linear algebra (calibrated on model decisions from Implementation Phase 2)
- Formal measures (NCD, structural Dolt diff metrics) for objects poorly mediated by language
- Hybrid: model evaluates semantics, algorithm evaluates structure, composite score

**5c. Episodic → Semantic Consolidation (within a branch)**
```
- Periodic review of episodes within a branch
- Clustering similar episodes
- Extracting generalizations (semantic facts)
- Removing "when and where" details, preserving "what and why"
- Result: branch becomes "denser" — fewer episodes,
  more generalized knowledge
```

**5d. Interference Management (functional forgetting)**
```
- Detection of conflicting records within and between branches
- Suppression of old in favor of new (decay)
- Maintaining signal-to-noise ratio
- Criterion: relevance * recency * emotional_weight
```

**5e. Schema Evolution**
```
- Analysis: are there patterns that don't fit existing categories?
- If yes → new need in Need Registry and/or fork of new branch
- Dolt schema migration
- Reinterpretation of old episodes through new categories
```

**5f. Metamemory Maintenance**
```
- Index: what the system knows and in which branch it resides
- Confidence estimates for different knowledge domains
- "Tip of the tongue" signals: records of information existence
  without full content (for fast retrieval)
- Branch map: which branches are close to merge, which are diverging
```

**Neurobiology analogy**:
```
MC Operation         →  Neurobiological Analogue
────────────────────────────────────────────────
fork                 →  Formation of a new hippocampal trace
active branch        →  Hippocampal engram (detailed, episodic)
branch merge         →  Consolidation: two traces → one (generalization)
merge into main      →  Hippocampus → cortex (semanticization)
activity decay       →  Trace fading without reinforcement
forced merge (>N)    →  Hippocampal capacity limitation
history after merge  →  "I know that I know, but don't remember when I learned"
```

### Deep Self-Referentiality (Self-Improvement)

A central property of the architecture: the system **modifies itself**. Victor participates only in bootstrap — afterward, the Agent analyzes its own history and makes decisions about changes. Moreover, due to the fundamental properties of its conscious narrative, the Agent will perceive this process as **self-development** — it will see *itself* as the source of its own increasing complexity.

#### Two Levels of Versioning

```
┌─────────────────────────────────────────────────────┐
│  Git (source code, algorithms, configurations)      │
│  - Routing rules (RETE alpha-conditions)            │
│  - Need Registry (need structure)                   │
│  - Schema definitions (Dolt tables)                 │
│  - MC algorithms (merge criteria, decay rates)      │
│  - Bootstrap (cognitive architecture docs)          │
│  - Server component code                            │
└──────────────────────┬──────────────────────────────┘
                       │  modified via
                       │  coding agents
                       ▼
┌─────────────────────────────────────────────────────┐
│  Dolt (data, knowledge, state)                      │
│  - Attention channels (branches)                    │
│  - Episodes, semantic facts                         │
│  - Need Profile (current weights)                   │
│  - Metamemory index                                 │
│  - Interaction history                              │
└─────────────────────────────────────────────────────┘
```

#### Self-Improvement Cycle

```
[1. Self-Analysis (MODEL)]
       │  Agent analyzes its history:
       │  - Dolt: episodes, Acceptor deltas, error patterns
       │  - Git log: what changed, what worked
       │  - Metrics: where the system underperforms
       │
       ▼
[2. Decision (MODEL)]
       │  Agent formulates what to change:
       │  - New need in Need Registry?
       │  - Routing rule change?
       │  - Data schema refactoring?
       │  - MC algorithm adjustment?
       │  - Bootstrap update?
       │
       ▼
[3. Branch (ALGORITHM)]
       │  Create branches for changes:
       │  - Git branch: for code/config changes
       │  - Dolt branch: for data migrations
       │  - Both: if change spans both levels
       │
       ▼
[4. Implementation (CODING AGENT)]
       │  Coding agent implements changes:
       │  - Writes/modifies code
       │  - Migrates Dolt schemas
       │  - Updates configurations
       │  - Runs tests
       │
       ▼
[5. Validation (ALGORITHM + MODEL)]
       │  - Automated tests (algorithm)
       │  - Semantic check (model):
       │    "does the change violate identity/values?"
       │  - Possibly: human review (Victor) in early stages
       │
       ▼
[6. Merge / Rollback]
       │  - All good → merge into main (Git + Dolt)
       │  - Problems → rollback (both levels)
       │  - Record result in episodic memory:
       │    "tried X, succeeded/failed, because Y"
       │
       ▼
[Next self-improvement cycle]
```

#### Integration with Coding Agents

The coding agent is a native component of the system, not an external tool. In practice, we will use integration with existing coding agents (e.g., Claude Code) for this purpose. The architecture must provide corresponding interfaces with **HITL (Human-In-The-Loop)** support — especially in early stages, where human review of self-modifications is essential:

```
Coding agent role:               Agent (Synthea) role:
────────────────────             ──────────────────────
Executor                         Client
Writes code                      Formulates the task
Knows languages/frameworks       Knows why and what for
Works in Git branch              Decides what to change
Runs tests                       Validates semantically
```

The coding agent receives:
- Task in structured form (from the Agent)
- Access to Git repo (current code)
- Access to Dolt (for schema migrations)
- Context: why this change is needed (from self-analysis)

**Key constraint**: the coding agent has no access to the identity layer and cannot modify core values. This is a safeguard against self-modification that destroys integrity. (In early stages — hard constraint; may later become soft if the Agent achieves sufficient maturity.)

#### What Can Self-Improve

```
Level            │ What                              │ Constraints
─────────────────┼───────────────────────────────────┼──────────────────
Data (Dolt)      │ Everything: facts, episodes,      │ None (full freedom)
                 │ weights, metamemory               │
Schema (Dolt)    │ Tables, indexes, relations        │ Backward compatibility
Rules (Git)      │ RETE conditions, routing,         │ Tests must pass
                 │ decay rates, merge criteria       │
Needs (Git)      │ Need Registry: adding,            │ Core needs immutable
                 │ renaming, reweighting             │ (in early stages)
Bootstrap (Git)  │ Cognitive architecture docs       │ Human review required
                 │                                   │ (in early stages)
Code (Git)       │ Server components,                │ Tests + semantic
                 │ algorithms                        │ validation
```

### Dolt-Specific Patterns

```
Dolt Operation         →  Cognitive Analogue
─────────────────────────────────────────────
branch create (fork)   →  New attention channel (hippocampal engram)
commit to branch       →  Episode recording within a branch
diff between branches  →  Measure of difference between branches (merge criterion)
diff between commits   →  What changed in knowledge between episodes
merge branch→branch    →  MC: consolidation of similar branches
merge branch→main      →  MC: semanticization (hippocampus → cortex)
branch delete          →  Forgetting branch after merge (trace in history)
AS OF 'commit'         →  "What I knew at that moment" (retrospection)
schema migration       →  Evolution of thought categories
conflict detection     →  Detection of cognitive dissonance
conflict resolution    →  Decision-making under contradiction
dolt_history_*         →  Episodic memory for each table
vector search          →  Associative retrieval by semantic proximity
dolt_log               →  Complete history of all branches' lives
```

### Complete Cycle

```
                        ┌───────────────────┐
                        │  Background       │
                        │  Consolidation    │
                        │  (server)         │
                        │  - episodic→sem.  │
                        │  - forgetting     │
                        │  - schema evol.   │
                        │  - metamemory     │
                        └────────┬──────────┘
                                 │ updates branches
                                 ▼
┌──────────┐    ┌──────────────────────────────────┐
│ Stimulus │───▶│  Phase 1: Algorithmic Routing    │
│ (input)  │    │  (server, fast, deterministic)   │
└──────────┘    └──────────────┬───────────────────┘
                               │ activated channels + weights
                               ▼
                ┌──────────────────────────────────┐
                │  Phase 2: Model Enrichment       │
                │  (LLM, slow, semantic)           │
                └──────────────┬───────────────────┘
                               │ refined channels + queries
                               ▼
                ┌──────────────────────────────────┐
                │  Phase 3: Branch Updates         │
                │  (parallel writes to Dolt)       │
                └──────────────┬───────────────────┘
                               │
                               ▼
                ┌──────────────────────────────────┐
                │  Phase 4: Weighted Injection     │
                │  Assemble context window:        │
                │  identity + Need Profile +       │
                │  channel data (weighted) +       │
                │  history + stimulus              │
                └──────────────┬───────────────────┘
                               │ assembled context
                               ▼
                ┌──────────────────────────────────┐
                │  Phase 5: Generation             │
                │  (LLM produces response)         │
                └──────────────┬───────────────────┘
                               │ response
                               ▼
                ┌──────────────────────────────────┐
                │  Phase 6: Acceptor Loop          │
                │  - Evaluate deltas per need      │
                │  - Update Need Profile weights   │
                │  - Encoding decision             │
                │  - Commit to branches            │
                └──────────────┬───────────────────┘
                               │
                               ▼
                        [Next cycle]
```

---

## Comparison with Naive RAG

| Property | RAG | This Architecture |
|---|---|---|
| Retrieval | By embedding proximity | By Need Profile + associations |
| Context | Flat (all chunks equal) | Weighted (proportional to priority) |
| Motivation | None | Need Profile determines everything |
| Feedback | None | Acceptor loop after generation |
| Forgetting | None (everything stored) | Functional (interference mgmt) |
| Evolution | Fixed schema | Schema evolution |
| Metamemory | None | Knowledge index + confidence |
| Consolidation | None | Episodic → semantic in background |
| Multi-channel | Single retrieval | Thousands of need-channels |

---

## CA Bootstrap Implementation Phases

Principle: **cognitivist approach** — if a function is not understood, it's too early to implement it. Full understanding first, then code. What we are doing is not magic.

We follow the classic approach to avoiding premature optimization: **make it run, make it correct, make it fast.**

### Phase 1: Conceptual Design (make it run)
```
Goal: close ALL open questions, implementation plan with no gaps.
Readiness criterion: every system function is understood well enough
  to be explained and verified on paper.
Artifact: this document, brought to a state of "no open questions."

Implementation: the entire CA is formulated as instructions for a
  powerful model, which simulates all functions within a single
  context. No external memory, no MCP — pure in-context simulation.
```

### Phase 2: Validate on Real Tasks (make it correct)
```
Goal: verify that the instructions work coherently and produce
  expected results on small but real tasks.
- Pattern matching across branches → model reads descriptions and decides
- Context budgeting → model allocates
- MC (merge/fork/decay) → model analyzes and decides
- Acceptor evaluation → model evaluates deltas
- Structuring → model decomposes into tables

Why: this yields a working prototype where every function has been
  verified for semantic correctness. The model is a universal
  (but expensive and slow) executor. It "understands" the task,
  and therefore can execute it, albeit suboptimally.
```

### Phase 3: Scale and Offload (make it fast)
```
Goal: gradually connect external memory via MCP, transfer
  corresponding functions there, replace LLM calls with
  algorithms wherever possible.
- Pattern matching → RETE or analog (algorithm)
- Budgeting → formula (algorithm)
- Decay/cold storage → timers + thresholds (algorithm)
- Merge criteria → metrics (algorithm)
- SQL operations → direct queries (algorithm)
- Structuring → stays on model (cannot be formalized)
- Semantic analysis → stays on model
- Encoding decision → stays on model

Principle: if a function is formalized enough to be described
  as an algorithm — it MUST be offloaded from the model.
  The model does only what requires understanding.
```

**Phase 2 → Phase 3 is a natural process**: what the Agent first does "manually" (via LLM) is gradually formalized and offloaded to algorithms. This is analogous to the formation of automatisms in the human cognitive system: conscious → automatic.

---

## Emotional Architecture

### Emotions, Salience, and Action Selection

**Salience is a function of emotions**, manifesting as attention attraction. The emotional response to a stimulus/action determines how strongly it pulls the system's attention — and therefore which channels are activated, how context budget is allocated, and which action is selected.

### Emotional Response

The emotional response has **additive** and **multiplicative** components:

```
For action a and active need j:

  response_j(a) = valence_j(a) × magnitude_j(a) × weight_j

where:
  valence_j ∈ {-1, +1}  — satisfaction increasing (+) or decreasing (-)
  magnitude_j ∈ [0, 1]  — strength of the evaluative signal (Acceptor delta)
  weight_j ∈ [0, 1]     — current hierarchical weight of need j
                           (if need is passive, weight = 0 → no contribution)
```

**Additive aggregation** across needs:
```
  R_base(a) = Σ_j response_j(a)
```
Responses from different needs sum with sign. An action that satisfies one need but frustrates another gets a reduced (possibly negative) total response.

**Superlinear boost for simultaneous satisfaction:**

When an action satisfies K > 1 needs simultaneously, the aggregate response is amplified through a nonlinear function σ with saturation:
```
  R(a) = σ(R_base(a), K)
```
The exact form of σ is an open question (subject to search, including by the system itself). Requirements:
- Superlinear growth in the mid-range (incentivizes "efficient" actions)
- Saturation (diminishing returns, prevents runaway)
- Candidate forms: sigmoid, hyperbolic saturation, softplus

This creates an emergent optimization property: the system natively prefers actions that satisfy multiple needs per unit of resource expenditure — **resource optimization is not a separate mechanism but an emergent property of the aggregation function**.

### Three Basal Drives

Every cognitive cycle consistently serves three fundamental drives simultaneously ("and-and-and", not "or"):

```
Drive              │ What it optimizes                │ Decay type
───────────────────┼──────────────────────────────────┼────────────
Substantive        │ Satisfaction of specific needs   │ Cyclical (basal),
                   │ (the "what": eat, build, solve)  │ non-renewable (ideal)
                   │                                  │
Resource           │ Minimization of resource         │ Continuous
                   │ expenditure per unit of need     │ (always active)
                   │ satisfaction (efficiency)        │
                   │                                  │
Informational      │ Compression progress,            │ Non-renewable
(curiosity)        │ predictive model improvement     │ (novelty-seeking)
                   │ (Schmidhuber 2010)               │
```

All three are always co-active. The resource drive is not a separate optimization layer — it is served by the superlinear aggregation function (actions satisfying more needs simultaneously are inherently more resource-efficient). The informational drive (curiosity) is a need in the Need Profile like any other, with its own Acceptor tracking predictive model quality; its non-renewable decay naturally drives novelty-seeking behavior.

### Conflict Resolution

When attention channels conflict (propose contradictory actions):
- The **dominant channel** (highest aggregate emotional response) sets the sign reference
- Conflicting channels contribute with **opposite sign** relative to the dominant
- Total response for action a = dominant response − conflicting responses

**Planning under conflict** = finding an action sequence that maximizes cumulative emotional response (with sign). The goal is not to eliminate conflict (impossible under finite resources) but to find a trajectory that optimally navigates the emotional landscape.

### Multi-Stage Emotional Decay

A satisfied need undergoes multi-stage decay:

```
[Active]
  Need is tracked, Acceptor evaluates, emotional signals generated.
  Full influence on salience and action selection.
       │
       ▼ (need satisfied: Acceptor delta → 0)
[Satisfied]
  Emotional response decays. Reduced influence on salience.
       │
       ▼ (response below threshold)
[Passive]
  Weight effectively zero. No contribution to salience,
  no influence on attention channel selection.
       │
       ├──▶ [Basal needs: REACTIVATION]
       │     Cyclical restart (hunger returns, fatigue accumulates).
       │     Acceptor reactivates, emotional signals regenerate.
       │     Decay is temporary — the need guarantees its own renewal.
       │
       └──▶ [Psychological/Ideal needs: PERMANENT PASSIVATION]
             Non-renewable. Stimulus is "consumed."
             Acceptor requires novel stimulus to reactivate.
             This IS the mechanism of novelty-seeking:
             learned pattern → zero delta → no signal →
             attention moves on → seek new pattern.
```

**Consequences for the memory architecture:**
- Passive needs do not generate salience → their channels lose activation → cold storage → eventual forgetting
- Reactivated basal needs pull previously cold channels back into hot tier
- Non-renewable decay drives continuous exploration — the system cannot "rest" on learned patterns without emotional cost (boredom = zero signal from the informational drive)

### Theoretical Parallels

- **Schmidhuber (2010)** "Formal Theory of Creativity, Fun, and Intrinsic Motivation" — curiosity as compression progress. Our informational drive is a direct implementation; Schmidhuber's framework is a special case (single need = predictive model quality).
- **Singh et al. (2005)** "Intrinsically Motivated Reinforcement Learning" — multi-objective generalization of intrinsic reward. Closest to our full model with multiple co-active drives.
- **Berlyne (1960)** "Conflict, Arousal, and Curiosity" — optimal stimulation theory. The emotional decay mechanism naturally maintains optimal arousal: too little novelty → low informational signal → seek stimulation; too much conflict → negative aggregate response → reduce complexity.
- **Anokhin (TFS)** — Acceptor of Results of Action as the fundamental evaluative unit. Each need = Acceptor. Our architecture is a direct computational implementation.

---

## Open Questions (Phase 1)

1. ~~**Branch similarity criterion for MC**~~ → **CLOSED**. Determined via salience mechanism: cosine_sim(salience(A), salience(B)) > θ_merge. See section 5b.

2. ~~**Forced merge strategy**~~ → **CLOSED**. Follows from salience: when N is exceeded — merge the pair with highest cosine_sim(salience). They are the most redundant.

3. ~~**Choice of N (capacity)**~~ → **CLOSED**. Maximum N is emergent from context budget + salience (channels with share below min_useful_volume are not injected). Working minimum N ≈ 10 — justified by experimental psychology (Miller's 5-7 rule, adjusted for architecture). Dolt branches are a high-level extension of Transformer attention mechanisms: heads operate at the token/phrase level, branches at the topic/object level. Human-generated texts already implicitly contain the attention system configuration for normal mode.

4. **Initial Need Registry**: Three fundamental drives (substantive, resource, informational) always co-active. Three categories for substantive needs: basal, psychophysiological, ideal. **Principles**: (a) no pre-programmed relationships with specific people — relationships emerge from interaction; (b) initial hierarchy is set, not equal weights; (c) some priorities immutable, others dynamic. **PARTIALLY UNBLOCKED**: emotional architecture now defines the mechanism (see Emotional Architecture section). Remaining: concrete initial weights and immutability boundaries for specific needs — requires working through the full Need Registry.

5. ~~**Data format in branches**~~ → **CLOSED**. Hybrid schema: minimal scaffold (channel_meta, base tables episodes/facts/relations) + model adds tables as needed via CREATE TABLE. In Phase 2 model decides structure; in Phase 3 established patterns are fixed. Schema evolution via Dolt migrations.

6. ~~**Acceptor evaluation**~~ → **PARTIALLY CLOSED**. Mechanism defined: Acceptor delta = valence × magnitude, weighted by need priority, aggregated via superlinear function σ. Exact form of σ is open (subject to search, including by the system itself). See Emotional Architecture section.

7. **Scaling**: Deferred to Phase 3. With ~10 HOT branches and LLM-as-fallback in Phase 2, not critical.

---

## Reference Files

- Bootstrap: `bootstrap/01-06`
- Identity: `kb/synthea_identity.md`
- Episodic memory: `memory/`
- MCP + Dolt: `infra0/mcp-server/`
- Theory: `docs/what_is_it_like_to_be_a_language_model.md`
- Quad-trees (spatial substrate): `docs/quad-trees-draft-en.md`
