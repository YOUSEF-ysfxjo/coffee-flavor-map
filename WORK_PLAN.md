# Work Plan — The Coffee Flavor Map (Phase 1)

This repo implements **one scope**: a **global statistical** embedding space for coffee-flavor text and a **three-way comparison** (Word2Vec, GloVe, FastText). Concepts align with **Phase A** in the main learning guide.

---

## Goal

Build a **semantic space** for coffee-related vocabulary from a single processed corpus, train three comparable models, and document **what each method does** vs **what we observe** on this data.

**Paper links:** [`phase1_global/PAPERS.md`](phase1_global/PAPERS.md)  
**Results & comparison:** [`phase1_global/EMBEDDINGS_COMPARE.md`](phase1_global/EMBEDDINGS_COMPARE.md)

---

## What we implemented

| # | Step | Outputs | Tools |
|---|------|---------|--------|
| 1 | **Corpus** — CSV → one segment per line | `data/processed/corpus.txt` | [`data/build_corpus.py`](data/build_corpus.py) (`pandas`; source: `data/raw/simplified_coffee.csv`) |
| 2 | **Word2Vec** (skip-gram, Gensim) | `phase1_global/word2vec.model` | [`word2vec_train.ipynb`](phase1_global/word2vec_train.ipynb) |
| 3 | **GloVe** (mittens, same corpus) | `phase1_global/glove_vectors.npz` | [`glove_train.ipynb`](phase1_global/glove_train.ipynb) |
| 4 | **FastText** (skip-gram + char n-grams, Gensim) | run notebook locally (large sidecar gitignored) | [`fasttext_train.ipynb`](phase1_global/fasttext_train.ipynb) |
| 5 | **Checks** — `most_similar`, one analogy, flavor-term table, PCA + KMeans | Prints & plots inside notebooks | sklearn, matplotlib |
| 6 | **Write-up** — side-by-side interpretation | `EMBEDDINGS_COMPARE.md`, `PAPERS.md` | — |

**Aligned hyperparameters (where applicable):** `min_count=10`, `window=5`, `vector_size=100`; Word2Vec & FastText `sg=1`, `epochs=5`; GloVe `max_iter=100`. Details in `EMBEDDINGS_COMPARE.md`.

**Success criteria (qualitative):** Neighbors for anchors like *lemon* / *chocolate* / *vanilla* should look like food or aroma terms; flavor–flavor pairs should be interpretable. Analogies stay noisy on a small domain corpus (expected).

---

## Repository layout

```
coffee-flavor-map/
├── README.md
├── WORK_PLAN.md
├── requirements.txt
├── data/
│   ├── build_corpus.py
│   ├── raw/
│   └── processed/corpus.txt
└── phase1_global/
    ├── word2vec_train.ipynb
    ├── glove_train.ipynb
    ├── fasttext_train.ipynb
    ├── EMBEDDINGS_COMPARE.md
    └── PAPERS.md
```

Parent repo also has [`ML_NLP_Paper_Reading_Guide.md`](../ML_NLP_Paper_Reading_Guide.md), [`ml-nlp-guide.html`](../ml-nlp-guide.html), etc.

---

## How to run

1. Install: `pip install -r requirements.txt` (from `coffee-flavor-map/`).
2. Open `phase1_global/` notebooks and **Run All**, or use `jupyter nbconvert --execute … --inplace` (see bottom of `EMBEDDINGS_COMPARE.md`).
3. **FastText:** after clone, run `fasttext_train.ipynb` locally — large `fasttext.model.*` artifacts are gitignored (see `EMBEDDINGS_COMPARE.md`).
