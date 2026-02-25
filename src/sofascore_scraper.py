import requests
from bs4 import BeautifulSoup
import datetime

PLAYER_SOFA_URL = "https://www.sofascore.com/darts/player/van-veen-gian/410446"

def parse_matches(soup_section, limit, section_name):
    matches = []
    rows = soup_section.select("div.styles__MatchCardWrapper-sc-1qsabs6-0")
    for row in rows[:limit]:
        match = {}
        date_elem = row.select_one("div.sc-ecffda1a-7")
        match["date"] = date_elem.text.strip() if date_elem else ""
        event_elem = row.select_one("div.sc-ecffda1a-13")
        match["event"] = event_elem.text.strip() if event_elem else ""
        home_elem = row.select_one("div.styles__OpponentName-sc-1qsabs6-13")
        match["opponent"] = home_elem.text.strip() if home_elem else ""
        score_elem = row.select_one("div.styles__Score-sc-1qsabs6-16")
        match["score"] = score_elem.text.strip() if score_elem else ""
        matches.append(match)
    return matches

def get_player_events_and_results(player_name, upcoming_limit=6, results_limit=6):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    r = requests.get(PLAYER_SOFA_URL, headers=headers, timeout=20)
    r.raise_for_status()
    soup = BeautifulSoup(r.content, "html.parser")

    results_section = soup.find("section", attrs={"id": "player-matches"})
    upcoming_section = soup.find("section", attrs={"id": "player-upcoming-matches"})
    results = []
    upcoming = []
    if results_section:
        results = parse_matches(results_section, results_limit, "results")
    if upcoming_section:
        upcoming = parse_matches(upcoming_section, upcoming_limit, "upcoming")

    out = {
        "player_name": player_name,
        "player_profile_url": PLAYER_SOFA_URL,
        "results": results,
        "upcoming": upcoming,
        "scraped_at": datetime.datetime.now().isoformat()
    }
    return out
