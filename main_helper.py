import os


def write_pp_csv_file(input_file, bookings):
    export_file = input_file + '_convert.csv'
    counter = 1
    while True:
        if not os.path.isfile(export_file):
            f = open(export_file, 'w')
            for line in bookings:
                f.write(line)
            f.close()
            break
        else:
            export_file = input_file + '_convert(' + str(counter) + ').csv'
            counter = counter + 1
