import os.path

from FunFiles.file_reader import FileReader


class TextReader(FileReader):
    def check(self):
        name = FileReader.name(self)
        split_name = name.split(".")
        if split_name[-1] == "txt":
            return True

    def read(self):
        with open(self.file_path, "r") as my_file:
            data = my_file.read()
            print(data)
