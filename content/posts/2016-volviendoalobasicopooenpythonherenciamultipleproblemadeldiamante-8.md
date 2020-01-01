Title: Volviendo a lo básico, POO en Python ( herencia multiple, problema del diamante) (parte 8)  
Date: 2016-12-31 17:00  
Category: Tutorial Python    
Tags: Python,POO
lang: es  
translation: true  

Continuando con los artículos sobre [programación orientada a objetos en python](https://www.seraph.to/tag/poo.html).

En el artículo anterior se explicó como trabajar con la herencia multiple. Ahora se  explicará el problema del diamante y como lo resuelve Python.

La herencia en diamante se muestra en la siguiente figura:

![](./images/volviendoalobasicopooenpythonherenciamultipleproblemadeldiamante8-1.png)


Donde la clase padre es la clase A, y la clase B y C heredan de ella, al final la clase D hereda tanto de B como de C y ambas clases como ya se saben heredan de A. ¿Por que vía se hereda de A, por B o por C?

Ese es en sí el problema del diamante; pueden encontrar más información en la página de [wikipedia](https://es.wikipedia.org/wiki/Problema_del_diamante). 

Cada lenguaje tiene una forma de resolver este problema, para el caso de Python, este crea una lista de clases, que se buscan de izquierda a derecha y de abajo a arriba (D,B,A,C,A), luego elimina todas las apariciones de una clase repetida menos la última. Por lo que el orden de resolución queda D,B,C,A. 

A continuación se muestra un ejemplo en python: 

```python

#!/usr/bin/env python3


# -*- coding: utf-8 -*-


"""multiple herencia, problema del diamante"""




class A(object):


    def __init__(self,mensajeA):


        self.mensajeA = mensajeA




    @staticmethod


    def quienSoy():


        return "Soy A"





class B(A):


    def __init__(self,mensajeA, mensajeB):


        A.__init__(self,mensajeA)


        self.mensajeB = mensajeB





    @staticmethod


    def quienSoy():


        return "Soy B"




class C(A):


    def __init__(self,mensajeA,mensajeC):


        A.__init__(self,mensajeA)


        self.mensajeC = mensajeC





    @staticmethod


    def quienSoy():


        return "Soy C"




class D(B,C):


    def __init__(self,mensajeA,mensajeB,mensajeC,mensajeD):


        B.__init__(self,mensajeA,mensajeB)


        C.__init__(self,mensajeA,mensajeC)


        self.mensajeD = mensajeD




    @staticmethod


    def quienSoy():


        return "Soy D"




if __name__ == '__main__':


    ca = A("prueba de A")


    cb = B("prueba de A desde B","prueba de B")


    cc = C("prueba de A desde C","prueba de C")


    cd = D("prueba de A desde D","prueba de B desde D","prueba de C desde D","prueba de D")


    print ("Mensaje de A:",ca.mensajeA)


    print ("Quien es?: ",ca.quienSoy())


    print ("Mensaje 1 de B:", cb.mensajeB)


    print("Mensaje 2 de B:", cb.mensajeA)


    print ("Quien es?:",cb.quienSoy())


    print ("Mensaje 1 de C:", cc.mensajeC)


    print ("Mensaje 2 de C:", cc.mensajeA)


    print ("Quien es?:", cc.quienSoy())


    print ("Mensaje 1 de D:", cd.mensajeD)


    print ("Mensaje 2 de D:", cd.mensajeB)


    print ("Mensaje 3 de D:", cd.mensajeC)


    print ("Mensaje 4 de D:", cd.mensajeA)


    print("Quien es?:", cd.quienSoy())

```


Noten que no se usó super, ya que para poder resolver la evaluación se hace más fácil definiendo el objeto directamente en vez de usar super una llamada de la herencia. 


Al ejecutar el código se tiene la siguiente salida:
```
Mensaje de A: prueba de A
Quien es?:  Soy A
Mensaje 1 de B: prueba de B
Mensaje 2 de B: prueba de A desde B
Quien es?: Soy B
Mensaje 1 de C: prueba de C
Mensaje 2 de C: prueba de A desde C
Quien es?: Soy C
Mensaje 1 de D: prueba de D
Mensaje 2 de D: prueba de B desde D
Mensaje 3 de D: prueba de C desde D
Mensaje 4 de D: prueba de A desde D
Quien es?: Soy D
``` 

Como pueden notar la ejecución de la última clase muestra la secuencia explicada en este artículo.

El código de este ejemplo lo pueden descargar desde [gitlab](https://gitlab.com/ecrespo/tutorial-poo/blob/master/ej18.py). 



##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)



