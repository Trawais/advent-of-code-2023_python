import os
from common import get_lines_from_file

lines = get_lines_from_file(os.environ.get('DATA_FILE'))

def __parse_races(lines):
    races = {
        'time': [],
        'distance': []
    }
    for line in lines:
        for number in line.split(':')[1].strip().split(' '):
            if number:
                if "Time:" in line:
                    races['time'].append(int(number))
                else:
                    races['distance'].append(int(number))

    return races

def __get_result(races: dict):
    multiplied_result = 1
    for race_number, time in enumerate(races['time']):
        distance = races['distance'][race_number]
        sum = 0
        for speed in range(1, time): # holding the button time equals the speed actually
            rest_of_the_time = time - speed
            travelled_distance = rest_of_the_time * speed
            if travelled_distance > distance:
                sum += 1
        multiplied_result *= sum
    return multiplied_result

def first():
    races = __parse_races(lines)
    return __get_result(races)


def second():
    for line in lines:
        line = line.replace(' ', '')
        number = int(line.split(':')[1])
        if "Time:" in line:
            time = number
        else:
            distance = number
    races = {
        'time': [time],
        'distance': [distance]
    }
    return __get_result(races)


if __name__ == "__main__":
    print(f"First part: {first()}")
    print(f"Second part: {second()}")
