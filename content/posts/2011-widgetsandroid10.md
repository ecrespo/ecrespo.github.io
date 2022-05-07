Title: Introducción a webview en Android con python
Date: 2011-04-02 11:00
Category: Tutorial Python en Android
Tags: Android, Python, webview
lang: es
translation: true

La serie de widgets del SL4A que se ha explicado en el blog no son suficientes para realizar aplicaciones tal como las que se bajan del market de Android, pues existe una forma de aumentar las posibilidades en interfaz gráfica para Android y es usando webview.

Webview permite visualizar páginas html con contenidos en javascript.

En la página de SL4A tienen una introducción sobre [webview](http://code.google.com/p/android-scripting/wiki/UsingWebView).

Se tiene un archivo html llamado text_to_speech.html con código javascript, es un formulario html  donde se le pasa un texto a reproducir.

![html con javascript speech.html](./images/webview3.png)

Luego se tiene el código python en un archivo llamado webview.py. Se crea la instancia de android, se abre el archivo text_to_speech2.html, se espera por el evento tomando el resultado y reproduciendolo con text to speech.

```python
import android
droid = android.Android()
droid.webViewShow('file:///sdcard/sl4a/scripts/text_to_speech2.html')
while True:
  result = droid.waitForEvent('say').result
  droid.ttsSpeak(result['data'])
```
![script Python android](./images/webview4.png)

La siguiente imagen muestra la pantalla de la página web.

![wepapp](./images/webview1.png)

Y la figura donde se muestra que se escribió un texto en el formulario, al darle clip al botón el celular reproduce el texto que se le paso al formulario.


![wepapp demo](./images/webview2.png)

===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
