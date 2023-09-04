from game.tiles import BagTiles
class Player:
    def __init__(self):
        self.tiles = []
    
    def draw_tiles(self,bag,count):
        drawn_tiles = bag.take(count)
        self.tiles.extend(drawn_tiles)
