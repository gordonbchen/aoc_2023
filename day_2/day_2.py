import re
from dataclasses import dataclass

with open("day_2/data/data.txt") as f:
    data = f.read().split("\n")

@dataclass
class Game:
    game_id: int
    reds: list[int]
    blues: list[int]
    greens: list[int]
    
    def is_valid(self, max_colors: list[int]):
        for color, max_color in zip([self.reds, self.blues, self.greens], max_colors):
            for i in color:
                if i > max_color:
                    return False
        return True
    
    def power(self):
        power = 1
        for color in [self.reds, self.blues, self.greens]:
            power *= max(color)
        return power

games = []
for line in data:
    game_id_regex = re.compile("Game (\d+):")
    game_id = int(game_id_regex.match(line).group(1))

    reds_blues_greens = []
    for color in ["red", "blue", "green"]:
        color_regex = re.compile(f"(\d+) {color}")
        colors = [int(i) for i in color_regex.findall(line)]
        reds_blues_greens.append(colors)

    game = Game(game_id, *reds_blues_greens)
    games.append(game)

s = 0
for game in games:
    # if game.is_valid([12, 14, 13]):
        # s += game.game_id
    s += game.power()

print(s)