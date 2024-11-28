FILEPATH = "todos.txt"

def read_file(file_path=FILEPATH):
    try:
        with open(file_path) as f:
            return f.readlines()
    except FileNotFoundError:
        with open(file_path, "w"):
            return []


def write_file(to_do, file_path=FILEPATH):
    with open(file_path, "w") as f:
        f.writelines(to_do)