Title: Hacer traducciones con google translate desde python
Date: 2015-10-19 9:00
Category: Tutorial Python
Tags: Canaima,Debian,Python,Ubuntu,Google Translate
lang: es
translation: true

Google Translate tiene un API que permite usar el traductor desde un programa, en el caso de Python se tiene [goslate](https://pypi.python.org/pypi/goslate).


Para instalarlo se usa `pip`:
```python
pip install goslate
```

Se ejecuta python. Y se prueba Hola Mundo en Inglés a otros idiomas:

Se importa el módulo:
```python
>>> import goslate
```
Se crea la instancia del objeto:
```python
>>> gs = goslate.Goslate()
```python

Se traduce hello world a alemán, español e italiano:
```python
>>> print gs.translate('hello world', 'de')
Hallo Welt
>>> print gs.translate('hello world', 'es')
Hola mundo
>>> print gs.translate('hello world', 'it')
Ciao mondo
```
En el sitio de `pypi` de la aplicación muestra otras funcionalidades de la aplicación como detectar el idioma, busquedas, entre otras.


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
