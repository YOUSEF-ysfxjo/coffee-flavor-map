# Word2Vec vs GloVe vs FastText — same coffee corpus

This file is the **single place** for: what each paper does, **saved run outputs** from all three notebooks, and a **short comparison**.

**Original papers (citations + links, no PDFs in repo):** [`PAPERS.md`](PAPERS.md).

**Notebooks in this folder** (`word2vec_train.ipynb`, `glove_train.ipynb`, `fasttext_train.ipynb`) are the **executed** versions: they already contain saved cell outputs (plots, prints). You can open them to see results without re-running.

**Last full run:** all three were executed with `jupyter nbconvert` (Python 3.9 venv). To refresh outputs, run the notebooks again or use nbconvert as described at the bottom of this file.

**Setup (aligned where possible):** same `corpus.txt`, `min_count=10`, `window=5`, `vector_size=100`. **Word2Vec** & **FastText**: skip-gram (`sg=1`), `epochs=5`; FastText uses character n-grams `min_n=3`, `max_n=6`. **GloVe**: mittens `max_iter=100`.

---

## What each paper is about (short)

|                    | **Word2Vec** (Mikolov et al.)                                                                           | **GloVe** (Pennington et al., 2014)                                                    | **FastText** (Bojanowski et al.)                                                            |
| ------------------ | ------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **Core idea**      | Train vectors so the model **predicts** nearby words from **local** context windows (skip-gram / CBOW). | **Fit** vectors so **dot products** match **global** **log** co-occurrence statistics. | Like skip-gram, but each word is also built from **character n-grams** (subword structure). |
| **Training input** | Sentence stream + sliding window.                                                                       | Precomputed **co-occurrence matrix**.                                                  | Same sentence stream as Word2Vec; **subwords** share statistics across surface forms.       |
| **Objective**      | Prediction loss (predict context).                                                                      | Weighted least squares on **log X_ij**.                                                | Predict context using **word + character n-gram** representations.                          |

**One line:** Word2Vec = _predict context_; GloVe = _reproduce global co-occurrence counts_; FastText = _predict context with internal word structure (n-grams)_.

---

## Captured output — Word2Vec (from saved notebook run, cleaned below)

```
PROJECT_ROOT = .../coffee-flavor-map
file_path     = .../data/processed/corpus.txt

Loaded 5092 sentences. First 3: [['crisply', 'sweet', 'cocoa-toned'], ['lemon', 'blossom', ...], ...]

Saved .../phase1_global/word2vec.model | vocab=359

Most similar to 'lemon':
  tangerine: 0.9576
  guava: 0.9539
  nectarine: 0.9448
  peach: 0.9440
  honey: 0.9428

Most similar to 'chocolate':
  dark: 0.9251
  fudge: 0.9235
  caramel: 0.9143
  spices: 0.9105
  cherry: 0.9092

Most similar to 'vanilla':
  candied: 0.9958
  salted: 0.9954
  pomelo: 0.9948
  mesquite: 0.9942
  clove: 0.9939

Analogy: berry + chocolate - lemon ≈
  tones: 0.8553
  wood: 0.8489
  cappuccino-scaled: 0.8385
  while: 0.8375
  fruit: 0.8327

Flavor terms in vocab: 13 | dropped: {'acidic'}

Top neighbor within flavor list:
  lemon      -> honey      (0.943)
  chocolate  -> caramel    (0.914)
  cocoa      -> lemon      (0.928)
  floral     -> nutty      (0.861)
  nutty      -> fruity     (0.863)
  citrus     -> berry      (0.977)
  berry      -> citrus     (0.977)
  honey      -> vanilla    (0.976)
  vanilla    -> caramel    (0.985)
  fruity     -> nutty      (0.863)
  caramel    -> vanilla    (0.985)
  roasted    -> honey      (0.928)
  jasmine    -> honey      (0.948)

PCA explained variance ratio: [0.673, 0.139]  (among the 13 flavor vectors)
Clusters (KMeans on those vectors): lemon/cocoa/honey/roasted/jasmine in one group; chocolate/vanilla/caramel in another; citrus/berry together; etc.
```

---

## Captured output — GloVe (from saved notebook run, cleaned below)

```
PROJECT_ROOT = .../coffee-flavor-map
file_path     = .../data/processed/corpus.txt

Loaded 5092 sentences

Vocabulary size (min_count=10): 359
Non-zero co-occurrence entries: 34,234 / 128,881

(GloVe training: error dropped from ~907 at iter 10 to ~120 at iter 100)

Saved .../phase1_global/glove_vectors.npz

GloVe neighbors of 'lemon':
  verbena: 0.9344
  nib: 0.7779
  cocoa: 0.7528
  almond: 0.7311
  plum: 0.7219

GloVe neighbors of 'chocolate':
  dark: 0.9407
  cedar: 0.8387
  and: 0.8336
  almond: 0.8168
  in: 0.8129

GloVe neighbors of 'vanilla':
  grapefruit: 0.7025
  pink: 0.6496
  mulberry: 0.6316
  dried: 0.6241
  dark: 0.6154

Analogy: berry + chocolate - lemon ≈
  goji: 0.7035
  dark: 0.5308
  citrus: 0.5204
  notes: 0.5059
  spicy: 0.5001

In vocab: 13 | dropped: {'acidic'}

Top neighbor within list:
  lemon      -> cocoa      (0.753)
  chocolate  -> cocoa      (0.698)
  cocoa      -> jasmine    (0.783)
  floral     -> berry      (0.471)
  nutty      -> floral     (0.283)
  citrus     -> berry      (0.645)
  berry      -> citrus     (0.645)
  honey      -> cocoa      (0.661)
  vanilla    -> chocolate  (0.580)
  fruity     -> nutty      (0.280)
  caramel    -> chocolate  (0.643)
  roasted    -> lemon      (0.548)
  jasmine    -> cocoa      (0.783)

PCA explained variance ratio: [0.304, 0.173]  (among the 13 flavor vectors)
Clusters: more cocoa/chocolate/lemon/jasmine mass; function words pulled into chocolate neighbors in full vocab (see below).
```

---

## Captured output — FastText (from saved notebook run, cleaned below)

```
PROJECT_ROOT = .../coffee-flavor-map
file_path     = .../data/processed/corpus.txt

Loaded 5092 sentences. First 3: [['crisply', 'sweet', 'cocoa-toned'], ['lemon', 'blossom', ...], ...]

Saved .../phase1_global/fasttext.model | vocab=359

Most similar to 'lemon':
  star: 0.9905
  jasmine: 0.9862
  lilac: 0.9815
  tangerine: 0.9804
  nectarine: 0.9795

Most similar to 'chocolate':
  spices: 0.9375
  nut: 0.9217
  passionfruit: 0.9119
  aged: 0.9093
  date: 0.9086

Most similar to 'vanilla':
  pomelo: 0.9983
  pomegranate: 0.9982
  lychee: 0.9978
  clove: 0.9977
  guava: 0.9974

Analogy: berry + chocolate - lemon ≈
  support: 0.8955
  supported: 0.8933
  spice: 0.8840
  tones: 0.8732
  chocolate-toned: 0.8653

Flavor terms in vocab: 14 | dropped: none   (← 'acidic' passes here; subword signal can change effective frequency behavior)

Top neighbor within flavor list:
  lemon      -> jasmine    (0.986)
  chocolate  -> caramel    (0.903)
  cocoa      -> jasmine    (0.977)
  floral     -> fruity     (0.931)
  nutty      -> citrus     (0.957)
  citrus     -> nutty      (0.957)
  berry      -> caramel    (0.915)
  honey      -> vanilla    (0.978)
  vanilla    -> caramel    (0.994)
  fruity     -> floral     (0.931)
  caramel    -> vanilla    (0.994)
  roasted    -> vanilla    (0.939)
  jasmine    -> lemon      (0.986)
  acidic     -> fruity     (0.876)

PCA explained variance ratio: [0.748, 0.135]  (among the 14 flavor vectors)
Clusters: overlapping groups; jasmine/lemon/cocoa/honey cluster tightly in this run.
```

---

## Compare this run (same text, three-way)

### Neighbors

| Query         | **Word2Vec**                                                      | **GloVe**                                              | **FastText**                                                                                                                                      |
| ------------- | ----------------------------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **lemon**     | Strong **fruit** chain: tangerine, guava, nectarine, peach, honey | Herb/cocoa/nut mix: verbena, nib, cocoa, almond, plum  | **star** at top (spurious substring / co-occurrence artifact), then **jasmine**, lilac, tangerine, nectarine — still fruity but noisier at rank 1 |
| **chocolate** | Food/dessert: dark, fudge, caramel, spices, cherry                | **dark**, cedar, then **and**, **in** (function words) | spices, nut, **passionfruit**, aged, date — plausible domain words but less “chocolate = chocolate” than Word2Vec                                 |
| **vanilla**   | candied, salted, pomelo, mesquite, clove                          | Lower scores; grapefruit, pink, mulberry               | Very tight fruit list: pomelo, pomegranate, lychee, clove, guava (similar “all high cosines” profile to Word2Vec)                                 |

**Paper link:** Skip-gram ranks **local** predictors. GloVe ranks **global** co-occurrence similarity (function words can dominate). FastText adds **subwords** — sometimes helpful for morphology, sometimes **confusable** when short substrings link unrelated tokens.

### Analogy _berry + chocolate − lemon_

- **Word2Vec:** tones, wood, cappuccino-scaled, while, fruit — not a clean flavor answer.
- **GloVe:** goji, dark, citrus, notes, spicy — not textbook.
- **FastText:** support, supported, spice, tones, **chocolate-toned** — slightly more **morphology / compound** flavor (expected from n-grams), still not a clean human analogy on this tiny corpus.

### Flavor list (within-list neighbors)

- **Word2Vec:** many **0.9+** pairs; citrus↔berry, vanilla↔caramel very strong.
- **GloVe:** lower scores; **cocoa** hub.
- **FastText:** also **very high** within-list scores; **14** terms including **acidic**; lemon↔jasmine and citrus↔nutty are very tight — good for a “wheel” view, but **not identical** roles to Word2Vec (e.g. berry’s top partner is caramel here).

### PCA (2D of the flavor vectors)

- **Word2Vec:** ~**67% + 14%** on PC1+2 (13 words).
- **GloVe:** ~**30% + 17%** (13 words).
- **FastText:** ~**75% + 14%** (**14** words, includes acidic) — **most** variance in the first two PCs among the three, on this subset.

**Note:** PCA is only on the small flavor matrix — it is a **projection diagnostic**, not a gold quality metric. Comparing **13 vs 14** points is not apples-to-apples; still useful side by side.

---

## Verdict: which model looks best _on this coffee corpus_?

**Overall winner (anchor neighbors + clarity): Word2Vec (skip-gram, 5 epochs).**

**Runner-up for structure on the flavor subset: FastText** — strong within-list similarities and the **best PC1+PC2 concentration** in this run, but **noisier full-vocab neighbors** for some anchors (_lemon_ → _star_, _chocolate_ → mixed fruit/spice).

**Third on these checks: GloVe** — interpretable global story, but **function-word** neighbors and **cocoa hub** in the flavor table hurt readability here.

There is no official “coffee embedding” benchmark; the call uses **neighbor identity**, **flavor-table coherence**, and **PCA as a secondary geometric cue**.

### What the judgment is based on

| Criterion                   | Word2Vec                                                    | GloVe                                     | FastText                                                                                |
| --------------------------- | ----------------------------------------------------------- | ----------------------------------------- | --------------------------------------------------------------------------------------- |
| **Anchor neighbors**        | Best **semantic** fit for _lemon_ / _chocolate_ in this run | Spurious **and** / **in** for _chocolate_ | Mixed: _vanilla_ neighbors fruit-heavy (good), _lemon_/**chocolate** have odd top items |
| **Flavor-list consistency** | Excellent **0.9+** pairs, clear roles                       | Hub **cocoa**, weaker pairs               | Excellent scores; **acidic** included; some pairings differ from Word2Vec               |
| **Analogy**                 | Noisy                                                       | Noisy                                     | Noisy (slightly more **word-shape** hits like _chocolate-toned_)                        |
| **PCA PC1+2**               | ~67% + 14%                                                  | ~30% + 17%                                | ~75% + 14% (14 terms)                                                                   |

### Why Word2Vec still edges FastText _here_

1. **What you read first is `most_similar` on head words.** Word2Vec’s _lemon_ and _chocolate_ lists look **most like human “flavor families”** without a bogus top neighbor.

2. **FastText’s strengths (subwords, OOV)** matter more when you have **many inflections / typos / rare splits**. This corpus is mostly **short lemmas**; subwords can still create **false similarity** (e.g. shared character pieces or spurious ties).

3. **Do not compare raw cosine numbers across models** — use **ranked neighbor words** and **within-model** tables.

### When to prefer FastText or GloVe

- **FastText:** more **morphological** variation, **rare** descriptors, or you need **vectors for unseen tokens** built from n-grams.
- **GloVe:** **large** corpora where **global** PMI-style structure is stable; analogy benchmarks at scale.

---

## One-sentence summary

- **Word2Vec:** predict **local** context. **GloVe:** match **global** co-occurrence. **FastText:** same local idea as skip-gram plus **character n-grams**.

**On this run, Word2Vec gives the cleanest anchor neighbors; FastText is competitive on the flavor block and PCA; GloVe is hardest to read on these checks** — mostly because the corpus is **small**, not because any paper is “wrong.”

---

## Re-run and refresh this comparison

```bash
cd coffee-flavor-map/phase1_global
jupyter notebook word2vec_train.ipynb   # Run All, then save
jupyter notebook glove_train.ipynb
jupyter notebook fasttext_train.ipynb
```

Or overwrite the notebooks with fresh executed copies:

```bash
python -m jupyter nbconvert --to notebook --execute word2vec_train.ipynb --inplace
python -m jupyter nbconvert --to notebook --execute glove_train.ipynb --inplace
python -m jupyter nbconvert --to notebook --execute fasttext_train.ipynb --inplace
```

Then update the **Captured output** sections in this `.md` if you want the text snapshot to match.

**GitHub:** `fasttext.model` and `fasttext.model.*` (Gensim FastText sidecar, often hundreds of MB) are **not** tracked in git — run **`fasttext_train.ipynb`** after clone to regenerate them. `word2vec.model` and `glove_vectors.npz` are small and safe to commit.
