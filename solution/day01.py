import re

def sum_numbers(lines):
    sum = 0
    for line in lines:
        left_match = re.search(r"^.*?(\d)", line)
        right_match = re.search(r"(\d)[^\d]*?$", line)
        number = int(f"{left_match.group(1)}{right_match.group(1)}", 10)
        sum += number

    return sum

def __normalize_number(number: str):
    hash_map = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    if number in hash_map.keys():
        return hash_map[number]
    return number

def sum_numbers_2(lines):

    sum = 0
    for line in lines:
        left_match = re.search(r"^.*?(\d|one|two|three|four|five|six|seven|eight|nine)", line)
        right_match = re.search(r".*(\d|one|two|three|four|five|six|seven|eight|nine).*?$", line)

        left_number = __normalize_number(left_match.group(1))
        right_number = __normalize_number(right_match.group(1)
                                          )
        number = int(f"{left_number}{right_number}", 10)
        sum += number

    return sum
