import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url, timeout=10)
        players_dict = response.json()
        return [Player(player_dict) for player_dict in players_dict]
    def __str__(self):
        return "Data fetcher class"
