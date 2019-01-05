Title: Desarrollo de aplicaciones gráficas con python+gtk+glade. Parte 4
Date: 2009-06-17 10:00
Category: Tutorial Python
Tags: Linux,Python,gtk,glade
lang: es
translation: true

El siguiente ejemplo explicará como manejar 2 ventanas en una aplicación.

La primera venta muestra 2 etiquetas una con un texto y la otra en blanco, luego
una entrada de datos solicitando el nombre, 2 botones uno de capturar texto y otra
de salir. Al darle al botón de capturar texto se abre otra ventana preguntando si está
seguro de lo que desea hacer, si se le da aceptar presenta el texto en la etiqueta.

La siguiente figura muestra la interfaz desarrollado con glade.

![Tutorial 4 Glade 1](./images/tutorialglade4-1.png)

El código del programa es el siguiente:

![Código](./images/tutorialpythongtkglade4-codigo.png)


Al ejecutar el programa se muestra la siguiente figura:

![Tutorial 4 Glade 2](./images/tutorialglade4-2.png)

Se escribe el nombre y se presiona capturar texto:
![Tutorial 4 Glade 3](./images/tutorialglade4-3.png)

Al presiona capturar texto y se abre una ventana con la pregunta si se desea
aceptar o salir de la aplicación.

![Tutorial 4 Glade 4](./images/tutorialglade4-4.png)

Para finalizar se muestra la captura de texto en la etiqueta.

![Tutorial 4 Glade 5](./images/tutorialglade4-5.png)


El código de la aplicación lo pueden descargar de github en el siguiente
[enlace](https://github.com/ecrespo/ecrespo.github.io/blob/master/content/code/2009/tutorialgtkglade4.py).


===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)