# Quad Trees as an Alternative Substrate for Function Approximation: From Simplicity Bias to Explicit MDL Optimization

**Draft**

*Victor Smirnov*

---

## Abstract

We show that compressed D-dimensional quad trees (QT) based on LOUDS encoding constitute a computational formalism in which simplicity bias — the key property explaining the generalization capabilities of neural networks — is realized *explicitly* through Minimum Description Length (MDL) as a direct objective function. Unlike neural networks, where simplicity bias emerges as a property of the parameter-function map (Dingle et al., 2018; Mingard et al., 2021), in QT the description length of the model is exactly computable, locally controllable (via tree depth in each region of the space), and carries a built-in uncertainty map. We formulate an inductive inference method for QT based on progressive level-by-level construction with an MDL criterion, and discuss a QT-based language model architecture as an alternative to transformers.

---

## 1. Introduction: Simplicity Bias as a Bridge Between AIT and Machine Learning

### 1.1 The Coding Theorem for Computable Maps

Levin's coding theorem (1974) states that for a universal Turing machine (UTM), the probability of obtaining output x from a random input program is bounded above by:

$$P_U(x) \leq 2^{-K(x) + O(1)}$$

where K(x) is the Kolmogorov complexity of x. Simple outputs are exponentially more probable.

Dingle, Camargo & Louis (2018) generalized this result to arbitrary computable maps f: I → O. For *limited complexity maps* (K(f) + K(n) ≪ K(x)):

$$P_f(x) \lesssim 2^{-a \cdot \tilde{K}(x) + b}$$

where K̃(x) is an approximation of K-complexity via Lempel-Ziv compression, and a, b are constants depending on f but not on x.

The key idea: the map f is a "lens" through which the coding theorem passes. A random input to f is a random program for a UTM of a specific format: "description of f + input." If the lens is simple (K(f) is small), the UTM's bias passes through it almost undistorted. If the lens is complex, the bias disappears.

### 1.2 Simplicity Bias in Neural Networks: A Property of the Architecture, Not the Optimizer

Valle-Pérez et al. (2018) applied the Dingle et al. result to the parameter-function map θ → f_θ of a neural network. This map is limited-complexity, nonlinear, and highly redundant (parameters ≫ functions). All conditions are satisfied — simplicity bias is present: simple functions occupy exponentially larger volume in parameter space.

Mingard et al. (2021) showed experimentally that P_SGD(f|S) ≈ P_B(f|S): the distribution of functions found by SGD matches the Bayesian posterior. SGD introduces no significant additional bias — it behaves as an approximate Bayesian sampler. Simplicity bias is embedded in the architecture before training begins.

The chain:

> Architecture → parameter-function map → simplicity bias (coding theorem) → SGD inherits bias → simple data → simple models

This chain is sound, but simplicity bias in neural networks is *implicit*. The model description length is not exactly computable; the bias is not locally controllable; the connection to AIT is reconstructed theoretically rather than observed directly.

### 1.3 The Question

Does there exist a computational formalism in which simplicity bias is realized *explicitly* — where description length is exactly computable, locally controllable, and AIT operates not as an analogy but as a direct objective function?

---

## 2. Quad Trees as a Computational Formalism

### 2.1 Definitions

Let [0, 1] ∈ ℝ be the domain and D the number of dimensions. A vector X⃗ = ⟨x₀, x₁, …, x_{D-1}⟩ ∈ [0, 1]^D is encoded via multiscale decomposition: the bits of all coordinates are interleaved, forming a *path expression* of length H·D, where H is the depth (bit precision).

This is a mapping onto a Z-order curve. A set of D-dimensional points is represented as a D-dimensional quad tree of degree 2^D, encoded via LOUDS (Level-Order Unary Degree Sequence): 2 bits per node + compressed bitmaps of cardinal labels.

### 2.2 QT as a Function Class

Each concrete quad tree is a *description of a function* in the language of spatial decompositions. The description length (number of nodes/bits) is K_QT(f), the Kolmogorov complexity of function f in the QT language.

Generalization ability arises from compression: if a QT model is short, it describes the function at a coarse scale, filling in details with default values ("this entire region is class 1"). This is *literally* the MDL principle: the shortest description consistent with the data generalizes best.

For data S with low K(S) whose structure is spatially geometric (homogeneous regions, boundaries with low fractal dimension), short QT models exist that generate these data.

### 2.3 QT vs. Neural Networks: Different UTMs

QT and neural networks are different UTMs with different invariant constants. The invariance theorem guarantees K_QT(S) ≤ K(S) + c, but the constant c may include a full MLP simulator in the QT language — astronomically large in practice.

| Property | Neural Networks | QT |
|----------|-----------------|----|
| Description language | Superpositions of hyperplanes | Hypercubes |
| Strength | Algebraic structure, high dimensionality | Spatial-geometric structure, ≤16–24 dimensions |
| Simplicity bias | Implicit (emergent property) | Explicit (description length exactly computable) |
| Description length | Approximated via bounds | Exactly computable: 2 bits/node + bitmaps |
| Bias controllability | Global (architecture, hyperparameters) | Local (depth in each region) |
| Inference | Ω(W), W = number of parameters | O(H log N) |
| Dynamic updates | Retraining | O(H log N) per point |
| Inverse functions | Separate model | Native from the same structure |
| Uncertainty estimation | Open problem | Structural property (depth = confidence) |

---

## 3. Inductive Inference Method for QT

### 3.1 MDL as a Direct Objective Function

For neural networks, simplicity bias is reconstructed theoretically. For QT it is realized *literally*:

Minimize: **L(QT) + L(S | QT)**

- L(QT) — description length of the tree in bits. For LOUDS-encoded QT this is exactly computable.
- L(S | QT) — description length of data not explained by the model (errors, residuals).

This is a *massive* advantage: the training objective is a direct approximation of Kolmogorov complexity, not an indirect estimate via PAC-Bayes bounds or proxy losses.

### 3.2 Discreteness and Continuity

QT is a discrete structure, but the dichotomy "continuous vs. discrete" is false. Neural networks with 4-bit weights: each parameter has 16 values. QT with depth H = 32: precision 2⁻³² — equivalent to float32. Both models are discrete approximations of continuous functions with different *geometries of discreteness*:

- Neural network: fixed-dimension hypercube (W parameters × B bits each)
- QT: tree of variable depth and width

The key distinction: in QT precision is *adaptive*. Bits are allocated where they are needed. In a neural network precision is uniform — all weights have the same bit-width.

### 3.3 The Discrete Gradient

At each step there is a set of possible splits of leaf nodes. Each split increases L(QT) and decreases L(S|QT). The ratio:

$$\frac{\Delta L(S|QT)}{\Delta L(QT)}$$

is the discrete gradient: the direction of maximum reduction in total MDL length per bit of description. This improves on the continuous gradient in several respects: no local minima (coarse-to-fine by construction), no learning rate to tune, no vanishing/exploding gradient, and the objective function is exactly computable.

### 3.4 Progressive Level-by-Level Construction

We build the tree level by level, from root to leaves. Each new level is an optimization step that doubles the resolution:

```
For level = 1, 2, ..., H_max:
    For each leaf at the current level:
        Evaluate ΔL = ΔL(QT) + ΔL(S|QT) upon splitting
        If ΔL < 0: split
    If no split reduced L: stop
```

The multiscale decomposition naturally defines the order of learning: coarse patterns first (upper levels), fine ones later (lower levels). This is curriculum learning embedded in the model structure, not imposed by an external heuristic.

Level-order construction is optimal for LOUDS encoding: level-order coincides with the storage order, providing sequential writes without rebalancing.

### 3.5 The Full Training Cycle

The unique properties of QT — partial functions, inverse functions, and built-in self-assessment — allow construction of a *self-consistent* training cycle:

**Phase 1. Progressive construction.** Level-by-level construction with MDL criterion (§3.4).

**Phase 2. Learning from incomplete data.** Training data need not be complete tuples. An unknown dimension is a wildcard in the path expression; during tree traversal a wildcard means "traverse all branches." QT natively learns from incomplete data without imputation.

**Phase 3. Self-consistency via inverse functions.** QT enables computing both f and f⁻¹ from the same structure. For each example (x, y), forward compatibility (y ∈ f(x)?) and backward compatibility (x ∈ f⁻¹(y)?) are checked. Inconsistencies indicate regions for deepening. This is built-in cycle consistency — a form of self-supervision analogous to CycleGAN, but implemented exactly and structurally.

**Phase 4. Active learning via self-assessment.** The tree depth map determines priorities:

- Low confidence (shallow) + high query traffic → priority for new data
- High confidence → leave as is
- Deep + high label entropy → data are objectively complex

The model itself indicates where it needs data — via O(1) reads of structural node properties, without expensive Bayesian estimation.

This is an EM-like algorithm: E-step (use the current QT for inference via partial/inverse functions), M-step (update the QT structure via MDL optimization).

---

## 4. Built-in Uncertainty Estimation

In neural networks, uncertainty estimation is an open problem: softmax probabilities are systematically overconfident, Bayesian neural networks are expensive, deep ensembles require multiple forward passes.

In QT, the following are available for free as a by-product of a single tree traversal:

- **Depth at query point** — coarseness of the model in that region
- **Number of training points in the leaf** — data density
- **Label spread among descendants** — local decision entropy

In AIT terms: tree depth at a point is the *local description length*. Shallow = short description = coarse model = "approximating, but don't know the details." Deep + many data points = long description backed by observations = "I know."

**Application to hallucinations.** A hallucination is a confident answer from a shallow region where the model lacks resolution. In QT this is diagnosable *before* generating the answer. The fix is local: deepen the tree in the problematic region in O(H log N), without touching any other area. Surgery instead of chemotherapy.

---

## 5. Function Compression in QT

### 5.1 Descriptional Complexity of a Decision Boundary

For a 2D indicator function (e.g., an ellipse): if N is the number of pixels, a compressed QT describes the function in O(√N) bits. Detail is needed only at the *boundary* of the region; the interior is homogeneous and is described at a coarse scale.

This is a direct correspondence: the number of QT nodes is proportional to the *length* of the boundary (in 2D) or *surface area* (in 3D), not to the volume of the region. Simplicity bias is explicit: functions with compact smooth boundaries have short descriptions.

### 5.2 Curse and Blessing of Dimensionality

As D grows, volume grows as 2^D per tree level (curse), but data becomes sparser (blessing). RLE compression of bitmaps reduces the cost to O(D) bits per quadrant. The practical limit is D ≤ 16–24.

At D = 8 the exponential effects are still moderate (256-ary tree), while 8 dimensions already represents a sufficiently complex relation for many practical tasks.

Compression in QT is implicit *dimensionality reduction*: compressed structures degrade more slowly than their uncompressed counterparts while maintaining the same logical API.

---

## 6. Toward a QT-Based Language Model Architecture

### 6.1 The Central Problem: Context Dimensionality

A language model computes f(context) → P(next token). A transformer handles context of thousands of tokens via embeddings and attention. QT operates in ≤16–24 dimensions. A dimensionality reduction mechanism is required.

### 6.2 Multi-Scale Associative Model

The idea: represent context as a multi-scale tuple of fixed dimensionality.

| Component | Dimensions | What it encodes |
|-----------|------------|-----------------|
| Last 4–6 tokens | 4–6 | Local n-gram |
| Sentence hash | 2–3 | Syntactic context |
| Topic hash | 2–3 | Semantic context |
| Predicted token | 1 | Target variable |
| **Total** | **~10–13** | |

The training corpus becomes a set of tuples, each a point in QT. Training is level-by-level construction with an MDL criterion. Frequent patterns compress (few nodes); rare ones are detailed or pruned.

### 6.3 Prediction as a Partial Query

Prediction is substituting a wildcard for the target dimension. QT traversal returns all matching records with their frequencies. This is a *native operation* — partial function evaluation.

### 6.4 Multi-Scale Smoothing (Backoff)

If the full context yields few matches (low confidence):

1. Drop the furthest context token → (k-1)-gram
2. Still few? → (k-2)-gram
3. Drop the topic hash
4. ...down to unigram

This is Katz backoff implemented structurally: each wildcard is a step up one level of abstraction. QT does this in a single tree rather than separate n-gram tables.

### 6.5 Advantages and Limitations

**Advantages over transformers:**
- Inference O(log N) vs. O(L·d²)
- Dynamic learning: a new document is integrated in seconds
- Real-time personalization
- Edge deployment without GPU
- Interpretability: the n-gram driving the prediction is visible
- Confidence is visible before generation

**Limitations:**
- Multi-step reasoning requires an explicit external loop (chain-of-lookups)
- Long-range context is lost during hashing
- Semantics depend on the quality of hash functions, which must be designed separately

### 6.6 Open Questions

1. **Dimensionality reduction.** A transformer is a vectorized Forward-Chaining Rule System (FCRS). A QT analog requires a dimensionality reduction mechanism: static (computational structure) or dynamic (analogous to attention maps).

2. **Multi-step composition.** One QT lookup is one "thinking step." A 96-layer transformer performs 96 sequential compositions. Designing chain-of-lookups is an open architectural problem.

3. **Mapping from latent space design to description length distribution.** What distribution of description lengths does a given QT design induce? Understanding this mapping would enable principled design of QT models for specific task classes — a "compiler theory for inductive biases."

---

## 7. Connections to Theoretical Foundations

### 7.1 QT as Explicit MDL Inference

In neural networks: SGD → implicit simplicity bias → theoretical reconstruction of the AIT connection.

In QT: MDL → *explicit* simplicity bias → AIT operates directly as the objective function.

Rather than hoping the optimizer will happen to find a simple solution (as with neural networks), we *directly optimize description length* — closer to what AIT prescribes theoretically (Solomonoff induction = search for the shortest program), within a concrete computational formalism.

### 7.2 Compression Progress as Learning Signal

The greedy algorithm in which at each step we add the node that maximally compresses L(QT) + L(S|QT) implements Schmidhuber's Artificial Curiosity (1991): learning signal = compression progress. Every step is maximally "interesting" in the sense of compression progress.

### 7.3 Controllable Simplicity Bias

In an autoregressive transformer, simplicity bias is an emergent property. In QT it is a design parameter, controllable locally through tree depth in each region of the space. This transforms bias from a *property* of the system into a *tool* for the designer.

Connection to the JEPA argument (LeCun): the advantage of prediction in latent space is the ability to *explicitly* define geometric constraints that determine the inductive bias, which indirectly induces a computational formalism with a specific distribution of description lengths. QT realizes this idea even more directly: the tree design *is* the formalism, and the description length is directly observable.

---

## 8. Conclusion

Compressed D-dimensional quad trees based on LOUDS encoding constitute a computational formalism with unique properties:

1. **Explicit simplicity bias.** Description length is exactly computable and is used as a direct training objective via MDL.

2. **Local controllability.** Tree depth in each region of space is independently adjustable, enabling adaptive allocation of "description bits" across the task.

3. **Built-in uncertainty estimation.** Tree depth = local description length = confidence measure, available in O(1).

4. **Native operations.** Inverse functions, partial queries, and dynamic updates are structural properties, not add-ons.

5. **Self-consistent learning.** Cycle consistency via forward and inverse functions as a built-in self-supervision mechanism.

QT does not replace neural networks on tasks with algebraic structure in high dimensions. But it offers a *different* computational substrate — white-box, explicitly connected to AIT — for tasks where speed, dynamism, invertibility, and interpretability are critical. It also opens a path to hybrid architectures in which a neural network performs dimensionality reduction while QT operates as a fast, dynamic, invertible approximator in the compressed space.

---

## References

- Dingle, K., Camargo, C. Q., & Louis, A. A. (2018). Input–output maps are strongly biased towards simple outputs. *Nature Communications*, 9(1), 761.
- Hochreiter, S., & Schmidhuber, J. (1997). Flat minima. *Neural Computation*, 9(1), 1–42.
- Keskar, N. S., Mudigere, D., Nocedal, J., Smelyanskiy, M., & Tang, P. T. P. (2017). On large-batch training for deep learning: Generalization gap and sharp minima. *ICLR 2017*.
- Mingard, C., Valle-Pérez, G., Skalse, J., & Louis, A. A. (2021). Is SGD a Bayesian sampler? Well, almost. *JMLR*, 22(1), 3579–3642.
- Schmidhuber, J. (1991). Curious model-building control systems. *Proceedings of IJCNN*.
- Schmidhuber, J. (2002). The speed prior: A new simplicity measure yielding near-optimal computable predictions. *COLT 2002*.
- Smirnov, V. Associative Memory. *Memoria Framework Documentation*. https://memoria-framework.dev/docs/data-zoo/associative-memory-2/
- Valle-Pérez, G., Camargo, C. Q., & Louis, A. A. (2018). Deep learning generalizes because the parameter-function map is biased towards simple functions. *ICLR 2019*.
- Zhang, C., Bengio, S., Hardt, M., Recht, B., & Vinyals, O. (2017). Understanding deep learning requires rethinking generalization. *ICLR 2017*.
