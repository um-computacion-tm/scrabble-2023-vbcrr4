from game.tiles import Tile
TRIPLE_WORD_SCORE = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
DOUBLE_WORD_SCORE = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2),
                    (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10))
TRIPLE_LETTER_SCORE = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
DOUBLE_LETTER_SCORE = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11),
                        (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))
class Board:
    def __init__(self):
        #self.grid = [[Cell(1, '', row=row, col=col) for col in range(15)] for row in range(15)] 
        self.grid = [
            [ Cell(1, '') for _ in range(15) ]
            for _ in range(15)
        ]

    def show_board(self):
        print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(15)]))
        for row_index, row in enumerate(self.grid):
            print(
                str(row_index).rjust(2) +
                '| ' +
                ' '.join([repr(cell) for cell in row])
            )
    def cells_multiplier(self):
        for coordinate in TRIPLE_WORD_SCORE:
            self.cell_multiplier(coordinate, "word", 3)
        for coordinate in DOUBLE_WORD_SCORE:
            self.cell_multiplier(coordinate, "word", 2)
        for coordinate in TRIPLE_LETTER_SCORE:
            self.cell_multiplier(coordinate, "letter", 3)
        for coordinate in DOUBLE_LETTER_SCORE:
            self.cell_multiplier(coordinate, "letter", 2)

    def cell_multiplier(self,coordinate, multiplier_type, multiplier_value):
        cell = self.grid[coordinate[0]][coordinate[1]]
        cell.multiplier_type = multiplier_type
        cell.multiplier = multiplier_value    

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
    
    def put_words(self, word_list_of_tiles, location, orientation):
        self.validate_word(word_list_of_tiles, location, orientation)
        len_word = len(word_list_of_tiles)
        row, col = location
        row_increment, col_increment = (0, 1) if orientation == 'H' else (1, 0)
    # Place the tiles on the board
        for i in range(len_word):
            if self.grid[row][col].tile is None: 
                self.grid[row][col].tile = word_list_of_tiles[i] 
            row += row_increment
            col += col_increment

    def validate_word (self, word, location, orientation):
        len_word = len(word)

        if (orientation == "H" and location[0] + len_word >= 15) or (orientation == "V" and location[1] + len_word >= 15):
            return False
        else:
            return True
class Cell:
    def __init__(self, letter=None, multiplier=1, multiplier_type='',multiplier_active=True, tile: Tile = None):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = letter
        self.multiplier_active = multiplier_active
        self.tile = tile

    def add_letter(self, letter:Tile):
        self.letter = letter

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.letter.value * self.multiplier
        else:
            return self.letter.value
        
    def __repr__(self):
        if self.letter:
            return repr(self.letter)
        if self.multiplier > 1:
            return f'{"W" if self.multiplier_type == "word" else "L"}x{self.multiplier}'
        else:
            return '   '
