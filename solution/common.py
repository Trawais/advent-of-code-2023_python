def get_lines_from_file(file_path: str) -> [str]:
    file = open(file_path, 'r')
    lines = file.readlines()
    file.close()
    return lines
