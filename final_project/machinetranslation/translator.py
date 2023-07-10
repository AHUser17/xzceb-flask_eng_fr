'''Import MyMemoryTranslator to translate from eng to fr'''
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    '''french_text equals the value of english_text 
    and translate it to french using MyMemoryTranslator, 
    then print and return the value'''
    french_text=MyMemoryTranslator(source='en-GB',target='fr-FR').translate(english_text)
    print (french_text)
    return french_text

def french_to_english(french_text):
    '''english_text equals the value of french_text 
    and translate it to english using MyMemoryTranslator, 
    then print and return the value'''
    english_text=MyMemoryTranslator(source='fr-FR',target='en-GB').translate(french_text)
    print(english_text)
    return english_text
