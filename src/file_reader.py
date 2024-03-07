"""
Purpose: Return the name and the size of a file.
Auther: Roza Hadid
Date: 5.3.2024
"""
import os
from abc import abstractmethod


class FileReader:
    """
    Gets path and check that it is a path for file, then return the size and th name of it.
    """
    def __init__(self, file_path):
        """
        Initialize class and check if the path is file.
        :param file_path: Path that the function receive.
        """
        if os.path.isfile(file_path):
            self.file_path = file_path

    def size(self) -> int:
        """
        Returning the size of the file by using the module os.
        :return: File size
        """
        file_size = os.stat(self.file_path).st_size
        return file_size

    def name(self) -> str:
        """
        Returning the name of the file by using the module os.
        :return: File name.
        """
        file_name = os.path.basename(self.file_path)
        return file_name

    @abstractmethod
    def read(self):
        """
        Abstract methods that read the text from a file.
        """
        pass
