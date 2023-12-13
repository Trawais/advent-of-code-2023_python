import re

def __has_special_symbol(input_list: list[str]):
    for symbol in input_list:
        if not symbol.isdigit() and symbol != '.':
            return True
    return False

def __get_neighbors(lines, line_number, number_match):
    neighbors = []
    for row_offset in [-1, 0, 1]:
        row = line_number + row_offset
        for col in range(number_match.start()-1, number_match.end()+1):
            if 0 <= row < len(lines) and 0 <= col < len(lines[row]): neighbors += lines[row][col]
    return neighbors


def sum_engine_parts(lines: list[str]) -> int:
    sum = 0
    for line_number, line in enumerate(lines):
        for number in re.finditer(r"\d+", line):
            neighbors = __get_neighbors(lines, line_number, number)
            if __has_special_symbol(neighbors):
                sum += int(number.group())

    return sum

def sum_gear_ratios(lines: list[str]) -> int:
    sum = 0
    engine_parts = set()
    for line_number, line in enumerate(lines):
        for match in re.finditer(r"[*]{1}", line):
            gear_position_set = set([i for i in range(match.start()-1, match.end()+1)])
            for r in [-1 , 0, 1]:
                for number in re.finditer(r"\d+", lines[line_number + r]):
                    number_position_set = set([i for i in range(number.start(), number.end())])
                    if number_position_set.intersection(gear_position_set):
                        engine_parts.add(int(number.group()))
            if len(engine_parts) >= 2:
                temp_result = 1
                for part in engine_parts:
                    temp_result *= part
                sum += temp_result
            engine_parts.clear()

    return sum
