# coding=utf-8
import argparse

import bondora_helper
import via_helper as via
import main_helper as helper
import os.path


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inputfile', dest="input_file", required=True,
                        help='Name (inkl. Pfad) zur Eingangsdatei.')
    parser.add_argument('-f', '--format', dest="file_format", required=True,
                        help='Format bzw. Datentyp der Datei. Mögliche Werte: \r\n * viainvest *bondora')

    # Startparameter einlesen
    int_arg = parser.parse_args()
    input_file = int_arg.input_file
    if os.path.isfile(input_file):
        # Header in für die PP CSV Datei
        bookings = ['Datum;Typ;Wert;Buchungswährung;Notiz\r\n']

        # Fall unterscheidung treffen.
        if int_arg.file_format.lower() == 'viainvest' or int_arg.file_format.lower() == 'via':
            bookings = via.write_lines(input_file, bookings)
        elif int_arg.file_format.lower() == 'bondora':
            bookings = bondora_helper.write_lines(input_file, bookings)

        # Ausgabe der Datei
        helper.write_pp_csv_file(input_file, bookings)
    else:
        print("Die Datei '"+input_file+"' wurde nicht gefunden.")
