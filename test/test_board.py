import unittest
from game.board import *
class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(
            len(board.grid),
            15,
        )
        self.assertEqual(
            len(board.grid[0]),
            15,
        )  
    def test_place_word_cross_vertical_fine(self):
        fill_with = (
            '               ' # 0
            '               ' # 1
            '               ' # 2
            '               ' # 3
            '               ' # 4
            '               ' # 5
            '               ' # 6
            '       CASA    ' # 7
            '        S      ' # 8
            '        A      ' # 9
            '        D      ' # 0
            '        O      ' # 1
            '               ' # 2
            '               ' # 3
            '               ' # 4
        )   #012345678901234
        board = Board()
        # show_board(board)
        word = "FACULTAD"
        location = (6, 11)
        orientation = "vertical"
        word_is_valid = board.validate_word(word, location, orientation)
        assert word_is_valid == True
    def test_cells_multiplier(self):
        grid = Board()
        grid.cells_multiplier()
        for coordinate in TRIPLE_WORD_SCORE:
            cell = grid.grid[coordinate[0]][coordinate[1]]
            self.assertEqual(cell.multiplier_type, "word")
            self.assertEqual(cell.multiplier, 3)

        for coordinate in DOUBLE_WORD_SCORE:
            cell = grid.grid[coordinate[0]][coordinate[1]]
            self.assertEqual(cell.multiplier_type, "word")
            self.assertEqual(cell.multiplier, 2)

        for coordinate in TRIPLE_LETTER_SCORE:
            cell = grid.grid[coordinate[0]][coordinate[1]]
            self.assertEqual(cell.multiplier_type, "letter")
            self.assertEqual(cell.multiplier, 3)

        for coordinate in DOUBLE_LETTER_SCORE:
            cell = grid.grid[coordinate[0]][coordinate[1]]
            self.assertEqual(cell.multiplier_type, "letter")
            self.assertEqual(cell.multiplier, 2)

    def test_cell_multiplier(self):
        grid = Board()
        coordinate = (0, 1)
        multiplier_type = "word"
        multiplier_value = 3
        grid.cell_multiplier(coordinate, multiplier_type, multiplier_value)
        cell = grid.grid[coordinate[0]][coordinate[1]]
        self.assertEqual(cell.multiplier_type, multiplier_type)
        self.assertEqual(cell.multiplier, multiplier_value)

    def test_word_inside_board(self):
        board = Board()
        word = "Facultad"
        location = (5, 4)
        orientation = "H"
        
        word_is_valid = board.validate_word(word, location, orientation)
    
        assert word_is_valid == True
    

    def test_word_out_of_board(self):
        board = Board()
        word = "Facultad"
        location = (14, 4)
        orientation = "H"

        word_is_valid = board.validate_word(word, location, orientation)

        assert word_is_valid == False

    def test_word_in_board_V(self):
        board = Board()
        word = "Facultad"
        location = (4, 4)
        orientation = "V"

        word_is_valid = board.validate_word(word, location, orientation)

        assert word_is_valid == True

    def test_word_out_of_board_V(self):
        board = Board()
        word = "Facultad"
        location = (4, 14)
        orientation = "V"

        word_is_valid = board.validate_word(word, location, orientation)
        assert word_is_valid == False    
        
    def test_put_words_horizontal(self):
        board = Board()
        tile1 = Tile('H',4)
        tile2 = Tile('O',1)
        tile3 = Tile('Y',4)
        word = [tile1, tile2, tile3]
        board.put_words(word, (4,4),'H')
        self.assertEqual(board.grid[4][4].tile, tile1) #para que 'H' sea igual a 'H'
        self.assertEqual(board.grid[4][5].tile, tile2)
        self.assertEqual(board.grid[4][6].tile, tile3)

    def test_put_words_horizontal_exception(self):
        board = Board()
        tile1 = Tile('H',4)
        tile2 = Tile('O',1)
        tile3 = Tile('Y',4)
        word = [tile1, tile2, tile3]
    # Puts the word
        board.put_words(word, (4,4),'H')
    # Try to put a letter
        self.assertFalse(board.put_words('A', (4,4),'H')) #no la pone

    def test_put_words_vertical(self):
        board = Board()
        tile1 = Tile('H',4)
        tile2 = Tile('O',1)
        tile3 = Tile('Y',4)
        word = [tile1, tile2, tile3]
        board.put_words(word, [4,4],'V')
        self.assertEqual(board.grid[4][4].tile, tile1) #para que 'H' sea igual a 'H'
        self.assertEqual(board.grid[5][4].tile, tile2)
        self.assertEqual(board.grid[6][4].tile, tile3)

    def test_put_words_vertical_exception(self):
        board = Board()
        tile1 = Tile('H',4)
        tile2 = Tile('O',1)
        tile3 = Tile('Y',4)
        word = [tile1, tile2, tile3]
    # Puts the word
        board.put_words(word, [4,4],'H')
    # Try to put a letter
        self.assertFalse(board.put_words('A', (4,4),'H'))

 

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
        cell = Cell(multiplier=3, multiplier_type='letter')
        letter = Tile(letter='q', value=5)
        cell.add_letter(letter=letter)

        self.assertEqual(
            cell.calculate_value(),
            15,
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