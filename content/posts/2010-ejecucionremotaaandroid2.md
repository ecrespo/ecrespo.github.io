Title: Ejecución remota de scripts python desde Linux a un celular con Android (versión conectado el celular por USB)
Date: 2010-12-15 10:00
Category: Tutorial de Python en Android
Tags: Android, Python, Debian, Linux
lang: es
translation: true

En el post anterior explique como ejecutar script python en un celular con Android de forma remota desde Linux por wifi, ahora explicaré como hacerlo por cable USB, en realidad es más sencillo que el artículo anterior.
Me basaré en lo explicado en el post [anterior](https://www.seraph.to/ejecucion-remota-de-scripts-python-desde-linux-a-un-celular-con-android.html#ejecucion-remota-de-scripts-python-desde-linux-a-un-celular-con-android) y en el post sobre [envío de mensajes de texto](https://www.seraph.to/enviar-mensajes-de-texto-desde-android-con-python.html).

Lo primero que se necesita hacer es conectar el celular al computador por USB, activar el modo depuración y la conexión USB a Portal y Herramientas.

Se debe iniciar el servidor de SL4A. Menú->Ver->Interpretes->Menú->Iniciar Servidor->Privado.

Luego se averigua en los mensajes de notificiación que puerto abre el servidor. En mí caso fue el 58825.

Desde la consola de Linux se ejecutan los siguientes comandos:
Redirecciona toda petición al puerto 9999 al puerto 58825.

```
./adb forward tcp:9999 tcp:58825

```

Se exporta una variable de ambiente.

```
export AP_PORT=9999
```

El programa es el siguiente:

```python
#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-
#Script que permite enviar mensaje de texto a un celular android desde Linux.
#Autor: Ernesto Crespo
#Correo:ecrespo@gmail.com
#Licencia: GPLv3
#Versión:0.1

#Importando el módulo android,sys y re
import android,sys,re


#Función de envio de mensajes
def Enviomensaje():
    #Se averigua si se le pasa al script el número celular y el mensaje, y que el número sea válido para venezuela.
    if len(sys.argv) == 3:
        numero = sys.argv[1]
        mensaje = sys.argv[2]
    else:
        print "error enviando mensaje, se necesita pasar el número y mensaje"
        sys.exit
    if Validar(numero) == 0:
        print "Número invalido"
        sys.exit
    #Creando la instancia droid del objeto Android
    droid = android.Android()
    #Enviando el mensaje de texto
    droid.smsSend(numero,mensaje)
    #Se presenta un mensaje de notificación en el celular.
    droid.makeToast('Mensaje enviado')


#Función que válida si el número es de movilnet, digitel o movistar.
def Validar(numero):
    #Valida si los numeros tienen 11 digitos y que sean de los proveedores movilnet, digitel y movistar
    if len(numero) == 11 and ((re.search("041[2|4|6]\d\d\d\d\d\d\d",numero)) or (re.search("042[4|6]\d\d\d\d\d\d\d",numero))) :
        return 1
    else:
        return 0
#Ejecución del programa.
if __name__ == "__main__":
    Enviomensaje()
```

Ejecutar el script.
```
enviomensajes.py 0xxxyyyzzww  "2da prueba, avisame si te llega el sms"
```

===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)