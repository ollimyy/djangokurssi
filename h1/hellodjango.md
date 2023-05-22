# h1 Hello Django

## Ympäristö
Tein harjoituksen 22.05.2023 virtuaalikoneessa Debian 11 käyttöjärjestelmällä.

## Django kehitysympäristön asennus
Asensin virtualenv-työkalun komennolla:
```$ sudo apt get install virtualenv```.
Loin uuden virtuaaliympäristön, jossa on viimeisimmät paketit ja käytetään python versiota kolme, komennolla
```virtualenv --system-site-packages -p python3 env/```.
Aktivoin virtuaaliympäristön komennolla:
```$ source env/bin/activate```.
Ennen djangon asennusta varmistin, että asennus tapahtuu virtuaaliympäristöön.
```which pip```
Loin tekstitiedoston, jossa määritellään projektin riippuvuudet, tässä tapauksessa pelkkä django ja asensin sen käyttäen pip-työkalua.
```$ echo django > requirements.txt
$ pip install -r requirements.txt```
Varmistin, että django on asennettu komennolla
```$ django-admin --version
4.2.1```.

## Django projektin luonti ja testaus
Loin uuden django-projektin nimeltä ollico: ```$ django-admin startproject ollico```
Testasin, että djangon oletussivu tulee näkyviin selaimessa:
```$ cd ollico
$ ./manage.py runserver```
![Django-oletussivu](./django_install_test.png)
