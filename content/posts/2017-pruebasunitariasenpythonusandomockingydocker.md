Title: Pruebas unitarias en Python usando mocking y docker
Date: 2017-03-11 09:00
Category: Tutorial Python
Tags: Numpy,Python,Mocking,Docker,Pruebas unitarias
lang: es
translation: true

Hace un tiempo escribí un artículo de [pruebas unitarias con python usando Docker](https://www.seraph.to/pruebas-unitarias-con-unitest-en-python-usando-nosetests-y-dockerdocker-compose.html).  En ese artículo se muestras las distintas opciones de métodos para hacer pruebas unitarias, este caso se enfoca en hacer un mocking de datos (simulación de datos).

Este artículo se basa en el artículo del sitio [semaphoreci](http://semaphoreci.com/), el artículo se llama [Getting Started with Mocking in Python](http://semaphoreci.com/community/tutorials/getting-started-with-mocking-in-python).

A continuación dejo el código inicial del `Dockerfile`, de la `calculadora.py` y de la prueba:

Archivo `Dockerfile`:

```python
FROM python
WORKDIR /code/

RUN pip3 install --upgrade pip
RUN pip3 install nose
RUN pip3 install nose-cov
RUN pip3 install rednose
RUN pip3 install pytest
RUN pip3 install pytest-cov
RUN pip3 install mock


#EXPOSE 5000

ADD . /code/
COPY . /code/


#CMD nosetests  --with-coverage
#CMD nosetests -sv --rednose
CMD python -m unittest

```

Archivo `docker-compose.yml`:
```python
pruebas:
  build: .

  volumes:
    - ".:/code"
```

Archivo `calculadora.py`:
```python
#!/usr/bin/env python
#Se importa sqrt de math
from math import sqrt


#Clase calculadora
class Calculadora:
    #Metodo suma de x y y, se evalua si son enteros si no, devuelve error.
    def suma(self,x,y):
        if type(x) == int and type(y) == int:
            return x + y
        else:
            raise TypeError("Invalid type: {} and {}".format(type(x),type(y)))
```
Archivo `calculadora_test.py`:
```python
#!/usr/bin/env python3

from unittest import TestCase
from app.calculadora import Calculadora





class TestCalculadora(TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_suma_retorna_resultado_correcto(self):
        ##Asegura que sea igual la operacion de suma 2+2 a 4
        respuesta = self.calc.suma(2,4)
        self.assertEqual(respuesta, 6)

```

Al ejecutar `docker-compose up` se tiene:
```python
docker-compose up 
Starting tutorialespruebas_pruebas_1
Attaching to tutorialespruebas_pruebas_1
pruebas_1 | .
pruebas_1 | Name                 Stmts   Miss  Cover
pruebas_1 | ----------------------------------------
pruebas_1 | app.py                   0      0   100%
pruebas_1 | app/calculadora.py       6      0   100%
pruebas_1 | unit.py                  0      0   100%
pruebas_1 | ----------------------------------------
pruebas_1 | TOTAL                    6      0   100%
pruebas_1 | ----------------------------------------------------------------------
pruebas_1 | Ran 1 test in 0.022s
pruebas_1 | 
pruebas_1 | OK
tutorialespruebas_pruebas_1 exited with code 0
```
Ahora se hará un cambio. En vez de llamar a suma a partir de la calculadora se hará una simulación del resultado usando `mocking`. Para ello el único cambio que se hará es el de `calculadora_test.py`.

A continuación el código del archivo:
```python
#!/usr/bin/env python3

from unittest import TestCase
from app.calculadora import Calculadora
from unittest.mock import patch



class TestCalculadora(TestCase):
    

    @patch('app.calculadora.Calculadora.suma', return_value=9)
    def test_suma_retorna_resultado_correcto(self,suma):
        self.assertEqual(suma(2,3), 9)
```

Se importa `patch` a partir de `mock`, y se llama al decorador `patch`  pasando como argumento el método suma de calculadora, donde se le define que va a devolver el valor de 9 sin importar los argumentos de entrada de dicho método.  Luego se ejecuta el método `test_suma_retorna_resultado_correcto` donde se le pasa suma y se asegura que la suma de 2 y 3 da 9. 

Al ejecutar `docker-compose up` se tiene el siguiente resultado:
```python
docker-compose up 
Starting tutorialespruebas_pruebas_1
Attaching to tutorialespruebas_pruebas_1
pruebas_1 | .
pruebas_1 | Name                 Stmts   Miss  Cover
pruebas_1 | ----------------------------------------
pruebas_1 | app.py                   0      0   100%
pruebas_1 | app/calculadora.py       7      0   100%
pruebas_1 | unit.py                  0      0   100%
pruebas_1 | unittest/mock.py      1278   1278     0%
pruebas_1 | ----------------------------------------
pruebas_1 | TOTAL                 1285   1278     1%
pruebas_1 | ----------------------------------------------------------------------
pruebas_1 | Ran 1 test in 0.100s
pruebas_1 | 
pruebas_1 | OK
```

Como se muestra, la prueba pasa sin probemas, la razón es que se está pasando vía mocking el valor que tiene que devolver la suma sin importar la entrada de datos del método a ejecutar.

El código de los distintos archivos se pueden ver en el [repositorio de gitlab en la rama mocking](http://gitlab.com/ecrespo/tutoriales-pruebas/tree/mocking).

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
