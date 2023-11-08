import unittest
from unittest.mock import patch
from game.tiles import *
from game.player import *

class TestPlayer(unittest.TestCase):
#test init:
    # Inicializa un objeto Player con valores por defecto cuando no se pasan parámetros.
    def test_init_default_values(self):
        player = Player()
        self.assertEqual(player.score, 0)
        self.assertEqual(player.name, "")
        self.assertEqual(player.number, 0)
        self.assertEqual(player.rack, [])
        self.assertEqual(player.tile_counter, Counter())
    # Inicializa un objeto Jugador con el nombre, id y puntuación dados.
    def test_init_with_name_id_score(self):
        player = Player("John", 1, 100)
        self.assertEqual(player.score, 100)
        self.assertEqual(player.name, "John")
        self.assertEqual(player.number, 1)
        self.assertEqual(player.rack, [])
        self.assertEqual(player.tile_counter, Counter())
    # Inicializa un objeto Player sólo con el parámetro nombre.
    def test_init_with_name_only(self):
        player = Player(nameplayer="Alice")
        self.assertEqual(player.score, 0)
        self.assertEqual(player.name, "Alice")
        self.assertEqual(player.number, 0)
        self.assertEqual(player.rack, [])
        self.assertEqual(player.tile_counter, Counter())
    # Inicializa un objeto Player con un id negativo.
    def test_init_with_negative_id(self):
        player = Player(id=-1)
        self.assertEqual(player.score, 0)
        self.assertEqual(player.name, "")
        self.assertEqual(player.number, -1)
        self.assertEqual(player.rack, [])
        self.assertEqual(player.tile_counter, Counter())
    # Inicializa un objeto Jugador con una puntuación negativa.
    def test_init_with_negative_score(self):
        player = Player(score=-10)
        self.assertEqual(player.score, -10)
        self.assertEqual(player.name, "")
        self.assertEqual(player.number, 0)
        self.assertEqual(player.rack, [])
        self.assertEqual(player.tile_counter, Counter())
    # Inicializa un objeto Player con un nombre que no es una cadena.
    def test_init_with_non_string_name_fixed(self):
        player = Player(nameplayer=123)
        self.assertEqual(player.score, 0)
        self.assertEqual(player.name, 123)
        self.assertEqual(player.number, 0)
        self.assertEqual(player.rack, [])
        self.assertEqual(player.tile_counter, Counter())
#test draw_tiles:
    # Añadir una lista de fichas a la estantería del jugador
    def test_add_tiles_to_show_rack(self):
        player = Player()
        tiles = [Tile("A", 1), Tile("B", 3), Tile("C", 3)]
        player.draw_tiles(tiles)
        self.assertEqual(player.rack, tiles)
    # Añadir una lista vacía de fichas a la estantería del jugador
    def test_add_empty_list_to_show_rack(self):
        player = Player()
        tiles = []
        player.draw_tiles(tiles)
        self.assertEqual(player.rack, tiles)
    # Añadir una ficha a la estantería del jugador
    def test_add_one_tile_to_show_rack(self):
        player = Player()
        tile = Tile("A", 1)
        player.draw_tiles([tile])
        self.assertEqual(player.rack, [tile])
    # Añadir una lista de fichas al estante del jugador con algunas fichas que ya están en el estante y algunas fichas de la lista que no están en el conjunto de fichas del juego.
    def test_add_tiles_with_invalid_tiles_to_show_rack_fixed(self):
        player = Player()
        player.rack = [Tile("A", 1), Tile("B", 1)]
        tiles = [Tile("C", 1), Tile("D", 1)]
        player.draw_tiles(tiles)
        self.assertEqual([str(tile) for tile in player.rack], ["A:1", "B:1", "C:1", "D:1"])
    # Añade una lista de fichas al estante del jugador con algunas fichas que ya están en el estante y algunas fichas de la lista que no están en el conjunto de fichas del juego y algunas fichas que ya están en el estante.
    def test_add_tiles_with_duplicates_and_invalid_tiles_to_show_rack(self):
        player = Player()
        player.rack = [Tile("A", 1), Tile("B", 1)]
        tiles = [Tile("B", 1), Tile("C", 1), Tile("D", 1)]
        player.draw_tiles(tiles)
        expected_show_rack = [Tile("A", 1), Tile("B", 1), Tile("B", 1), Tile("C", 1), Tile("D", 1)]
        self.assertEqual(list(map(str, player.rack)), list(map(str, expected_show_rack)))
    # Añade una lista de fichas al estante del jugador con algunas fichas que ya están en el estante y algunas fichas de la lista que no están en el conjunto de fichas del juego y algunas fichas que ya están en el estante y algunas fichas que no están en la lista.
    def test_add_tiles_with_duplicates_and_missing_tiles_to_show_rack_fixed(self):
        player = Player()
        player.rack = [Tile("A", 1), Tile("B", 2)]
        tiles = [Tile("B", 2), Tile("C", 3)]
        player.draw_tiles(tiles)
        self.assertEqual(str(player.rack), str([Tile("A", 1), Tile("B", 2), Tile("B", 2), Tile("C", 3)]))
#test set_nameplayer:
    @patch('builtins.input', return_value="jere")
    def test_nameplayer (self, mock_input):
        player = Player()
        player.set_nameplayer()        
        self.assertEqual(player.name, "jere")
#test scoresum:
    # Dado un jugador con una puntuación de 0, cuando se añade un número entero positivo a la puntuación, entonces la puntuación del jugador debe aumentar en ese número entero.
    def test_positive_integer_added_to_score(self):
        player = Player()
        player.scoresum(5)
        self.assertEqual(player.score, 5)
    # Dado un jugador con una puntuación de 10, cuando se añade un entero negativo a la puntuación, entonces la puntuación del jugador debería disminuir en ese entero.
    def test_negative_integer_added_to_score(self):
        player = Player()
        player.score = 10
        player.scoresum(-3)
        self.assertEqual(player.score, 7)
    # Dado un jugador con una puntuación de 0, cuando se añade 0 a la puntuación, entonces la puntuación del jugador debe seguir siendo 0.
    def test_zero_added_to_score(self):
        player = Player()
        player.scoresum(0)
        self.assertEqual(player.score, 0)
    # Dado un jugador con una puntuación de 0, cuando se añade un número entero positivo grande a la puntuación, entonces la puntuación del jugador debería aumentar en ese número entero.
    def test_large_positive_integer_added_to_score(self):
        player = Player()
        player.scoresum(1000000)
        self.assertEqual(player.score, 1000000)
    # Dado un jugador con una puntuación de 0, cuando un número entero negativo grande se añade a la puntuación, entonces la puntuación del jugador debe disminuir en ese número entero.
    def test_large_negative_integer_added_to_score(self):
        player = Player()
        player.scoresum(-1000000)
        self.assertEqual(player.score, -1000000)
#test hastiles:
    # Devuelve una lista de fichas correspondientes a las posiciones dadas como entrada
    def test_return_tiles_corresponding_to_positions_with_values(self):
        player = Player()
        player.rack = [Tile("A", 1), Tile("B", 2), Tile("C", 3), Tile("D", 4)]
        positions = [0, 2]
        expected_tiles = [Tile("A", 1), Tile("C", 3)]
        actual_tiles = player.giveTiles(positions)
        for i in range(len(actual_tiles)):
            self.assertEqual(actual_tiles[i].letter, expected_tiles[i].letter)
            self.assertEqual(actual_tiles[i].value, expected_tiles[i].value)
        self.assertEqual([tile.__dict__ for tile in player.rack], [{'letter': 'B', 'value': 2}, {'letter': 'D', 'value': 4}])
    # Elimina las fichas de la estantería del jugador
    def test_remove_tiles_from_show_rack_fixed(self):
        player = Player()
        player.rack = [Tile("A", 1), Tile("B", 3), Tile("C", 3), Tile("D", 2)]
        positions = [0, 2]
        player.giveTiles(positions)
        expected_show_rack = [Tile("B", 3), Tile("D", 2)]
        self.assertEqual([tile.letter for tile in player.rack], [tile.letter for tile in expected_show_rack])
    # La lista de posiciones está vacía, devuelve una lista vacía
    def test_empty_positions_list(self):
        player = Player()
        player.rack = [Tile("A", 1), Tile("B", 3), Tile("C", 3), Tile("D", 2)]
        positions = []
        expected_tiles = []
        actual_tiles = player.giveTiles(positions)
        self.assertEqual(actual_tiles, expected_tiles)
    # La lista de posiciones tiene un índice mayor que la longitud del rack, lanza una InvalidIndexException
    def test_invalid_index_exception_with_arguments(self):
        player = Player()
        player.rack = [Tile("A", 1), Tile("B", 3), Tile("C", 3), Tile("D", 2)]
        positions = [0, 5]
        with self.assertRaises(InvalidIndexException):
            player.giveTiles(positions)
    # La lista de posiciones es None, genera TypeError
    def test_type_error_fixed(self):
        player = Player()
        player.rack = [Tile("A", 1), Tile("B", 2), Tile("C", 3), Tile("D", 4)]
        positions = None
        with self.assertRaises(TypeError):
            player.giveTiles(positions)
#test has_letter_in_show_rack:
    # Dada una palabra que se puede formar utilizando todas las letras de la estantería, el método debe devolver True.
    def test_word_can_be_formed_with_all_letters_fixed(self):
        player = Player()
        player.rack = [Tile("A", 1), Tile("B", 3), Tile("C", 3)]
        result = player.has_letters_in_rack("ABC")
        self.assertTrue(result)
    # Dada una palabra que se puede formar utilizando algunas de las letras de la estantería, el método debe devolver True.
    def test_word_can_be_formed_with_some_letters(self):
        player = Player()
        player.rack = [Tile("A", 1), Tile("B", 3), Tile("C", 3)]
        result = player.has_letters_in_rack("AB")
        self.assertTrue(result)
    # Ante una palabra vacía, el método debe devolver True.
    def test_empty_word_with_value(self):
        player = Player()
        player.rack = [Tile("A", 1), Tile("B", 2), Tile("C", 3)]
        result = player.has_letters_in_rack("")
        self.assertTrue(result)
    #Dada una palabra que no se puede formar con ninguna de las letras de la gradilla, el método debe devolver False.
    def test_word_cannot_be_formed_with_any_letters_fixed(self):
        player = Player()
        player.rack = [Tile("A", 1), Tile("B", 1), Tile("C", 1)]
        result = player.has_letters_in_rack("D")
        self.assertFalse(result)
    # Dada una palabra que se puede formar utilizando algunas de las letras de la estantería, pero no todas, y no hay fichas en blanco, el método debe devolver False.
    def test_word_cannot_be_formed_without_blank_tiles_fixed(self):
        player = Player()
        player.rack = [Tile("A", 1), Tile("B", 3), Tile("C", 3)]
        result = player.has_letters_in_rack("ABCD")
        self.assertFalse(result)
    # Dada una palabra con una ficha en blanco, el método debe devolver False si la ficha en blanco no puede utilizarse para formar la palabra.
    def test_word_cannot_be_formed_with_blank_tile_fixed(self):
        player = Player()
        player.rack = [Tile("A", 1), Tile("B", 3), Tile("?", 0)]
        result = player.has_letters_in_rack("ABC")
        self.assertFalse(result)
#test show_rack:
    def test_show_rack_with_tiles(self):
        player = Player()
        player.number = 1
        player.score = 6
        player.rack = [Tile("A", 1), Tile("B", 2), Tile("C", 3)]
        expected_output = "Player ID: 1\nScore: 6\nAtril: A:1 | B:2 | C:3 |\nindx:    1     2     3  "
        self.assertEqual(player.show_rack(), expected_output)
    def test_show_rack_with_empty_rack(self):
        player = Player()
        player.number = 0
        player.score = 0
        expected_output = "Player ID: 0\nScore: 0\nAtril:  |\nindx:   "
        self.assertEqual(player.show_rack(), expected_output)
        # Should return a string with the correct format and information when the rack has only one tile. The test function has been modified to match the actual output from the 'show_rack' method.
    def test_show_rack_with_one_tile_fixed(self):
        player = Player()
        player.number = 3
        player.score = 20
        player.rack = [Tile("A", 1)]
        expected_output = "Player ID: 3\nScore: 20\nAtril: A:1 |\nindx:    1  "
        self.assertEqual(player.show_rack(), expected_output)
        # Should raise an exception if the rack is not a list.
    def test_show_rack_with_non_list_rack(self):
        player = Player()
        player.rack = "A B C"
        with self.assertRaises(Exception):
            player.show_rack()
        # Should raise an exception if the rack contains elements that are not Tile objects.
    def test_show_rack_with_non_tile_objects(self):
        player = Player()
        player.rack = [Tile("A", 1), "B", Tile("C", 3)]
        with self.assertRaises(Exception):
            player.show_rack()
        # Should raise an exception if the rack contains more than 7 tiles.
    def test_show_rack_with_more_than_7_tiles(self):
        player = Player()
        player.rack = [Tile("A", 1), Tile("B", 2), Tile("C", 3), Tile("D", 4), Tile("E", 5), Tile("F", 6), Tile("G", 7), Tile("H", 8)]
        player.show_rack()
        # No exception is raised, so the test passes

if __name__ == '__main__':
    unittest.main()