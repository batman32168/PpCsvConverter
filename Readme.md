# Portfolio CSV Converter
Konvertiert Excel und CSV Dateien in das für den CSV Import von Portfolio 
Perfromance notwendige format.

## Verwendung

``` python
python3 PpCsvConverter.py -i[nputfile] <DateiMitPfad> -f[ormat] <EingabeFormat>
```

## Unterstützte Importformate
### VIAInvest 
Exceldatei die über ***Kontoübersicht herunterladen*** lokal gespeichert werden kann. Aktuell erfolgt eine Unterscheidung nach Zinszahlung und Einzahlung.
![img.png](pictures/img.png)
Auszahlungen sind - noch - **nicht** umgesetzt.