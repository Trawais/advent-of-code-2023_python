from solution.day03 import sum_engine_parts, sum_gear_ratios
from solution.common import get_lines_from_file

def test_first_part_example():
    lines = get_lines_from_file('./data/day03/example.data')
    assert sum_engine_parts(lines) == 4361

def test_first_part_solution():
    lines = get_lines_from_file('./data/day03/input.data')
    assert sum_engine_parts(lines) == 529618

def test_second_part_example():
    lines = get_lines_from_file('./data/day03/example.data')
    assert sum_gear_ratios(lines) == 467835

def test_second_part_solution():
    lines = get_lines_from_file('./data/day03/input.data')
    assert sum_gear_ratios(lines) == 77509019
