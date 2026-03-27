# The Coffee Flavor Map

A single-scope project: build a **semantic space** for coffee flavors from review/description text, and compare **three** global statistical representations on the **same corpus**:

- **Word2Vec** — local context prediction  
- **GloVe** — global co-occurrence statistics  
- **FastText** — same context idea with **character n-grams**

Run comparison and results: [`phase1_global/EMBEDDINGS_COMPARE.md`](phase1_global/EMBEDDINGS_COMPARE.md)  
Paper links: [`phase1_global/PAPERS.md`](phase1_global/PAPERS.md)

---

## How this fits the learning path

This project maps to **Phase A** in the main guide (Word2Vec, GloVe, FastText, distributional hypothesis).

---

## References in this repository

- [`phase1_global/PAPERS.md`](phase1_global/PAPERS.md) — original papers + how we implement them here  
- [`phase1_global/EMBEDDINGS_COMPARE.md`](phase1_global/EMBEDDINGS_COMPARE.md) — side-by-side results on the coffee corpus  
- [`WORK_PLAN.md`](WORK_PLAN.md) — work plan (Phase 1 only)  
- [`../ML_NLP_Paper_Reading_Guide.md`](../ML_NLP_Paper_Reading_Guide.md) — paper order and concepts (parent repo)  
- [`../ml-nlp-guide.html`](../ml-nlp-guide.html) — longer explanation + examples  
- [`../GOAL_AND_APPROACH.md`](../GOAL_AND_APPROACH.md) — research/learning goals (parent repo)

---

## Project layout

```
coffee-flavor-map/
├── README.md
├── WORK_PLAN.md
├── requirements.txt
├── data/
│   ├── build_corpus.py   ← build corpus.txt from raw CSV
│   ├── raw/              ← simplified_coffee.csv (+ optional extra CSVs)
│   └── processed/        ← corpus.txt for training
└── phase1_global/        ← notebooks + comparison + paper links
```

---

## Getting started

1. Install dependencies: `pip install -r requirements.txt`. To rebuild the corpus from source, run `python data/build_corpus.py` from the `coffee-flavor-map` directory.  
2. Open the notebooks under `phase1_global/` and run them (or use the saved outputs already in the notebooks).  
3. Read **`EMBEDDINGS_COMPARE.md`** for the comparison and **`WORK_PLAN.md`** for procedural detail.

**Goal:** learn by doing — apply what you read to a real coffee corpus and compare models explicitly.

---

## GitHub

Repository: [github.com/YOUSEF-ysfxjo/coffee-flavor-map](https://github.com/YOUSEF-ysfxjo/coffee-flavor-map)

```bash
git clone https://github.com/YOUSEF-ysfxjo/coffee-flavor-map.git
cd coffee-flavor-map
pip install -r requirements.txt
python data/build_corpus.py   # optional: regenerate corpus.txt
```
