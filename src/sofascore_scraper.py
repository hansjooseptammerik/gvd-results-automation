from sofascore_wrapper import SofaScore

def get_player_events_and_results(player_name, upcoming_limit=6, results_limit=6):
    sofascore = SofaScore()
    sport = 'darts'

    # Otsi mängija Sofascore'ist
    player_search = sofascore.search(sport=sport, query=player_name)
    players = player_search.get('player', [])
    if not players:
        raise Exception(f"No player found for name: {player_name}")

    player_id = players[0]['id']

    # Viimased tulemused (results)
    results = sofascore.players_results(sport=sport, player_id=player_id, limit=results_limit)
    # Tulevased mängud (fixtures/upcoming)
    upcoming = sofascore.players_fixtures(sport=sport, player_id=player_id, limit=upcoming_limit)

    return {
        "player_id": player_id,
        "player_name": player_name,
        "results": results,
        "upcoming": upcoming
    }
