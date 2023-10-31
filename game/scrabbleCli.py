from game.scrabble_game import ScrabbleGame
from game.player import *
class ScrabbleCli:
    def __init__(self): 
        self.game = ScrabbleGame(players_count=0)
        self.game_status = True

    def get_player_count(self):
        while True:
            try:
                player_count = self.get_valid_player_count_input()
                if player_count is not None:
                    return player_count
            except ValueError:
                print('Ingrese un número válido por favor.')
            return None

    def get_valid_player_count_input(self):
        try:
            player_count = int(input('Cantidad de jugadores (1-3): '))
            if 1 <= player_count <= 3:
                return player_count
            else:
                print('Número de jugadores no válido. Intente de nuevo.')
                return None
        except ValueError:
            return None
        
    def create_players(self, player_count):
        players = []
        for i in range(player_count):
            player_name = input(f'Nombre del Jugador {i + 1}: ')
            player = Player(nameplayer=player_name)
            players.append(player)
        return players
    
    """def menu (self):
        self.game.next_turn()
        self.game.board.show_board()
        self.game.comodin()
        self.game.players()
        self.game.scoresum()
        print(f"puntaje de jugador: {self.game.scoresum}")

    def main (self):
        while self.game_status is True:
            self.menu()
            menu = int(input("eliga algo del menu"))
            #if menu == 1:"""


if __name__ == "__main__":
    main = ScrabbleCli()
    main.main()