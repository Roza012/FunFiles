import os
from abc import abstractmethod


class FileReader:
    def __init__(self, file_path):
        if os.path.isfile(file_path):
            self.file_path = file_path

    def size(self):
        file_size = os.stat(self.file_path).st_size
        return file_size

    def name(self):
        file_name = os.path.basename(self.file_path)
        return file_name

    @abstractmethod
    def read(self):
        pass
