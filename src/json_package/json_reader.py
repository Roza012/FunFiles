"""
Purpose: To read json_package file and print his keys.
Auther: Roza Hadid
Date: 5.3.2024
"""
import json

from src.file_reader import FileReader


class JsonReader(FileReader):
    """
    Class that hair from FileReader class.
    Read and print keys from the file that it gets.
    """
    def read(self):
        """
        Reading a json_package file and print then print te keys.
        """
        with open(self.file_path, 'r') as my_json_file:
            contact = json.load(my_json_file)
            print(contact.keys())
