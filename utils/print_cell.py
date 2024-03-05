"""
Purpose: Contains a function that print the cell according to the difference between the variables.
Auther: Roza Hadid
Date: 5.3.2024
"""


def printing_cell(cell: str, num_of_char: int):
    """
    Getting cell and number of character.
    Check if the difference between the variables positive.
    :param cell: A Variable the function gets.
    :param num_of_char: A Variable the function gets.
    """
    difference = num_of_char - len(cell)
    if difference > 0:
        print(cell[0:num_of_char], end=f"{' ' * difference}| ")
    else:
        print(cell[0:num_of_char], end="| ")
