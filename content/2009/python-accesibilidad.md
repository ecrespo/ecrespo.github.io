Title: Creado el proyecto python-autoaccesibilidad
Date: 2009-07-04 06:00
Category: Anuncio
Tags: Accesibilidad
lang: es
translation: true

La página del proyecto se encuentra en:

http://code.google.com/p/python-autoaccesibilidad/

La descripción del mismo se encuentra en el wiki:

### Introducción

Este programa permitirá la instalación de aplicaciones accesibles en equipos con
Debian ya instalados sin necesidad de tener una conexión a internet o un mirror
en la red; es útil para laboratorios y centros de navegación.

Para los usuarios se tendrá 2 paquetes de Debian (metapaquete accesibilidad,
accesibilidad-gnome-conf-spanish y accesibilidad-gnome-conf-english) que
facilitará la instalación de sus equipos.

### Detalles

La aplicación tendrá las siguientes características:

* Desarrollado en python
* Modular
* Usará el módulo gksu de python para la instalación de paquetes de Debian, modificación
del sources.list y ejecutar un servidor web escrito en python.

* Se agrega los directorios de configuración y un módulo para copiar las configuraciones a todos los usuarios.
* Se incorpora un repositorio pequeño de debian que tendrá el metapaquete accesibilidad y
las dependencias necesarias para así no necesitar un mirror de debian (un disco duro o conexión a internet).

* Por los momentos sólo funcionará con Debian Squeeze y Sid, ya que el metapaquete accesibilidad
funciona para esas dos versiones de Debian (problemas de dependencias y existencia de paquetes
  en Lenny), en un futuro se sacará una versión para lenny.

* Tendrá la posibilidad de actualizar el repositorio de paquetes local para así no depender
de versiones de paquetes y que se cambie la aplicación debido a esos cambios.

Los módulos que se necesitan son:

* web.py : Inicia un servidor web.
* su.py : Facilita la ejecución de comandos como root pidiendo la clave de root.
* users.py : Devuelve los usuarios que existen en el computador.
* apt.py : Realiza cambios en el repositorio que usa el equipo e instala aplicaciones.
* autoaccesibilidad.py : Programa principal que realiza la instalación de aplicaciones
accesibles en un equipo utilizando un mirror y servidor web local.

Contendrá 2 directorios:

* conf: En este directorio se tendrá toda la configuración de la sesión del Escritorio Gnome,
la configuración del lector de pantalla orca y cualquier otra configuración de la sesión del usuario.

* debian: En este directorio se tendrá un repositorio local de paquetes de Debian que son necesarios
para que un computador sea accesible.

Más información en el blog de libre accesibilidad:

http://libreaccesibilidad.blogspot.com/2009/07/proyecto-python-autoaccesibilidad.html




===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./imagenes/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
