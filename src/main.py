
from file_reader import FileReader
from text_reader import TextReader


def main():
    path = FileReader(r"C:\Users\User\Documents\meow.txt")
    path.size()
    path.name()
    print_file = TextReader(r"C:\Users\User\Documents\meow.txt")
    print_file.read()


if __name__ == '__main__':
    main()
