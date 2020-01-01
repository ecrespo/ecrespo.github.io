Title: Volviendo a lo básico, POO en Python ( composición) (parte 9)  
Date: 2016-12-31 18:00  
Category: Tutorial Python  
Tags: Python,POO
lang: es  
translation: true  


Para terminar la serie de artículos sobre [programación orientada a objetos con python](https://www.seraph.to/tag/poo.html), 

La composición significa utilizar objetos dentro de otro objetos sin usar herencia.

A continuación se muestra el diagrama UML de dos objetos A y B. 

![](./images/volviendoalobasicopooenpythoncomposicion9-1.png)

A continuación se muestra el código de ejemplo: 

```python
#!/usr/bin/env python3


# -*- coding: utf-8 -*-


"""Composición"""


class A(object):


    def a1(self):


        print("a1")


class B(object):


    def b(self):


        print ("b")


        A().a1()


if __name__ =="__main__":


    objetoB = B()


    objetoB.b()

```

Al ejecutar el código se tiene la siguiente salida:
```
b
a1
```

Este ejemplo es algo sencillo. La composición es otra forma de reutilizar código.

El código lo pueden ver en [gitlab](https://gitlab.com/ecrespo/tutorial-poo/blob/master/ej16.py). 



##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)




