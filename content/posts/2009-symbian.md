Title: Sistema Operativo para celulares Symbian
Date: 2009-05-10 08:00
Category: Sistemas Operativos
Tags: Symbian
lang: es
translation: true

### SymbianOS

Es un sistema operativo abierto diseñado para dispositivos moviles, con librerias,
framework de interfaz de usuario y herramientas desarrolladas por Symbian Ltd, correo
exclusivamente en procesadores ARM

### Diseño

Su estructura es parecida a muchos sistemas operativos de escritorio, con multitareas
preeemptivas y protección de memoria. EPOC fue inspirado por el maneja de multiples tareas de OpenVMS.

SymbianOS fue construido manteniendo 3 reglas, la integridad y seguridad de los datos del
usuario es primordial, el tiempo del usuario no debe desperdiciarse y todos los recursos
son escasos. Todas las aplicaciones y el sistema operativo fueron desarrollados con
programación orientada a objetos siguiendo el paradigma MVC.

### Estructura

El modelo del Sistema Operativo Symbian contiene las siguientes capas desde arriba
hasta abajo:

* Capa del framework de la Interfaz de Usuario
* Capa de servicios de aplicación
* Java ME
* Capa de servicios del Sistema Operativo
* Servicios genéricos del Sistema Operativo
* Servicios de comunicación
* Servicios multimedia y de gráficos
* Servicios de conectividad
* Capa de sevicios base
* Capa de Interfaz del Hardware y servicios del kernel

Los Servicios base se encuentra en el nivel más bajo con respecto a las operaciones del
usuario, este incluye Servidor de archivo y librerías de usuario, el framework de plugins
el cual administra todos los plugins, repositorio central, manejador de base de datos
y servicios de cifrado.

El sistema operativo Symbian tiene una arquitectura de microkernel, lo cual significa
que usará lo mínimo necesario dentro del kernel logrando robustez y disponibilidad. Este
contiene un categorizador, administración de memoria, y drivers de dispositivos, pero
otros servicios como redes, telefonía, o soporte al sistema de archivos se ubican
en la capa de servicio del sistema operativo o la capa de servicios base. La inclusión
de los drivers de los dispositivos significa que el kernel no es un verdadero microkernel.

El sistema operativo Symbian se diseño tomando en cuenta la compatibilidad con otros
dispositivos, especialmente dispositivos de manejo de sistemas de archivos removibles,
a sus inicios EPOC adoptó el sistema de archivos FAT como sistema de archivos interno.

Hay un gran número de subsistemas de redes y comunicaciones en cual tiene 3 servidores
principales: ETEL (Telefonía EPOC), ESOCK (Sockets EPOC) y C32 (responsable de la
  comunicación serial); cada uno de estos tiene un esquema de plugins. El subsistema
  también contiene código que pertenece a un corto rango de comunicaciones como
  Bluetooth, IrDA y USB.



Software Libre para Symbian 9.1

* Utilidades
* Putty: Cliente ssh y telnet
* Radio por Internet
* SymTorrent: Cliente torrent
* Symella: Cliente gnutella
* Interprete de python: Esto nos da la oportunidad de desarrollar aplicaciones para Symbian con python aparte de Java.
* Servidor Web Apache
* Emulación de juegos
* ScummVM
* Multimedia
* Oggplay
* Symbian anuncia PIPS (Posix sobre symbian) el cual incrementará la cantidad de aplicaciones de software libre escritos para symbian

===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)