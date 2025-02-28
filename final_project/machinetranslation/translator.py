"""
This module uses deep_translator package to convert text from one language to another 
"""
from deep_translator import MyMemoryTranslator
def english_to_french(english_text):
    """This function will translate from english to french"""
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text

def french_to_english(french_text):
    """This function will translate from french to english"""
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
