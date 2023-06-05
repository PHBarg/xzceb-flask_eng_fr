import json
import os
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translates English text to French using the MyMemory Translator.
    """
    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    print(french_text)
    return french_text

def french_to_english(french_text):
    """
    Translates French text to English using the MyMemory Translator.
    """
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    print(english_text)
    return english_text
