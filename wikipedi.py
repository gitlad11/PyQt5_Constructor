import wikipedia

wiki = wikipedia
wiki.set_lang('ru')

def question_to_wiki(question):
    try:
        result = wiki.summary(question)
        return result
    except:
        try:
            result = wiki.search(question)
            if result:
                return result
            else:
                return 'pizdec'    
        except wikipedia.exceptions.PageError:
            return 'pizdec'