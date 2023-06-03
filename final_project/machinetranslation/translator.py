'''English-French-English translator'''
from deep_translator import MyMemoryTranslator

# englishToFrench, englishText, etc had to change english_to_french, english_text because
# pylint required to it
def english_to_french(english_text):
    '''Translating english to french'''
    if english_text == "" or english_text is None:
        return "Please type or paste a word or phrase in English."
    translator = MyMemoryTranslator(source='english', target='french')
    french_text = translator.translate(english_text)
    return french_text

def french_to_english(french_text):
    '''Translating french to english'''
    if french_text == "" or french_text is None:
        return "Please type or paste a word or phrase in French."
    translator = MyMemoryTranslator(source='french', target='english')
    french_text = translator.translate(french_text)
    return french_text
