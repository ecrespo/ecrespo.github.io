Title: Generando una gráfica con PyQT y matplotlib (escala semilogaritmica). Parte 13
Date: 2011-06-10 09:00
Category: Tutorial Python
Tags: Linux,Python,pyqt,matplotlib,numpy
lang: es
translation: true

En este artículo se explicará como crear gráficas con escala semilogaritmitca.

La idea es graficar la función:
y = sin(pi*(x**(1/2)))

La gráfica muestra la figura de la función con escala semilogaritmica.

![Gráfica semilogaritmica 1](./images/matplotlib13-1.png)

El código para generar la gráfica mostrada simplemente usando numpy y matplotlib es la siguiente:

```python 
#!/usr/bin/env python

#Importar matplotlib
import matplotlib as mpl
#Definir el tamaño de la fuente
mpl.rcParams['font.size'] = 10.
#Importar pyplot
import matplotlib.pyplot as plt
#Importar numpy
import numpy as np

#Se crea el rango de valores de
# 0 a 20 con saltos de 0.01
x = np.arange(0., 20, 0.01)
#Se instancia la figura
fig = plt.figure()
#Se define  la grafica
ax2 = fig.add_subplot(311)
#Se genera el calculo de la funcion
#con numpy
y2 = np.sin(np.pi*(x**(1.0/2.0)))
#Se define el eje X con escala
#logaritmica
ax2.semilogx(x, y2);
#Se define el limite del eje X
ax2.set_xlim([0, 20]);
#Se define la grilla a la grafica
ax2.grid(True)
#se define una etiqueta en el eje Y
ax2.set_ylabel('log X')
#Se muestra la grafica
plt.show()
```

En la siguiente figura se genera la gráfica utilizando PyQT, matplotlib y numpy:

![Gráfica semilogaritmica 1](./images/matplotlib13-2.png)

A la gráfica se le agrego la barra de navegación y se le coloco un título a la ventana.

El código para crear la gráfica utilizando PyQT es el siguiente:

```python
#!/usr/bin/env python
#Importar numpy 
import numpy as np
# Importar el objeto Figure de matplotlib
from matplotlib.figure import Figure

#Importar el Objeto FigureCanvas de Qt4Qgg,
#Se heredara desde QWidget.
from matplotlib.backends.backend_qt4agg \
  import FigureCanvasQTAgg as FigureCanvas

#Importar el widget de la barra de navegacion 
# import the NavigationToolbar Qt4Agg widget
from matplotlib.backends.backend_qt4agg \
  import NavigationToolbar2QTAgg as NavigationToolbar

#Importar QTGui de PyQt4.
from PyQt4 import QtGui

#Se crea la Clase Qt4MplCanvas heredando FigureCanvas
class Lienzo(FigureCanvas):
    
    def __init__(self, parent):
        # Se instancia el objeto figure
        self.fig = Figure()
        #Se define la grafica en coordenadas polares
        self.axes = self.fig.add_subplot(111)
        
        #Se define el rango de 0 a 20 con saltos de 0.01

        x = np.arange(0., 20, 0.01)
        #Se calcula los valores de la funcion.
        y2 = np.sin(np.pi*(x**(1.0/2.0)))
        #Se define el eje X como logaritmico
        #y se pasan los valores de x y y2.
        self.axes.semilogx(x, y2);
        #Se define el limite del eje X
        self.axes.set_xlim([0, 20]);
        #Se define una grilla
        self.axes.grid(True)
        #Se crea una etiqueta en el eje Y
        self.axes.set_ylabel('log X')
        
        # se inicializa FigureCanvas
        FigureCanvas.__init__(self, self.fig)
        # se define el widget padre
        self.setParent(parent)
        # se define el widget como expandible
        FigureCanvas.setSizePolicy(self,
                QtGui.QSizePolicy.Expanding,
                QtGui.QSizePolicy.Expanding)
        # se notifica al sistema de la actualizacion
        #de la politica
        FigureCanvas.updateGeometry(self)

#Se crea la clase Ventana que hereda QMainWindow
class Ventana(QtGui.QMainWindow):
    
    def __init__(self):
        
        #Inicializacion del widget QMainWindow
        QtGui.QMainWindow.__init__(self)
        # se define el titulo de la ventana
        self.setWindowTitle("Ventana PyQT con graficas a escala logaritmica")
        # instantiate a widget, it will be the main one
        # Se instancia el widget.
        self.main_widget = QtGui.QWidget(self)
        
        #Se crea una layout vbox
        vbl = QtGui.QVBoxLayout(self.main_widget)
        
        #Se instancia el Lienzo con la grafica de Matplotlib
        qmc = Lienzo(self.main_widget)
        # se instancia la barra de navegacion
        ntb = NavigationToolbar(qmc, self.main_widget)
        # se empaqueta el lienzo y 
        #la barra de navegacion en el vbox
        vbl.addWidget(qmc)
        vbl.addWidget(ntb)
        # se le asigna foco a la ventana
        self.main_widget.setFocus()
        #Se define el widget central
        self.setCentralWidget(self.main_widget)

if __name__ == '__main__':
    #Importar sys
    import sys
    #Importar QtGui de PyQt4
    from PyQt4 import QtGui
    #Se crea la aplicacion grafica
    qApp = QtGui.QApplication(sys.argv)
    # se instancia la ventana
    aw = Ventana()
    # se muestra el widget
    aw.show()
    #Se inicia el lazo principal de QT
    sys.exit(qApp.exec_())
```



===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
