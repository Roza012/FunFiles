
from FunFiles.file_reader import FileReader
from csv_reader import CsvReader
from text_reader import TextReader


def main():
    path = FileReader(r"C:\Users\User\Documents\meow.txt")
    path.size()
    path.name()
    print_file = TextReader(r"C:\Users\User\Documents\meow.txt")
    # print_file.read()
    csv_file = CsvReader(r"C:\Users\User\Documents\csv_file.csv")
    csv_file.read(6)


if __name__ == '__main__':
    main()
