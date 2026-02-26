import requests
import datetime

PLAYER_ID = 410446
API_BASE_URL = "https://api.sofascore.com/api/v1/player"

def fetch_player_results(player_id, limit=6):
    url = f"{API_BASE_URL}/{player_id}/events/last/0"
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    resp = requests.get(url, headers=headers, timeout=10)
    data = resp.json()
    results = data.get("events", [])[:limit]
    return results

def fetch_player_upcoming(player_id, limit=6):
    url = f"{API_BASE_URL}/{player_id}/events/next/0"
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    resp = requests.get(url, headers=headers, timeout=10)
    data = resp.json()
    events = data.get("events", [])[:limit]
    return events

def get_player_events_and_results(player_name="Gian van Veen", results_limit=6, upcoming_limit=6):
    results = fetch_player_results(PLAYER_ID, results_limit)
    upcoming = fetch_player_upcoming(PLAYER_ID, upcoming_limit)
    return {
        "player_id": PLAYER_ID,
        "player_name": player_name,
        "results": results,
        "upcoming": upcoming,
        "scraped_at": datetime.datetime.now().isoformat()
    }
