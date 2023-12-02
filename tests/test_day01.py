from src import day01

def test_first_part_example():
    file = open('./tests/data/day01/example.data', 'r')
    lines = file.readlines()
    file.close()

    assert sum_numbers(lines) == 142
