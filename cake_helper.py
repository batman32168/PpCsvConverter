# coding=utf-8
from datetime import datetime


def write_lines(input_file, auto_invest):
    booking_lines = ['Datum;Typ;Wert;Buchungswährung;Stück;WKN;Notiz\r\n']
    if input_file.lower().endswith('csv'):
        try:
            f = open(input_file, 'r')
            line_counter=1
            for r in f.readlines():
                try:
                    values = r.split(',')
                    if values[1].lower().replace('\"', '') in ['staking reward', 'Freezer staking bonus',
                                                               'Liquidity mining reward BTC-DFI',
                                                               'Freezer liquidity mining bonus']:
                        valuate_date = datetime.fromisoformat(values[0].replace('\"', '')).strftime('%Y-%m-%dT%H:%M')
                        fiat_currency = values[5].replace('\"', '')
                        fiat_value = values[4].replace('\"', '').replace('.', ',')
                        coin = values[3].replace('\"', '')
                        amount = values[2].replace('\"', '').replace('.', ',')
                        reference = values[8].replace('\"', '')
                        if auto_invest.lower == 'auto_invest':
                            booking_lines.append(valuate_date + ';Kauf;' + fiat_value + ';' + fiat_currency + ';' +
                                                 amount + ';' + coin + ';Reference ' + reference + '\r\n')
                        booking_lines.append(valuate_date + ';Zinsen;' + fiat_value + ';' + fiat_currency +
                                             ';;;Reference ' + reference + '\r\n')
                except Exception as inner_error:
                    print('Fehler bei der Verarbeitung der Zeile ' + str(line_counter) + ': ' + repr(inner_error))
                line_counter = line_counter + 1
        except Exception as error:
            print('Allgemeiner Fehler beim Verarbeiten der CSV Datei: ' + repr(error))
    else:
        print('Die angegeben Dateiendung wird nicht unterstützt.' + input_file)
    return booking_lines
