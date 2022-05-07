Title: PDF Scraping para Pandas usando tabula-py  
Date: 2018-04-15 07:00  
Category: Tutorial Python  
Tags: Python,pwd scraping,Pandas
lang: es  
translation: true  

Hace un tiempo quería hacer pruebas de extracción de datos de PDF que publica la Administración Pública en Venezuela, ya que el concepto de Datos Abiertos no está muy claro por acá, lo más que se logra son documentos en PDF donde pegan gráficas y tablas como capturas de pantalla.

[Artículos sobre webscraping.](https://www.seraph.to/tag/pdf-scraping.html)

Por cierto, existe un evento del día de los datos abiertos. Ese día fue el 3 de Marzo en este año. si le dan click al [mapa](https://opendataday.org/es_es/#map), aparece la lista de eventos de ese día por países.


Este artículo se basa en un artículo en inglés publicado en [Medium sobre tabula-py](https://blog.chezo.uno/tabula-py-extract-table-from-pdf-into-python-dataframe-6c7acfa5f302).

Para el caso de Venezuela, no aparece en la lista de eventos de la fecha del 3 de Marzo.


[![](./images/pdfscrapingparapandasusandotabulapy-1.png)](https://1.bp.blogspot.com/-_Hea6roASQo/WtPsQEi6JiI/AAAAAAAASl4/-0UBdnMlWhgB47bd2rKFHTYpELNMJwLWgCLcBGAs/s320/dia-datosabiertos-suramerica.png)


Alianza para el gobierno Abierto.

[https://youtu.be/QbGDoV_HoFY](https://youtu.be/QbGDoV_HoFY "https://youtu.be/QbGDoV_HoFY")

<iframe width="560" height="315" src="https://www.youtube.com/embed/QbGDoV_HoFY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Iniciativas de sitios de Datos Abiertos.

[https://youtu.be/oh3g-iYAaDo](https://youtu.be/oh3g-iYAaDo "https://youtu.be/oh3g-iYAaDo")

<iframe width="560" height="315" src="https://www.youtube.com/embed/oh3g-iYAaDo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Que tal que pueda hacer un scrapping y de una usar [Pandas](https://www.seraph.to/tag/pandas.html) ([Introducción a pandas](https://www.seraph.to/introduccion-a-pandas.html)) para Ciencia de Datos.

Existe una librería para Python llamada [tabula-py](https://github.com/chezou/tabula-py/tree/master/examples), en el github de tabula-py se encuentra un archivo llamado [data.pdf](https://github.com/chezou/tabula-py/blob/master/examples/data.pdf), ese será el archivo pdf que se va a extraer la información.


Para usar `tabula-py` se puede instalar vía `pip`:
```python
pip install tabula-py
```
A continuación se muestra en `jupyter` como usar `tabula-py`:

In [1]:
```python
#Se importa read_pdf de tabula
from tabula import read_pdf
```
In [2]:
```python
#Se lee el archivo data.pdf y se muestra el encabezado del dataframe
df = read_pdf('./Data/data.pdf')
df.head()
```
Out[2]:

| ID | Unnamed: 0        | mpg  | cyl  | disp  | hp    | drat |  wt   | qsec  | vs    | am | gear | carb |
| :- | :--------------:  | :--: | :--  | :--:  | :---: | :-   | :----:| :---: |:-----:|:--:|:----:|:----:|
| 0	 | Mazda RX4         | 21.0 | 6	   | 160.0 | 110   | 3.90 | 2.620 | 16.46 | 0	  | 1  | 4    |	4    |
| 1	 | Mazda RX4 Wag     | 21.0 | 6	   | 160.0 | 110   | 3.90 |	2.875 |	17.02 |	0	  | 1  | 4	  | 4    |
| 2	 | Datsun 710        | 22.8 | 4	   | 108.0 | 93	   | 3.85 |	2.320 |	18.61 |	1     | 1  | 4    |	1    |
| 3	 | Hornet 4 Drive    | 21.4 | 6    | 258.0 | 110   | 3.08 |	3.215 |	19.44 |	1	  | 0  | 3    |	1    |
| 4	 | Hornet Sportabout | 18.7	| 8	   | 360.0 | 175   | 3.15 |	3.440 |	17.02 |	0     | 0  | 3    |	2    |

In [3]:
```python
#También se puede mostrar los datos en formato json
js = read_pdf('./Data/data.pdf',output_format='json')
```
In [4]:
```python
#También se puede guardar un archivo en JSON, CSV,TSV
from tabula import convert_into
convert_into('./Data/data.pdf',"./Data/data.json",output_format='json')
#!cat ./Data/data.json
```
In [5]:
```python
convert_into('./Data/data.pdf',"./Data/data.tsv",output_format='tsv')
#!cat ./Data/data.tsv
```
In [6]:
```python
convert_into('./Data/data.pdf',"./Data/data.csv",output_format='csv')
#!cat ./Data/data.csv
```

A continuación se muestra la figura del editor que muestra data.csv:

![](./images/pdfscrapingparapandasusandotabulapy-2.png)


Ahora se muestra el contenido del archivo data.tsv:

![](./images/pdfscrapingparapandasusandotabulapy-3.png)


Al tener los datos en un dataframe se puede realizar toda la analítica de datos que se puede hacer con Pandas.


								

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)

