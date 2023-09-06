import unittest
from game.board import Board
from game.board import Cell
from game.tiles import Tile


class TestCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        board = Board()
        word = [
            Cell(letter=Tile('C', 1)),
            Cell(letter=Tile('A', 1)),
            Cell(letter=Tile('S', 2)),
            Cell(letter=Tile('A', 1)),
        ]
        
        value = board.calculate_word_value(word)
        self.assertEqual(value, 5)

    def test_with_letter_multiplier(self):
        board = Board()
        word = [
            Cell(letter=Tile('C', 1)),
            Cell(letter=Tile('A', 1)),
            Cell(
                letter=Tile('S', 2),
                multiplier=2,
                multiplier_type='letter',
            ),
            Cell(letter=Tile('A', 1)),
        ]
        value = board.calculate_word_value(word)
        self.assertEqual(value, 7)

    def test_with_word_multiplier(self):
        board = Board()
        word = [
            Cell(letter=Tile('C', 1)),
            Cell(letter=Tile('A', 1)),
            Cell(
                letter=Tile('S', 2),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(letter=Tile('A', 1)),
        ]
        value = board.calculate_word_value(word)
        self.assertEqual(value, 10)

    def test_with_letter_word_multiplier(self):
        board = Board()
        word = [
            Cell(
                multiplier=3,
                multiplier_type='letter',
                letter=Tile('C', 1)
            ),
            Cell(letter=Tile('A', 1)),
            Cell(
                letter=Tile('S', 2),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(letter=Tile('A', 1)),
        ]
        value = board.calculate_word_value(word)
        self.assertEqual(value, 14)

    def test_with_letter_word_multiplier_no_active(self):
        board = Board()
        word = [
            Cell(
                multiplier=3,
                multiplier_type='letter',
                letter=Tile('C', 1)
            ),
            Cell(letter=Tile('A', 1)),
            Cell(
                letter=Tile('S', 2),
                multiplier=2,
                multiplier_type='word',
            ),
            Cell(letter=Tile('A', 1)),
        ]
        value1 = board.calculate_word_value(word)    # Calcula el valor con multiplicadores
        value2 = board.calculate_word_value(word)    # Calcula el valor sin multiplicadores
        self.assertEqual(value1, 14)
        self.assertEqual(value2, 7)
if __name__ == '__main__':
    unittest.main()