from game.tiles import *
class Player:
    def __init__(self, bag_tiles=None , nameplayer=None, player_id=None):
        self.bag_tiles = bag_tiles
        self.tiles = []
        self.score = 0
        #self.nameplayer = nameplayer
        #self.player_id = player_id
    
    def draw_tiles(self,bag,count):
        drawn_tiles = bag.take(count)
        self.tiles.extend(drawn_tiles)
    
    def reset(self):
        self.tiles = []  # Restablece las fichas del jugador.
        
    #def play_tile(self, tile):
    #    if tile in self.tiles:
    #        self.tiles.remove(tile)
    #    else:
    #        print("Tile not found in player's hand.")
    
    #def display_hand(self):
    #    print("Player's hand: ", self.tiles.__str__())

    def scoresum (self, score:int ):
        self.score += score
        #agregar suma del valor de palabras

class Rack:
    def __init__(self, bag):
        self.rack = []
        self.bag = bag
        self.initialize()

    def initialize(self):
        #le da sus 7 fichas.
        for i in range(7):
            self.add_rack()
    
    def add_rack(self):
        #toma las fichas de la bag y se las da al atril.
        self.rack.append(self.bag.take(1))
    
    def get_rack(self):
        self.get_letter = Tile()
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
        self.get_remaining_tiles = BagTiles()
        #Añade fichas a la estantería después de un turno, de forma que la estantería tenga 7 fichas
        while self.get_rack_length() < 7 and self.bag.get_remaining_tiles() > 0:
            self.add_rack()
