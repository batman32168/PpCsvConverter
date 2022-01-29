# Portfolio CSV Converter
Konvertiert Excel und CSV Dateien in das für den CSV Import von Portfolio 
Performance notwendige format.

## Usages

``` python
python3 PpCsvConverter.py -i[nputfolder] <pathToFolderWithFiles
```

## Output  
The result files - in csv format - will be stored in a new folder named 'output' inside the input folder.

## Configuration
For configuration there is a **configuration.yml** file used.

```yaml
---
- name: 'Viainvest'                               # the name of the current config
  filepattern: 'transactions202*.xlsx'            # the pattern is used to identify the necessary files
  start_row: 2                                    # start reading in this row. Count starts at 1
  summary: 'weekly'                               # *optional: calculate at sum.
  columns:                                        # list of columns which will be read
    - name: 'amount'                              # name/header in the export file
      column_number: 7                            # column number in the original file. Count start at 1
      format: '.2f'                               # format of the value
    - name: 'valuta_date'
      column_number: 2
      format: '%m/%d/%Y'
    - name: 'note'
      column_number: 5
    - name: 'booking_type'
      column_number: 3
      mapping:                                          # mapping list only available in column booking_type.
        - type: 'Einlage'
          search_value: 'Amount of funds deposited'
        - type: 'Zinsen'
          search_value: 'Amount of interest payment'
```

