import argparse
from sources import FEEDS
from fetch import fetch_entries

def parse_args():
    p = argparse.ArgumentParser(description="Automação de notícias de IA (RSS).")
    p.add_argument("--since", type=int, default=7, help="Filtrar últimos N dias (default: 7)")
    p.add_argument("--limit", type=int, default=50, help="Limite de itens (default: 50)")
    p.add_argument("--format", choices=["print","csv","json","markdown"], default="print", help="Formato de saída")
    p.add_argument("--out", type=str, default="", help="Arquivo de saída (csv/json/md)")
    return p.parse_args()

def main():
    args = parse_args()
    raw = fetch_entries(FEEDS)
    print(f"[FETCH] total itens: {len(raw)}")
    # próximos passos: normalizar, filtrar, exportar...

if __name__ == "__main__":
    main()
