import os
from common import get_lines_from_file
from multiprocessing import Pool

lines = get_lines_from_file(os.environ.get('DATA_FILE'))

def __process_input(lines):
    maps = []
    for line_number, line in enumerate(lines):
        if line_number == 0: # line with seeds
            seeds = [int(i) for i in line.split(':')[1].strip().split(' ')]
            continue
        if not line: # empty line
            maps.append([])
            continue
        if ":" in line:
            continue
        maps[-1].append([int(i) for i in line.split(" ")])
    return seeds, maps

def __find_min_location_seed(seeds, maps):
    print(f"Finding minimal location for {len(seeds)} seeds")
    min_seed = float('inf')
    for seed in seeds:
        for map in maps:
            for map_row in map:
                destination, source, length = map_row
                if source <= seed and seed < (source + length):
                    offset = seed - source
                    seed = offset + destination
                    break
        if seed < min_seed:
            min_seed = seed
    return min_seed

def task_second(seed_start, seed_length, maps):
    print(f"seed_start: {seed_start}")
    print(f"seed_length: {seed_length}")
    seeds = [s for s in range(seed_start, seed_start + seed_length)]
    print(f"Length of seeds: {len(seeds)}")

    return __find_min_location_seed(seeds, maps)

def first():
    seeds, maps = __process_input(lines)
    return __find_min_location_seed(seeds, maps)

def second():
    seeds, maps = __process_input(lines)
    inputs = []
    for i in range(0, len(seeds), 2):
        seed_start, seed_length = seeds[i], seeds[i+1]
        inputs.append((seed_start, seed_length, maps))

    with Pool() as pool:
        minimal_location = float('inf')
        for result in pool.starmap(task_second, inputs):
            print(f"result: {result}")
            if result < minimal_location:
                minimal_location = result
    return minimal_location



if __name__ == "__main__":
    print(f"First part: {first()}")
    print(f"Second part: {second()}")
