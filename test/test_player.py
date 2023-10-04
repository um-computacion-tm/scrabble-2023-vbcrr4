import unittest
from game.tiles import BagTiles
from game.player import Player

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player()
        self.assertEqual(
            len(player_1.tiles),
            0,
        )
    def test_draw_tiles(self): #verifica que el jugador y la bag tengan el numero correcto de ficha 
        bag = BagTiles()  
        player = Player(bag) 
        player.draw_tiles(bag,7)
        self.assertEqual(len(player.tiles),7)
        self.assertEqual(len(bag.tiles),93)

    def test_reset(self):
        bag = BagTiles()
        player = Player(bag)
        player.draw_tiles(bag, 7) 
        player.reset()
        self.assertEqual(len(player.tiles), 0)# Verifica que el jugador tenga 0 fichas después del reset

    def test_print(self):
        bag = BagTiles()
        player = Player(bag)
        player.draw_tiles(bag, 7) 
        player.display_hand()
if __name__ == '__main__':
    unittest.main()