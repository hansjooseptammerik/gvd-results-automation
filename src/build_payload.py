from __future__ import annotations

from dataclasses import asdict
from datetime import datetime
from typing import Any, Dict, List

from sofascore_scraper import MatchItem


def build_payload(upcoming: List[MatchItem], results: List[MatchItem]) -> Dict[str, Any]:
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M")

    def _clean(items: List[MatchItem]) -> List[Dict[str, Any]]:
        out: List[Dict[str, Any]] = []
        for it in items:
            d = asdict(it)
            # Ensure scores are strings (Shopify JSON metafield is strict sometimes)
            d["player1_score"] = str(d.get("player1_score") or "")
            d["player2_score"] = str(d.get("player2_score") or "")
            out.append(d)
        return out

    return {
        "last_updated": now,
        "upcoming": _clean(upcoming),
        "results": _clean(results),
    }
