import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french_translation(self):
        self.assertEqual(english_to_french("hello"), "bonjour")
        self.assertEqual(english_to_french("world"), "monde")
        self.assertIsNotNone(english_to_french("nhello"))

    def test_french_to_english_translation(self):
        self.assertEqual(french_to_english("bonjour"),"hello")
        self.assertEqual(french_to_english("monde"),"world")
        self.assertIsNotNone(french_to_english("nbonjour"))

if __name__ == '__main__':
    unittest.main()