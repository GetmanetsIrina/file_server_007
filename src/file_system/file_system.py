import os
from src import utils


def read_file(filename):
    with open(filename, "r") as f:
        data = f.read()
    return data


def get_unique_file_name(length):
    filename = utils.get_random_string(length)
    while os.path.isfile(filename) or os.path.isdir(filename):
        filename = utils.get_random_string(length)
    return filename


def create_file(content, prefix_length):
    file_name = get_unique_file_name(prefix_length)
    with open(file_name, "w") as f:
        f.write(content)
    return file_name


def delete_file(filename):
    os.remove(filename)


def list_dir():
    os.listdir()


def change_dir(directory):
    dir_path = os.path.abspath(directory)
    if os.getcwd() != dir_path:
        os.chdir(dir_path)
        return True
    return False
