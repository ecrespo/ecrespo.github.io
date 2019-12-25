Title: Árbol de decisión hecho en Python 
Date: 2017-11-19 09:00
Category: Tutorial Python
Tags: General,Debian,Python,Machine Learning,Scikit-Learn
lang: es
translation: true

Tenía algo de tiempo sin escribir (la situación en Venezuela no está facil).

Voy a ir retomando poco a poco los artículos en el blog,  tengo algunas cosas sobre Inteligencia Artificial (Redes Neuronales, Lógica Difusa, machine learning y deep learning), patrones de diseño con Python.

Este artículo trata de un modeo de predicción llamado árbol de decisión, según [wikipedia es](https://es.wikipedia.org/wiki/%C3%81rbol_de_decisi%C3%B3n): Es un modelo de predicción utilizado en diversos ámbitos que van desde la inteligencia artificial hasta la economía. Dado un conjunto de datos se fabrican diagramas de construcciones lógicas, muy similares a los sistemas de predicción basados en reglas, que sirven para representar y categorizar una serie de condiciones que ocurren de forma sucesiva, para la resolución de un problema.

En youtube hay un canal dedicado a la ciencia de datos principalmente con Python, el youtuber es [Siraj Raval](https://www.youtube.com/channel/UCWN3xxRkmTPmbKwht9FuE5A) . En el siguiente vídeo explica como hacer un clasificador de género hecho con un Árbol de decisión, el vídeo lo pueden ver en el siguiente [enlace](https://www.youtube.com/watch?v=T5pRlIbr6gg).

<iframe width="560" height="315" src="https://www.youtube.com/embed/T5pRlIbr6gg" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


El código fuente del ejercicio del vídeo se puede ver en [github](https://github.com/llSourcell/gender_classification_challenge/blob/master/demo.py).

La idea es tener los datos de altura, peso y talla de zapato y si es hombre o mujer, se construye el árbol de decisión, se pasa los datos y de ahí al pasar otro dato se genera una salida de si es hombre o mujer.

A continuación el código:

```python


#!/usr/bin/env python

"""

https://www.youtube.com/watch?v=T5pRlIbr6gg

https://github.com/llSourcell/gender_classification_challenge/blob/master/demo.py



"""

#Se importa la librería sklearn el módulo tre

from sklearn import tree



#Se crea la instancia del árbol de decisión.

clf = tree.DecisionTreeClassifier()



#[altura, peso, talla de zapato]

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],

     [190, 90, 47], [175, 64, 39],

     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]



#La salida donde se dice si es hombre o mujer

Y = ['hombre', 'hombre', 'mujer', 'mujer', 'hombre', 'hombre', 'mujer', 'mujer',

     'mujer', 'hombre', 'hombre']



#Se le pasa los datos  X y Y

clf = clf.fit(X, Y)



#Se definen los datos 1 y 2

dato1 = [190, 70, 43]

dato2 = [185, 62, 37]

prediction = clf.predict([dato1])

#Se muestra el resultado de la predicción de dato1

print(prediction)



prediction = clf.predict([dato2])


#Se muestra el resultado de la predicción de dato 2
print(prediction)
```

Al ejecutar el script se tiene:
```python
python3 arboldecision.py 
['hombre']
['mujer']
```

Significa que, para una altura de 1.90 mts, peso 70 kilograms, y talla de 43, el resultado es que es un hombre, y para altura de 1.85 mts, peso 62 kilogramos y talla de 37, el resultado es que es una mujer.

Recomiendo ver el vídeo completo para tener una mejor explicación del funcionamiento del árbol de decisión. 

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
