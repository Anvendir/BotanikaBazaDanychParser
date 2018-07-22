#uzyta wersja ptyhona:
Python 2.7.13

#sposob uzycia:
python BotanyDataBaseParser.py

#pliki wynikowe w katalogu:
/outputFiles/

- komendy do bazy danych mysql (testowane na bazie danych mysql postawionej na xamp)
insertCommandsForAllSpeciesList.txt
insertCommandsFor_0_1000.txt
insertCommandsFor_1000_2000.txt
insertCommandsFor_2000_3000.txt
insertCommandsFor_3000_4000.txt
insertCommandsFor_4000_5000.txt

- plik .csv do importu w arkuszu excel
excelDataBaseForImport.csv

#bazy danyc uzyte w projekcie
- bazaCalosc.txt - kompletna baza danych (22.07.2018) wyciagnieta z instytytu botaniki PAN w postaci odpowiedzi w formacie JSON
  adres powyzszej bazy: http://bomax.botany.pl/ib-db/check/

- BazaPolskichRodzinWGore.xlsx - recznie napisana baza danych polskich nazw taksonow od rodziny w gore (nazwy lacinksie taksonow z bazaCalosc.txt), plik nieuzywany w projekcie, stanowi jedynie podstawe do wygenerowania BazaPolskichRodzinWGore_unicode.txt

- BazaPolskichRodzinWGore_unicode.txt - plik wygenerowany z BazaPolskichRodzinWGore.xlsx poprzez zapisanie w programie wspomnianego pliku jako plik testowy w formacie unicode

#plik do generowania etykiet
BotanikaEtykiety.xlsx
