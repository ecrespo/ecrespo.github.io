Title: Resolución de sistemas de ecuaciones con Sympy  
Date: 2015-02-21 11:00  
Category: Tutorial Python  
Tags: Canaima,Debian,General,Python,Ubuntu,Sympy
lang: es  
translation: true  

Hasta ahora se tienen los siguientes artículos sobre el uso de la librería `Sympy`:
- [Cálculo de límites con la librería Sympy](https://www.seraph.to/calculo-de-limites-con-la-libreria-sympy.html#calculo-de-limites-con-la-libreria-sympy)
- [Cálculo de derivadas con la librería Sympy](https://www.seraph.to/calculo-de-derivadas-con-sympy.html#calculo-de-derivadas-con-sympy)
- [Cálculo de integrales con la librería Sympy](https://www.seraph.to/calculo-de-integrales-con-sympy.html#calculo-de-integrales-con-sympy)

En este caso se explicará el uso de la librería `Sympy` en la resolución de sistemas de ecuaciones, se utilizará el ejemplo de un artículo anterior ([Resolución de sistemas de ecuaciones lineales por descomposición QR usando Numpy](https://www.seraph.to/resolucion-de-sistemas-de-ecuaciones-lineales-por-descomposion-qr-usando-numpy.html)).

Se inicia ipython notebook (si desean usar el archivo lo pueden bajar del siguiente [enlace](https://bitbucket.org/ecrespo/ernesto-ecrespo.blogspot/src/d1791a6a85834e57c86721f892a3ad22dce6644f/sistecuaciones/sisteecuaciones.ipynb?at=default)):

A continuación se muestra el código del script:

```python
#!/usr/bin/env python


#Se importa sympy


from sympy import *


#Se define las variables simbolicas x,y,z


x = Symbol('x')


y = Symbol('y')


z= Symbol('z')


#Resolver el sistema de ecuaciones


#3x+9y-10z  =   24


#x-6y+4z      =   -4


#10x-2y+8z  =  20


resultado =solve([3*x+9*y-10*z-24,x-6*y+4*z+4,10*x-2*y+8*z-20],[x,y,z])


print resultado
```

Al ejecutar el script se obtiene lo siguiente:
```
{x: 308/103, z: -117/103, y: 42/103}
```

Se nota que el resultado obtenido es el mismo del artículo ya [mencionado](https://www.seraph.to/resolucion-de-sistemas-de-ecuaciones-lineales-por-descomposion-qr-usando-numpy.html).


La imagen de la utilización de notebook se muestra a continuación:

![](./images/resoluciondesistemasdeecuacionesconsympy-1.png)

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
