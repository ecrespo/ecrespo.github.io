Title: Volviendo a lo básico, POO en Python (parte 6)
Date: 2016-12-31 15:00
Category: Tutorial Python
Tags: Python,POO
lang: es  
translation: true

Continuando con la serie de artículos sobre [Programación Orientada a Objetos en Python](https://www.seraph.to/tag/poo.html).

En este artículo se explica el uso del decorador `classmethod` el cual se le pasa como argumentos la clase. 

Se tiene una clase abstracta que se llama figura, en ella  se tiene los siguientes decoradores:

- `abstractmethod`: Métodos abstractos que no contienen nada, sólo la descripción de los métodos, estos métodos son: area, perimetro y quienEresTu.  
- `abstractproperty`: Propiedad abstracta, en este caso se define el método color.   
- `property`: El método color devuelve el color como propiedad.  
- `@color.setter`: Define un nuevo color.   
- `classmethod`: Se define __subclasshook__ como un classmethod, quien permite personalizar el comportamiento de Issubclass sin necesidad de registrar subclase de la clase abstracta (este método debe devolver True, False o NotImplemented).  

Luego se crea la clase Rectangulo que hereda de la clase abstracta Figura, luego se crea la clase Cuadrado que hereda de la clase Rectangulo.


A continuación se muestra el código de la clase Figura:

```python
#Se importa sqrt de math



from math import sqrt



#Se importa ABCMeta, abstractmethod, abstractproperty



from abc import ABCMeta, abstractmethod,abstractproperty



#Interface



class Figura(object):



    __metaclass__ = ABCMeta




    @abstractmethod



    def area(self):



        """Calcula el area"""



        pass




    @abstractmethod



    def perimetro(self):



        """Calcula el perimetro"""



        pass




    @abstractmethod



    def quienEresTu(self):




        """Devuelve el mensaje de quien es el objeto"""



        print (u"Soy una forma y un método abstracto ")




    @abstractproperty



    def color(self):



        pass




    @property



    def color(self):



        pass




    @color.setter



    def color(self,valor):



        pass




    @classmethod



    def __subclasshook__(cls, C):



        return NotImplemented

```



Se muestra el código de la clase Rectangulo:


```python

class Rectangulo(Figura):

    def __init__(self,ancho, alto):

        """Define los atributos de rectangulo"""

        self.ancho, self.alto = ancho, alto

        super(Rectangulo,self).__init__()

        self.__color = "rojo"



    def area(self):

        """Devuelve el area"""

        return self.ancho*self.alto



    def perimetro(self):

        """devuelve el perimetro"""

        return 2*self.ancho+2*self.alto



    @property

    def color(self):

        """Devuelve el atributo color"""

        return self.__color



    @color.setter

    def color(self,valor):

        """Define el color del rectangulo"""

        self.__color = valor



    def quienEresTu(self):

        """devuelve que es el objeto"""

        print (u"Soy un Rectangulo")
```

A continuación se muestra el código de la clase Cuadrado:
```python
class Cuadrado(Rectangulo):

    def __init__(self,largo):
        """Define el largo del cuadrado y se lo pasa a la clase rectangulo"""
        self.largo = largo
        super(Cuadrado,self).__init__(largo,largo)

    def area(self):
        """DEvuelve el area del cuadrado"""
        return self.largo*self.largo
```

Para terminar se muestra la implementación de las clases:
 
```python


if __name__ == '__main__':


    r = Rectangulo(5,6)


    print ("Es una subclase rectangulo de shape?:",issubclass(Rectangulo,Figura))


    print ("Es una subclase cuadrado de shape?:",issubclass(Cuadrado,Figura))


    print ("Es una subclase cuadrado de rectangulo?:",issubclass(Cuadrado,Rectangulo))


    print ("Es una subclase rectangulo de cuadrado?:",issubclass(Rectangulo,Cuadrado))


    print ("r es una instancia de rectangulo?:",isinstance(r,Rectangulo))


    print ("r es una instancia de cuadrado?:",isinstance(r,Cuadrado))


    print ("Area del rectangulo:",r.area())


    print("Color del rectangulo:",r.color)


    r.color = "Black"


    print("Color del rectangulo:",r.color)


    print ("Perimetro del rectangulo",r.perimetro())


    r.quienEresTu()


    sq = Cuadrado(5)


    print ("Area del cuadrado:",sq.area())


    print ("Perimetro del cuadrado:",sq.perimetro())

```



Al ejecutar el código se tiene el siguiente resultado:

```
Es una subclase rectangulo de shape?: True
Es una subclase cuadrado de shape?: True
Es una subclase cuadrado de rectangulo?: True
Es una subclase rectangulo de cuadrado?: False
r es una instancia de rectangulo?: True
r es una instancia de cuadrado?: False
Area del rectangulo: 30
Color del rectangulo: rojo
Color del rectangulo: Black
Perimetro del rectangulo 22
Soy un Rectangulo
Area del cuadrado: 25
Perimetro del cuadrado: 20

```
El código completo de las clases lo pueden encontrar en gitlab en el siguiente [enlace](https://gitlab.com/ecrespo/tutorial-poo/blob/master/ej13.py).



##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)




