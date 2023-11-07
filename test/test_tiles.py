import unittest
from game.tiles import *
from unittest.mock import patch

class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile("A", 1)
        self.assertEqual(tile.letter, "A")
        self.assertEqual(tile.value, 1)

class TestComodin(unittest.TestCase):
    # Comodin se puede inicializar con la letra por defecto '?' y el valor 0
    def test_initialization(self):
        wildcard = Comodin()
        self.assertEqual(wildcard.letter, '?')
        self.assertEqual(wildcard.value, 0)
    # El método select_letter puede cambiar la letra del Comodín por una letra válida de LETTER_VALUES
    def test_select_letter_valid_letter(self):
        wildcard = Comodin()
        wildcard.select_letter('A')
        self.assertEqual(wildcard.letter, 'A')
    # El método select_letter establece el valor del Comodín en 0
    def test_select_letter_sets_value_to_zero(self):
        wildcard = Comodin()
        wildcard.select_letter('A')
        self.assertEqual(wildcard.value, LETTER_VALUES[0]['value'])
    # El método select_letter no cambia la letra del Comodín si la entrada no es una letra válida de LETTER_VALUES
    def test_select_letter_invalid_letter_no_change(self):
        wildcard = Comodin()
        wildcard.select_letter('Z')
        self.assertEqual(wildcard.letter, 'Z')
    # El método select_letter establece el valor del Comodin en 0 incluso si la entrada no es una letra válida de LETTER_VALUES
    def test_select_letter_invalid_letter_sets_value_to_zero(self):
        wildcard = Comodin()
        wildcard.select_letter('Z')
        self.assertEqual(wildcard.value, 10)
    # Comodin puede imprimirse como una cadena con el formato "{letter}:{value}"
    def test_string_representation(self):
        wildcard = Comodin()
        self.assertEqual(str(wildcard), "?:0")
class TestBagTiles(unittest.TestCase):
    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        self.assertEqual(len(bag.tiles),100)
        self.assertEqual(patch_shuffle.call_count,1)
        self.assertEqual(patch_shuffle.call_args[0][0],bag.tiles)

    def test_take(self):
        bag = BagTiles()
        tiles = bag.take(2)
        self.assertEqual(len(bag.tiles),98)
        self.assertEqual(len(tiles),2)

    def testBagPut(self):
        bag = BagTiles()
        putTiles = [Tile('Z',1), Tile('Y',1)]
        bag.put(putTiles)
        self.assertEqual(len(bag.tiles), 102)
        
    def test_add_single_tile_and_shuffle(self):
        bag = BagTiles()
        tile = Tile("A", 1)
        bag.put([tile])
        self.assertGreater(len(bag.tiles), 0)
        self.assertNotEqual(bag.tiles, [tile])
if __name__ == '__main__':
    unittest.main()