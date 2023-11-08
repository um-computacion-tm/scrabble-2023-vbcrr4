from game.tiles import *
from collections import Counter
from game.board import *
class InvalidIndexException(Exception):
    pass
class Player:
    def __init__(self,nameplayer="",id=0,score=0):
        self.score = score
        self.name = nameplayer
        self.number = id
        self.rack = []
        self.tile_counter = Counter() 
    
    def draw_tiles(self, tiles=[]):
        self.rack.extend(tiles)

    def set_nameplayer(self):
        self.name = str(input("Ingrese su nombre: "))

    def scoresum (self, score:int ):
        self.score += score

    def giveTiles(self, positions: list):
        tiles = []
        for i in range(len(positions)):
            if positions[i] < len(self.rack):
                tiles.append(self.rack.pop(positions[i]))
                for j in range(len(positions)):
                    if positions[i] < positions[j]:
                        positions[j] -= 1
            else:
                raise InvalidIndexException("Invalid index:")
        return tiles
    
    def hasTiles(self, word: str):
        # Comprueba si la palabra dada se puede formar utilizando las fichas de la estantería.
        # Devuelve:True si la palabra se puede formar con las fichas de la estantería, False en caso contrario.
        if len(word) == 0:
            return True
        while len(word) > 0:
            usedTiles = Counter()
            for letter in word:
                if not self.has_letters_in_rack(letter, usedTiles):
                    hasBlankTileUsed = False
                    for i in range(len(self.rack)):
                        if self.rack[i].letter == "?" and usedTiles[i] < 1:
                            hasBlankTileUsed = True
                            usedTiles[i] += 1
                            break
                    if not hasBlankTileUsed:
                        return False
        return True
    
    def has_letters_in_rack(self, word): 
        tiles = [tiles.letter for tiles in self.rack]
        for letter in word:
            if letter in tiles:
                tiles.remove(letter)
            else:
                return False
        return True
    def show_rack(self):
        lectern = " | ".join(f"{tile.letter}:{tile.value}" for tile in self.rack)
        indices = f"indx:" + " " * 3 + "  ".join(f'{i+1:^4}' for i, _ in enumerate(self.rack))
        return f"Player ID: {self.number}\nScore: {self.score}\nAtril: {lectern} |\n{indices}"

        
    #def play_tile(self, tile):
    #    if tile in self.tiles:
    #        self.tiles.remove(tile)
    #    else:
    #        print("Tile not found in player's hand.")
    
    #def display_hand(self):
    #    print("Player's hand: ", self.tiles.__str__())