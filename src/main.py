# -*- coding: utf-8 -*-
import argparse
from src.sources import FEEDS
from src.fetch import fetch_entries
from src.normalize import normalize, dedupe, filter_since
from src.save import save_csv, save_json

def parse_args():
    p = argparse.ArgumentParser(description="Automacao de noticias de IA (RSS).")
    p.add_argument("--since", type=int, default=7, help="Filtrar ultimos N dias (default: 7)")
    p.add_argument("--limit", type=int, default=50, help="Limite de itens (default: 50)")
    p.add_argument("--format", choices=["print","csv","json","markdown"], default="print", help="Formato de saida")
    p.add_argument("--out", type=str, default="", help="Arquivo de saida (csv/json/md)")
    return p.parse_args()

def main():
    args = parse_args()
    items = fetch_entries(FEEDS)
    items = normalize(items)
    items = dedupe(items)
    items = filter_since(items, args.since)
    items = sorted(items, key=lambda x: (x.get("published_dt") or 0), reverse=True)
    if args.limit: items = items[:args.limit]

    if args.format == "print":
        print(f"[RESULT] itens: {len(items)}")
        for i, it in enumerate(items, 1):
            print(f"{i:02d}. {it.get('title','')}\n    {it.get('link','')}\n")
    elif args.format == "csv":
        if not args.out: raise SystemExit("--out é obrigatório para CSV")
        save_csv(items, args.out); print(f"CSV salvo em: {args.out}")
    elif args.format == "json":
        if not args.out: raise SystemExit("--out é obrigatório para JSON")
        save_json(items, args.out); print(f"JSON salvo em: {args.out}")
    else:
        print("Formato ainda não implementado.")
if __name__ == "__main__":
    main()
