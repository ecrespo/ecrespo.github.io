Title: Widgets en Android con python. Parte 4 (notificación)
Date: 2010-07-15 11:00
Category: Tutorial Python en Android
Tags: Android, Python
lang: es
translation: true

A veces se necesita crear un mensaje de notificación al celular con Android.
El siguiente post explicará como crear ese mensaje.

A continuación se muestra el código:


```python
#importar módulos android y time
import android,time
 
#Crear la instancia de la clase Android
droid = android.Android()
 
#Se crea el mensaje de notificación.
droid.notify('Prueba' , 'Hola Mundo!')
```

A continuación se muestra la figura donde aparece en Android la notificación de un mensaje.

![Notificación -Entrada](./images/notificacion1.png)

En la siguiente figura se muestra ya el mensaje de notificación.


![Notificación - Resultado](./images/notificacion2.png)

Para finalizar les dejo el código qr del programa en python.

![Código](./images/notificacion.png)


===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)