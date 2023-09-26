import unittest
from game.dictionary import Dictionary

class TestDictionary(unittest.TestCase):
    def setUp(self):
        self.dictionary = Dictionary()

    def test_word_exists(self):
        word = "casa"
        result = self.dictionary.validate_word(word)
        self.assertTrue(result)

    def test_word_does_not_exist(self):
        word = "xyzabc"
        result = self.dictionary.validate_word(word)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
