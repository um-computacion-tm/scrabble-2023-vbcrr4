from game.tiles import BagTiles
class Player:
    def __init__(self,bag_tiles = None):
        self.bag_tiles = bag_tiles
        self.tiles = []
    
    def draw_tiles(self,bag,count):
        drawn_tiles = bag.take(count)
        self.tiles.extend(drawn_tiles)
    
    def reset(self):
        self.tiles = []  # Restablece las fichas del jugador.

