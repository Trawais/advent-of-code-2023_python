import os
from common import get_lines_from_file

lines = get_lines_from_file(os.environ.get('DATA_FILE'))

def first():
    pass

def second():
    pass

if __name__ == "__main__":
    print(f"First part: {first()}")
    print(f"Second part: {second()}")
