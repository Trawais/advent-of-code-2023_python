import re

def __is_possible(moves, game_cubes) -> bool:
    for move in moves:
        cubes = re.findall(r"(\d+) (\w+)", move)
        for cube in cubes:
            if int(cube[0]) > game_cubes[cube[1]]:
                return False
    return True

def sum_possible_games(games, game_cubes):
    sum = 0
    for i, line in enumerate(games, start=1):
        moves = line.split(':')[1].split(';')
        if __is_possible(moves, game_cubes):
            sum += i
    return sum
