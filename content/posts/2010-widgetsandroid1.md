Title: Widgets en Android con python. Parte 1 (entrada de datos)
Date: 2010-07-05 10:00
Category: Tutorial Python en Android
Tags: Android, Python
lang: es
translation: true

A continuación viene una serie de scripts para probar los distintos widgets (Entrada de datos, presentar en pantalla, selección simple, multiple, etc).

El primero que se probará es el de entrada de datos y luego el dato insertado se presentará en la pantalla del celular.

El código a continuación:

```python
#Importar módulo Android
import android

#Crear la instancia del objeto android
droid = android.Android()

#Solicitar la entreda de datos en este caso el mensaje Escriba su nombre como título
#Y luego como campo de entrada el nombre
#Se guarda el dato en texto
texto = droid.getInput("Escriba su nombre","Nombre:")

#Se manda un saludo en pantalla con el nombre del usuario, la info se encuentra en
#texto el cual es una lista.
droid.makeToast('Hola %s' %texto[1])
```

A continuación se presenta las imagenes del script.

Entrada de datos:


![Entrada de datos](./images/entradanombre.png)


Resultado:

![Entrada de datos - Resultado](./images/salidanombre.png)


El código lo pueden bajar del siguiente código QR:

![Código](./images/entradadatoscodigo.png)


===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)