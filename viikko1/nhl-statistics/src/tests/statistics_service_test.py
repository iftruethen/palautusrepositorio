import unittest
from statistics_service import StatisticsService
from player import Player

# Stub-luokka, palauttaa kovakoodatun pelaajalistan
class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),   # 16 pistettä
            Player("Lemieux", "PIT", 45, 54),  # 99 pistettä
            Player("Kurri",   "EDM", 37, 53),  # 90 pistettä
            Player("Yzerman", "DET", 42, 56),  # 98 pistettä
            Player("Gretzky", "EDM", 35, 89)   # 124 pistettä
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # Injectataan stub StatisticsService-luokalle
        self.stats = StatisticsService(PlayerReaderStub())

    # --- TESTAA SEARCH-METODI ---
    def test_search_existing_player(self):
        player = self.stats.search("Kurri")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Kurri")

    def test_search_nonexistent_player_returns_none(self):
        player = self.stats.search("Nonexistent")
        self.assertIsNone(player)

    # --- TESTAA TEAM-METODI ---
    def test_team_returns_correct_players(self):
        edm_players = self.stats.team("EDM")
        self.assertEqual(len(edm_players), 3)
        names = [p.name for p in edm_players]
        self.assertIn("Semenko", names)
        self.assertIn("Kurri", names)
        self.assertIn("Gretzky", names)

    def test_team_with_no_players_returns_empty_list(self):
        empty_team = self.stats.team("XYZ")
        self.assertEqual(empty_team, [])

    # --- TESTAA TOP-METODI ---
    def test_top_returns_correct_number_of_players(self):
        top_3 = self.stats.top(2)  # top(2) = 3 pelaajaa (huom: indeksi <= how_many)
        self.assertEqual(len(top_3), 3)
        # Ensimmäinen pistepörssissä pitäisi olla Gretzky
        self.assertEqual(top_3[0].name, "Gretzky")
        self.assertEqual(top_3[0].points, 124)
        # Toiseksi pistepörssissä Lemieux
        self.assertEqual(top_3[1].name, "Lemieux")
        self.assertEqual(top_3[1].points, 99)
        # Kolmanneksi Yzerman
        self.assertEqual(top_3[2].name, "Yzerman")
        self.assertEqual(top_3[2].points, 98)

    def test_top_with_how_many_zero_returns_first_player(self):
        top_0 = self.stats.top(0)
        self.assertEqual(len(top_0), 1)
        self.assertEqual(top_0[0].name, "Gretzky")
        self.assertEqual(top_0[0].points, 124)

    """
    def test_top_with_how_many_larger_than_list(self):
        top_10 = self.stats.top(10)
        # Listassa on vain 5 pelaajaa
        self.assertEqual(len(top_10), 5)
        # Ensimmäinen edelleen Gretzky
        self.assertEqual(top_10[0].name, "Gretzky")
    """