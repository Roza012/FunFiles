"""
Purpose: Importing from another moduls to run them.
Auther: Roza Hadid
Date: 5.3.2024
"""
from src.csv_reader import CsvReader
from src.file_reader import FileReader
from src.json.json_reader import JsonReader
from text_reader import TextReader


def main():
    """ Entry point """
    path = FileReader(r"C:\Users\User\Documents\meow.txt")
    path.size()
    path.name()
    print_file = TextReader(r"C:\Users\User\Documents\meow.txt")
    print_file.read()
    csv_file = CsvReader(r"C:\Users\User\Documents\csv_file.csv")
    csv_file.read(6)
    json_file_path = JsonReader(r"C:\Users\User\PycharmProjects\fun_files\json_file.json")
    json_file_path.read()

if __name__ == '__main__':
    main()
