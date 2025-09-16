from typing import List, Dict
from dateutil import parser as dateparser

def _parse_date(s: str):
    if not s: return None
    try: return dateparser.parse(s)
    except Exception: return None

def normalize(items: List[Dict]) -> List[Dict]:
    out = []
    for it in items:
        dt = _parse_date(it.get("published",""))
        out.append({ **it, "published_dt": dt })
    return out

def dedupe(items: List[Dict]) -> List[Dict]:
    seen = set()
    out = []
    for it in items:
        key = (it.get("title","").lower().strip(), it.get("link","").lower().strip())
        if key in seen: continue
        seen.add(key); out.append(it)
    return out

def filter_since(items: List[Dict], days: int) -> List[Dict]:
    if days is None: return items
    from datetime import datetime, timedelta, timezone
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    out = []
    for it in items:
        dt = it.get("published_dt")
        if dt is None or (dt.tzinfo is None):
            out.append(it)
        elif dt >= cutoff:
            out.append(it)
    return out
