import re

def sum_numbers(lines):
    sum = 0
    for line in lines:
        left_match = re.search(r"^.*?(\d)", line)
        right_match = re.search(r"(\d)[^\d]*?$", line)
        number = int(f"{left_match.group(1)}{right_match.group(1)}", 10)
        sum += number

    return sum
