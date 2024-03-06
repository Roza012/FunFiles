"""
Purpose: Importing from another moduls to run them.
Auther: Roza Hadid
Date: 5.3.2024
"""
from src.csv_reader import CsvReader
from src.file_reader import FileReader

def main():
    """ Entry point """
    path = FileReader(r"C:\Users\User\Documents\meow.txt")
    path.size()
    path.name()
    csv_file = CsvReader(r"C:\Users\User\Documents\csv_file.csv")
    csv_file.read(6)

if __name__ == '__main__':
    main()
