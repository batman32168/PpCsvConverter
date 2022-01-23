import column
import uuid
import xlrd
import openpyxl
from datetime import datetime


class extractor:
    def __init__(self,configuration:str):
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
        temp_columns ={}
        if self._configuration['columns'] is not None:
            for column_config in self._configuration:
                column_name = column_config['name']
                print('Lese Spalte ' + column_name)
                temp_columns[column_name] = column.column(column_config)
        return temp_columns


    def extract_lines(self, file:str):
        transaction = []
        if self.filepattern.lower().endswith('.xls'):
            transaction = self.__extract_xls_file(file)
        elif self.filepattern.lower().endswith('.xlsx'):
            transaction = self.__extract_xlsx_file(file)
        elif self.filepattern.lower().endswith('.csv'):
            transaction = self.__extract_csv_file(file)


    def __extract_xls_file(self,input_file:str):
        transaction =[]
        if input_file.lower().endswith('.xls'):
            try
                workbook = xlrd.open_workbook(input_file)
                sheet = workbook.sheet_by_index(0)
                max_rows = sheet.nrows
                for r in range(self.start_row, max_rows):
                    try:
                        note = sheet.cell_value(rowx=r, colx=1)
                        '''
                        valuate_date = datetime.strptime(sheet.cell_value(rowx=r, colx=0), '%Y-%m-%d %H:%M:%S') \
                            .strftime('%Y-%m-%dT%H:%M')
                       
                        amount = str(sheet.cell_value(rowx=r, colx=2)).replace('.', ',')
                        booking_type = ''
                        if note.upper().startswith('GELD EINZAHLEN') or note.upper().startswith('ADDING FUNDS'):
                            booking_type = 'Einlage'
                        elif note.upper().startswith('ZINSZAHLUNG') or note.upper().startswith('PAYING INTEREST'):
                            booking_type = 'Zinsen'
                        if booking_type != '':
                            booking_lines.append(
                                valuate_date + ';' + booking_type + ';' + amount + ';EUR;' + note + '\r\n')
                        '''
            except Exception as error:
                print('Allgemeiner Fehler beim Verarbeiten der XLS Datei: ' + repr(error))
        return transaction


    def __extract_xlsx_file(self,input_file:str):
        transaction =[]
        if input_file.lower().endswith('.xlsx'):
            try:
                workbook = openpyxl.load_workbook(input_file)
                sheet = workbook.active
                row_counter=0
                for row in sheet.values:
                    try:
                        if(row_counter > self.start_row):
                            self.__extract_line(";".join(row))
                        row_counter+=1
                    except Exception as inner_error:
                        print('Fehler bei der Verarbeitung der Zeile ' + str(row_counter) + ': ' + repr(inner_error))
            except Exception as error:
                print('Allgemeiner Fehler beim Verarbeiten der XLSX Datei: ' + repr(error))
        return transaction


    def __extract_line(self,line):
        print(line)