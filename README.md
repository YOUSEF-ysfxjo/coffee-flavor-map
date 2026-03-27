# The Coffee Flavor Map

مشروع تطبيقي واحد النطاق: بناء **فضاء دلالي** لنكهات القهوة من نصوص مراجعات/توصيفات، ومقارنة **ثلاثة** تمثيلات إحصائية عالمية على **نفس الكوربوس**:

- **Word2Vec** (تنبؤ سياق محلي)
- **GloVe** (إحصاءات تزامن عالمية)
- **FastText** (نفس فكرة السياق مع **n-grams** حرفية)

الخلاصة التشغيلية والمقارنة: [`phase1_global/EMBEDDINGS_COMPARE.md`](phase1_global/EMBEDDINGS_COMPARE.md)  
روابط الأوراق الأصلية: [`phase1_global/PAPERS.md`](phase1_global/PAPERS.md)

---

## الربط مع مسار التعلّم

يُقابل هذا المشروع **Phase A** في الدليل العام (Word2Vec، GloVe، FastText، فرضية التوزيع).

---

## المراجع داخل المستودع

- [`phase1_global/PAPERS.md`](phase1_global/PAPERS.md) — روابط الأوراق + تنفيذات المشروع.
- [`phase1_global/EMBEDDINGS_COMPARE.md`](phase1_global/EMBEDDINGS_COMPARE.md) — مقارنة التشغيل على كوربوس القهوة.
- [`WORK_PLAN.md`](WORK_PLAN.md) — خطة العمل (Phase 1 فقط).
- [`../ML_NLP_Paper_Reading_Guide.md`](../ML_NLP_Paper_Reading_Guide.md) — ترتيب الأوراق والمفاهيم.
- [`../ml-nlp-guide.html`](../ml-nlp-guide.html) — شرح مفصّل + أمثلة.
- [`../GOAL_AND_APPROACH.md`](../GOAL_AND_APPROACH.md) — هدف الرحلة البحثية–التطبيقية.

---

## هيكل المشروع

```
coffee-flavor-map/
├── README.md
├── WORK_PLAN.md
├── requirements.txt
├── data/
│   ├── build_corpus.py   ← توليد corpus.txt من CSV الخام
│   ├── raw/              ← simplified_coffee.csv (وغيره اختياري)
│   └── processed/        ← corpus.txt للتدريب
└── phase1_global/        ← النوتبوكات + المقارنة + المراجع
```

---

## كيف تبدأ

1. ثبّت `requirements.txt`. لإعادة بناء الكوربوس من المصدر: `python data/build_corpus.py` من مجلد `coffee-flavor-map`.
2. افتح النوتبوكات في `phase1_global/` وشغّلها (أو اقرأ المخرجات المحفوظة فيها).
3. اقرأ **`EMBEDDINGS_COMPARE.md`** للمقارنة، و**`WORK_PLAN.md`** للتفاصيل الإجرائية.

هدف المشروع: **تعلّم بالتطبيق** — تطبيق ما نقرأه على كوربوس قهوة حقيقي ومقارنة النماذج صراحةً.

---

## GitHub

المستودع: [github.com/YOUSEF-ysfxjo/coffee-flavor-map](https://github.com/YOUSEF-ysfxjo/coffee-flavor-map)

```bash
git clone https://github.com/YOUSEF-ysfxjo/coffee-flavor-map.git
cd coffee-flavor-map
pip install -r requirements.txt
python data/build_corpus.py   # اختياري إن أردت إعادة بناء corpus.txt
```
