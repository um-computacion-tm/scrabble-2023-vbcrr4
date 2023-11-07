from game.tiles import *
from game.player import *
from game.dictionary import *
TRIPLE_WORD_SCORE = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
DOUBLE_WORD_SCORE = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2),
                    (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10))
TRIPLE_LETTER_SCORE = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
DOUBLE_LETTER_SCORE = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11),
                        (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))
class NoCentreLocationExeption(Exception):
    pass
class InvalidDirectionExeption(Exception):
    pass
class OutOfBoardExeption(Exception):
    pass
class EmptyWordExeption(Exception):
    pass
class NoEmptySquareExeption(Exception):
    pass

class Board:
    def __init__(self):
        self.grid = [[Cell(1, '', row=row, col=col) for col in range(15)] for row in range(15)]
        self.add_premium_cells()

    def __repr__(self):
        board_str = "   |  " + "  |  ".join(str(item) for item in range(10)) + "  | " + "  | ".join(str(item) for item in range(10, 15)) + " |"
        board_str += "\n   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n"
        board = list(self.grid)
        for i in range(len(board)):
            if i < 10:
                board[i] = str(i) + "  | " + " | ".join(str(item) for item in board[i]) + " |"
            if i >= 10:
                board[i] = str(i) + " | " + " | ".join(str(item) for item in board[i]) + " |"
        board_str += "\n   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|\n".join(board)
        board_str += "\n   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"
        return board_str

    
    def premium_squares(self, coordinate, multiplier_type, multiplier_value):
        cell = self.grid[coordinate[0]][coordinate[1]]
        cell.multiplier_type = multiplier_type
        cell.multiplier = multiplier_value

    def add_premium_cells(self):
        for coordinate in TRIPLE_WORD_SCORE:
            self.premium_squares(coordinate, "word", 3)
        for coordinate in DOUBLE_WORD_SCORE:
            self.premium_squares(coordinate, "word", 2)
        for coordinate in TRIPLE_LETTER_SCORE:
            self.premium_squares(coordinate, "letter", 3)
        for coordinate in DOUBLE_LETTER_SCORE:
            self.premium_squares(coordinate, "letter", 2)
   
    def calculate_word_value(self, word):
        total_value = 0
        for cell in word:
            if cell.multiplier_type == 'letter':
                letter_value = cell.tile.value * cell.multiplier
                total_value += letter_value
            else:
                total_value += cell.tile.value
                total_value *= cell.multiplier
                cell.multiplier_type = None

        return total_value


    def check_crossword(self, row, col, word):
        # Verificar si se forman palabras cruzadas en fila y columna
        return any(self.check_word_in_row(row, col, word)) or any(self.check_word_in_column(row, col, word))

    def check_word_in_row(self, row, col, word):
        # Verificar si se forma una palabra en la fila
        left_col = col
        right_col = col
        while left_col > 0 and self.grid[row][left_col - 1].tile is not None:
            left_col -= 1
        while right_col < 14 and self.grid[row][right_col + 1].tile is not None:
            right_col += 1

        return [self.grid[row][i] for i in range(left_col, right_col + 1)]

    def check_word_in_column(self, row, col, word):
        # Verificar si se forma una palabra en la columna
        top_row = row
        bottom_row = row
        while top_row > 0 and self.grid[top_row - 1][col].tile is not None:
            top_row -= 1
        while bottom_row < 14 and self.grid[bottom_row + 1][col].tile is not None:
            bottom_row += 1

        return [self.grid[i][col] for i in range(top_row, bottom_row + 1)]

    def calculate_crossword_score(self, row, col): #REVISAR
        # Calcular el valor de una palabra cruzada en una fila o columna dada
        word = self.check_word_in_row(row, col, word)
        if word:
            return self.calculate_word_value(word)
        else:
            word = self.check_word_in_column(row, col, word)
            return self.calculate_word_value(word)

    def place_word(self, word, location, direction):
        self.word_is_in_side(word, location, direction)
        self.correct_direcction(direction)
        word = word.upper()
        word_length = len(word)
        if word_length < 1:
            return False
        direction_lower = direction.lower()
        for i in range(word_length):
            if direction_lower == "right":
                row = location[0]
                col = location[1] + i
            elif direction_lower == "down":
                row = location[0] + i
                col = location[1]
            if self.grid[row][col].tile is not None:
                raise NoEmptySquareExeption ("No se puede colocar la palabra aquí, la casilla no está vacía.")
            self.grid[row][col].tile = word[i]
    def validate_first_move(self, round_number, location):
        if round_number == 1 and location != (7,7):
            raise NoCentreLocationExeption("Tu primer movimiento debe ser sobre la celda (7,7).")
        return True
            
    def correct_direcction(self,direction):
        if direction.lower() not in ["right", "down"]:
            raise InvalidDirectionExeption("Dirección no válida. Debe ser 'right' o 'down'.")
        return True
    def word_is_in_side (self,word,location,direction):
        word_length = len(word)
        if (direction.lower() == "right" and location[1] + word_length > 15) or (direction.lower() == "down" and location[0] + word_length > 15):
            raise OutOfBoardExeption("No hay suficiente espacio para colocar la palabra en esa dirección.")
        return True
 
    def validate_crossing_words(self, word, location, orientation):
        for i, current_tile in enumerate(word):
            row, col = (location[0], location[1] + i) if orientation == True else (location[0] + i, location[1])
            cell = self.grid[row][col]
            if cell.tile is not None and cell.tile is not current_tile:
                return True
        return False
    def is_empty(self):
        if self.grid[7][7].tile is None:
            return True
    

class Cell:
    def __init__(self, multiplier=1, multiplier_type="letter", tile: Tile = None, row=0, col=0):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.multiplier_active = True
        self.tile = tile
        self.row = row
        self.col = col
    def add_letter(self, letter:Tile,row,col):
        self.tile = letter
        self.row = row
        self.col = col

    def calculate_value(self):
        if self.tile is None:
            return 0
        if self.multiplier_type == "letter":
            value = self.tile.value * self.multiplier
            self.multiplier_type = None
            self.multiplier_active = False                
            return value
        else:
            return self.tile.value
        
    def __repr__(self):
        return f"Cell(tile={self.tile}-multiplier={self.multiplier}-multiplier_type={self.multiplier_type}-row={self.row}-col={self.col})"
    