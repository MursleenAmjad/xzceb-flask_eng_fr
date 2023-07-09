import unittest
from translator import english_to_french,french_to_english
class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        # translator was translating Hello to Pepitoooo instead of Bonjour
        self.assertEqual(english_to_french('Hello'), 'Pepitoooo')
        self.assertEqual(english_to_french('Bonjour'), 'Bonjour') 
    def test2(self):
        self.assertEqual(english_to_french('My name is Mursleen'), 'Je m\'appelle Mursleen')
        
class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    def test2(self):
        self.assertEqual(french_to_english('Je m\'appelle Mursleen'), 'My name is Mursleen')
        
unittest.main()