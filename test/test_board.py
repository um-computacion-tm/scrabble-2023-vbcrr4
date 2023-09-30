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
    def test_positions_word_3_first(self): 
        board = Board()
        board.positions()
        self.assertEqual(board.grid[0][0].multiplier, 3)
        self.assertEqual(board.grid[0][0].multiplier_type, 'rata')
        self.assertEqual(board.grid[7][0].multiplier, 3)
        self.assertEqual(board.grid[7][0].multiplier_type, 'rata')
        self.assertEqual(board.grid[14][14].multiplier, 3)
        self.assertEqual(board.grid[14][14].multiplier_type, 'rata')
        self.assertNotEqual(board.grid[0][14], board.grid[5][7])

    def test_positions_word_3_second(self):  
        board = Board()
        board.positions()
        self.assertEqual(board.grid[1][1].multiplier, 2)
        self.assertEqual(board.grid[2][12].multiplier_type, 'rata')
        self.assertEqual(board.grid[11][3].multiplier, 2)
        self.assertEqual(board.grid[1][13].multiplier_type, 'rata')
        self.assertNotEqual(board.grid[0][14].multiplier, 2)
        self.assertNotEqual(board.grid[7][7].multiplier, 2)
        self.assertNotEqual(board.grid[6][7].multiplier, 2)

    def test_positions_letter_2(self):
        board = Board()
        board.positions()
        self.assertEqual(board.grid[0][3].multiplier, 2)
        self.assertEqual(board.grid[0][3].multiplier_type, 'pensar')
        self.assertEqual(board.grid[6][6].multiplier, 2)
        self.assertEqual(board.grid[6][6].multiplier_type, 'pensar')
        self.assertNotEqual(board.grid[0][14].multiplier, 2)
        self.assertNotEqual(board.grid[7][7].multiplier, 2)
        self.assertNotEqual(board.grid[6][1].multiplier, 2)

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