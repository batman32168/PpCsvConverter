class column:
    def __init__(self, definition:str):
        self._definition = definition

    @property
    def header(self):
        if self._definition['name'] is None:
            raise KeyError('Der Name/Spaltenüberschrift muss angegeben sein.')
        else:
            return self._definition['name']

    @property
    def column_number(self):
        if self._definition['column_number'] is None:
            return -1
        else:
            return self._definition['column_number']

    @property
    def format(self):
        if self._definition['format'] is None:
            return ''
        else:
            return self._definition['format']
