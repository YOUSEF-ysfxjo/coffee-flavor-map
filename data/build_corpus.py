"""
Build `data/processed/corpus.txt` from `data/raw/simplified_coffee.csv`.

One text segment per line (sentence split), UTF-8 — same logic as the old exploratory
notebook, with paths relative to the repo (no hard-coded machine paths).

Run from anywhere:  python data/build_corpus.py
Or from coffee-flavor-map:  python -m data.build_corpus  (if package) — simplest:
  cd coffee-flavor-map && python data/build_corpus.py
"""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
RAW_CSV = ROOT / "data" / "raw" / "simplified_coffee.csv"
OUT_TXT = ROOT / "data" / "processed" / "corpus.txt"


def main() -> None:
    df = pd.read_csv(RAW_CSV)
    sentences = df["review"].str.split(r"(?<=[.!?])\s+").explode().tolist()
    sentences = [s.strip() for s in sentences if s and len(s.strip()) > 0]
    OUT_TXT.parent.mkdir(parents=True, exist_ok=True)
    OUT_TXT.write_text("\n".join(sentences) + "\n", encoding="utf-8")
    print(f"Wrote {len(sentences)} segments to {OUT_TXT}")


if __name__ == "__main__":
    main()
