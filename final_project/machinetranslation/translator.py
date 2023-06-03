import json
import os
from deep_translator import MyMemoryTranslator

def englishToFrench(englishText):
    """
    Translates English text to French using the MyMemory Translator.
    """
    frenchText = MyMemoryTranslator(source='en', target='fr').translate(englishText)
    print(frenchText)
    return frenchText

def frenchToEnglish(frenchText):
    """
    Translates French text to English using the MyMemory Translator.
    """
    englishText = MyMemoryTranslator(source='fr', target='en').translate(frenchText)
    print(englishText)
    return englishText
