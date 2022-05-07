Title: Enviar mensajes de texto desde Android con python
Date: 2010-06-27 15:00
Category: Tutorial Python
Tags: Android, Linux, Python, SMS
lang: es
translation: true


Continuando con la referencia del API de ASE para Android se explicará como enviar un mensaje de texto desde python para un celular con Android.

EL API para enviar mensajes de texto es el siguiente:

```
smsSend(String destinationAddress: typically a phone number,String text) Sends an SMS.
```

A continuación el código de envío de SMS:



```python

#Importando el módulo android y el módulo time
import android, time

#Creando la instancia droid del objeto Android
droid = android.Android()

#Asignando el número de teléfono y mensaje
telefono ="0xxxyyyyyyy"
mensaje = "Esta es una prueba de envio de sms a la hora %s" %time.ctime()

#Enviar mensaje a la pantalla de android con la info del número y mensaje
droid.makeToast("enviando mensaje a %s, con el siguiente contenido: %s" %(telefono,mensaje))

#Enviando el mensaje de texto
droid.smsSend(telefono,mensaje)

```

El mensaje llego al celular del número asignado sin problemas.


===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)