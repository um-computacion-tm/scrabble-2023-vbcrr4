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

    def positions(self):
        self.letter_multiplier()
        self.word_multiplier()

    def word_multiplier(self):
        word_multi = [
            (0,0), (7,0), (14,0), (0,7), (0,14), (7,14), (14,14)
        ]
        for i in range(15):
            for j in range(15):
                cell = self.grid[i][j]
                if (i,j) in word_multi:
                    cell.multiplier = 3
                    cell.multiplier_type = 'rata'
                    
        for i in range(15):
            for j in range(15):
                not_there = [0, 5, 6, 7, 8, 9, 14]
                cell = self.grid[i][j]
                if i == j or (i + j == 14):
                    if (i and j) not in not_there:
                        cell.multiplier = 2
                        cell.multiplier_type = 'rata'

    def letter_multiplier(self):
        letter_multi_2 = [
            (3,0), (11,0), (6,2), (8,2), (0,3), (14,3), (7,3),
            (2,6), (6,6), (8,6), (12,6), (3,7), (11,7), (2,8),
            (6,8), (8,8), (12,8), (14,11), (0,11), (7,11), (6,12),
            (8,12), (11,14), (3,14), 
        ]

        letter_multi_3 = [
            (1,5), (1,9), (5,1), (5,5), (5,9), (5,13), (9,1),
            (9,5), (9,9), (9,13), (13,5), (13,9),
        ]
        for i in range(15):
            for j in range(15):
                cell = self.grid[i][j]
                if (i,j) in letter_multi_2:
                    cell.multiplier = 2
                    cell.multiplier_type = 'pensar'
                if (i,j) in letter_multi_3:
                    cell.multiplier = 3
                    cell.multiplier_type = "pensar"

