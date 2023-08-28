import random
from piezas import DATA

TOTALTILES = 100

class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value
class Comodin:
    def __init__(self):
        self.letter = '_'
        self.value = 0

class BagTiles:
    def __init__(self):
        self.tiles = []
        for i in DATA:
            for _ in range(i["quantity"]):
                self.tiles.append(Tile(i["letter"], i["value"]))
        random.shuffle(self.tiles)

    def take(self, count):
        tiles_taken = []
        for _ in range(count):
            if len(self.tiles) > 0:
                tiles_taken.append(self.tiles.pop())
        return tiles_taken

    def put(self, tiles: list):
        if len(tiles) + len(self.tiles) <= TOTALTILES:
            self.tiles.extend(tiles)

class Cell:
    def __init__(self, multiplier, multiplier_type):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = None

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

