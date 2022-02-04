from googletrans import Translator

translator = Translator()

def translate (text, lang):
    
    txt = ''.join(text)
    result = translator.translate(txt, dest=lang)
    return result.text

