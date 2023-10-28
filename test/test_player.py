import unittest
from game.tiles import *
from game.player import *

class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player()
        self.assertEqual(
            len(player_1.tiles),
            0,
        )

    def test_draw_tiles(self): #verifica que el jugador y la bag tengan el numero correcto de ficha 
        bag = BagTiles()  
        player_1 = Player(bag) 
        player_1.draw_tiles(bag,7)
        self.assertEqual(len(player_1.tiles),7)
        self.assertEqual(len(bag.tiles),93)

    def test_reset(self):
        bag = BagTiles()
        player = Player(bag)
        player.draw_tiles(bag, 7) 
        player.reset()
        self.assertEqual(len(player.tiles), 0)# Verifica que el jugador tenga 0 fichas después del reset

    #def test_print(self):
    #    bag = BagTiles()
    #    player = Player(bag)
    #    player.draw_tiles(bag, 7) 
    #    player.display_hand()

    def SumScore(self):
        player = Player()
        self.assertEqual(player.score, 0)
        player.sumScore(15)
        self.assertEqual(player.score, 15)
        player.sumScore(32)
        self.assertEqual(player.score, 47)
class TestRack(unittest.TestCase):
    def setUp(self):
        # Crea una bolsa y un atril para cada prueba
        self.bag = BagTiles()
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


if __name__ == '__main__':
    unittest.main()