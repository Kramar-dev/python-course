### Struktury danych:
###### magazyn
* id towaru
* nazwa
* ilość na stanie
* cena za sztukę

###### użytkownicy
* id użytkownika
* email
* hasło
* czy administrator?
* historia zamówień

###### koszyk
* id towaru
* ilość w koszyku
* całkowita cena
* (pamiętaj, że użytkownik będzie chciał zobaczyć też nazwę towaru, <br>
cenę za sztukę i sumę całego koszyka, <br>
ale nie musisz tych informacji trzymać w koszyku, żeby mu to wyświetlić)

### Użytkownik:
* zaloguj na konto
* wyświetl towary
* wyszukaj towar
* dodaj towar do koszyka
* usuń towar z koszyka
* zmień ilość towaru w koszyku
* sfinalizuj zamówienie(dopisz do historii transakcji i <br>
usuń odpowiednie ilości poszczególnych towarów z magazynu)

### Administrator:
* zaloguj na konto
* wyświetl towary
* wyszukaj towar
* dodaj nowy towar
* usuń towar
* zmień ilość towaru na stanie
* zmień cenę towaru
* usuń użytkownika
* dodaj użytkownika
* zmień hasło użytkownika
* wyświetl dane użytkownika(włącznie z historią zamówień)