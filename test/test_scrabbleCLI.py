import unittest
from unittest.mock import patch
from game.scrabbleCli import ScrabbleCli

class TestScrabbleCli(unittest.TestCase):
#Arreglar tests
    @patch('builtins.input', return_value='3')
    def test_get_player_count(self, input_patched):
        scrabble_cli = ScrabbleCli()
        self.assertEqual(scrabble_cli.get_player_count(), 3)

    @patch('builtins.input', side_effect=['A', '3'])
    def test_player_count_wrong_input(self, input_patched):
        scrabble_cli = ScrabbleCli()
        result = scrabble_cli.get_player_count()
        self.assertIsNone(result)  # Verifica que el resultado sea None en caso de entrada incorrecta

    @patch('builtins.input', side_effect=['10', '1'])
    def test_player_count_max(self, input_patched):
        scrabble_cli = ScrabbleCli()
        #with self.assertRaises(ValueError):
        #    scrabble_cli.get_player_count()

        self.assertEqual(scrabble_cli.get_player_count(), None)

if __name__ == "__main__":
    unittest.main()
