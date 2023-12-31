from game.tiles import Tile
class Player:
    def __init__(self,bag_tiles = None):
        self.bag_tiles = bag_tiles
        self.tiles = []
    
    def draw_tiles(self,bag,count):
        drawn_tiles = bag.take(count)
        self.tiles.extend(drawn_tiles)
    
    def reset(self):
        self.tiles = []  # Restablece las fichas del jugador.
        
    def play_tile(self, tile):
        if tile in self.tiles:
            self.tiles.remove(tile)
        else:
            print("Tile not found in player's hand.")
    
    def display_hand(self):
        print("Player's hand: ", self.tiles.__str__())
