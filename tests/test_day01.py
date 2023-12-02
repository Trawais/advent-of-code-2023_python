from solution.day01 import sum_numbers, sum_numbers_2
from solution.common import get_lines_from_file

def test_first_part_example():
    lines = get_lines_from_file('./data/day01/example01.data')
    assert sum_numbers(lines) == 142

def test_first_part_solution():
    lines = get_lines_from_file('./data/day01/input.data')
    assert sum_numbers(lines) == 54634

def test_second_part_example():
    lines = get_lines_from_file('./data/day01/example02.data')
    assert sum_numbers_2(lines) == 281

def test_second_part_solution():
    lines = get_lines_from_file('./data/day01/input.data')
    assert sum_numbers_2(lines) == 53855
