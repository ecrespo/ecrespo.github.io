Title: Widgets en Android con python. Parte 5 (Botón)
Date: 2010-07-16 10:00
Category: Tutorial Python en Android
Tags: Android, Python
lang: es
translation: true

Este artículo explicará como crear un mensaje con un botón de continuar, luego de presionar el botón se presenta un mensaje del resultado del botón.

El código de la aplicación es el siguiente:

```python
#Importar módulo android
import android
#Se crea la instancia del objeto Android
droid = android.Android()

#título y mensaje del botón 
title = 'Interfaz de usuario'
message = 'Esta es una prueba'

#Se crea la alerta con el título y mensaje 
droid.dialogCreateAlert(title, message)

#Se define el botón 
droid.dialogSetPositiveButtonText('Continuar')
 
#Se muestra el mensaje 
droid.dialogShow()

#Se captura el resultado del resultado de darle clip al botón
#El resultado es un diccionario
response = droid.dialogGetResponse().result
 
#Se muestra el resultado del clip del botón 
droid.makeToast('El resultado de la ejecucion del boton es: %s' 
                                %response['which'])
```

A continuación se muestra el botón.

![Boton ](./images/mensaje_alerta1.png)

La siguiente figura se muestra el mensaje del resultado de darle clip al botón.

![Boton - Resultado](./images/mensaje_alerta2.png)

Para finalizar se muestra la imagen del código qr del programa.

![Código](./images/mensaje_alerta3.png)


===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)