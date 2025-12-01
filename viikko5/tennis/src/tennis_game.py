class TennisGame:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_points += 1
        else:
            self.player2_points += 1

    def get_score(self):
        if self.player1_points == self.player2_points:
            return self._tie_score()

        if self.player1_points >= 4 or self.player2_points >= 4:
            return self._advantage_or_win_score()

        return self._normal_score()

    # --- Private helper methods ---

    def _tie_score(self):
        if self.player1_points < 3:
            return f"{self.SCORE_NAMES[self.player1_points]}-All"
        return "Deuce"

    def _advantage_or_win_score(self):
        diff = self.player1_points - self.player2_points

        if diff == 1:
            return "Advantage player1"
        if diff == -1:
            return "Advantage player2"
        if diff >= 2:
            return "Win for player1"
        return "Win for player2"

    def _normal_score(self):
        return f"{self.SCORE_NAMES[self.player1_points]}-{self.SCORE_NAMES[self.player2_points]}"
