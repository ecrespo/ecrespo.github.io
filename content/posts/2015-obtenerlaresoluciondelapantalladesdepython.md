Title: Obtener la resolución de la pantalla desde Python
Date: 2015-08-27 9:00
Category:
Tags: Canaima,Debian,Python,Ubuntu
lang: es
translation: true

Este artículo se basa en un [artículo](http://www.blog.pythonlibrary.org/2015/08/18/getting-your-screen-resolution-with-python/) en inglés sobre el tema.

Desde la línea de comandos en Linux se puede ejecutar el comando `xrandr` como se muestra a continuación:
```
ernesto@grievous:~$ xrandr | grep '*'
   1366x768      60.00*+
```
La resolución es de 1366x768.

El script se muestra a continuación:
```python
#!/usr/bin/env python

#Se importa el modulo subprocess
import subprocess

#Se define un par de variables con los comandos a pasar:
cmd = ['xrandr']
cmd2 = ['grep', '*']

#Se ejecuta el comando xrandr y luego se abre una tuberia.
p = subprocess.Popen(cmd, stdout=subprocess.PIPE)

#Se ejecuta el segundo comando
p2 = subprocess.Popen(cmd2, stdin=p.stdout, stdout=subprocess.PIPE)

#Se cierra la salida estandar.
p.stdout.close()


#Obteccion de la resolucion
resolution_string, junk = p2.communicate()
resolution = resolution_string.split()[0]
width, height = resolution.split('x')
print width,height
```

Al ejecutar el script se obtiene:
```python
./screencatch.py
1366 768
```
Obtener resolución con gtk con el siguiente script:
```python
#!/usr/bin/env python

#Se importa gtk
import gtk

#Se captura el ancho y alto
width = gtk.gdk.screen_width()
height = gtk.gdk.screen_height()

#Se muestra en la consola el resultado
print width,height
```
Al ejecutar el script se obtiene:
```python
 ./screencatch2.py
1366 768
```
Obtener la resolución con `PySide/PyQT` con el siguiente script:
```python
#!/usr/bin/env python
#Importar QtGui de PySide
#para solo PyQt se cambia a
#from PyQt4 import QtGui

from PySide import QtGui

#Se crea la instancia de la aplicacion
app = QtGui.QApplication([])
#Se captura la resolucion y se muestra  en la consola
screen_resolution = app.desktop().screenGeometry()
width, height = screen_resolution.width(), screen_resolution.height()

print width,height
```
El resultado de ejecutar el script  es:
```python
./screencatch3.py
1366 768
```

En el artículo mencionado se muestra como obtener la información con `wxPython` y en un enlace en el artículo como obtener la información desde windows y desde MacOS.

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
