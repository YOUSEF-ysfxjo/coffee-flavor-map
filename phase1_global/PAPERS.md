# Phase 1 — Original papers & stable links

We do **not** store PDFs in this repo (size, licensing). Use the links below to read or download the official versions.

---

## Word2Vec (predict local context)

1. **Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013).** *Efficient Estimation of Word Representations in Vector Space.*  
   - arXiv: [https://arxiv.org/abs/1301.3781](https://arxiv.org/abs/1301.3781)  
   - Introduces continuous bag-of-words (CBOW) and skip-gram training.

2. **Mikolov, T., Sutskever, I., Chen, K., Corrado, G., & Dean, J. (2013).** *Distributed Representations of Words and Phrases and their Compositionality.*  
   - arXiv: [https://arxiv.org/abs/1310.4546](https://arxiv.org/abs/1310.4546)  
   - Negative sampling, phrases, and practical improvements often used with “Word2Vec.”

**Implementation here:** [Gensim](https://radimrehurek.com/gensim/models/word2vec.html) `Word2Vec` — see `word2vec_train.ipynb`.

---

## GloVe (global word–word co-occurrence)

**Pennington, J., Socher, R., & Manning, C. (2014).** *GloVe: Global Vectors for Word Representation.* (EMNLP 2014)

- ACL Anthology (stable PDF landing): [https://aclanthology.org/D14-1162/](https://aclanthology.org/D14-1162/)  
- Stanford NLP project page + pre-trained vectors: [https://nlp.stanford.edu/projects/glove/](https://nlp.stanford.edu/projects/glove/)

**Implementation here:** [mittens](https://github.com/hansenjohnson/mittens) `GloVe` (NumPy implementation of the GloVe objective) — see `glove_train.ipynb`.

---

## FastText (subword information)

**Bojanowski, P., Grave, E., Joulin, A., & Mikolov, T. (2017).** *Enriching Word Vectors with Subword Information.* (Transactions of the ACL, 2017)

- arXiv: [https://arxiv.org/abs/1607.04606](https://arxiv.org/abs/1607.04606)  
- Original library & docs: [https://fasttext.cc/](https://fasttext.cc/)

**Implementation here:** [Gensim](https://radimrehurek.com/gensim/models/fasttext.html) `FastText` (same ideas; API aligned with `Word2Vec`) — see `fasttext_train.ipynb`.

---

## How this maps to `EMBEDDINGS_COMPARE.md`

The comparison doc summarizes **what each objective does** and **what we observed** on the coffee corpus. When interpretation disagrees with textbook analogies, check **corpus size** first; the papers above were evaluated on **large** general-domain corpora.
