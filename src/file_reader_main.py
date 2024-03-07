"""
Author: Roza Hadid
Purpose: Import from another modules and run them.
Date: 6.3.2024
"""
from file_reader import FileReader
from text_reader import TextReader


def main():
    """ Entry point """
    path = FileReader(r"C:\Users\User\Documents\meow.txt")
    path.size()
    path.name()
    print_file = TextReader(r"C:\Users\User\Documents\meow.txt")
    print_file.read()


if __name__ == '__main__':
    main()
