import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french_translation(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertEqual(english_to_french("World"),"Monde")
        self.assertIsNotNone(english_to_french("HNello"))

    def test_french_to_english_translation(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Monde"), "World")
        self.assertIsNotNone(french_to_english("Bonjour"))

if __name__ == '__main__':
    unittest.main()