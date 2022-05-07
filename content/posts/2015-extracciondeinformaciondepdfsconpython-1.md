Title: Extracción de información de PDFs con python (parte 1).
Date: 2015-08-29 9:00
Category: Tutorial Python
Tags: Debian,General,Python,pdf scraping
lang: es
translation: true

Existen varias herramientas en python para obtener información de PDF.
En este caso visite la página de [Cencoex](www.cencoex.gob.ve), en la sección de Cencoex en cifras hay un enlace a un pdf a [Liquidaciones a Empresas Agremiadas del Sector Salud (Ordinarias + ALADI + SUCRE)](http://www.cencoex.gob.ve/images/stories/pdfs/estadisticas/Salud.pdf).

Para este primer artículo se usará [pycurl](http://pycurl.io/) para bajar el pdf y [peepdf](http://eternal-todo.com/tools/peepdf-pdf-analysis-tool) para analizarlo. Para descargar peepdf se puede hacer desde el repositorio del proyecto en [github](https://github.com/jesparza/peepdf).

En el caso de `pycurl` se instala por `pip` o por `apt-get` en Debian.

Se baja `peepdf`:
```
git clone https://github.com/jesparza/peepdf.git
```
Para bajar el archivo se ejecuta el código a continuación, el cual baja el archivo pdf y lo salva como `salud.pdf`:
```python
import pycurl

with open('salud.pdf', 'wb') as f:
    c = pycurl.Curl()
    c.setopt(c.URL, 'http://www.cencoex.gob.ve/images/stories/pdfs/estadisticas/Salud.pdf')
    c.setopt(c.WRITEDATA, f)
    c.perform()
    c.close()
```

En el directorio de la aplicación se ejecuta (opción `-f` para el archivo y `-i` en modo interactivo:
```python
./peepdf.py  -f ../salud.pdf -i
```
Y devuelve:
```python
File: salud.pdf
MD5: e639fca504182dc5cb383cc455d30c21
SHA1: 2c29f4a20e4e0b6a3c10decbfacced991e59ad79
SHA256: 9a4d3d48f060d1fa29fe9cb5e7a435643586e9871e62254839daf3fd87e45506
Size: 57611 bytes
Version: 1.3
Binary: True
Linearized: False
Encrypted: False
Updates: 0
Objects: 34
Streams: 7
Comments: 0
Errors: 0

Version 0:
 Catalog: 1
 Info: 2
 Objects (34): [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
 Streams (7): [10, 33, 32, 5, 15, 21, 27]
  Encoded (7): [10, 33, 32, 5, 15, 21, 27]
```
El comando tree devuelve la estructura lógica del archivo:
```python
PPDF> tree

/Catalog (1)
 /Pages (3)
  /Page (4)
   /Pages (3)
   stream (5)
    integer (6)
    Unknown (0)
    /Catalog (1)
   /R10 (12)
    stream (10)
   /R7 (11)
    /ExtGState (7)
   /R8 (13)
    /Font (8)
     /Encoding (34)
     /FontDescriptor (9)
      stream (32)
     stream (33)
  /Page (14)
   /Pages (3)
   stream (15)
    integer (16)
    Unknown (0)
    /Catalog (1)
   /R10 (18)
    stream (10)
   /R7 (17)
    /ExtGState (7)
   /R8 (19)
    /Font (8)
  /Page (20)
   /Pages (3)
   stream (21)
    integer (22)
    Unknown (0)
    /Catalog (1)
   /R10 (24)
    stream (10)
   /R7 (23)
    /ExtGState (7)
   /R8 (25)
    /Font (8)
  /Page (26)
   /Pages (3)
   stream (27)
    integer (28)
    Unknown (0)
    /Catalog (1)
   /R10 (30)
    stream (10)
   /R7 (29)
    /ExtGState (7)
   /R8 (31)
    /Font (8)
/Info (2)
```

Para ver la estructura física se usa el comando `offsets`:
```python
PPDF> offsets

       0 Header
      15
        Object  5 (8865)
    8879
    8881
        Object  6 (19)
    8899
    8901
        Object  15 (9005)
   17905
   17907
        Object  16 (20)
   17926
   17928
        Object  21 (8618)
   26545
   26547
        Object  22 (20)
   26566
   26568
        Object  27 (6554)
   33121
   33123
        Object  28 (20)
   33142
   33144
        Object  4 (189)
   33332
   33334
        Object  14 (191)
   33524
   33526
        Object  20 (191)
   33716
   33718
        Object  26 (191)
   33908
   33910
        Object  3 (88)
   33997
   33999
        Object  1 (47)
   34045
   34047
        Object  7 (40)
   34086
   34088
        Object  11 (29)
   34116
   34118
        Object  12 (31)
   34148
   34150
        Object  10 (4140)
   38289
   38291
        Object  13 (29)
   38319
   38321
        Object  17 (29)
   38349
   38351
        Object  18 (31)
   38381
   38383
        Object  19 (29)
   38411
   38413
        Object  23 (29)
   38441
   38443
        Object  24 (31)
   38473
   38475
        Object  25 (29)
   38503
   38505
        Object  29 (29)
   38533
   38535
        Object  30 (31)
   38565
   38567
        Object  31 (29)
   38595
   38597
        Object  33 (614)
   39210
   39212
        Object  8 (436)
   39647
   39649
        Object  34 (408)
   40056
   40058
        Object  9 (204)
   40261
   40263
        Object  32 (16249)
   56511
   56513
        Object  2 (243)
   56755
   56757
        Xref Section (709)
   57465
   57467
        Trailer (138)
   57604
   57605 EOF
```
Para ver el metadato del pdf se ejecuta metadata:
```python
PPDF> metadata

Info Object in version 0:

<< /ModDate D:20140908210848+04'-30'
/CreationDate D:20140908210848+04'-30'
/Producer Nitro PDF PrimoPDF
/Title LIQUIDACIONES DEL 1 ENERO AL 5 DE SEPTIEMBRE 2014.xls
/Creator PrimoPDF http://www.primopdf.com
/Author lrojas >>
```
La fecha de creación del archivo es 09-08-2014 y la hora es 21:08:48  hora de Venezuela. El título del archivo Liquidaciones del 1 enero al 5 de septiembre de 2014, ah, es un archivo xls de excel. Y usaron primopdf para generar el pdf, por último el autor del pdf es lrojas.

Si se quiere revisar el objeto 2:
```python
PPDF> object 2

<< /ModDate D:20140908210848+04'-30'
/CreationDate D:20140908210848+04'-30'
/Producer Nitro PDF PrimoPDF
/Title LIQUIDACIONES DEL 1 ENERO AL 5 DE SEPTIEMBRE 2014.xls
/Creator PrimoPDF http://www.primopdf.com
/Author lrojas >>
```
Es el que contiene la información de los metadatos.

Revisando el objeto 15 se obtiene:
```
432 1739.33 3991 6 re
f
432 1642.33 3991 6 re
f
432 1545.33 3991 6 re
f
432 1448.33 3991 6 re
f
432 1351.33 3991 6 re
f
432 1254.33 3991 6 re
f
432 1157.33 3991 6 re
f
432 1060.33 3991 6 re
f
432 963.332 3991 6 re
f
432 866.332 3991 6 re
f
432 769.332 3991 6 re
f
432 672.332 3991 6 re
```
O usando `rawstream`:
```
rawstream 15
50 9f fa 71 0f 29 76 8a bc 44 3e dd c6 15 84 9e   öP..q.)v..D>.....ö
4c 89 76 f6 75 8c 3d 23 65 11 fb 65 48 d1 0e a1   öL.v.u.=#e..eH...ö
37 f6 08 d3 b6 f8 d2 17 15 4a 76 29 b0 04 86 e1   ö7........Jv)....ö
b4 9e 9b 3a 34 e7 d1 ce 91 9a c9 c0 91 9e cc 6c   ö...:4..........lö
4a 5d 24 67 c7 aa 21 fe 2c ea e6 ea 9e 8d 95 33   öJÅ$g..!.,......3ö
61 e5 55 2c 13 3c cd 61 21 d1 26 03 47 ba 32 b3   öa.U,.<.a!.&.G.2.ö
09 da cc ce 8e da e4 61 a1 85 34 d6 ba 00 63 5c   ö.......a..4...cÖö
08 f1 63 34 7a 90 44 cb 79 4d 95 50 58 6c e7 55   ö..c4z.D.yM.PXl.Uö
74 d4 da fb 44 4c 8a 48 a8 ae 41 42 b1 e5 44 a8   öt...DL.H..AB..D.ö
e9 bb 42 bb 47 28 3b cd 5e 22 0f 5d 3b 42 e8 d9   ö..B.G(;.Ü".Å;B..ö
e4 68 93 af 5f ec 99 50 8b d8 7f 03 08 05 8b 04   ö.h.._..P......ö
f5 a3 48 d5 bc 7b 7d 97 33 80 d8 c6 f6 85 57 90   ö..H..äå.3.....W.ö
4b 6a 8c 50 15 17 e4 e2 3a ca ce 7e 55 46 e4 5a   öKj.P....:..üUF.Zö
d4 d9 d5 eb 7d 70 a0 fb d6 a0 98 7d 3e 8f d9 72   ö....åp.....å>..rö
12 6d 08 55 71 41 2e 79 12 93 b3 9f 36 d4 72 5a   ö.m.UqA.y....6.rZö
68 a3 40 78 6b 9a 72 79 8c e9 6e 67 6c b9 cb ce   öh.@xk.ry..ngl...ö
9a 4b 4d ec f8 02 e7 f3 3e fa f8 f8 cd 2f 6e 7e   ö.KM.....>..../nüö
79 d3 c5 a0 96 4f 37 9d f1 46 3b 8e ea 1b 4d 13   öy....O7..F;...M.ö
7a fd 8d c9 ae fb 3e 4d 16 4c 7d e1 e9 63 a1 bc   öz.....>M.Lå..c..ö
eb 47 b5 bc 1d a2 5a de 0c ad 5a 5e 0f 83 5a 1e   ö.G....Z...ZÜ..Z.ö
c7 a0 96 d3 21 d8 ab 72 3a 16 77 5d 9e 4f a7 3c   ö....!..r:.wÅ.O.<ö
2f 2f 07 c1 ad ca e9 64 a7 55 39 9d eb b2 2a a7   ö//.....d.U9...*.ö
d3 1c 56 e5 b4 01 fb aa 9c 36 37 5e 95 d3 fe 9c   ö..V......67Ü....ö
ab 72 da b9 6e 55 4e fb 48 ad ca 69 57 96 f3 f2   ö.r..nUN.H..iW...ö
b2 af c0 aa 9c d6 e9 ae ca 69 85 dd aa 9c 96 b5   ö.........i......ö
ac ca 29 b9 7c 55 4e f9 9b ab 72 ca c2 5a 95 53   ö..).öUN...r..Z.Sö
8e c2 aa 9c a6 b4 56 e5 34 5a 7b 5e 5e 06 75 ce   ö......V.4ZäÜÜ.u.ö
cb 4b 1f ec bc bc b4 8d ce cb 0b 79 b0 fc 47 37   ö.K.........y..G7ö
ff 07 29 f1 43 c1                                 ö..).C.ö
```

Uno de los problemas de analizar pdf generados en la APN en Venezuela es que no lo generan a partir de la información que manejan directamente de las bases de datos, si no que usan una hoja de cálculo en este caso en windows y la de Microsoft Office, y generan el pdf con herramientas para windows.

¿Será autentica la información que tiene el pdf luego de manipulación con varias herramientas?

En siguientes post seguiré probando distintas herramientas en Python para ver si logro hacer un pdfscraping decente del pdf de Cencoex.


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
