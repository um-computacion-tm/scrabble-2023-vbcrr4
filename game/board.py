from pyrae import dle
from game.tiles import Tile
class Cell:
    def __init__(self, letter=None, multiplier=1, multiplier_type=''):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = letter

    def add_letter(self, letter:Tile):
        self.letter = letter

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.letter.value * self.multiplier
        else:
            return self.letter.value

class Board:
    def __init__(self):
        self.grid = [
            [ Cell(1, '') for _ in range(15) ]
            for _ in range(15)
        ]
    
    def calculate_word_value(self, word):
        word_value = 0
        word_multiplier = 1

        for cell in word:
            cell_value = cell.calculate_value()
            word_value += cell_value

            if cell.multiplier_type == 'word':
                word_multiplier *= cell.multiplier
                cell.multiplier = 1  # Reinicia el multiplicador de la celda a 1

        word_value *= word_multiplier
        return word_value
    
    def validate_word (self, word, location, orientation):
        len_word = len(word)

        if (orientation == "H" and location[0] + len_word >= 15) or (orientation == "V" and location[1] + len_word >= 15):
            return False
        else:
            return True

    def validate_word_rae(self, word):
        word_to_check = ''
        for cell in word:
            if cell.letter:
                word_to_check += cell.letter.letter

        result = dle.search_by_word(word_to_check)

        if result and 'Versión electrónica 23.6' not in result[0].text:
            return True  # La palabra existe en "pyrae"
        else:
            return False  # La palabra no existe en "pyrae"
