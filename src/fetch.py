from typing import List, Dict
import feedparser

def fetch_entries(feed_urls: Dict[str, str]) -> List[Dict]:
    items = []
    for key, url in feed_urls.items():
        parsed = feedparser.parse(url)
        for e in parsed.entries:
            items.append({
                "source": key,
                "title": getattr(e, "title", "").strip(),
                "link": getattr(e, "link", "").strip(),
                "summary": getattr(e, "summary", "")[:800].strip(),
                "published": getattr(e, "published", "") or getattr(e, "updated", ""),
            })
    return items
