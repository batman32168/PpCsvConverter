import mapping
from datetime import datetime
from column_types import column_types


class column:
    def __init__(self, definition: str):
        self._definition = definition

    @property
    def header(self):
        if self._definition['name'] is None:
            raise KeyError('Der Name/Spaltenüberschrift muss angegeben sein.')
        else:
            temp = self._definition['name'].lower()
            if (temp == 'amount'):
                return column_types.amount
            if (temp == 'valuta_date'):
                return column_types.valuta_date
            if (temp == 'note'):
                return column_types.note
            if (temp == 'booking_type'):
                return column_types.booking_type
            if (temp == 'currency'):
                return column_types.currency
            if (temp == 'wkn'):
                return column_types.wkn
            return column_types.note

    @property
    def column_number(self):
        if 'column_number' in self._definition and self._definition['column_number'] is not None:
            return int(self._definition['column_number'])
        else:
            return -1

    @property
    def format(self):
        if 'format' in self._definition and self._definition['format'] is not None:
            return self._definition['format']
        else:
            return ''

    @property
    def mappings(self):
        temp_maps = {}
        if 'mapping' in self._definition and self._definition['mapping'] is not None:
            for map_config in self._definition['mapping']:
                temp_maps[map_config['search_value']] = map_config['type']
        return temp_maps

    def get_formated_value(self, original_value: str):
        ret_value: str = original_value
        if (self.format != ''):
            if (self.header == column_types.valuta_date):
                ret_value = datetime.strptime(original_value, self.format).strftime('%Y-%m-%dT%H:%M')
            else:
                ret_value = str(original_value).format(self.format)
        elif self.header == column_types.booking_type:
            if self.mappings is not None and len(self.mappings)!= 0:
                for search_value in self.mappings.keys():
                    if search_value in original_value:
                        ret_value = self.mappings[search_value]
                        break
            if ret_value == original_value:
                raise ValueError('No mapping foung')
        return ret_value
