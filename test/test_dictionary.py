import unittest
from unittest.mock import patch, Mock
from game.dictionary import Dictionary

class TestDictionary(unittest.TestCase):
    @patch('pyrae.dle.search_by_word')
    def test_get_word_dictionary(self, mock_search_by_word):
        # Configura el comportamiento simulado de la función mock
        mock_search_by_word.return_value = Mock(to_dict=lambda: {'title': ''})

        scrabble_game = Dictionary()
        word = "Alambrado"
        valor = scrabble_game.get_word(word)
        self.assertTrue(valor)

    @patch('pyrae.dle.search_by_word')
    def test_get_word_dictionary_not(self, mock_search_by_word):
        # Configura el comportamiento simulado de la función mock
        mock_search_by_word.return_value = Mock(to_dict=lambda: {'title': 'Diccionario de la lengua española | Edición del Tricentenario | RAE - ASALE'})

        scrabble_game = Dictionary()
        word = "Sanacaramalana"
        valor = scrabble_game.get_word(word)
        self.assertFalse(valor)

if __name__ == '__main__':
    unittest.main()
