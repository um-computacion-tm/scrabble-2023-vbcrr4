from game.tiles import *
from game.player import *
from game.dictionary import *

TRIPLE_WORD_SCORE = ((0,0), (7, 0), (14,0), (0, 7), (14, 7), (0, 14), (7, 14), (14,14))
DOUBLE_WORD_SCORE = ((1,1), (2,2), (3,3), (4,4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2),
                    (11, 3), (10, 4), (13,13), (12, 12), (11,11), (10,10))
TRIPLE_LETTER_SCORE = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13, 5), (13,9))
DOUBLE_LETTER_SCORE = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11),
                        (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))
class Board:
    def __init__(self):
        self.board = [["   " for i in range(15)] for j in range(15)]
        self.board[7][7] = " * "
        self.premium_squares()
        

    def show_board(self):
        #board en formato string
        board_str = "   |  " + "  |  ".join(str(item) for item in range(10)) + "  | " + "  | ".join(str(item) for item in range(10, 15)) + " |"
        board_str += "\n   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n"
        board = list(self.board) #copia de board para no modificar la original del init
        for i in range (len(board)):
            if i < 10:
                board[i] = str(i) + "  | " + " | ".join(str(item) for item in board[i]) + " |"
            if i >= 10:
                board[i] = str(i) + " | " + " | ".join(str(item) for item in board[i]) + " |"
        board_str += "\n   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|\n".join(board)
        board_str += "\n   _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"
        return board_str

    def premium_squares(self):
        #agrega todas las square con multiplicadores al board.
        for coordinate in TRIPLE_WORD_SCORE:
            self.board[coordinate[0]][coordinate[1]] = "TWS"
        for coordinate in TRIPLE_LETTER_SCORE:
            self.board[coordinate[0]][coordinate[1]] = "TLS"
        for coordinate in DOUBLE_WORD_SCORE:
            self.board[coordinate[0]][coordinate[1]] = "DWS"
        for coordinate in DOUBLE_LETTER_SCORE:
            self.board[coordinate[0]][coordinate[1]] = "DLS"

        
    def board_array(self):
    #Returns del board.
        return self.board
    
    def place_word(self, word, location, direction, player):

        # Inicializa la lista de premium_spots
        premium_spots = []
        # Verifica la dirección
        if direction.lower() not in ["right", "down"]:
            raise ValueError("Dirección no válida. Debe ser 'right' o 'down'.")

            # Convierte la palabra a mayúsculas
        word = word.upper()

            # Verifica si la palabra es vacía
        if not word:
            raise ValueError("La palabra no puede ser vacía.")

            # Obtiene la longitud de la palabra
        word_length = len(word)

            # Verifica si la ubicación está dentro de los límites del tablero
        if not (0 <= location[0] < 15 and 0 <= location[1] < 15):
            raise ValueError("Ubicación fuera de los límites del tablero.")

            # Comprueba si hay suficiente espacio para colocar la palabra
        if (direction.lower() == "right" and location[1] + word_length > 15) or (direction.lower() == "down" and location[0] + word_length > 15):
            raise ValueError("No hay suficiente espacio para colocar la palabra en esa dirección.")
         
     # Coloca la palabra en el tablero
        for i in range(word_length):
            if direction.lower() == "right":
                row = location[0]
                col = location[1] + i
            elif direction.lower() == "down":
                row = location[0] + i
                col = location[1]
            else:
                    # Maneja el caso en el que la dirección no es "right" ni "down"
                raise ValueError("Dirección no válida. Debe ser 'right' o 'down'.")

                
                # Verifica si la casilla no está vacía
            if self.board[row][col] != "   ":
                premium_spots.append((word[i], self.board[row][col]))
                
                # Coloca la letra en el tablero
            self.board[row][col] = " " + word[i] + " "

            # Remueve las fichas del jugador y repone el atril
        for letter in word:
            Rack.remove_from_rack(letter)

        Rack.replenish_rack()


class Rack:
    def __init__(self, bag):
        self.bag = bag
        self.rack = []
        self.initialize()

    def initialize(self):
        #le da sus 7 fichas.
        for i in range(7):
            self.add_rack()
    
    def add_rack(self):
        #toma las fichas de la bag y se las da al atril.
        self.rack.append(self.bag.take(7))
    
    def get_rack(self):
        self.get_letter = Tile.get_letter()
        #muestra el atril en fomato string.
        return ", ".join(str(item.get_letter() for item in self.rack)) # join toma una secuencia de elementos y los concatena en una cadena, separándolos con el delimitador especificado (en este caso, la coma seguida de un espacio). convierte cada letra en una cadena utilizando str().

    def get_rack_arr(self):
       #Devuelve el rack como una matriz de tile
        return self.rack

    def remove_from_rack(self, tile):
        #Quita una ficha de la estantería
        if tile in self.rack:
           self.rack.remove(tile)

    def get_rack_length(self):
        #Devuelve el número de fichas que quedan en la estantería.
        return len(self.rack)
    
    def replenish_rack(self):
        bag = BagTiles()
        self.get_remaining_tiles = bag.get_remaining_tiles
        #self.get_remaining_tiles = BagTiles.get_remaining_tiles
        #Añade fichas a la estantería después de un turno, de forma que la estantería tenga 7 fichas
        while self.get_rack_length() < 7 and self.get_remaining_tiles() > 0:
            self.add_rack()

class Cell:
    def __init__(self,letter = None, multiplier = 1, multiplier_type=None):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = letter

    def add_letter(self, letter:Tile):
        self.letter = letter

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter':
            value = self.letter.value * self.multiplier
            self.multiplier_type = None                  
            return value
        else:
            return self.letter.value
        
    """def __repr__(self):
        if self.letter:
            return repr(self.letter)
        if self.multiplier > 1:
            return f'{"W" if self.multiplier_type == "word" else "L"}x{self.multiplier}'
        else:
            return '   '
"""