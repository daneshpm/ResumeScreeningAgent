import pandas as pd
import json
import os

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def export_csv(results):
    path = os.path.join(OUTPUT_DIR, "ranked_candidates.csv")
    pd.DataFrame(results).to_csv(path, index=False)
    return path


def export_json(results):
    path = os.path.join(OUTPUT_DIR, "ranked_candidates.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=4)
    return path