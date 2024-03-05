"""
Purpose: To read and print csv file.
Auther: Roza Hadid
Date: 5.3.2024
"""
import csv
from utils import print_cell
from file_reader import FileReader


class CsvReader(FileReader):
    """
    Class that hair from FileReader class.
    Print csv file in order of what number it gets.
    """
    def read(self, num_of_char: int = 5):
        """
        Reading a csv file.
        Print all the cells from this file in limit of the number that the function receive.
        :param num_of_char: The maximum number of litters in the cell to print.
        """
        with open(self.file_path, 'r') as my_csv_file:
            csv_reader = csv.reader(my_csv_file)
            for row in csv_reader:
                for cell in row:
                    print_cell.printing_cell(cell, num_of_char)
                print()
