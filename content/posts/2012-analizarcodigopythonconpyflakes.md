Title: Analizar código Python con Pyflakes
Date: 2012-12-10 9:00
Category: Tutorial Python
Tags: General,Linux,Python,Pyflakes
lang: es
translation: true

Pyflakes es una herramienta de análisis de código Python.

Pyflakes puede detectar potenciales problemas como:

Módulos importados sin usar.
Variables sin usar.

Para instalarlo se puede bajar desde [PyPI](https://pypi.org/project/pyflakes/) ó desde el sitio de [Launchpad](https://launchpad.net/pyflakes); también se puede instalar con easy_install ó pip y para las distribuciones basadas en Debian se instala vía `apt-get` o `aptitude`.
```
easy_install pyflakes
```

```
pip install pyflakes
```

```
apt-get install pyflakes
```

Para probar el uso de `pyflakes` se usará el código del tutorial de debugging, se agregará la importación de string y una instrucción if donde se compara el valor de i con una variable llamada plataforma.

A continuación el código:
```python
#!/usr/bin/env python

# -*- coding: utf-8 -*-



#Se importa numpy como np

import numpy as np



from pudb import set_trace; set_trace()

import string



a = np.arange(10)

print a

print a[8]

print a[9]



for i in a:

    if i == plataforma:

        print i
```
Este script se salvará con el nombre de `arreglo.py`.

Ahora se ejecutará `pyflakes`:
```python
pyflakes arreglo.py 

arreglo.py:8: 'string' imported but unused

arreglo.py:18: undefined name 'plataforma'
```

La ejecución devuelve la línea donde hay definiciones sin usar (import string) y una variable sin definir (plataforma).

Al eliminar la importación de la línea 8 y areglar la definición de la variable plataforma o cambiar dicha parte del código se eliminará los mensajes que devuelve pyflakes. Esto permite prevenir errores en el código.

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)