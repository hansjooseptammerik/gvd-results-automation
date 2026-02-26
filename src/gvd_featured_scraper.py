import requests
import json
import datetime
import os

FEATURED_URL = "https://api.sofascore.com/api/v1/team/410446/featured-event"

def fetch_featured_event():
    resp = requests.get(FEATURED_URL, headers={"User-Agent": "Mozilla/5.0"})
    resp.raise_for_status()
    data = resp.json()
    return data

def save_event_to_file(event_data, outpath="output/gvd_featured_event.json"):
    os.makedirs(os.path.dirname(outpath), exist_ok=True)
    out = {
        "scraped_at": datetime.datetime.now().isoformat(),
        "event": event_data.get("featuredEvent", {})
    }
    with open(outpath, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"Saved featured event to {outpath}")

if __name__ == "__main__":
    event_data = fetch_featured_event()
    save_event_to_file(event_data)
