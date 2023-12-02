from solution.common import get_lines_from_file
from solution.day02 import sum_possible_games

first_part_cubes = {
        'red':   12,
        'green': 13,
        'blue':  14
    }

def test_first_part_example():
    lines = get_lines_from_file('./data/day02/example01.data')
    assert sum_possible_games(lines, first_part_cubes) == 8

def test_first_part_solution():
    lines = get_lines_from_file('./data/day02/input.data')
    assert sum_possible_games(lines, first_part_cubes) == 2278
