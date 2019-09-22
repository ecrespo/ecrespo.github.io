Title: Gráfica de presión de vapor con numpy y matplotlib
Date: 2015-01-11 13:00
Category: Tutorial Python 
Tags: Debian,General,matplotlib,numpy,Python,Ubuntu
lang: es
translation: true


Retomando los [artículos de numpy y matplotlib](https://www.seraph.to/tag/matplotlib.html), en este caso se mostrará una gráfica del cálculo del vapor de agua entre -100 a 100 grados centigrados.

La ecuación de vapor es la siguiente:

![](./images/graficadepresiondevaporconnumpyymatplotlib-1.png)

Donde es está en pascal, T en grados centigrados.

A continuación se muestra el código para generar la gráfica:
```python
#!/usr/bin/env python3


# -*- coding: utf-8 -*-


#Se importa numpy como np


import numpy as np


#Se importa xlabel, ylabel, plot y show de pylab


from pylab import xlabel,ylabel, plot, show


#Se define el rango de la temperatura, de -100 a 100 con


#incrementos de 50.


T = np.linspace(-100,100,50)


#Se realiza el cálculo de la presión pasandole el arreglo de valores de


#la temperatura


es = 611*np.exp(17.27*T/(237.3+T))


#Se crea la gráfica


plot(T,es)


#Se define las etiquetas de los ejes X y Y.


xlabel('T (Grados centigrados)')


ylabel(u'Presión de vapor (Pa)')


#Se muestra la gráfica

show()

```

La gráfica se muestra a continuación:

![](./images/graficadepresiondevaporconnumpyymatplotlib-2.png)


####
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)