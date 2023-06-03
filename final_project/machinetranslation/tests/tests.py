'''Testing English-French-English translator'''
import unittest
from deep_translator import MyMemoryTranslator
from translator import english_to_french, french_to_english


class TestTranslation(unittest.TestCase):

    '''Class for testing English-French-English translator'''
    def test_english_to_french(self):
        '''Testing translating english to french'''
        result = english_to_french("Hello World")
        self.assertEqual(result, "Bonjour le monde")

    def test_french_to_english(self):
        '''Testing translating french to english'''
        result = french_to_english("Bonjour le monde")
        self.assertEqual(result, "Hello World")

    def test_english_to_french_empty(self):
        '''Testing translating english to french'''
        result = english_to_french(None)
        self.assertEqual(result, "Please type or paste a word or phrase in English.")

    def test_french_to_english_empty(self):
        '''Testing translating french to english'''
        result = french_to_english("")
        self.assertEqual(result, "Please type or paste a word or phrase in French.")


if __name__ == '__main__':
    unittest.main()
