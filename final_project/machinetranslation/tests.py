import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
    def test_englishToFrench_translation(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
        self.assertEqual(englishToFrench("World"), "Monde")
        self.assertIsNotNone(englishToFrench("HNello"))

    def test_frenchToEnglish_translation(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
        self.assertEqual(frenchToEnglish("Monde"), "World")
        self.assertIsNotNone(frenchToEnglish("Bonjour"))

if __name__ == '__main__':
    unittest.main()