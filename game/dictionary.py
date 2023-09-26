from pyrae import dle

class Dictionary:
    """def validate_word(self,word):
        word_check = ''
        for i in word:
            word_check += i.letter.letter
        # Search on the RAE dictionary
        result = dle.search_by_word(word=word_check)

        if result:
            title = result.to_dict().get('title') 

            if title != 'Diccionario de la lengua española | Edición del Tricentenario | RAE - ASALE':
                return True 
        return False"""
    
    def validate_word(self, word):
        result = dle.search_by_word(word)

        if result:
            title = result.to_dict().get('title') 

            if title != 'Diccionario de la lengua española | Edición del Tricentenario | RAE - ASALE':
                return True  # La palabra existe en el diccionario
        return False  # La palabra no existe
