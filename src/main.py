import os
import json
from sofascore_api_scraper import get_player_events_and_results  # UUS import!
from shopify_update import maybe_update_shopify

def main():
    player_name = os.getenv("PLAYER_NAME", "Gian van Veen")
    results_limit = int(os.getenv("RESULTS_LIMIT", 6))
    upcoming_limit = int(os.getenv("UPCOMING_LIMIT", 6))

    stats = get_player_events_and_results(
        player_name=player_name,
        upcoming_limit=upcoming_limit,
        results_limit=results_limit
    )

    outdir = "output"
    os.makedirs(outdir, exist_ok=True)
    with open(f"{outdir}/gvd_stats.json", "w", encoding="utf-8") as fp:
        json.dump(stats, fp, indent=2, ensure_ascii=False)

    success = maybe_update_shopify(stats)
    if success:
        print("[main] Data successfully uploaded to Shopify metafield.")
    else:
        print("[main] Shopify upload skipped or failed.")

if __name__ == "__main__":
    main()
