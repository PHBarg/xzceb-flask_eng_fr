"""Step1"""
from deep_translator import MyMemoryTranslator

"""Used as variable"""
language_translator = MyMemoryTranslator()

def english_to_french(english_text):
    """
    Translates English text to French using the MyMemory Translator.
    """
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr'
    ).get_result()

    french_text = translation['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    """
    Translates French text to English using the MyMemory Translator.
    """
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en'
    ).get_result()

    french_text = translation['translations'][0]['translation']
    return french_text