import xlrd
from datetime import datetime


def write_lines(input_file, header):
    booking_lines = header
    if input_file.lower().endswith('.xls'):
        try:
            workbook = xlrd.open_workbook(input_file)
            sheet = workbook.sheet_by_index(0)
            max_rows = sheet.nrows
            for r in range(1, max_rows):
                try:
                    valuate_date = datetime.strptime(sheet.cell_value(rowx=r, colx=0),'%Y-%m-%d %H:%M:%S')\
                        .strftime('%Y-%m-%dT%H:%M')
                    note = sheet.cell_value(rowx=r, colx=1)
                    amount = str(sheet.cell_value(rowx=r, colx=2)).replace('.', ',')
                    booking_type = ''
                    if note.upper().startswith('GELD EINZAHLEN') or note.upper().startswith('ADDING FUNDS') :
                        booking_type = 'Einlage'
                    elif note.upper().startswith('ZINSZAHLUNG') or note.upper().startswith('PAYING INTEREST') :
                        booking_type = 'Zinsen'
                    if booking_type != '':
                        booking_lines.append(valuate_date + ';' + booking_type + ';' + amount + ';EUR;' + note + '\r\n')
                except Exception as inner_error:
                    print('Fehler bei der Verarbeitung der Zeile ' + str(r) + ': ' + repr(inner_error))
        except Exception as error:
            print('Allgemeiner Fehler beim Verarbeiten der XLS Datei: ' + repr(error))
    else:
        print('Die angegeben Dateiendung wird nicht unterstützt.')
        raise ValueError('Die Dateiendung wird nicht unterstützt.')
    return booking_lines
