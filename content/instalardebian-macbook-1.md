Title: Instalación de Debian en un mac Book. Primera parte
Date: 2008-06-08 10:00
Category: Debian, Linux, MacBook
Tags: Debian, MacBook
lang: es
translation: true

### Preparativos 

Lo primero que hay que hacer es bajar la aplicación [rEFIT](http://refit.sourceforge.net/) e instalar 
en el MacOSX. Reparticionar el disco duro via el MacOSX y reiniciar el equipo.

En este momento aparece el menu de arranque de refit; en este menu aparece un icono de una 
consola que dice refit, hay que seleccionar esta y al terminar de arrancar refit es necesario 
ejecutar gptsync para sincronizar las particiones del disco duro con la aplicación refit, se 
le dice Y (si) y luego se reinicia el equipo para arrancar con el CD de instalación de Debian.


### ¿Cuál version utilizar ?

Depende del procesador que se tiene en el equipo, en mi caso en la mac book que tengo no puedo 
instalar con el cd de amd4, solo se instala con el cd de i386. Pero si el equipo tiene un procesador 
core duo de última generación se usará el de AMD64.

Yo prefiero instalar un laptop con lenny en vez de etch en este momento, en especial que lenny ya se 
encuentra en proceso de estabilización.

Si se va a utilizar lenny se recomienda instalar en modo experto para la instalación ya que esta versión 
tiene un problema al momento de configurar el video ya que se pierde el entorno de instalación y se hace 
necesario realizar una instalación remota via ssh.

### Proceso de instalación

Se reinicia el equipo colocando el CD de Debian Lenny, seleccionando en refit el arranque por cdrom y 
luego colocar expert.

1. Selección de Idioma : Español
2. Selección del país: Venezuela
3. Selección del teclado: Latinoamericano (por los momentos)
4. Seleccione UTF-8 venezuela.
5. Verificación del cd y selección de componentes del cdrom: se selecciona las opciones de ssh.
6. Configuración de la tarjeta de red (claro por los momentos hacer instalación por cable de red).
7. Confiruación de la red via DHCP.
8. Configuración de instalación remota via ssh: se crea una clave para el usuario installer y luego nos da la ip a utilizar.
9. Desde un 2do equipo conectarse por ssh a la ip del equipo, ejm: ssh installer@x.x.x.x
10. Se selecciona instalar debian (primera opción).
11. En este momento se repiten los pasos 1,2,3 y 4.
12. Detección del disco duro y particionado del mismo (existen muchas posibilidades), cree sólo 3 particiones: /, /home y swap y depende del tamaño del disco duro el tamaño que se le va a asignar a las particiones.
13. Formateo del disco duro y se instala un sistema base
14. Crear la clave de administrador del equipo.
15. Crear una cuenta de usuario.
16. Seleccionar un repositorio
17. Selección de la aplicación de popularidad de programas instalados, puede decir si o no.
18. Selección de los paquetes a instalar (Sistema base, Escritorio y Laptop). Con esta opción se tendrá un laptop base con todo lo necesario para que trabaje un usuario.

19. Se inicia el proceso de instalación de paquetes.
20. Cofiguración de resolución de la pantalla (depende del laptop): Seleccione 1280x800.
21. Configuración del arranque (si prueban con grub va a dar un error), en este caso hay que instalar lilo como administrador de arranque en la partición raíz.

22. Luego de instalar el gestor de arranque es bueno volver a sincronizar el disco duro:
Abra una segunda consola (control+alt+F2) desde el cd de instalación y ejecute
```
chroot /target aptitude install refit
 /target/sbin/gptsync /dev/sda
```

23. En este momento ya se tendrá Debian instalado y solo queda retirar el cd de instalación y reniciar el equipo.

En la segunda parte del post se tratará la configuración y puesta a punto del equipo.

===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC) 
usando la billetera digital de tu preferencia a la siguiente 
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./imagenes/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
