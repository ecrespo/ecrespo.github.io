Title: Accesibilidad en squeeze
Date: 2011-02-06 09:00
Category: Tutorial Linux
Tags: Linux, Debian, Accesibilidad
lang: es
translation: true

Desde que se inicio el desarrollo de squeeze tenía claro que vendrían mejoras en el proceso de accesibilidad en el instalador de Debian. Con Lenny se podía usar una lectora Braille USB sin problemas en el proceso de instalación en modo texto y gráfico.


Con la versión de squeeze incluso en el documento de instalación se explica como habilitar la accesibilidad en este proceso, la información se encuentra en este [enlace](http://www.debian.org/releases/stable/i386/ch05s02.html.es).

A continuación daré un breve resumen de la guía:

1. Dispositivos Braille USB: Estos se detectan automáticamente en el proceso de arranque del instalador gracias a la aplicación brltty, para más información sobre está aplicación pueden visitar el [enlace](http://www.mielke.cc/brltty/doc/drivers/).
2. Dispositivos Braille seriales: Para estos dispositivos es necesario pasarle unos parámetros al kernel al momento de arranque del instalador. La sintaxis es brltty=controlador, puerto,tabla.Donde el puerto por defecto es ttyS0, la lista de controladores la puede encontrar [aquí](http://www.mielke.cc/brltty/doc/Manual-BRLTTY/English/BRLTTY-11.html) y la lista de códigos de las tablas [aquí](http://www.mielke.cc/brltty/doc/Manual-BRLTTY/English/BRLTTY-6.html).
3. Dispositivos sintetizadores de voz: Está es la mejora que tiene squeeze, ya que ahora se puede reproducir voces en el proceso de instalación de Debian sólo para el instalador gráfico; es necesario pasarle unos parámetros de arranque al cd de instalación con la siguiente sintaxis: speakup.synth=controlador. La reproducción de las voces se logra por medio de la aplicación speakup pero es necesario pasarle el tipo de controlador para que pueda reproducir las voces de forma adecuada. En este [enlace](http://www.linux-speakup.org/spkguide.txt) se encuentra la guía de como usar speakup y la lista de controladores.
4. Temas de alto contraste: Para las personas con visión disminuida se puede usar un tema de alto contraste, para habilitarlo en el arranque coloque el siguiente parámetro theme=dark. Está opción ya existía en Lenny en la interfaz gráfica del instalador.

Adicionalmente el equipo de Debian ha creado un grupo dedicado a accesibilidad en la personalización del cd de Debian, para más información visiten el sitio de Debian Pure Blends dedicado a la [accesibilidad](http://www.debian.org/devel/debian-accessibility/).




===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
