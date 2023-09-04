import unittest

from game.tiles import BagTiles,Tile, Comodin
from piezas import DATA
from unittest.mock import patch

class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('Z', 10)
        self.assertEqual(tile.letter, 'Z')
        self.assertEqual(tile.value, 10)
class TestComodin(unittest.TestCase):
    def test_Comodin_tile(self):
        Comodin_tile = Comodin()
        self.assertEqual(Comodin_tile.letter, '_')
        self.assertEqual(Comodin_tile.value, 0)
class TestBagTiles(unittest.TestCase):
    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        self.assertEqual(
            len(bag.tiles),
            100,
        )
        self.assertEqual(
            patch_shuffle.call_count,
            1,
        )
        self.assertEqual(
            patch_shuffle.call_args[0][0],
            bag.tiles,
        )

    def test_take(self):
        bag = BagTiles()
        tiles = bag.take(2)
        self.assertEqual(
            len(bag.tiles),
            98,
        )
        self.assertEqual(
            len(tiles),
            2,
        )

    def test_put(self):
        bag = BagTiles()
        put_tiles = [Tile('Z', 1), Tile('Y', 1)]
        bag.put(put_tiles)
        self.assertEqual(
            len(bag.tiles),
            100,
        )
    def test_put_comodin(self):
        bag = BagTiles()
        Comodin_tiles = bag.take(2)
        bag.put(Comodin_tiles)
        self.assertEqual(len(bag.tiles), 100)


if __name__ == '__main__':
    unittest.main()