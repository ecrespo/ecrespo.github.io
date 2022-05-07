Title: Pruebas unitarias con unitest en Python usando nosetests y Docker/docker-compose
Date: 2016-10-05 09:00
Category: Tutorial Python
Tags: Docker,Docker-compose,nosetests,Prueba de cobertura,Pruebas unitarias,unittest
lang: es
translation: true

Ya se han tocado en el blog el tema de pruebas unitarias, y usando Docker, los artículos anteriores lo pueden encontrar en la etiqueta [unittest](https://www.seraph.to/tag/unittest.html).

En este artículo se mostrará una clase calculadora que hace una suma y raíz cuadrada, y se tiene la clase para las pruebas unitarias. 

#### Estructura de archivos y directorios

La estructura de archivos y directorios del directorio de trabajo del repositorio es la siguiente:
```
tutoriales-pruebas
├── app
│   ├── calculadora.py
│   └── __init__.py
├── docker-compose.yml
├── Dockerfile
└── test
    └── unit
        ├── calculadora_test.py
        └── __init__.py
```

Archivo `Dockerfile` y `docker-compose.yml`

En el archivo Dockerfile se define como sistema base python, se pasa las dependencias  para usar nosetests y cobertura. 

A continuación el código del archivo Dockerfile:

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





ADD . /code/


COPY . /code/





CMD nosetests  --with-coverage

#CMD nosetests -sv --rednose 


```


Toca comentar y descomentar las dos líneas de CMD si se requiere usar cobertura o no.



El archivo `docker-compose.yml` contiene lo siguiente:

```
pruebas:

  build: .



  volumes:

    - ".:/code"
```


Se define el microservicio pruebas que usará el archivo Dockerfile, y se define el volumen.

#### Módulo cálculadora

Este módulo tiene la clase calculadora con los métodos suma y raíz cuadrada, el código se muestra a continuación: 

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





    #Metodo raizcuadrada de X, devuelve la raiz cuadrada si es entero positivo, si no


    #devuelve mensaje de error.


    def raizCuadrada(self,x):


        if type(x) == int and x >= 0:


            return math.sqrt(x)


        else:


            raise TypeError("Invalid type: {} ".format(type(x)))



if __name__ == '__main__':


    #Se crea una instancia de la clase


    calc = Calculadora()


    #Se calcula la suma de 2 y 2, se muestra en pantalla.


    results = calc.sum(2, 2)


    print (results)

```

#### Módulo de las pruebas

El archivo `calculadora_tests.py` contiene las pruebas para la suma y para la raíz cuadrada, adicional muestra una serie de métodos de otras pruebas que existen en unittest (que no tiene que ver con las pruebas de calculadora, sólo con fines ilustrativos del uso de unittest).


A continuación se muestra el código:

```python
#!/usr/bin/env python3


import unittest


from app.calculadora import Calculadora




class TestCalculadora(unittest.TestCase):


    def setUp(self):


        self.calc = Calculadora()



    def test_suma_retorna_resultado_correcto(self):


        ##Asegura que sea igual la operacion de suma 2+2 a 4


        self.assertEqual(4, self.calc.suma(2,2))



    def test_suma_devuelve_error_si_el_tipo_no_es_entero(self):


        #Asegura error, si es de tipo, cuando se le pasa dos string.


        self.assertRaises(TypeError, self.calc.suma, "Hello", "World")



    def test_asegura_que_sea_verdadero(self):


        #Se asegura que el valor 1 es true y un string.


        self.assertTrue(1)


        self.assertTrue("Hello, World")



    def test_aseura_que_sea_falso(self):


        #Se asegura que el string vacio y cero son falso.


        self.assertFalse(0)


        self.assertFalse("")




    def test_asegura_que_es_mayor(self):


        #Se asegura que 2>1


        self.assertGreater(2, 1)



    def test_asegura_que_es_mayor_e_igual(self):


        #Se asegura que 2>=2


        self.assertGreaterEqual(2, 2)



    def test_asegura_que_es_casi_igual_a_delta_0_5(self):


        #Se asegura que sea casi igual 1 y 1.2 con delta de 0.5


        self.assertAlmostEqual(1, 1.2, delta=0.5)



    def test_asegura_lugares_casi_igual(self):


        #Se asegura que es casi igual 1 y 1.00001 por 4 lugares.


        self.assertAlmostEqual(1, 1.00001, places=4)




    def test_asegura_diccionario_contiene_subconjunto(self):


        esperado = {'a': 'b'}


        actual = {'a': 'b', 'c': 'd', 'e': 'f'}


        #Se asegura que el diccionario actual contiene lo esperado.


        self.assertDictContainsSubset(esperado, actual)



    def test_asegura_diccionarios_iguales(self):


        esperado = {'a': 'b', 'c': 'd'}


        actual = {'c': 'd', 'a': 'b'}


        #Se asegra que el diccionario esperado sea igual al actual.


        self.assertDictEqual(esperado, actual)



    def test_asegura_que_esta_en(self):


        #Se asegura que 1 este en la lista


        self.assertIn(1, [1,2,3,4,5])



    def test_asegura_expresiones_iguales(self):


        #Se asegura que las expresiones son iguales expre1 y expre2


        self.assertIs("a", "a")



    def test_asegura_objeto_es_instancia_de_una_clase(self):


        #Se asegura que el objeto 2 sea de la clase entero


        self.assertIsInstance(2, int)



    def test_asegura_objeto_no_es_instancia_de_una_clase(self):


        #Se asegura que el objeto 2 no sea una clase str


        self.assertNotIsInstance(2, str)



    def test_asegura_que_es_none(self):


        #Se asegura que es None.


        self.assertIsNone(None)



    def test_asegura_expresiones_no_sean_iguales(self):


        self.assertIsNot([], [])



    def test_asegura_que_no_sea_none(self):


        #Se asegura que 1 no es None.


        self.assertIsNotNone(1)



    def test_asegura_que_es_menor(self):


        #Se asegura que 3 es menor que 5


        self.assertLess(3, 5)



    def test_asegura_que_es_menor_e_igual(self):


        #Se asegura que 7 es menor o igual que 7.


        self.assertLessEqual(7, 7)




if __name__ =




= '__main__':



  unittest.main()
```

### Ejecución de las pruebas

#### Ejecución de pruebas unitarias

Para ejecutar las pruebas se deja descomentada la línea en el archivo Dockerfile que dice:
```
#CMD nosetests  --with-coverage
CMD nosetests -sv --rednose
```

Se construye la imagen:
```
docker-compose build
``` 
Se ejecuta el contenedor:
```
docker-compose up
```

El resultado de la ejecución se muestra a continuación:
``` 
Recreating tutorialespruebas_pruebas_1
Attaching to tutorialespruebas_pruebas_1
pruebas_1 | test_asegura_diccionario_contiene_subconjunto (unit.calculadora_test.TestCalculadora) ... passed
pruebas_1 | test_asegura_diccionarios_iguales (unit.calculadora_test.TestCalculadora) ... passed
pruebas_1 | test_asegura_expresiones_iguales (unit.calculadora_test.TestCalculadora) ... passed
pruebas_1 | test_asegura_expresiones_no_sean_iguales (unit.calculadora_test.TestCalculadora) ... passed
pruebas_1 | test_asegura_lugares_casi_igual (unit.calculadora_test.TestCalculadora) ... passed
pruebas_1 | test_asegura_objeto_es_instancia_de_una_clase (unit.calculadora_test.TestCalculadora) ... passed
pruebas_1 | test_asegura_objeto_no_es_instancia_de_una_clase (unit.calculadora_test.TestCalculadora) ... passed
pruebas_1 | test_asegura_que_es_casi_igual_a_delta_0_5 (unit.calculadora_test.TestCalculadora) ... passed
pruebas_1 | test_asegura_que_es_mayor (unit.calculadora_test.TestCalculadora) ... passed
pruebas_1 | test_asegura_que_es_mayor_e_igual (unit.calculadora_test.TestCalculadora) ... passed
pruebas_1 | test_asegura_que_es_menor (unit.calculadora_test.TestCalculadora) ... passed
pruebas_1 | test_asegura_que_es_menor_e_igual (unit.calculadora_test.TestCalculadora) ... passed
pruebas_1 | test_asegura_que_es_none (unit.calculadora_test.TestCalculadora) ... passed
pruebas_1 | test_asegura_que_esta_en (unit.calculadora_test.TestCalculadora) ... passed
pruebas_1 | test_asegura_que_no_sea_none (unit.calculadora_test.TestCalculadora) ... passed
pruebas_1 | test_asegura_que_sea_verdadero (unit.calculadora_test.TestCalculadora) ... passed
pruebas_1 | test_aseura_que_sea_falso (unit.calculadora_test.TestCalculadora) ... passed
pruebas_1 | test_suma_devuelve_error_si_el_tipo_no_es_entero (unit.calculadora_test.TestCalculadora) ... passed
pruebas_1 | test_suma_retorna_resultado_correcto (unit.calculadora_test.TestCalculadora) ... passed
pruebas_1 | 
pruebas_1 | -----------------------------------------------------------------------------
pruebas_1 | 19 tests run in 0.072 seconds (19 tests passed)
tutorialespruebas_pruebas_1 exited with code 0
```
Se ejecutaron 19 pruebas y todas pasaron, la ejecución se tardó 0.072 segundos.

Ejecución de pruebas de cobertura
La cobertura de código permite medir la calidad de las pruebas ( más información en wikipedia).

Para ejecutar la prueba es necesario modificar el archivo Dockerfile para que se use la cobertura:
```
CMD nosetests  --with-coverage
#CMD nosetests -sv --rednose
```

Se construye la imagen Docker:
```
docker-compose build 
```
Se ejecuta el contendor de la prueba:
```
docker-compose up
```
El resultado se muestra a continuación:

```
Recreating tutorialespruebas_pruebas_1
Attaching to tutorialespruebas_pruebas_1
pruebas_1 | ...................
pruebas_1 | Name                 Stmts   Miss  Cover
pruebas_1 | ----------------------------------------
pruebas_1 | app.py                   0      0   100%
pruebas_1 | app/calculadora.py      14      6    57%
pruebas_1 | unit.py                  0      0   100%
pruebas_1 | ----------------------------------------
pruebas_1 | TOTAL                   14      6    57%
pruebas_1 | ----------------------------------------------------------------------
pruebas_1 | Ran 19 tests in 0.019s
pruebas_1 | 
pruebas_1 | OK
tutorialespruebas_pruebas_1 exited with code 0
```


Como se ve el módulo calculadora cubre un 57% de cobertura.

El código de este proyecto se encuentra en el [repo tutoriales de pruebas en la rama nosetests](gitlab.com/ecrespo/tutoriales-pruebas/tree/nosetests). 


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)


![](./images/.png)
