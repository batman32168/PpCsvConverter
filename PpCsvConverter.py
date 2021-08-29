# coding=utf-8
import argparse
import via_helper as via
import main_helper as helper


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inputfile', dest="input_file", required=True,
                        help='Name (inkl. Pfad) zur Eingangsdatei.')
    parser.add_argument('-f', '--format', dest="file_format", required=True,
                        help='Format bzw. Datentyp der Datei. Mögliche Werte: \r\n * viainvest')

    # Startparamter einlesen
    int_arg = parser.parse_args()
    input_file = int_arg.input_file

    # Header in für die PP CSV Datei
    bookings = ['Datum;Typ;Wert;Buchungswährung;Notiz\r\n']

    # Fall unterscheidung treffen.
    if int_arg.file_format.lower() == 'viainvest' or int_arg.file_format.lower() == 'via':
        bookings = via.write_lines(input_file)

    # Ausgabe der Datei
    helper.write_pp_csv_file(input_file, bookings)
