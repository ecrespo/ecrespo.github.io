Title: Manejar los mensajes de Texto del celular desde Linux (Android)
Date: 2010-12-16 09:00
Category: Tutorial Python en Android
Tags: Android, Linux, Python, SMS
lang: es
translation: true


Para continuar con los scripts que se ejecutan de forma remota en el celular, ahora mostraré como se maneja los mensajes de texto, buscar mensajes y borrarlos.

La idea es buscar todos los mensajes de un número celular dado, presentar el mensaje en la consola y borrar dichos mensajes.

Se sigue el procedimiento de ejecución remota explicado en el [post anterior](https://www.seraph.to/ejecucion-remota-de-scripts-python-desde-linux-a-un-celular-con-android-version-conectado-el-celular-por-usb.html#ejecucion-remota-de-scripts-python-desde-linux-a-un-celular-con-android-version-conectado-el-celular-por-usb).



El código es el siguiente:

```python
#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-
#Script que permite manejar los SMS del celular con android desde Linux.
#Autor: Ernesto Crespo
#Correo:ecrespo@gmail.com
#Licencia: GPLv3
#Versión:0.1


#Importando el módulo android,sys y re
import android


#Función de envio de mensajes
def Contactos():
    #Se crea la instancia de la clase Android
    droid = android.Android()
    #Se captura la cantidad de mensajes de texto )como en mi caso todos los 
    #mensajes han sido leídos coloco 0, si quiero los no leídos coloco 1.
    cantidad = droid.smsGetMessageCount(0)[1]
    #El número de celular a buscar
    numero = "0xxxyyyzzww"
    #Se recorren todos los mensajes.
    for i in range(cantidad):
        #Si el mensaje es del número dado se captura el identificador
        #del mensaje, se imprime un mensaje  en pantalla con la información:
        #read:Si mensaje ya fue leído
        #date: la fecha del mensaje
        #_id:identificador del mensaje.
        #address: número celular.
        #body:cuerpo del mensaje.
        #Toda está información se maneja desde un diccionario.
        #Si el celular no es de la persona buscada se continua con la 
        #siguiente iteración. 
        #A la función de borrar se le pasa el identificador del mensaje
        if droid.smsGetMessages(0)[1][i]["address"] == numero:
            identificador = droid.smsGetMessages(0)[1][i]["_id"]
            print "Borrando mensaje\t",i,droid.smsGetMessages(0)[1][i]["read"],droid.smsGetMessages(0)[1][i]["date"],droid.smsGetMessages(0)[1][i]["address"],droid.smsGetMessages(0)[1][i]["body"]
            droid.smsDeleteMessage(identificador)
        else:
            continue
if __name__ == "__main__":
    #Ejecución de la función
    Contactos()

```

La salida del programa es la siguiente:

 Devuelve el mensaje que se ha borrado el SMS, el número del mensaje, si está leído, la fecha, el número y el cuerpo del mensaje.

```
Borrando mensaje 296 1 1285030227398 0xxxyyyzzww Ah bueno... Yo les aviso.
Borrando mensaje 358 1 1283635867054 0xxxyyyzzww Ok. Ahi voy.
```



===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)