import re

def __is_possible(game, game_cubes) -> bool:
    cubes = re.findall(r"(\d+) (\w+)", game)
    for cube in cubes:
        if int(cube[0]) > game_cubes[cube[1]]:
            return False
    return True

def sum_possible_games(games, game_cubes):
    sum = 0
    for i, game in enumerate(games, start=1):
        game = game.split(':')[1]
        if __is_possible(game, game_cubes):
            sum += i
    return sum

def __get_power(game):
    power = { 'red': 0, 'green': 0, 'blue': 0 }
    cubes = re.findall(r"(\d+) (\w+)", game)
    for cube in cubes:
        number_of_cubes = int(cube[0])
        color_of_cubes = cube[1]
        power[color_of_cubes] = max(number_of_cubes, power[color_of_cubes])
    return power['red'] * power['green'] * power['blue']

def get_sum_of_the_powers(games):
    sum = 0
    for game in games:
        sum += __get_power(game)
    return sum
