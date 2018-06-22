Title: Hola mundo 2da versión con hildon y python
Date: 2008-03-23 10:40
Category: Debian, Maemo, Nokia, N810, Python
Tags: Maemo, Nokia, Python,N810
lang: es
translation: true

La segunda versión del hola mundo se basará en el framework 
hildon el cual permite manejar el look,temas del entorno de 
maemo, acceso a barra de herramientas y menus.

```
#!/usr/bin/env python2.5

import gtk
import hildon

window = hildon.Window()
window.connect("destroy", gtk.main_quit)
label = gtk.Label("Hola mundo!")
window.add(label)

label.show()
window.show()

gtk.main()
```

Captura de pantalla de la ejecución del script:

![Hola Mundo desde Maemo](./imagenes/holamundo-maemosdk2.png)

===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC) 
usando la billetera digital de tu preferencia a la siguiente 
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./imagenes/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
