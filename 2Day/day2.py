import re

def main():
    with open("input.txt", encoding="utf-8") as f:
        data = f.read()

    inputs = list(filter(lambda word : len(word) >= 2, data.split('\n')))

#    inputs = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
#'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
#'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
#'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
#'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',]

    games = []

    for i in inputs:
        games.append(parse_game(i))

    id_sum = 0
    power_sum = 0
    for game in games:
        power_sum += max_each(game)
        #if is_valid(game, 12, 14, 13):
        #    id_sum += game.game_num
        #print(game.game_num)
        #for ball_set in game.balls:
        #    print("red:", ball_set.red,"green:", ball_set.green,"blue:", ball_set.blue)
    print(power_sum)

def parse_game(game):
    game_and_balls = game.split(':')
    game_num = int(re.search(r'(\d)+', game_and_balls[0]).group(0))
    str_ball_sets = game_and_balls[1].split(';')
    ball_sets = []
    for sets in str_ball_sets:
        split_set = sets.split(',')
        red = 0
        blue = 0
        green = 0
        for thing in split_set:
            if 'red' in thing:
                red = int(re.search(r'(\d)+', thing).group(0))
                continue
            if 'blue' in thing:
                blue = int(re.search(r'(\d)+', thing).group(0))
                continue
            if 'green' in thing:
                green = int(re.search(r'(\d)+', thing).group(0))
                continue
        ball_sets.append(BallSet(red, blue, green))
    full_game = Game(game_num, ball_sets)
    return full_game

def max_each(game):
    max_red = 0
    max_blue = 0
    max_green = 0

    for ball_set in game.balls:
        max_red = max_red if max_red > ball_set.red else ball_set.red
        max_green = max_green if max_green > ball_set.green else ball_set.green
        max_blue = max_blue if max_blue > ball_set.blue else ball_set.blue
        print(max_red, max_green, max_blue)
    return max_red * max_blue * max_green

def is_valid(game, max_red, max_blue, max_green):
    for ball_set in game.balls:
        if ball_set.red > max_red or ball_set.blue > max_blue or ball_set.green > max_green:
            return False

    return True

class BallSet:
    def __init__(self, red, blue, green):
        self.red = red
        self.blue = blue
        self.green = green

class Game:
    def __init__(self, game_num, balls):
        self.game_num = game_num
        self.balls = balls

if __name__ == "__main__":
    main()