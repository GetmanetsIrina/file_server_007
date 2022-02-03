#! /usr/bin/env python3
import argparse
import os
from src import file_system


def read_file():
    filename = input("Enter file name : ")
    if os.path.isfile(filename):
        data = file_system.read_file(filename)
        print(f"Content of file {filename} : {data}")
    else:
        print(f"File {filename} does not exit")


def create_file():
    content = input("Enter file content : ")
    prefix_length = 4
    file_name = file_system.create_file(content, prefix_length)
    print(f"create_file : {file_name}")


def delete_file():
    filename = input("Enter file name : ")
    print(f"delete file : {filename}")
    if os.path.isfile(filename):
        file_system.delete_file(filename)
    else:
        print("File does not exist")


def list_dir():
    print(f"List dir {os.getcwd()}")
    print(os.listdir())


def change_dir():
    directory = input("Enter dir name : ")
    print("Current path " + os.getcwd())
    result = file_system.change_dir(directory)
    if result:
        print("Set path " + os.getcwd())
    else:
        print("Already in current directory")


def main():
    parser = argparse.ArgumentParser(description='Restful File server')
    parser.add_argument('-d', '--directory', dest="path", help='Root directory', required=True)
    args = parser.parse_args()
    file_system.change_dir(args.path)
    print(f"Working directory {os.getcwd()}")

    commands = {
        "get": read_file,
        "create": create_file,
        "delete": delete_file,
        "ls": list_dir,
        "cd": change_dir
    }
    while True:
        command = input("Enter command: ")
        if command == "exit":
            return
        if command not in commands:
            print("Unknown command")
            continue
        command = commands[command]
        try:
            command()
        except Exception as ex:
            print(f"Error on {command} execution : {ex}")


if __name__ == "__main__":
    main()