import os
from common import get_lines_from_file

lines = get_lines_from_file(os.environ.get('DATA_FILE'))

def __get_cards(lines):
    cards = []
    for line in lines:
        camel_cards, bid = line.split(' ')
        cards.append([camel_cards, int(bid)])
    return cards

def __get_frequency(input_string):
    frequency = {}
    for char in input_string:
        if char in frequency.keys():
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def __get_type(freq: dict):
    values = list(freq.values())
    values.sort()
    if [5] == values: # five of a kind
        return '90'
    elif [1, 4] == values: # four of a kind
        return '80'
    elif [2, 3] == values: # full house
        return '70'
    elif [1, 1, 3] == values: # three of a kind
        return '60'
    elif [1, 2, 2] == values: # two pair
        return '50'
    elif [1, 1, 1, 2] == values: # one pair
        return '40'
    else:
        return '30'

def __transform_card_to_number(card, with_joker=False):
    transform_hash_table = {
        'A': '14',
        'K': '13',
        'Q': '12',
        'J': '11',
        'T': '10',
        '9': '09',
        '8': '08',
        '7': '07',
        '6': '06',
        '5': '05',
        '4': '04',
        '3': '03',
        '2': '02',
    }
    if with_joker and card == 'J':
        return '01'
    return transform_hash_table[card]

def __total_winnings(cards):
    result = 0
    for rank, card in enumerate(cards, start=1):
        result += rank * card[1]
    return result

def sorting_fnc(item):
    freq = __get_frequency(item[0])
    rank_string = __get_type(freq)
    for card in item[0]:
        rank_string += __transform_card_to_number(card)
    return int(rank_string)

def sorting_fnc_second(item):
    freq = __get_frequency(item[0])
    if 'J' in freq.keys() and freq['J'] != 5: # The full hand of jokers must be treated in special way
        number_of_jokers = freq.pop('J')
        sorted_freq = sorted(freq.items(), key=lambda x:x[1])
        freq_key = sorted_freq[-1][0]
        freq[freq_key] += number_of_jokers
    rank_string = __get_type(freq)
    for card in item[0]:
        rank_string += __transform_card_to_number(card, with_joker=True)
    return int(rank_string)

# ####################
def first():
    cards = __get_cards(lines)
    cards.sort(key=sorting_fnc)
    return __total_winnings(cards)


def second():
    cards = __get_cards(lines)
    cards.sort(key=sorting_fnc_second)
    return __total_winnings(cards)

if __name__ == "__main__":
    print(f"First part: {first()}")
    print(f"Second part: {second()}")
