#uzyta wersja ptyhona:
Python 2.7.13

#sposob uzycia:
python BotanyDataBaseParser.py

#plik do generowania etykiet
- BotanikaEtykiety.xlsx

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

#bazy danych użyte w projekcie
- bazaCalosc.txt - kompletna baza danych (22.07.2018) wyciagnieta z instytytu botaniki PAN w postaci odpowiedzi w formacie JSON
  adres powyzszej bazy: http://bomax.botany.pl/ib-db/check/

- BazaPolskichRodzinWGore.xlsx - recznie napisana baza danych polskich nazw taksonow od rodziny w gore (nazwy lacinksie taksonow z bazaCalosc.txt), plik nieuzywany w projekcie, stanowi jedynie podstawe do wygenerowania BazaPolskichRodzinWGore_unicode.txt

- BazaPolskichRodzinWGore_unicode.txt - plik wygenerowany z BazaPolskichRodzinWGore.xlsx poprzez zapisanie w programie wspomnianego pliku jako plik testowy w formacie unicode

#Przypadki użycia.

I. Potrzebujemy wygenerować etykiety bez zmian w bazie:

1. Pobieramy plik BotanikaEtykiety.xlsx
2. W akruszu 'Etykiety' wpisujemy w polu pierwszym (wiersz 9) nazwę polską rośliny.
3. Reszta pól powinna być uzupełniona automatycznie

II. Potrzebujemy wczytać ponownie bazę danych w Excella

1. Generujemy nową baze do wczytania
	python BotanyDataBaseParser.py
	
2. Kopiujemy plik excelDataBaseForImport.csv oraz BotanikaEtykiety.xlsx

3. W excelu w arkuszu 'Baza danych' pliku BotanikaEtykiety.xlsx usuwamy wszystko (ctr + a, delete)
W oknie dialogowym ktore pyta o to usuniecie kwerend wykoszsytujacych baze, klikamy na 'Tak'

4. Wczytujemy nowa baze danych
a) zazanczamy trojkacik nad polem A1
b) w wstazce 'Dane' klikamy 'Z tekstu'
c) wybieramy plik excelDataBaseForImport.csv 
d) I karta, wybieramy:
- typ pliku: 'rozdzielany'
- rozpocznij import od wiersza: '1'
- pochodzenie pliku: '65001: Unicode (UTF-8)'
- moje dane maja naglowki: zostawiaomy niezaznaczone
Klikamy dalej

e) II karta, wybieramy:
- ograniczniki: 'średnik' (reszta niezaznaczona)
- kwafilikator tekstu: '{brak}'
Klikamy dalej

f) II karta, wybieramy:
- format danych w kolumnie: 'Ogolny'
Klikamy zakoncz

g) Importowanie danych - koncowe okno
- zostawiamy bez zmian

Powinno byc: 'Istniejacy arkusz' a dalej '=$A$1'
Klikamy OK

Dalej jak w przypadku uzycia I (pomijajac punkt 1)

III. Chcemy dodac polskie nazwy taksonow do bazy od rodziny wzwyż

1. edytujemy plik BazaPolskichRodzinWGore.xlsx wedlug przyjetej konwencji

2. Generujemy nowy plik BazaPolskichRodzinWGore_unicode.txt
a) w otwartym pliku BazaPolskichRodzinWGore.xlsx klikamy zapisz jako i wybieramy: 'BazaPolskichRodzinWGore.txt'
b) nazwa pliku wynikowego musi brzmiec: BazaPolskichRodzinWGore_unicode.txt w oknie dialogowym wybieramy tak

3. Przenosimy wygenerowany plik BazaPolskichRodzinWGore_unicode.txt do katalogu repozytorium
4. Postepujemy zgodnie z krokami opisanymi w przypadku uzycia II

#DO ZROBIENIA
- Poprawka w bazie dla wpisy topola kanadyjska, obecnie jest topola kandyjska
- uzueplnianie danych na podstawie synonimow, w bazie glownej sa synonimy moznaby zrobic tak aby po wpisaniu synonimu rowniez uzueplnialo nam arkusz
- arkusz z nowymi rekodami o ktore moznaby uzupelniac baze
