from solution.common import get_lines_from_file
from solution.day02 import sum_possible_games, get_sum_of_the_powers

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

def test_second_part_example():
    lines = get_lines_from_file('./data/day02/example01.data')
    assert get_sum_of_the_powers(lines) == 2286

def test_second_part_solution():
    lines = get_lines_from_file('./data/day02/input.data')
    assert get_sum_of_the_powers(lines) == 67953
