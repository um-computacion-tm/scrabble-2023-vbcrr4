from game.board import Board
from game.player import Player
from game.tiles import BagTiles

class ScrabbleGame:
    def __init__(self, players_count: int):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players:list[Player] = []
        for _ in range(players_count):
            self.players.append(Player(bag_tiles=self.bag_tiles))
        
        self.current_player=None

    def start_game(self):
        for player in self.players:
            tiles_to_draw = 7 - len(player.tiles)
            new_tiles = self.bag_tiles.take(tiles_to_draw)
            player.tiles.extend(new_tiles)

    def next_turn(self):
        if self.current_player is None: #verifica si es None significa que es el primer turno de juego
            self.current_player = self.players[0]
        else:  
            index = self.players.index(self.current_player) + 1 #busca el indice del jugador actual, y le pasa el turno al siguiente 
            if index >= len(self.players):
                index = 0  #vuelve al primer jugador
            self.current_player = self.players[index]     #establece quien es el jugador actual para poder pasar al siguiente turno.   
  
    def end_game(self):
        if not self.bag_tiles.tiles:
            print("¡La bolsa de fichas está vacía!")
            print("El juego ha terminado.")
            # mostrar las puntuaciones finales y al ganador aquí.
            self.reset_game()
    def reset_game(self):
        self.board = Board()
        self.bag_tiles = BagTiles()
        for player in self.players:
            player.reset() 
        self.current_player = None
        
