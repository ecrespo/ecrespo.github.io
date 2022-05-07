Title: Tutorial de python+qt. Parte 1
Date: 2010-01-25 10:00
Category: Tutorial Python
Tags: Linux,Python,qt
lang: es
translation: true


Luego de unos cuantos artículos sobre gtk empezaré a publicar artículos sobre pyqt debido a que me asignaron a otro proyecto estoy evaluando desarrollar en pyqt o en wxwidget.

Los primeros tutoriales se enfocarán al desarrollo de la interfaz a pie sin utilizar qtdesigner.

Este ejemplo simplemente muestra una ventana con un tamaño definido y el título de la misma.





```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Importar módulo sys
import sys
#importar QTGui de pyQt4
from PyQt4 import QtGui

#Se instancia la clase QApplication pasandole sys.argv
app = QtGui.QApplication(sys.argv)

#Se crea la instancia de QWidget.
widget = QtGui.QWidget()
#Se define el tamaño de la ventana
widget.resize(250, 150)
#Se le coloca el título a la ventana
widget.setWindowTitle('Es una prueba')
#Se muestra la ventana
widget.show()
#Se sale de la aplicación
sys.exit(app.exec_())

```


La figura muestra la ventana que se creó:


![Tutorial 1 pyqt 1](./images/tutorialpyqt1-1.png)


===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)