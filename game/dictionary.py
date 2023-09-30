from pyrae import dle

class Dictionary:
    def get_word(self, word):
        res = dle.search_by_word(word)
        result = res.to_dict()
        if result.get('title') == 'Diccionario de la lengua española | Edición del Tricentenario | RAE - ASALE':
            return False
        else:
            return True
        