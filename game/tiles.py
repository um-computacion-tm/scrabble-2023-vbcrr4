import random
from piezas import *
class NoTilesInTheBagException(Exception):
    pass
class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value
        
    def __repr__(self): 
        return f"{self.letter}:{self.value}"
class Comodin(Tile):
    def __init__(self):
        super().__init__(letter='?', value=0)

    def select_letter(self, selection):
        selection = selection.upper()
        for tile in LETTER_VALUES:
            if selection == tile['letter']:
                self.letter = tile['letter']
                self.value = tile['value']
class BagTiles:
    def __init__(self):
        self.tiles = []
        for i in LETTER_VALUES:
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
        self.tiles.extend(tiles)
        random.shuffle(self.tiles)