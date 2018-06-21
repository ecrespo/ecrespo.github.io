Title: Actualizando el firmware al Nokia N810
Date: 2010-23-03 10:10
Category: Nokia N810

En esta Semana Santa me dedique a actualizar mis dispositivos 
que manejan Linux (nslu2 y nokia n810). Sólo me falta comprar 
una memoria al PSP para instalar Linux también.
Este post es dedicado al Nokia N810 y la actualización del firmware.

El firmware que viene con el equipo tiene unos problemas con algunos 
paquetes y sus dependencias como por ejemplo skype y xchat. Así que 
lo primero que hay que hacer es actualizarlo antes de ponerse a 
instalar programas adicionales.

Los pasos son los siguientes:

1. Bajar el programa [flasher-3.0](http://tablets-dev.nokia.com/d3.php).
2. Bajar el firmware para el Nokia N810. Puede bajarse la última versión del firmware aquí.
3. Asegurarse que la bateria del Nokia tiene full carga.
4. Desconectar el Nokia de la alimentación de corriente y apagarlo.
5. Conectar el Nokia al puerto USB del computador sin encenderlo.
6. Ejecute como root el siguiente comando:
```
./flasher-3.0 -F  RX-44_2008SE_2.2007.51-3_PR_COMBINED_MR0_ARM.bin -f -R
```
7. En el computador aparecerá el siguiente mensaje en la consola :"Suitable USB device not found, waiting"
8. Encienda el Nokia y se iniciará el proceso de actualización del firmware, en el tablet aparecerá el símbolo de conectado por USB.
9. Al terminar se muestra en la consola el mensaje: you're done now!
10. Ya el equipo está actualizado, ahora si la actualización no se hace cuando el equipo está recien comprado es necesario realizar un respaldo del mismo con las herramienta de recuperación y respaldo
