# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import random
import string


class Game:
    def __init__(self):
        """Attribute a random grid to size 9"""
        # the join method is used to convert the list into a string and ramdom.choices
        # is used to ramdomly choose 9 letters from the string.ascii_uppercase
        self.grid = list(''.join(random.choices(string.ascii_uppercase, k=9)))

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        grid_copy = self.grid.copy() # copy the grid to avoid mutating it and modify it
        if len(word) != 0: # if the word is not empty
            for letter in word: # for each letter in the word
                if letter in grid_copy: # if the letter is in the grid
                    grid_copy.remove(letter) # remove the letter from the grid
                else:
                    return False # if the letter is not in the grid
            return True # if all the letters are in the grid
        else:
            return False #if the word is empty
