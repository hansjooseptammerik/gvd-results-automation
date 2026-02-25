import os
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, List, Optional

from dateutil import tz

# sofascore-wrapper is async and uses Playwright under the hood.
from sofascore_wrapper.api import SofascoreAPI
from sofascore_wrapper.search import Search
from sofascore_wrapper.player import Player


@dataclass
class MatchItem:
    date: str
    tournament_name: str
    match_stage: str
    player1_name: str
    player2_name: str
    player1_score: str
    player2_score: str
    player1_country: str = ""
    player2_country: str = ""


def _fmt_date_from_ts(ts: Optional[int]) -> str:
    if not ts:
        return ""
    # SofaScore timestamps are seconds.
    dt_utc = datetime.utcfromtimestamp(int(ts)).replace(tzinfo=tz.UTC)
    dt_local = dt_utc.astimezone(tz.gettz(os.getenv("TIMEZONE", "Europe/Tallinn")))
    return dt_local.strftime("%b %d, %Y")


def _safe_get(d: Any, *path: str, default: Any = "") -> Any:
    cur = d
    for k in path:
        if not isinstance(cur, dict) or k not in cur:
            return default
        cur = cur[k]
    return cur


def _score_str(score_obj: Any) -> str:
    if isinstance(score_obj, dict):
        val = score_obj.get("current")
        if val is None:
            val = score_obj.get("display")
        if val is None:
            val = score_obj.get("normaltime")
        if val is None:
            return ""
        return str(val)
    if score_obj is None:
        return ""
    return str(score_obj)


def _to_match_item(event: Dict[str, Any]) -> MatchItem:
    date = _fmt_date_from_ts(event.get("startTimestamp"))

    tournament_name = _safe_get(event, "tournament", "name", default="")
    stage = (
        _safe_get(event, "roundInfo", "name", default="")
        or _safe_get(event, "season", "name", default="")
        or _safe_get(event, "status", "description", default="")
    )

    p1 = _safe_get(event, "homeTeam", "name", default="")
    p2 = _safe_get(event, "awayTeam", "name", default="")

    p1_country = _safe_get(event, "homeTeam", "country", "name", default="")
    p2_country = _safe_get(event, "awayTeam", "country", "name", default="")

    p1_score = _score_str(event.get("homeScore"))
    p2_score = _score_str(event.get("awayScore"))

    return MatchItem(
        date=date,
        tournament_name=tournament_name,
        match_stage=stage,
        player1_name=p1,
        player2_name=p2,
        player1_score=p1_score,
        player2_score=p2_score,
        player1_country=p1_country,
        player2_country=p2_country,
    )


async def fetch_player_matches(
    player_name: str,
    upcoming_limit: int = 6,
    results_limit: int = 6,
) -> Dict[str, List[MatchItem]]:
    """Fetch upcoming and last matches for a player via SofaScore.

    Uses sofascore-wrapper (Playwright-based) to reduce 403/blocked requests.
    """

    api = SofascoreAPI()

    api = SofascoreAPI() search = Search(api, player_name) res = await search.search_all(player_name)
    res = await search.search_all(player_name)

    # The wrapper returns a dict with keys like 'players', 'events', etc.
    players = res.get("players") or []

    if not players:
        raise RuntimeError(f"No SofaScore player found for query: {player_name!r}")

    # Prefer an exact-ish name match.
    def _score_player(p: Dict[str, Any]) -> int:
        name = (p.get("name") or "").lower()
        q = player_name.lower()
        if name == q:
            return 3
        if q in name:
            return 2
        return 1

    players_sorted = sorted(players, key=_score_player, reverse=True)
    player_id = players_sorted[0].get("id")
    if not player_id:
        raise RuntimeError("SofaScore search returned player without id")

    player = Player(api, int(player_id))

    next_events = await player.next_fixtures(page=0)
    last_events = await player.last_fixtures(page=0)

    # Wrapper returns dicts with key 'events'
    next_list = (next_events or {}).get("events") or []
    last_list = (last_events or {}).get("events") or []

    upcoming_items = [_to_match_item(e) for e in next_list[:upcoming_limit]]
    result_items = [_to_match_item(e) for e in last_list[:results_limit]]

    return {"upcoming": upcoming_items, "results": result_items}
