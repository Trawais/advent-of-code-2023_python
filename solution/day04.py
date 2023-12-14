import os
from common import get_lines_from_file

lines = get_lines_from_file(os.environ.get('DATA_FILE'))

def __get_count_of_same_numbers(line):
    numbers = line.split(':')[1].split('|')
    winning_numbers = set([int(i) for i in numbers[0].strip().split(' ') if i])
    your_numbers = set([int(i) for i in numbers[1].strip().split(' ') if i])
    return len(your_numbers.intersection(winning_numbers))

def first():
    sum = 0
    for line in lines:
        count_of_same_numbers = __get_count_of_same_numbers(line)
        if count_of_same_numbers >= 1:
            value_of_card = 2 ** (count_of_same_numbers-1)
            sum += value_of_card

    return sum


def second():
    cards = {}
    for card_number, line in enumerate(lines, start=1):
        if card_number not in cards.keys():
            cards[card_number] = 1
        count_of_same_numbers = __get_count_of_same_numbers(line)
        for i in range(1, count_of_same_numbers+1):
            if card_number+i not in cards.keys():
                cards[card_number+i] = 1
            cards[card_number+i] += cards[card_number]

    sum = 0
    for card_value in cards.values():
        sum += card_value
    return sum

if __name__ == "__main__":
    print(f"First part: {first()}")
    print(f"Second part: {second()}")
