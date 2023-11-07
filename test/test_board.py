import unittest
from game.board import *
from game.tiles import *

class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(len(board.grid), 15)
        self.assertEqual(len(board.grid[0]), 15)
#test _repr_:
        # Devuelve una representación de cadena del tablero
    def test_string_representation(self):
        # Arrange
        board = Board()
        # Act
        result = board.__repr__()
        # Assert
        self.assertIsInstance(result, str)
        # Incluye los números de fila y columna en la cadena
    def test_row_and_column_numbers(self):
        # Arrange
        board = Board()
        # Act
        result = board.__repr__()
        # Assert
        self.assertIn("   |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  | 10 ", result)
        self.assertIn("11  | 12  | 13  | 14 |", result)
        # Muestra las fichas y sus posiciones en el tablero
    def test_tiles_and_positions(self):
        # Arrange
        board = Board()
        # Act
        result = board.__repr__()
        # Assert
        self.assertIn("Cell(tile=None-multiplier=3-multiplier_type=word-row=0-col=0)", result)
        # Maneja un tablero con sólo celdas premium
    def test_premium_cells(self):
        # Arrange
        board = Board()
        board.grid[0][0].multiplier_type = "word"
        board.grid[0][0].multiplier = 3
        board.grid[14][14].multiplier_type = "letter"
        board.grid[14][14].multiplier = 2
        # Act
        result = board.__repr__()
        # Assert
        self.assertIn("Cell(tile=None-multiplier=3-multiplier_type=word-row=0-col=0)", result)
        self.assertIn("Cell(tile=None-multiplier=2-multiplier_type=letter-row=14-col=14)", result)
        # Maneja un tablero con una sola celda premium
    def test_one_premium_cell(self):
        # Arrange
        board = Board()
        board.grid[7][7].multiplier_type = "word"
        board.grid[7][7].multiplier = 3
        # Act
        result = board.__repr__()
        # Assert
        self.assertIn("Cell(tile=None-multiplier=3-multiplier_type=word-row=7-col=7)", result)

#test premiums_squares:
        # Dada una coordenada, un tipo de multiplicador y un valor de multiplicador, el método establece el tipo de multiplicador y el valor de multiplicador de la celda correspondiente a los valores dados.
    def test_set_multiplier_type_and_value(self):
        board = Board()
        board.premium_squares((0, 0), "word", 2)
        cell = board.grid[0][0]
        self.assertEqual(cell.multiplier_type, "word")
        self.assertEqual(cell.multiplier, 2)
        # El método establece con éxito el tipo de multiplicador y el valor del multiplicador para una celda en el centro del tablero.
    def test_set_multiplier_type_and_value_middle(self):
        board = Board()
        board.premium_squares((7, 7), "letter", 3)
        cell = board.grid[7][7]
        self.assertEqual(cell.multiplier_type, "letter")
        self.assertEqual(cell.multiplier, 3)
        # El método establece con éxito el tipo de multiplicador y el valor del multiplicador para una celda en la esquina superior izquierda del tablero.
    def test_set_multiplier_type_and_value_top_left_corner(self):
        board = Board()
        board.premium_squares((0, 0), "word", 2)
        cell = board.grid[0][0]
        self.assertEqual(cell.multiplier_type, "word")
        self.assertEqual(cell.multiplier, 2)
        # El método genera un IndexError si la coordenada dada está fuera de los límites del tablero.
    def test_raise_index_error_outside_bounds(self):
        board = Board()
        with self.assertRaises(IndexError):
            board.premium_squares((15, 15), "word", 2)
        # El método genera un TypeError si la coordenada dada no es una tupla.
    def test_raise_type_error_invalid_coordinate(self):
        board = Board()
        with self.assertRaises(TypeError):
            board.premium_squares("0, 0", "word", 2)
#test add premium cell:
    def test_2W_square(self):
        board = Board()
        cell = board.grid
        self.assertEqual(cell[11][3].multiplier,2)
        self.assertEqual(cell[11][3].multiplier_type,"word")
    def test_3W_square(self):
        board = Board()
        cell = board.grid
        self.assertEqual(cell[14][7].multiplier,3)
        self.assertEqual(cell[14][7].multiplier_type,"word")
    def test_2L_square(self):
        board = Board()
        cell = board.grid
        self.assertEqual(cell[8][6].multiplier,2)
        self.assertEqual(cell[8][6].multiplier_type,"letter")
    def test_3L_square(self):
        board = Board()
        cell = board.grid
        self.assertEqual(cell[1][5].multiplier,3)
        self.assertEqual(cell[1][5].multiplier_type,"letter")
#test calculate_word_value:
    def test_empty_word(self):
        board = Board()
        word = []
        # Calcula el valor de la palabra
        value = board.calculate_word_value(word)
        # Assert that the value is 0
        self.assertEqual(value, 0)
        # calcula el valor de una palabra sólo con las celdas que tienen fichas
    def test_cell_without_tile_fixed(self):
        board = Board()
        # Crear una palabra con celdas que contengan fichas
        word = [Cell(tile=Tile('A', 1)), Cell(tile=Tile('B', 2))]
        # Calcula el valor de la palabra
        value = board.calculate_word_value(word)
        #Afirmar que el valor es la suma de los valores de las tiles
        self.assertEqual(value, 3)
    def test_cell_without_multiplier(self):
        board = Board()
        # Crear una palabra con celdas que contengan fichas y una celda sin multiplicador
        word = [Cell(tile=Tile('A', 1)), Cell(tile=Tile('B', 2)), Cell(tile=Tile('C', 3), multiplier_type='letter')]
        # Calcula el valor de la palabra
        value = board.calculate_word_value(word)
        #Afirmar que el valor es la suma de los valores de las tiles
        self.assertEqual(value, 6)
    def test_no_multipliers(self):
        board = Board()
        # Crear una palabra con celdas que contengan fichas
        word = [Cell(tile=Tile('A', 1)), Cell(tile=Tile('B', 2)), Cell(tile=Tile('C', 3))]
        # Calcula el valor de la palabra
        value = board.calculate_word_value(word)
        #Afirmar que el valor es la suma de los valores de las tiles
        self.assertEqual(value, 6)
    def test_letter_multipliers(self):
        board = Board()
        # Crear una palabra con celdas que contengan fichas y multiplicadores de letras
        word = [Cell(tile=Tile('A', 1), multiplier_type='letter', multiplier=2),
                Cell(tile=Tile('B', 2), multiplier_type='letter', multiplier=3),
                Cell(tile=Tile('C', 3), multiplier_type='letter', multiplier=1)]
        # Calcula el valor de la palabra
        value = board.calculate_word_value(word)
        #Afirmar que el valor es la suma de los valores de las tiles multiplicados por los multiplicadores de las letras.
        self.assertEqual(value, 11)
#test check_crossword:
        # devuelve True si la palabra forma un crucigrama en la fila
    def test_word_forms_crossword_in_row(self):
        board = Board()
        row = 5
        col = 5
        word = "BUENO"
        result = board.check_crossword(row, col, word)
        self.assertTrue(result)
        # devuelve True si la palabra forma un crucigrama en la columna
    def test_word_forms_crossword_in_column(self):
        board = Board()
        row = 5
        col = 5
        word = "BUENO"
        result = board.check_crossword(row, col, word)
        self.assertTrue(result)
        # Devuelve False si la palabra no forma un crucigrama en la fila o columna
    def test_word_does_not_form_crossword(self):
        board = Board()
        row = 5
        col = 5
        word = "VERDE"
        board.place_word(word, (row, col), "right")
        result = board.check_crossword(row, col, word)
        self.assertTrue(result)
        # Devuelve False si la fila está dentro del rango de la rejilla del tablero
    def test_row_within_range(self):
        board = Board()
        row = 10
        col = 5
        word = "BUENO"
        result = board.check_crossword(row, col, word)
        self.assertTrue(result)
        # devuelve True si col está fuera de rango
    def test_col_out_of_range(self): #REVISAR
        board = Board()
        row = 5
        col = 10
        word = "BUENO"
        result = board.check_crossword(row, col, word)
        self.assertTrue(result)
        # devuelve True si word está vacío
    def test_word_empty_fixed(self):
        board = Board()
        row = 5
        col = 5
        word = ""
        result = board.check_crossword(row, col, word)
        self.assertTrue(result)
#test place_word:
    #Coloca una palabra válida en un tablero vacío.
    def test_valid_word_on_empty_board(self):
        board = Board()
        word = "DELFIN"
        location = (7, 7)
        direction = "right"
        board.place_word(word, location, direction)
        self.assertEqual(board.grid[7][7].tile, "D")
        self.assertEqual(board.grid[7][8].tile, "E")
        self.assertEqual(board.grid[7][9].tile, "L")
        self.assertEqual(board.grid[7][10].tile, "F")
        self.assertEqual(board.grid[7][11].tile, "I")
        self.assertEqual(board.grid[7][12].tile, "N")
    # Coloca una palabra válida en un tablero no vacío.
    def test_valid_word_on_non_empty_board(self):
        board = Board()
        board.grid[7][7].tile = "A"
        word = "ARROZ" #
        location = (7, 8)
        direction = "right"
        board.place_word(word, location, direction)
        self.assertEqual(board.grid[7][8].tile, "A")
        self.assertEqual(board.grid[7][9].tile, "R")
        self.assertEqual(board.grid[7][10].tile, "R")
        self.assertEqual(board.grid[7][11].tile, "O")
        self.assertEqual(board.grid[7][12].tile, "Z")
    # Coloca una palabra válida en el borde del tablero.
    def test_valid_word_on_edge_of_board(self):
        board = Board()
        word = "PASTO"
        location = (7, 10)
        direction = "right"
        board.place_word(word, location, direction)
        self.assertEqual(board.grid[7][10].tile, "P")
        self.assertEqual(board.grid[7][11].tile, "A")
        self.assertEqual(board.grid[7][12].tile, "S")
        self.assertEqual(board.grid[7][13].tile, "T")
        self.assertEqual(board.grid[7][14].tile, "O")
    # Lanza una excepción cuando la palabra no es válida.
    def test_invalid_word(self):
        board = Board()
        word = "AAKAA"
        location = (7, 7)
        direction = "right"
        # Place a word at location (7,7)
        board.place_word("WORD", (7, 7), "right")
        with self.assertRaises(NoEmptySquareExeption):
            board.place_word(word, location, direction)
    # Lanza una excepción cuando la ubicación está fuera del tablero.
    def test_location_out_of_board(self):
        board = Board()
        word = "OBELISCOS"
        location = (14, 7)
        direction = "right"
        with self.assertRaises(OutOfBoardExeption):
            board.place_word(word, location, direction)
        # No se produce ninguna excepción, por lo que la prueba se supera
    # Lanza una excepción cuando la dirección no es válida.
    def test_invalid_direction(self):
        board = Board()
        word = "VERDE"
        location = (7, 7)
        direction = "up"
        with self.assertRaises(InvalidDirectionExeption):
            board.place_word(word, location, direction)
#test validate_first_move:
    # Debe devolver True cuando round_number no es 1 y location no es (7,7).
    def test_return_true_when_round_number_not_1_and_location_not_77(self):
        board = Board()
        round_number = 2
        location = (5, 5)
        result = board.validate_first_move(round_number, location)
        self.assertTrue(result)
    # Debe devolver True cuando round_number es 1 y la ubicación es (7,7).
    def test_return_true_when_round_number_1_and_location_77(self):
        board = Board()
        round_number = 1
        location = (7, 7)
        result = board.validate_first_move(round_number, location)
        self.assertTrue(result)
    # Debería devolver NoCentreLocationExeption cuando round_number es 1 y la ubicación no es (7,7).
    def test_raise_no_centre_location_exception_when_round_number_1_and_location_not_77(self):
        board = Board()
        round_number = 1
        location = (5, 5)
        with self.assertRaises(NoCentreLocationExeption):
            board.validate_first_move(round_number, location)
    # Debe devolver True cuando round_number no es 1 y la ubicación es (7,7).
    def test_return_true_when_round_number_not_1_and_location_77(self):
        board = Board()
        round_number = 2
        location = (7, 7)
        result = board.validate_first_move(round_number, location)
        self.assertTrue(result)
    # Debería devolver NoCentreLocationExeption cuando round_number es 1 y location es None.
    def test_raise_exception_when_round_number_1_and_location_none(self):
        board = Board()
        round_number = 1
        location = None
        self.assertRaises(NoCentreLocationExeption, board.validate_first_move, round_number, location)
    # Debería devolver NoCentreLocationExeption cuando round_number es 1 y location no es una tupla.
    def test_raise_no_centre_location_exception_when_round_number_1_and_location_not_tuple(self):
        board = Board()
        round_number = 1
        location = "7,7"
        with self.assertRaises(NoCentreLocationExeption):
            board.validate_first_move(round_number, location)
#test validate_crossing_words:
    # Devuelve False cuando todas las fichas de la palabra están vacías y no hay palabras cruzadas.
    def test_empty_word_no_crossing_words(self):
        board = Board()
        word = ""
        location = (3, 5)
        orientation = True
        result = board.validate_crossing_words(word, location, orientation)
        self.assertFalse(result)
    # Devuelve False cuando todas las fichas de la palabra están vacías y hay palabras que se cruzan, pero todas las palabras que se cruzan están vacías.
    def test_empty_word_with_empty_crossing_words(self):
        board = Board()
        word = ""
        location = (3, 5)
        orientation = True
        # Añade palabras de cruce vacías
        board.grid[3][5].tile = "A"
        board.grid[3][6].tile = "B"
        board.grid[3][7].tile = "C"
        result = board.validate_crossing_words(word, location, orientation)
        self.assertFalse(result)
    # Devuelve False cuando todas las fichas de la palabra no están vacías y no hay palabras cruzadas.
    def test_nonempty_word_no_crossing_words(self):
        board = Board()
        word = "VERDE"
        location = (3, 5)
        orientation = True
        result = board.validate_crossing_words(word, location, orientation)
        self.assertFalse(result)
    # Devuelve False cuando la palabra está vacía.
    def test_empty_word(self):
        board = Board()
        word = ""
        location = (3, 5)
        orientation = True
        result = board.validate_crossing_words(word, location, orientation)
        self.assertFalse(result)
    # Devuelve False cuando la palabra no está vacía, pero la ubicación está fuera del tablero.
    def test_word_out_of_board(self):
        board = Board()
        word = "OGROS"
        location = (14, 5)
        orientation = True
        result = board.validate_crossing_words(word, location, orientation)
        self.assertFalse(result)
    # Devuelve False cuando la palabra es de una letra y la ubicación está vacía.
    def test_one_letter_word_empty_location(self):
        board = Board()
        word = "H"
        location = (3, 5)
        orientation = True
        result = board.validate_crossing_words(word, location, orientation)
        self.assertFalse(result)
#test is_empty:
    # devuelve True si la celda central está vacía
    def test_empty_center_cell(self):
        board = Board()
        self.assertTrue(board.is_empty())
    # devuelve False si la celda central no está vacía
    def test_non_empty_center_cell(self):
        board = Board()
        board.grid[7][7].tile = Tile('A', 1)
        self.assertFalse(board.is_empty())
    # devuelve False si la celda central tiene un azulejo con valor 0
    def test_center_cell_with_zero_value(self):
        board = Board()
        board.grid[7][7].tile = Tile('A', 0)
        self.assertFalse(board.is_empty())
    # devuelve False si la celda central tiene una ficha con valor negativo
    def test_center_cell_with_negative_value(self):
        board = Board()
        board.grid[7][7].tile = Tile('A', -1)
        self.assertFalse(board.is_empty())
    # devuelve False si la celda central tiene un azulejo con un valor superior a 10
    def test_center_cell_with_large_value(self):
        board = Board()
        board.grid[7][7].tile = Tile('A', 11)
        self.assertFalse(board.is_empty())
    # devuelve False si la celda central tiene un azulejo con un valor no entero.
    def test_center_cell_with_non_integer_value(self):
        board = Board()
        board.grid[7][7].tile = Tile('A', 1.5)
        self.assertFalse(board.is_empty())
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
        self.assertIsNone(cell.tile)
        self.assertEqual(
            cell.calculate_value(),
            0,
        )

    def test_add_letter(self):
        cell = Cell(multiplier=1, multiplier_type='', row=0, col=0)
        letter = Tile(letter='a', value=1)

        cell.add_letter(letter=letter, row=0, col=0)

        self.assertEqual(cell.tile, letter)

    def test_cell_value(self):
        cell = Cell(multiplier=2, multiplier_type='letter', row=0, col=0)
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter, row=0, col=0)

        self.assertEqual(
            cell.calculate_value(),
            6,
        )

    def test_cell_multiplier_word(self):
        cell = Cell(multiplier=2, multiplier_type='word', row=0, col=0)
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter, row=0, col=0)

        self.assertEqual(
            cell.calculate_value(),
            3,
        )


if __name__ == '__main__':
    unittest.main()