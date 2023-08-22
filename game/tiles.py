import random
from piezas import DATA

TOTALTILES = 100

class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value

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
    

