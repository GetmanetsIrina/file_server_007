import os
from src import utils
import logging


def read_file(filename: str) -> str:
    """
    Read a file content
    :param filename: The name of file for reading
    :return: the file content
    """
    logging.getLogger("telemetry").info("start reading")
    with open(filename, "r") as f:
        data = f.read()
        logging.info("File data is read")
        logging.getLogger("telemetry").info("stop reading")
    return data


def get_unique_file_name(length: int) -> str:
    """
    Creates a file name string

    :param length: the length of prefix for file name
    :return: the file name
    """
    filename = utils.get_random_string(length)
    while os.path.isfile(filename) or os.path.isdir(filename):
        filename = utils.get_random_string(length)
        logging.info("Random name creation")
    return filename


def create_file(content: str, prefix_length: int) -> str:
    """
    Creates a new file and writes the content to created file

    :param content: the content of file for writing
    :param prefix_length: the length of prefix for file name
    :return: the file name
    """
    file_name = get_unique_file_name(prefix_length)
    with open(file_name, "w") as f:
        f.write(content)
        logging.info("File data is written")
    return file_name


def delete_file(filename: str):
    """
    Deletes a file

    :param filename: the file name for deleting
    :return: none
    """
    os.remove(filename)
    logging.info("Remove File")


def list_dir() -> list:
    """
    Gives the list of directories in the current one

    :return: the list of the directories
    """
    return os.listdir()
    logging.info("Ls")


def change_dir(directory: str) -> bool:
    """
    Changes the current directory

    :param directory: a directory go to
    :return: a result of the operation, True in case of the directory has been changed, False - otherwise
    """
    dir_path = os.path.abspath(directory)
    if os.getcwd() != dir_path and os.path.isdir(dir_path):
        os.chdir(dir_path)
        return True
    return False

def get_file_metadata(filename: str):
    """
    Gets the metadata of file: creation data, modification data, size
    :param filename: file name to get metadata of
    :return: file metadata in case of file existence, None - otherwise
    """
    if os.path.isfile(filename):
        data = os.stat(filename)
        out = {'creation_data': data.st_atime, 'mod_data': data.st_mtime, 'size': data.st_size}
        return out
    logging.warning(f"File {filename} does not exist")
    return None
