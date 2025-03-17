class ScoreRow:
    def __init__(self, position, team, matches_played, wins, draws, losses, goals, diff, points):
        self.position = position
        self.team = team
        self.matches_played = matches_played
        self.wins = int(wins)
        self.draws = int(draws)
        self.losses = int(losses)
        self.gf, self.ga = self.parse_goals(goals)
        self.diff = diff
        self.points = points

    def parse_goals(self, goals):
        splitted = goals.split("-")
        return int(splitted[1]), int(splitted[0])

    def __repr__(self):
        return f"{self.position}| {self.team} - {self.points} pts (W:{self.wins}, D:{self.draws}, L:{self.losses}, GF:{self.gf}, GA:{self.ga})"

    def as_row(self):
        return [
            self.position,
            self.team,
            self.matches_played,
            self.wins,
            self.draws,
            self.losses,
            f"{self.gf}-{self.ga}",
            self.diff,
            self.points,
        ]