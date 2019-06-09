Title: Tutorial de PyQt. Desarrollo con QtDesigner. Parte 11.
Date: 2012-07-29 9:00
Category: Tutorial Python
Tags: Canaima,General,gnome,Linux,PyQt,Python,Ubuntu
lang: es
translation: true

Para repasar los artículos sobre `pyQt` pueden revisar el siguiente [enlace](https://www.seraph.to/tag/pyqt.html).

En este caso en vez de escribir todo el código de la intefaz gráfica se usará la herramienta `QtDesigner`.

Se pedirá el nombre de la persona y al darle click al botón Aplicar se mostrará el nombre colocado en la entrada de datos en la etiqueta, se tiene un segundo botón el cual termina la ejecución de la aplicación al darle click.

La siguiente figura muestra el diseño de la interfaz:

![](./images/tutorialdepyqtdesarrolloconqtdesigner-1.png) 

La siguiente figura muestra la relación entre los botones y señales:

![](./images/tutorialdepyqtdesarrolloconqtdesigner-2.png) 

A cada botón se le asocia una función como lo muestra las siguientes dos figuras:
Botón Salir:

![](./images/tutorialdepyqtdesarrolloconqtdesigner-3.png) 

Botón Aplicar:

![](./images/tutorialdepyqtdesarrolloconqtdesigner-4.png) 

Al salvar la interfaz gráfica con nombre `prueba3.ui` lo que se hará a continuación es generar el código python por medio del comando:
`pyuic4 -x prueba3.ui -o prueba3.py`

El código generado se muestra a continuación:
```python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prueba3.ui'

#

# Created: Sun Jul 29 22:49:50 2012

#      by: PyQt4 UI code generator 4.9.1

#

# WARNING! All changes made in this file will be lost!




from PyQt4 import QtCore, QtGui




try:

    _fromUtf8 = QtCore.QString.fromUtf8

except AttributeError:

    _fromUtf8 = lambda s: s




class Ui_Form(object):

    def setupUi(self, Form):

        Form.setObjectName(_fromUtf8("Form"))

        Form.resize(400, 300)

        self.pushButton = QtGui.QPushButton(Form)

        self.pushButton.setGeometry(QtCore.QRect(280, 260, 102, 28))

        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.pushButton_2 = QtGui.QPushButton(Form)

        self.pushButton_2.setGeometry(QtCore.QRect(140, 260, 102, 28))

        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.lineEdit = QtGui.QLineEdit(Form)

        self.lineEdit.setGeometry(QtCore.QRect(140, 40, 221, 28))

        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.label = QtGui.QLabel(Form)

        self.label.setGeometry(QtCore.QRect(20, 40, 69, 18))

        self.label.setObjectName(_fromUtf8("label"))

        self.label_2 = QtGui.QLabel(Form)

        self.label_2.setGeometry(QtCore.QRect(20, 160, 81, 18))

        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.label_3 = QtGui.QLabel(Form)

        self.label_3.setGeometry(QtCore.QRect(140, 160, 221, 18))

        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Form)

        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)

        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.label_3.update)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):

        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Prueba", None, QtGui.QApplication.UnicodeUTF8))

        self.pushButton.setText(QtGui.QApplication.translate("Form", "Salir", None, QtGui.QApplication.UnicodeUTF8))

        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "Aplicar", None, QtGui.QApplication.UnicodeUTF8))

        self.label.setText(QtGui.QApplication.translate("Form", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))

        self.label_2.setText(QtGui.QApplication.translate("Form", "Resultado:", None, QtGui.QApplication.UnicodeUTF8))

        self.label_3.setText(QtGui.QApplication.translate("Form", "Texto", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":

    import sys

    app = QtGui.QApplication(sys.argv)

    Form = QtGui.QWidget()

    ui = Ui_Form()

    ui.setupUi(Form)

    Form.show()

    sys.exit(app.exec_())
```

Se resalta en color azul la relación de ambos botones (Salir y Aplicar) con los eventos (Form.close y label_3.update).

El cambio en el código que se tiene que hacer es crear un método en la clase creada que toma el contenido del widget lineEdit y se la pasa a label_3, se muestra en la consola por medio de print y en la etiqueta por el método set de la etiqueta.

A continuación el código modificado con las secciones en azul que muestra lo explicado antes:
```python
#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prueba3.ui'

#

# Created: Sun Jul 29 22:27:29 2012

#      by: PyQt4 UI code generator 4.9.1

#

# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:

    _fromUtf8 = QtCore.QString.fromUtf8

except AttributeError:

    _fromUtf8 = lambda s: s

class Ui_Form(object):

    def Actualizar(self):

        texto = self.lineEdit.text()

        print texto

        self.label_3.setText(texto)

    

    def setupUi(self, Form):

        Form.setObjectName(_fromUtf8("Form"))

        Form.resize(400, 300)

        self.pushButton = QtGui.QPushButton(Form)

        self.pushButton.setGeometry(QtCore.QRect(280, 260, 102, 28))

        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.pushButton_2 = QtGui.QPushButton(Form)

        self.pushButton_2.setGeometry(QtCore.QRect(140, 260, 102, 28))

        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.lineEdit = QtGui.QLineEdit(Form)

        self.lineEdit.setGeometry(QtCore.QRect(140, 40, 221, 28))

        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.label = QtGui.QLabel(Form)

        self.label.setGeometry(QtCore.QRect(20, 40, 69, 18))

        self.label.setObjectName(_fromUtf8("label"))

        self.label_2 = QtGui.QLabel(Form)

        self.label_2.setGeometry(QtCore.QRect(20, 160, 81, 18))

        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.label_3 = QtGui.QLabel(Form)

        self.label_3.setGeometry(QtCore.QRect(140, 160, 221, 18))

        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Form)

        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)

        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Actualizar)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):

        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Prueba", None, QtGui.QApplication.UnicodeUTF8))

        self.pushButton.setText(QtGui.QApplication.translate("Form", "Salir", None, QtGui.QApplication.UnicodeUTF8))

        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "Aplicar", None, QtGui.QApplication.UnicodeUTF8))

        self.label.setText(QtGui.QApplication.translate("Form", "Nombre:", None, QtGui.QApplication.UnicodeUTF8))

        self.label_2.setText(QtGui.QApplication.translate("Form", "Resultado:", None, QtGui.QApplication.UnicodeUTF8))

        self.label_3.setText(QtGui.QApplication.translate("Form", "Texto", None, QtGui.QApplication.UnicodeUTF8))

if __name__ == "__main__":

    import sys

    app = QtGui.QApplication(sys.argv)

    Form = QtGui.QWidget()

    ui = Ui_Form()

    ui.setupUi(Form)

    Form.show()

    sys.exit(app.exec_())
```

A continuación se muestra la figura de la ejecución de la aplicación luego de capturar y mostrar la información del widget `LineEdit`:

![](./images/tutorialdepyqtdesarrolloconqtdesigner-5.png) 


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)