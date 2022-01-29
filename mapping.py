class mapping:
    def __init__(self, definition:str):
        self._definition = definition

    @property
    def value(self):
        if self._definition['value'] is None:
            return 'Einlage'
        else:
            return self._definition['value']

    @property
    def serach_values(self):
        if self._definition['search_values'] is None:
            return ''
        else:
            return self._definition['search_values'].lower().split(';')
