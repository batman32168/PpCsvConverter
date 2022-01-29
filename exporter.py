import os

class exporter:

    def set_raw_data(self,raw_data:list):
        self.rawdate = raw_data

    def write_csv_file(self, filename: str, path:str,export_name:str):
        output_folder= path + '/output'
        if not os.path.exists(output_folder):
            print('Ausgabeverzeichnis ist noch nicht vorhanden --> Wird erstellt für dich.')
            os.makedirs(output_folder)
        output_file = str.format("{}/{}_{}.csv",output_folder,export_name, filename)
        counter =1
        while os.path.isfile(output_file):
            output_file = str.format("{}/{}_{}({}).csv",output_folder, export_name, filename, str(counter))
            counter +=1
        print(str.format('Ausgabedatei {} wird geschrieben',output_file))
        with open(output_file, 'w') as file:
            file.write(self._header +'\n')
            for item in self.rawdate:
                file.write("%s\n" % item)

    def write_header(self,columns: list):
        self._header:str =''
        for column in columns:
            self._header =str.format("{}{};",self._header,column)



