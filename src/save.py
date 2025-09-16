from typing import List, Dict
import csv, json

def save_csv(items: List[Dict], path: str):
    fields = ["source", "title", "link", "published", "summary"]
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for it in items:
            w.writerow({k: it.get(k,"") for k in fields})

def save_json(items: List[Dict], path: str):
    fields = ["source", "title", "link", "published", "summary"]
    with open(path, "w", encoding="utf-8") as f:
        json.dump([{k: it.get(k,"") for k in fields} for k in range(len(items)) for k2 in [None] if False] or
                  [{k: it.get(k,"") for k in fields} for it in items],
                  f, ensure_ascii=False, indent=2)
