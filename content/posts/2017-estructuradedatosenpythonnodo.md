Title: Estructura de datos en Python (Nodo)
Date: 2017-03-07 09:00
Category: Tutorial Python
Tags: Python,Estructura de datos
lang: es
translation: true

Recuerdo en la Universidad de Carabobo como nos enseñaron en Computación Dígital II (metodología de la programación) estructuras de Datos y ADT (estructuras de datos abstractas). Entre ellas:

- Lista enlazada
- Lista doblemente enlazada
- Lista circular
- etc.

El curso fue dado con Turbo Pascal 6.0, Modula 3, Oberon y Component Pascal.

En este caso se hará la estructura de datos base llamada nodo, en el siguiente artículo se usará el nodo para construir una lista enlazada.

Un Nodo tiene los siguientes atributos y métodos:

- Atributos:
    - dato: dato.
    - prox: próximo nodo.
- Métodos:
    - getter dato: Devuelve el dato.
    - setter dato: Asigna el valor de dato.
    - getter proximo: Devuelve el valor de proximo.
    - setter proximo: Devuelve el valor de proximo.

Para probar la estructura de datos nodo (objeto nodo) se crean 3 instancias con los datos (manzana, pera y uva) y que apunte al siguiente nodo, el primer nodo apunta a `None`.

A continuación el código del módulo `nodos.py` que contiene la clase `Nodo`:

```python
#!/usr/bin/env python3



class Nodo(object) :

    """Objeto Nodo"""

    def __init__( self, dato,prox=None ) :

        """Construye el objeto nodo con los atributos 

        datos, prox, prev"""

        self.__dato = dato

        self.__prox = prox

    

    def __str__(self):

        return 'Nodo ['+str(self.__dato)+']'



    @property

    def dato(self):

        return self.__dato

    

    @dato.setter

    def dato(self,dato):

        self.__dato = dato



    @property

    def proximo(self):

        return self.__prox



    @proximo.setter

    def proximo(self,prox):

        self.__prox = prox 





if __name__ == '__main__':

    nodo1 = Nodo("manzana")

    nodo2 = Nodo("pera",nodo1)

    nodo3 = Nodo("uva",nodo2)

    print (nodo1.dato,nodo1.proximo)

    print (nodo2.dato,nodo2.proximo)

    print (nodo3.dato,nodo3.proximo)
    print (nodo1)
    print (nodo2)
    print (nodo3)
    
```

Al ejecutar el script se tiene lo siguiente:
```python
('manzana', None)
('pera', <__main__.Nodo object at 0x7f174f358290>)
('uva', <__main__.Nodo object at 0x7f174f3582d0>)
Nodo [manzana]
Nodo [pera]

Nodo [uva]
```
Para el siguiente artículo se explicará la herencia de la clase Nodo con la clase listaenlazada.

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
