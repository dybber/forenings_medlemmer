Før du går i gang med at kode så stik endelig forbi [slack](https://codingpirates.signup.team) 
og fortæl os om det du vil udvikle på, det kan jo tænkes vi allerede er i gang med det. 


## Første gangs opsætning
For at kunne køre medlemssystemet skal du have installeret docker. Hvis du bruger
Docker for Windows vil du opleve at django ikke fanger fil ændringer når du udvikler.
Der er lavet et tool til at omgå det indtil LCOW er i windows (Linux Containers On Windows). http://blog.subjectify.us/miscellaneous/2017/04/24/docker-for-windows-watch-bindings.html

De følgende kommandoer vil få dig hurtigt i gang og op at køre:
```
# git clone git@github.com:CodingPirates/forenings_medlemmer.git
# cd forenings_medlemmer
# docker-compose run --rm backend environment/reset-db.sh
# docker-compose up
```

Systemet er nu kørende og du kan tilgå admin interfacet gennem 
[localhost:8000/admin](http://localhost:8000/admin)
med username=admin, password=admin.

Hver gang du vil arbejde på systemet køres 
```
# docker-compose up
```
Når du henter ændringer ned fra git skal du for at sikre din
database er up to date restarte serveren.
```
# CTRL-c
# docker-compose up
```
Hvis requirements.txt er ændret, eller python version opdateret eller
lign. Kan det være docker image skal bygges igen. Det gøres med
```
# docker-compose build
```

## Pull requests
Pull request er altid velkommen, følgende krav skal dog opfyldes. 
* [flake](http://flake8.pycqa.org/en/latest/) skal køres på koden. 
* Alle tests case skal lykkes
  

---
Mange editors kan sætte op til at informere dig om formatering problemer, 
alternativ kan du køre flake8 fra kommandolinjen manuelt
```
# docker-compose run --rm backend flake8
```
  
Du kan tjekke om dig koden bryder nogle test cases passere ved at køre
```
# docker-compose run --rm backend ./manage.py test
```
Hvis du har tilføjet ny funktionalitet må du meget gerne skrive unit tests af det

## Debugging via PyCharm
Se https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html

Først skal der oprettes forbindelse til en docker server.
![Docker server config](./doc_assets/docker_server.png)

Derefter skal der oprettes en python interpreter, som kører via vores docker-compose spec.
![Interpreter config](./doc_assets/interpreter.png)

Sidst skal der laves en run configuration som benytter den nyoprettede interpreter.
Bemærk at host skal sættes til `0.0.0.0`.
![Run config](./doc_assets/run_conf.png)