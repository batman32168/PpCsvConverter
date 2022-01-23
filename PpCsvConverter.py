# coding=utf-8
import argparse
import yaml
import glob

import bondora_helper
import cake_helper
import extractor
import robo_helper
import via_helper as via


import os.path


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inputfolder', dest="input_folder", required=True,
                        help='Pfad der die Eingabedateien enthält.')
    parser.add_argument('-o', '--outputfolder', dest="output_folder", required=False,
                        help='Pfad für die CSV-Exporte')

    # Startparameter einlesen
    int_arg = parser.parse_args()
    input_folder = int_arg.input_folder
    print('Eingangsverzeichnis: '+ input_folder)


    with open("./configuration.yml", "r") as stream:
        try:
            print('Konfiguration wird ...')
            print('... gelesen...')
            configuration = yaml.safe_load(stream)
            print('... verarbeite ...')
            extrators ={}
            for data_type in configuration:
                temp_ext = extractor.extractor(data_type)
                extrators[temp_ext.name] =temp_ext
                print('... ' + temp_ext.name + ' hinzugefügt ...')
            print('... geschlossen.')
        except yaml.YAMLError as exc:
            print('Konfiguration konnte nicht gelesen werden.' + exec)
            exit(-1)

    for file_parser in extrators.values():
        print("Starte mit Konfiguration " + file_parser.name)
        print("Lade Dateiliste mit dem Muster " +file_parser.filepattern)
        file_list = glob.glob(input_folder+"/"+file_parser.filepattern)
        for work_file in file_list:
            print("Verarbeite Datei '{}'".format(work_file))
            file_parser.extract_lines(work_file)
        print('Konfiguration '+data_type['name'] +' abgeschlossen.')
    print('Geschaft')
    print('Viel Spaß beim Import in dein PP.')
    exit(1)

