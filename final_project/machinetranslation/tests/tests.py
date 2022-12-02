import unittest

from translator import french_to_english,english_to_french

class TestfrenchToEnglish(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')

    def test2(self):
        self.assertIsNone(french_to_english(None), None)

class TestenglishToFrench(unittest.TestCase):

    def test1(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
    
    def test2(self):
        self.assertIsNone(english_to_french(None), None)

unittest.main()