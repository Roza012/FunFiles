
from FunFiles.file_reader import FileReader


class TextReader(FileReader):

    def read(self):
        with open(self.file_path, "r") as my_file:
            data = my_file.read()
            print(data)
