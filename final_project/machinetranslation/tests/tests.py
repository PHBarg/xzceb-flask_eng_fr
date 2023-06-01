import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def english_to_french(self):
        self.assertIsNotNone(english_to_french("HNello"), msg=None)
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("World"), "Monde")
        self.assertNotEqual(english_to_french("Hello"), "Hello")

class TestFrenchToEnglish(unittest.TestCase):
    def french_to_english(self):
        self.assertIsNotNone(french_to_english("Bonjour"), msg=None)
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Monde"), "World")
        self.assertNotEqual(french_to_english("Bonjour"), "Bonjour")

if __name__ == '__main__':
    unittest.main()