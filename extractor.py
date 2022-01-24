import column
import uuid
import xlrd
import openpyxl
from collections import OrderedDict
from datetime import datetime


class extractor:
    def __init__(self, configuration: str):
        self._configuration = configuration

    @property
    def splitt_char(self):
        if self._configuration['splitt_char'] is None:
            return ';'
        else:
            return self._configuration['splitt_char']

    @property
    def start_row(self):
        if self._configuration['start_row'] is None:
            return 0
        else:
            return self._configuration['start_row']

    @property
    def filepattern(self):
        if self._configuration['filepattern'] is None:
            return '*.*'
        else:
            return self._configuration['filepattern']

    @property
    def name(self):
        if self._configuration['name'] is None:
            return uuid.UUID
        else:
            return self._configuration['name']

    @property
    def columns(self):
        temp_columns: OrderedDict ={}
        if self._configuration['columns'] is not None:
            for column_config in self._configuration['columns']:
                column_name = column_config['name']
                print('Lese Spalte ' + column_name)
                temp_class =column.column(column_config)
                temp_columns[column_name] = temp_class
        return temp_columns

    def extract_lines(self, file: str):
        transaction = []
        if self.filepattern.lower().endswith('.xls'):
            transaction = self.__extract_xls_file(file)
        elif self.filepattern.lower().endswith('.xlsx'):
            transaction = self.__extract_xlsx_file(file)
        elif self.filepattern.lower().endswith('.csv'):
            transaction = self.__extract_csv_file(file)

    def __extract_xls_file(self, input_file: str):
        transaction = []
        if input_file.lower().endswith('.xls'):
            try:
                workbook = xlrd.open_workbook(input_file)
                sheet = workbook.sheet_by_index(0)
                max_rows = sheet.nrows
                columns = self.columns.values()
                for r in range(self.start_row, max_rows):
                    try:
                        line = ''
                        for column in columns:
                            cell_value = column.get_formated_value(sheet.cell_value(rowx=r, colx=column.column_number))
                            line = line + cell_value + ';'
                    except Exception as innererror:
                        print('Allgemeiner Fehler beim Lesen der Zeile:{}{}'.format(r, repr(innererror)))
            except Exception as error:
                print('Allgemeiner Fehler beim Verarbeiten der XLS Datei: ' + repr(error))
        return transaction

    def __extract_xlsx_file(self, input_file: str):
        transaction = []
        if input_file.lower().endswith('.xlsx'):
            try:
                workbook = openpyxl.load_workbook(input_file)
                sheet = workbook.active
                max_rows = sheet.max_row
                columns = self.columns.values()
                for r in range(self.start_row, max_rows):
                    try:
                        line = ''
                        for column in columns:
                            cell_value = column.get_formated_value(sheet.cell(row=r, column=column.column_number).value)
                            line = line + cell_value + ';'
                    except Exception as inner_error:
                        print('Fehler bei der Verarbeitung der Zeile ' + str(r) + ': ' + repr(inner_error))
            except Exception as error:
                print('Allgemeiner Fehler beim Verarbeiten der XLSX Datei: ' + repr(error))
        return transaction

    def __extract_line(self, line):
        print(line)
