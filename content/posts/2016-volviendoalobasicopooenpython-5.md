Title: Volviendo a lo básico, POO en Python (parte 5)  
Date: 2016-12-19 09:00  
Category: Tutorial Python    
Tags: Python,POO
lang: es  
translation: true


Continuando con los artículos sobre Programación Orientada a Objetos en Python, en este caso se usará lo que se vió en la [parte 4 de la serie](https://www.seraph.to/volviendo-a-lo-basico-poo-en-python-parte-4.html), donde se creó una clase `Punto2D` y se creó una clase hija `Punto3D` que heredaba de la `Punto2D`.

En este caso se incorporarán nuevos conceptos:  
- meta clases (clase abstracta)
- método abstracto:   

Con la clase abstracta se define una clase con sus métodos abstractos que no hacen nada, sólo declaran las clases, luego se hereda dicha clase y se van implementando los métodos que se definieron abstractos. 

En este caso se crea la clase abstracta `ADTPunto` que define una serie de métodos, luego se crea la clase punto que hereda de `ADTPunto`, aquí se implementan los métodos que se definieron en la clase abstracta, la clase abstracta termina siendo como una interfaz de una clase. 

A continuación se muestra el código de la clase abstracta `punto`: 

```python

from abc import ABCMeta, abstractmethod


class ADTPunto (object):


    __metaclass__ = ABCMeta



    @abstractmethod


    def ValorX(self):


        pass



    @abstractmethod


    def ValorY(self):


        pass



    @abstractmethod


    def mover(self,puntoNuevo):


        pass



    @abstractmethod


    def reset(self):


        pass



    @abstractmethod


    def distanciaOtroPunto(self,punto):


        pass

```

A continuación se muestra la clase `Punto` que hereda de `ADTPunto`:
 
```python

from math import sqrt



class Punto(ADTPunto):


    def __init__(self,x,y):


        self.__x = x


        self.__y = y


        super(Punto,self).__init__()





    @property


    def punto(self):


        """el getter de punto, devuelve el punto"""


        return (self.__x,self.__y)





    @punto.setter


    def punto(self,Punto):


        """Asigna nuevo valor al punto"""


        self.__x = Punto.punto[0]


        self.__y = Punto.punto[1]





    @punto.deleter


    def punto(self):


        """Borra los valores del punto"""


        del self.__x


        del self.__y




    @property


    def ValorX(self):


        """Devuelve el valor de x"""


        return self.__x





    @property


    def ValorY(self):


        """Devuelve el valor de y"""


        return self.__y





    def reset(self):


        """Fija el punto en (0,0)"""


        self.__x = 0


        self.__y = 0





    def distanciaOtroPunto(self,oPunto):


        '''devuelve la distancia entre el punto original y un punto dado'''


        return sqrt((self.__x - oPunto.punto[0])**2 + (self.__y - oPunto.punto[1])**2 )





    def mover(self,oPunto):


        """Cambia el punto a un nuevo punto"""


        self.__x = oPunto.punto[0]


        self.__y = oPunto.punto[1]


```




Para finalizar se muestra la instanciación de ambas clases:


```python


if __name__ == "__main__":


    try:


        prueba = ADTPunto()


    except (TypeError):


        print ("No puede instanciar una clase abstracta")



    punto2d = Punto(3,5)


    print(punto2d.punto)


    print(punto2d.ValorX)


    print(punto2d.ValorY)


    punto2d.mover(Punto(5,5))


    print(punto2d.punto)


    print(punto2d.distanciaOtroPunto(Punto(10,10)))


    punto2d.reset()


    print(punto2d.punto)
```



Al ejecutar el script se tiene lo siguiente:
```
python ej12_adt.py 
No puede instanciar una clase abstracta
(3, 5)
3
5
(5, 5)
7.07106781187
(0, 0)
```

Como se puede ver, se intentó instanciar la clase `ADTPunto`, lo cual genera un error de tipo.

El código completo de las clases se encuentran en [gitlab en el repo tutorial-poo](https://gitlab.com/ecrespo/tutorial-poo/blob/master/ej12_adt.py).


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)




