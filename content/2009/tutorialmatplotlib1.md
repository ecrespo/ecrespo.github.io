Title: Tutoriales de matplotlib con python. Parte 1
Date: 2009-06-16 08:00
Category: Tutorial Python
Tags: Linux,Python,Matplotlib
lang: es
translation: true

Luego de un tiempo dedicado a otros asuntos y debido a mi reposo voy a empezar una
serie de tutoriales cortos sobre matplotlib.

Lo primero que se necesita tener es matplotlib instalado:
Como root:

```
aptitude install python-matplotlib python-matplotlib-data python-matplotlib-doc
```

Luego desde la línea de comandos se ejecuta python
```
ernesto@zvezda:~/bin$ python2.5
Python 2.5.4 (r254:67916, Feb 17 2009, 20:16:45)
[GCC 4.3.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.

>>> import matplotlib.pyplot as plt
>>> plt.plot([1,2,3],[5,7,9])
[]
>>> plt.ylabel('Eje Y')

>>> plt.xlabel('Eje X')
>>> plt.show()
```

El primer comando importa la librería matplotlib, luego se le pasan los puntos
a graficar, los del eje X y del eje Y; luego se colocan etiquetas a los ejes
cartesianos y se presenta la gráfica.


===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./imagenes/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
