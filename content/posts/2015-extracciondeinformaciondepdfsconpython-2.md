Title: Extracción de información de PDFs con python (parte 2).
Date: 2015-08-30 9:00
Category: Tutorial Python
Tags: Debian,General,Python,pdf scraping
lang: es
translation: true

En el primer artículo de la serie se explicó el uso de [peepdf](https://www.seraph.to/extraccion-de-informacion-de-pdfs-con-python-parte-1.html#extraccion-de-informacion-de-pdfs-con-python-parte-1), en este caso se utilizará [pdfminer](http://www.unixuser.org/~euske/python/pdfminer/index.html).

En el siguiente enlace consiguen un tutorial de como [usarlo](http://www.unixuser.org/~euske/python/pdfminer/programming.html), u [otro](https://www.binpress.com/manipulate-pdf-python/), y [otro más](https://quantcorner.wordpress.com/2014/03/16/parsing-pdf-files-with-python-and-pdfminer/).

El archivo a analizar será el mismo del artículo anterior el cual es un archivo de la página de [CENCOEX del área de salud](http://www.cencoex.gob.ve/images/stories/pdfs/estadisticas/Salud.pdf) .

En la siguiente figura se muestra el archivo `salud.pdf` donde el archivo tiene 4 páginas de una tabla con 4 columnas, No., Empresa, RIF y total asignado en Bsf.

![](./images/extracciondeinformaciondepdfsconpython2-1.png)

Para instalar `pypdf2` para Debian se usará `apt-get`:
```
apt-get install pdfminer-data python-pdfminer
```
Para `pip` de la siguiente forma:
```
pip install pdfminer
```

A continuación se muestra el código del script que se utilizará para extraer los datos:
```python
#!/usr/bin/env python

# -*- coding: utf-8 -*-



#Se importa los modulos necesarios de pdfminer



from pdfminer.pdfparser import PDFParser

from pdfminer.pdfdocument import PDFDocument

from cStringIO import StringIO

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter

from pdfminer.converter import TextConverter

from pdfminer.layout import LAParams

from pdfminer.pdfpage import PDFPage







def convertir(archivo, paginas=None):

    #Si no se le pasa el numero de paginas se inicializa pagenums si no se le pasa

    #a pagenums el numero de paginas.

    if not paginas:

        pagenums = set()

    else:

        pagenums = set(paginas)



    #Se define la salida

    output = StringIO()

    #Se crea la instancia del manejador

    manager = PDFResourceManager()

    #se instancia el conversor de texto donde se le pasa el manejador y la salida

    converter = TextConverter(manager, output, laparams=LAParams())

    #Se instancia el interprete pasando el manejador y el conversor

    interpreter = PDFPageInterpreter(manager, converter)



    #Se abre el archivo de entrada

    infile = file(archivo, 'rb')

    #Se crea un ciclo pasando el archivo de entrada y el numero de paginas.

    for page in PDFPage.get_pages(infile, pagenums):

        #Se procesa cada pagina

        interpreter.process_page(page)

    #Se cierra el archivo de entrada

    infile.close()

    #Se cierra el conversor

    converter.close()

    #Se obtiene los valores de la salida en texto

    texto = output.getvalue()

    #Se cierra la salida

    output.close

    #Se devuelve el texto

    return texto





if __name__ == "__main__":



    print convertir("salud.pdf")

```

Al ejecutar el script se obtiene lo siguiente ( a continuación se muestra la salida final):

```python
...
...
J-314931326
J-306044434
J-306652809
J-000273170
J-294885756
J-315368676
J-000276099
J-309260006
J-000068607
J-307695226
J-000886440
J-075558855
J-000298327
J-000440581
J-075265092
J-308718840

TOTAL

924.611,13
4.551.099,39
6.210.501,67
2.727.618,90
15.237.285,96
24.726.553,87
8.012.224,42
12.415.583,66
1.242.072,56
843.053,00
422.464,13
827.852,61
2.120.640,06
39.935.357,41
64.414.559,56
1.585.616,34
1.926.786,95
1.171.948,02
15.803.447,35
3.876.885,14
3.876.885,14
14.222.393,78
13.859.953,87
1.856.410,99
5.572.194,16
2.858.560,62
1.226.368,54
426.087,02
8.577.657,04
3.244.765,25
7.291.129,73
7.514.239,65
7.146.119,95
105.741.558,37
1.607.871,72
160.091.223,81
78.578.774,12
796.193,32
1.450.824,00
1.643.440,45
765.726,00
900.903,00
26.500,00
880.332,50
2.140.900,16
6.768.878,02
105.909.664,86
3.227.153,04
22.673.390,14
112.625,66
1.288.555,83
115.943.301,02
17.886.755,85
1.508.591,35


IMPORTACIONES TOTALES (ORDINARIAS + ALADI + SUCRE)

DISTRIBUCIÓN POR EMPRESAS AGREMIADAS DEL SECTOR SALUD

PERÍODO DE REFERENCIA: 01/01/2014 AL 05/09/2014

EMPRESA

Nº
163 RENTA MEDICA PC CA
164 REPRECLIN  LAB  C.A.
165 REPRESENTACIONES AITOR C.A.
166 REPRESENTACIONES DE LABORATORIO WEISS C.A.
167 REPRESENTACIONES LABIN-VE, S.A.
168 REPRESENTACIONES LUFRAN C.A.
169 REPRESENTACIONES MEDICAS YOMA CA
170 REPRESENTACIONES NOLVER C.A.
171 REPRESENTACIONES VARGAS C.A.
172 RESPITEC EQUIPOS MEDICOS C.A.
173 SANIFARMA PAÑALEX C.A
174 SANOFI-AVENTIS DE VENEZUELA S.A.
175 SEIJIRO YAZAWA IWAI C.A.
176 SERVIMEDIC SOLUCIONES CARDIOVASCULARES S.A.
177 SICA FARM DE VENEZUELA C.A
178 SINO PRODUCTS PAN AMERICAN SUPPLYC.A
179 SM PHARMA C.A.
180 SOLUCIONES ELECTRONICAS Y MEDICAS C.A.
181 SUMINISTROS BAIKOR CA
182 SUMINISTROS FOTOGRAFICOS Y MEDICOS SUFOMECA C.A. SUFOMECA
182 SUMINISTROS FOTOGRAFICOS Y MEDICOS SUFOMECA C.A. SUFOMECA
183 SUMINISTROS MEDICOS JAYOR C.A
184 SUMINISTROS MÉDICOS MULTIMÉDICA DMR C.A
185 SUMINISTROS RADI SURADI C.A.
186 SUPLIDORA HOSPIMED 2004 C.A
187 SURGILAP EQUIPOS C.A.
188 SYSMED EQUIPOS MEDICOS C.A.
189 TECNOLOGIA CLINICA CARDIOPULSO C.A.
190 TECNOLOGIA DOS C.A.
191 TECNOLOGIA MEDICA DEL CARIBE C.A.
192 TECNOMED J TRAPP C.A.
193 ULTRA CARE MEDICAL C.A.
194 WEST PHARMACEUTICAL SERVICES VENEZUELA C.A.
195 ZUOZ PHARMA S.A.

TOTAL GENERAL

RIF

J-306068848
J-002678143
J-308916064
J-000790078
J-003285536
J-001582738
J-001905545
J-003243906
J-002285540
J-300855775
J-002185449
J-303088481
J-000717184
J-306080740
J-306338438
J-303391923
J-070131390
J-303539661
J-312802316
J-001457810
J-001457810
J-003530255
J-303120784
J-003143324
J-300511529
J-302742463
J-308785539
J-306449191
J-304998074
J-001832726
J-000036071
J-310620440
J-002594160
J-002015080

TOTAL

4.310,96
5.676.457,12
205.152,00
6.221.734,67
4.270.788,35
1.954.333,42
1.996.335,62
51.816.733,75
5.653.885,98
58.431,62
410.002,29
103.980.350,21
3.252.208,70
2.382.957,73
212.924,97
171.935,94
27.281.496,00
572.896,00
492.918,00
3.033.050,09
3.033.050,09
12.005.888,05
1.313.993,48
9.298.817,31
4.714.939,88
1.085.603,86
1.190.975,38
831.945,94
271.105,08
2.048.621,93
1.900.646,66
1.151.336,80
2.011.181,88
22.706.399,72
2.237.473.782,31

```
NOTA: Las cifras de las modalidades de importacion ALADI y SUCRE se encuentran hasta el 31-08-2014


Como se nota, la información viene de manera inconsistente, tocaría trabajar el texto para ordenarlo (para próximo artículo).

Tomemos la empresa con el número 163. Es la empresa: Renta Médica PC, C.A., RIF: J-306068848 y le asignaron 4.310,96 (como lo muestra los campos del resultado subrayados y en italica y la figura a continuación).

![](./images/extracciondeinformaciondepdfsconpython2-2.png)

Ya se va obteniendo información útil. Sólo queda ordenarla un poco (siguiente artículo), aparte revisar otras herramientas. Los datos en un futuro se almacenarán en una base de datos `sqlite` o `mongodb` para crear un API Rest ful con Python (próximos artículos) de manera de mostrar la forma como debería visualizarse información de las instituciones para Datos Abiertos (OpenData).

Como ven extraer los datos no es difícil, lo complicado es que el archivo no tiene consistencia para manejarlo de manera fácil.


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
