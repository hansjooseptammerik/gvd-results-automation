import asyncio
import json
import os
from pathlib import Path

from build_payload import build_payload
from sofascore_scraper import fetch_player_matches
from shopify_update import maybe_update_shopify


OUTPUT_PATH = Path("output/gvd_stats.json")


def _env_int(name: str, default: int) -> int:
    try:
        return int(os.getenv(name, str(default)))
    except Exception:
        return default


async def _run() -> None:
    player_name = os.getenv("PLAYER_NAME", "Gian van Veen")
    upcoming_limit = _env_int("UPCOMING_LIMIT", 6)
    results_limit = _env_int("RESULTS_LIMIT", 6)

    data = await fetch_player_matches(
        player_name=player_name,
        upcoming_limit=upcoming_limit,
        results_limit=results_limit,
    )

    payload = build_payload(data["upcoming"], data["results"])

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[ok] Wrote {OUTPUT_PATH}")

    maybe_update_shopify(payload)


def main() -> None:
    asyncio.run(_run())


if __name__ == "__main__":
    main()
