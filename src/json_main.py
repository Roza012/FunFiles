"""
Author: Roza Hadid
Purpose: Import from another module and run them.
Date: 6.3.2024
"""
from file_reader import FileReader
from src.json_reader.json_reader import JsonReader


def main():
    """ Entry point """
    path = FileReader(r"C:\Users\User\Documents\meow.txt")
    path.size()
    path.name()
    json_file_path = JsonReader(r"C:\Users\User\PycharmProjects\FunFiles\src\json_reader\json_file.json")
    json_file_path.read()


if __name__ == '__main__':
    main()
