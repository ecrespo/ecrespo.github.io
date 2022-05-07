Title:  Introducción a Pandas  
Date: 2018-01-07 16:00  
Category: Tutorial Python  
Tags: Ciencia de Datos,Python,Pandas,Data Science
lang: es  
translation: true

Pandas es una librería de python para analizar datos, permite multiples entrada de datos.

El artículo se basa en un artículo en inglés [Building a neural network with python](http://www.springboard.com/blog/beginners-guide-neural-network-in-python-scikit-learn-0-18/), y en un [tutorial de pandas](http://www.tutorialspoint.com/python_pandas/).

Para este tutorial se usará un conjunto de datos en formato csv  sobre vinos ([análisis químico para saber el origen de los vinos](http://archive.ics.uci.edu/ml/datasets/Wine)).

A continuación de describe paso a paso la forma de manejar los datos a partir del archivo [wine_data.csv](http://github.com/ecrespo/codigo_blog/blob/master/pandas/wine_data.csv).

El archivo [Pandas.py](http://github.com/ecrespo/codigo_blog/blob/master/pandas/Pandas.py) y el [Pandas.ipynb](http://github.com/ecrespo/codigo_blog/blob/master/pandas/Pandas.ipynb) lo pueden descargar de github.

Se importa `Pandas` como `pd`:
```python
>>> import pandas as pd
```
Se extraen los datos del archivo csv y se define el nombres de las columnas:
```python
>>> wine = pd.read_csv('wine_data.csv', names = ["Cultivator", "Alchol", "Malic_Acid", "Ash", "Alcalinity_of_Ash", "Magnesium", "Total_phenols", "Falvanoids", "Nonflavanoid_phenols", "Proanthocyanins", "Color_intensity", "Hue", "OD280", "Proline"])
```
Se muestran los primeros datos:
```python
>>> wine.head()
```
![](./images/introduccionapandas-1.png) 

Se muestran las dimensiones de la tabla:
```
>>> wine.shape
(178, 14)
```
Se tienen 178 filas y 14 columnas.

Se muestran las 2 primeras filas de la tabla:
```python
wine.loc[[0,1]]
```
![](./images/introduccionapandas-2.png) 

Se muestran las dos primeras filas y las columnas `Cultivator` y `Alchol`
```python
>>> wine.loc[[0,1]][["Cultivator","Alchol"]]
```
![](./images/introduccionapandas-3.png) 

Está introducción es necesaria ya que en futuros artículos se trabajará mucho con la librería `pandas`.


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
