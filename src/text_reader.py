
"""
Purpose: To read and print a file.
Auther: Roza Hadid
Date: 5.3.2024
"""
from src.file_reader import FileReader


class TextReader(FileReader):
    """
    Class that hair from FileReader class.
    Have a function that read and print file.
    """
    def read(self):
        """
        Read a file and print his content.
        """
        with open(self.file_path, "r") as my_file:
            data = my_file.read()
            print(data)
