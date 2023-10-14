from game.scrabble_game import ScrabbleGame
class ScrabbleCli:
        def __init__(self): 
            self.game = ScrabbleGame(players_count=0)
        def get_player_count(self):
            while True:
                try:
                    player_count = int(input('Cantidad de jugadores (1-3): '))
                    if 1 <= player_count <= 3:
                        break
                    else:
                        print('Número de jugadores no válido. Intente de nuevo.')
                except ValueError:
                    print('Ingrese un número válido por favor.')
            return player_count
        