import unittest
from game.scrabble_game import *
from unittest.mock import patch

class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count = 3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(
            len(scrabble_game.players),
            3,
        )
        self.assertIsNotNone(scrabble_game.bag_tiles)

    def test_next_turn_when_game_is_starting(self):
        #Validar que al comienzo, el turno es del jugador 0
        scrabble_game = ScrabbleGame(players_count = 3)

        scrabble_game.next_turn()

        assert scrabble_game.current_player == scrabble_game.players[0]

    def test_next_turn_when_player_is_not_the_first(self):
        #Validar que luego del jugador 0, le toca al jugador 1
        scrabble_game = ScrabbleGame(players_count = 3)
        scrabble_game.current_player = scrabble_game.players[0]

        scrabble_game.next_turn()

        assert scrabble_game.current_player == scrabble_game.players[1]

    def test_next_turn_when_player_is_last(self):
        #Suponiendo que tenemos 3 jugadores, luego del jugador 3, le toca al jugador 1
        scrabble_game = ScrabbleGame(players_count = 3)
        scrabble_game.current_player = scrabble_game.players[2] #2 seria el player 3

        scrabble_game.next_turn()

        assert scrabble_game.current_player == scrabble_game.players[0]

    def test_start_game(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.start_game()     
        for player in scrabble_game.players:     # Verifica que cada jugador tenga exactamente 7 fichas al inicio
            self.assertEqual(len(player.tiles), 7)
            
        total_tiles = sum(len(player.tiles) for player in scrabble_game.players)   # Verifica que la bolsa de fichas tenga la cantidad correcta de fichas restantes
        self.assertEqual(len(scrabble_game.bag_tiles.tiles), 100 - total_tiles)

    def test_end_game_when_bag_is_empty(self):
        scrabble_game = ScrabbleGame(players_count=2)
        scrabble_game.bag_tiles.tiles = []  # Bolsa de fichas vacía

        #unittest.mock.patch para capturar la salida impresa.
        with patch('builtins.print') as mock_print:
            scrabble_game.end_game()
        # Verifica que los mensajes de "¡La bolsa de fichas está vacía!" y "El juego ha terminado." se impriman.
        mock_print.assert_any_call("¡La bolsa de fichas está vacía!")
        mock_print.assert_any_call("El juego ha terminado.")
    def test_reset_game(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.reset_game()

        #el juego se haya reiniciado correctamente
        self.assertIsNotNone(scrabble_game.board)
        self.assertIsNotNone(scrabble_game.bag_tiles)
        self.assertIsNone(scrabble_game.current_player)

        for player in scrabble_game.players:
        #cada jugador tenga una lista de fichas vacía
            self.assertEqual(len(player.tiles), 0)


if __name__ == '__main__':
    unittest.main()