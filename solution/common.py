def get_lines_from_file(file_path: str) -> list[str]:
    file = open(file_path, 'r')
    lines = file.readlines()
    file.close()
    return [line.strip() for line in lines]
