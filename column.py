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
            if (temp == 'total_amount'):
                return column_types.total_amount
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
        try:
            ret_value: str = original_value.replace('\"','')
            temp_value: str = original_value.replace('\"', '')
        except Exception:
            ret_value: str = original_value
            temp_value: str = original_value
        if (self.format != ''):
            if (self.header == column_types.valuta_date):
                try:
                    ret_value = temp_value.strftime('%Y-%m-%d %H:%M')
                except Exception:
                    try:
                        ret_value = datetime.fromisoformat(temp_value).strftime('%Y-%m-%d %H:%M')
                    except Exception:
                        ret_value = datetime.strptime(temp_value, self.format).strftime('%Y-%m-%d %H:%M')
            else:
                ret_value = str(temp_value).format(self.format)
        elif self.header == column_types.booking_type:
            if self.mappings is not None and len(self.mappings)!= 0:
                for search_value in self.mappings.keys():
                    if search_value.lower() in temp_value.lower():
                        ret_value = self.mappings[search_value]
                        break
            if ret_value == temp_value:
                raise ValueError('No mapping foung')
        return ret_value
