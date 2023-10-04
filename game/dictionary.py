from pyrae import dle

class Dictionary:
    dle.set_log_level(log_level='CRITICAL')
    def get_word(self, word):
        res = dle.search_by_word(word)
        result = res.to_dict()
        if result.get('title') == 'Diccionario de la lengua española | Edición del Tricentenario | RAE - ASALE':
            return False
        else:
            return True
        