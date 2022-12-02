import unittest

from translator import frenchToEnglish,englishToFrench

class TestfrenchToEnglish(unittest.TestCase):
    def test1(self):
        #self.assertNotEqual(frenchToEnglish('a'),'Oui')
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')


class TestenglishToFrench(unittest.TestCase):
    def test1(self):
        #self.assertNotEqual(englishToFrench('b'),'Hello')
        self.assertEqual(englishToFrench('Hello'),'Bonjour')

unittest.main()