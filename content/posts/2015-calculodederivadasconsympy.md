Title:Cálculo de derivadas con sympy
Date: 2015-02-21 09:00  
Category: Tutorial Python  
Tags: Canaima,Debian,General,Python,Ubuntu  
lang: es  
translation: true  


En el [artículo anterior](https://www.seraph.to/calculo-de-limites-con-la-libreria-sympy.html#calculo-de-limites-con-la-libreria-sympy) se explicó como calcular límites de funciones, en este artículo se muestra como calcular la derivada.


Se inicia notebook (si desea abrir el archivo que se utilizo para este artículo lo puede encontrar en el siguiente [enlace](https://bitbucket.org/ecrespo/ernesto-ecrespo.blogspot/src/286db40e8218d4d39863751a4bc850672bd93592/derivadas/derivadas.ipynb?at=default)):
```python
$ipython notebook
```
Puede crear un notebook (o abrir el notebook mencionado en el enlace anterior).

A continuación se muestra el script del calculo de derivadas de 3 funciones diferentes:
```python
#!/usr/bin/env python

# coding: utf-8


#Se importa sympy

from sympy import *


x = Symbol('x')



#Se calcula la derivada de la funcion cos(sin(x^3)) con respecto a x

print diff(cos(sin(x**3)),x)



#Se calcula la derivada de la funcion 5(x^5)+3(x^3)-6x+5

print diff(5*(x**5)+3*(x**3)-6*x+5,x)



#Calcula la derivada ene-sima de x^2+8x-4+sin(2x)

print diff(x**2+8*x-4+sin(2*x),x,2)

```

Al ejecutar el script se muestra el resultado de la ejecución de los 3 instrucciones print:
```
-3*x**2*sin(sin(x**3))*cos(x**3)
25*x**4 + 9*x**2 - 6
2*(-2*sin(2*x) + 1)
x,2)
```
Al ejecutar el script se muestra el resultado de la ejecución de los 3 instrucciones print:
```
-3*x**2*sin(sin(x**3))*cos(x**3)
25*x**4 + 9*x**2 - 6
2*(-2*sin(2*x) + 1)
```

A continuación se muestra una imagen del notebook resultante:

![](./images/calculodederivadasconsympy-1.png)


A continuación se muestra una imagen del notebook resultante:

![](./images/calculodederivadasconsympy-2.png)


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
