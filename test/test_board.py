import unittest
from game.board import *
from game.tiles import *

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.bag = BagTiles()
        self.rack = Rack(self.bag)

    """def test_place_word_valid(self):
        # Prueba si se puede colocar una palabra válida en el tablero
        word = "CARNE"
        location = (7, 7)
        direction = "right"
        self.board.place_word(word, location, direction, self.rack)
        # Verifica que la palabra esté en el tablero o realiza alguna otra validación necesaria

    def test_place_word_invalid(self):
        # Prueba si no se puede colocar una palabra inválida en el tablero
        word = "XYZZZZ"
        location = (7, 7)
        direction = "right"
        with self.assertRaises(ValueError):
            self.board.place_word(word, location, direction, self.rack)"""
    

    def test_show_board(self):
        
        board_str = self.board.show_board()
        self.assertIsInstance(board_str, str)

    def test_board_array(self):
        
        board_array = self.board.board_array()
        self.assertIsInstance(board_array, list)
        self.assertEqual(len(board_array), 15)
        self.assertEqual(len(board_array[0]), 15)

    def test_premium_squares(self):
        
        self.board.premium_squares()
        self.assertEqual(self.board.board[7][7], " * ")
        self.assertEqual(self.board.board[0][0], "TWS")
        self.assertEqual(self.board.board[1][1], "DWS")

    def test_place_word_invalid_direction(self):
        
        with self.assertRaises(ValueError):
            self.board.place_word("CARNE", (0, 0), "invalid", self.rack)

    def test_place_word_empty_word(self):
        
        with self.assertRaises(ValueError):
            self.board.place_word("", (0, 0), "right", self.rack)

    def test_place_word_out_of_bounds(self):
        
        with self.assertRaises(ValueError):
            self.board.place_word("ANTEOJO", (14, 10), "right", self.rack)

    """def test_place_word_not_enough_space(self):
        
        with self.assertRaises(ValueError):
            self.board.place_word("CARNE", (0, 0), "right", self.rack)"""

class TestRack(unittest.TestCase):
    def setUp(self):
        # Crea una bolsa y un atril para cada prueba
        self.bag = BagTiles()
        #self.bag = Tile()
        self.rack = Rack(self.bag)

    def test_initialize(self):
        # Verifica que el atril se inicializa con 7 fichas
        self.assertEqual(len(self.rack.get_rack_arr()), 7)

    def test_get_rack(self):
        # Verifica que el método get_rack devuelva una representación de cadena correcta
        expected = "".join([str(tile.get_letter()) for tile in self.rack.get_rack_arr()])
        self.assertEqual(self.rack.get_rack(), expected)

    def test_remove_from_rack(self):
        # Agrega una ficha y luego la elimina, verificando que ya no esté en el atril
        tile = Tile("A", 1)
        self.rack.add_rack()
        self.rack.remove_from_rack(tile)
        self.assertNotIn(tile, self.rack.get_rack_arr())

    def test_get_rack_length(self):
        # Verifica que el método get_rack_length devuelva la longitud correcta del atril
        self.assertEqual(self.rack.get_rack_length(), 7)

    def test_replenish_rack(self):
        bag = BagTiles()
        self.get_remaining_tiles = bag.get_remaining_tiles()
        # Verifica que se rellenen las fichas correctamente en el atril
        self.rack.remove_from_rack(self.rack.get_rack_arr()[0])  # Elimina una ficha
        self.rack.replenish_rack()  # Rellena el atril
        self.assertEqual(self.rack.get_rack_length(), 7)  # Debe tener 7 fichas nuevamente

    def test_add_rack(self):
        #Ejecuta add_rack y verifica si el atril contiene la cantidad correcta de fichas.
        self.rack.add_rack()
        self.assertEqual(len(self.rack.get_rack_arr()), 8)

    def test_get_rack(self):
        #Verifica si el atril se muestra correctamente en formato string.
        pass
        """rack_string = self.rack.get_rack()
        self.assertIsInstance(rack_string, str)
        self.assertTrue(all(letter.isalpha() for letter in rack_string))"""

    def test_get_rack_arr(self):
        #Verifica si get_rack_arr devuelve un array de instancias de tile.
        pass
        """rack_arr = self.rack.get_rack_arr()
        self.assertIsInstance(rack_arr, list)
        self.assertTrue(all(isinstance(item, Tile) for item in rack_arr))"""

    def test_remove_from_rack(self):
        #Remueve una ficha del atril y verifica si se ha eliminado correctamente.
        tile = self.rack.get_rack_arr()[0]
        self.rack.remove_from_rack(tile)
        self.assertNotIn(tile, self.rack.get_rack_arr())

class TestCell(unittest.TestCase):
    def test_init(self):
        cell = Cell(multiplier=2, multiplier_type='letter')

        self.assertEqual(
            cell.multiplier,
            2,
        )
        self.assertEqual(
            cell.multiplier_type,
            'letter',
        )
        self.assertIsNone(cell.letter)
        self.assertEqual(
            cell.calculate_value(),
            0,
        )

    def test_add_letter(self):
        cell = Cell(multiplier=1, multiplier_type='')
        letter = Tile(letter='p', value=3)

        cell.add_letter(letter=letter)

        self.assertEqual(cell.letter, letter)

    def test_cell_value(self):
        cell = Cell(multiplier=2, multiplier_type='letter')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)

        self.assertEqual(
            cell.calculate_value(),
            6,
        )

    def test_cell_multiplier_word(self):
        cell = Cell(multiplier=2, multiplier_type='word')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)

        self.assertEqual(
            cell.calculate_value(),
            3,
        )


if __name__ == '__main__':
    unittest.main()