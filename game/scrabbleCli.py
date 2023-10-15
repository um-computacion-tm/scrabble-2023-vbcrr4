from game.scrabble_game import ScrabbleGame

class ScrabbleCli:
    def __init__(self): 
        self.game = ScrabbleGame(players_count=0)

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
