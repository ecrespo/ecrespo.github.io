Title: Algoritmo de Clasificación con scikit-learn  
Date: 2018-04-21 09:00  
Category: Tutorial Python  
Tags: Python,Scikit-learn,Inteligencia Artificial,Machine Learning
lang: es  
translation: true


Continuando con los artículos sobre Inteligencia Artificial con Python.

La serie de artículos sobre Scikit-Learn han sido:

1. [Árbol de decisión hecho con Python](https://www.seraph.to/arbol-de-decision-hecho-en-python.html) (esté tendrá una segunda parte).  
2. [Una red neuronal para aprendizaje supervisado usando scikit-learn](https://www.seraph.to/una-red-neuronal-para-aprendizaje-supervisado-usando-scikit-learn.html).  
3. [Funciones de activación para un perceptron](https://www.seraph.to/funciones-de-activacion-para-un-perceptron.html).  


El ejercicio que se explicará será el de algoritmo de clasificación usando scikit-learn por medio del ejemplo de la resolución de la tabla de la verdad de un Or exclusivo (XOR).

[Scikit-learn](http://scikit-learn.org/) es una librería de Machine Learning para Python que soporta algoritmos de clasificación, regresión y clustering ([wikipedia](https://en.wikipedia.org/wiki/Scikit-learn)).

A continuación el notebook de jupyter:

#### Se creará una red neuronal para clasificación
Se usará la tabla de la verdad de XOR
x	y	Salida
0	0	0	
0	1	1	
1	0	1	
1	1	0	

Para instalar `scikit-learn` se usa `pip`
```python
pip3 install scikit-learn
```
In [4]:
```python
##Se importa Numpy, MLPCCLassifier y KNeighborsClassifier
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
```
In [5]:
```python
#un Arreglo con la tabla de la verdad
# 0 0
# 0 1
# 1 0
# 1 1
xs = np.array([
    0, 0,
    0, 1,
    1, 0,
    1, 1
]).reshape(4, 2)
xs
```
Out[5]:
```python
array([[0, 0],
       [0, 1],
       [1, 0],
       [1, 1]])
```
In [6]:
```python
#Se muestra un arreglo con el resultado de hacer un XOR
ys = np.array([0, 1, 1, 0]).reshape(4,)
ys
```
Out[6]:
```python
array([0, 1, 1, 0])
```
In [7]:
```python
#Se crea el clasificador con la función de activación relu,con 10k iteraciones y tiene capaz ocultas 4,2
model = MLPClassifier(activation='tanh', max_iter=10000, hidden_layer_sizes=(4,2))
model
```
Out[7]:
```python
MLPClassifier(activation='tanh', alpha=0.0001, batch_size='auto', beta_1=0.9,
       beta_2=0.999, early_stopping=False, epsilon=1e-08,
       hidden_layer_sizes=(4, 2), learning_rate='constant',
       learning_rate_init=0.001, max_iter=10000, momentum=0.9,
       nesterovs_momentum=True, power_t=0.5, random_state=None,
       shuffle=True, solver='adam', tol=0.0001, validation_fraction=0.1,
       verbose=False, warm_start=False)
```
In [8]:
```python
#Se entrena la red neuronal pasando los arreglos de entrada y de salida
model.fit(xs, ys)
```
Out[8]:
```python
MLPClassifier(activation='tanh', alpha=0.0001, batch_size='auto', beta_1=0.9,
       beta_2=0.999, early_stopping=False, epsilon=1e-08,
       hidden_layer_sizes=(4, 2), learning_rate='constant',
       learning_rate_init=0.001, max_iter=10000, momentum=0.9,
       nesterovs_momentum=True, power_t=0.5, random_state=None,
       shuffle=True, solver='adam', tol=0.0001, validation_fraction=0.1,
       verbose=False, warm_start=False)
```
In [9]:
```python
print('prediccion:', model.predict(xs)) # salida 0110
prediccion: [0 1 1 0]
```
In [10]:
```python
print('Se espera:', np.array([0, 1, 1, 0]))
Se espera: [0 1 1 0]
```
Otro ejercicio
Entrada	Salida
001	0	
111	1	
101	1	
011	0	
100	?	

In [11]:
```python
#Se importa de numpy array
from numpy import array
```
In [12]:
```python
#Datos de entrada y de salida
datos_entrada = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]]).reshape(4, 3)
datos_salida = array([[0, 1, 1, 0]]).reshape(4, )
print(datos_entrada)
print ("-"*4)
print(datos_salida)
[[0 0 1]
 [1 1 1]
 [1 0 1]
 [0 1 1]]
----
[0 1 1 0]
```
In [13]:
```python
#En este caso se usa KNeighborsClassifier con 2 capaz
KNC = KNeighborsClassifier(n_neighbors= 2)
```
In [14]:
```python
KNC.fit(datos_entrada,datos_salida)
```
Out[14]:
```python
KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
           metric_params=None, n_jobs=1, n_neighbors=2, p=2,
           weights='uniform')
```
In [15]:
```python
#Se predice el valor de 1,0,0 que da como resultado el mismo del artículo anterior.
print(KNC.predict([[1, 0,0]]))
[1]
```
In [16]:
```python
#Se crea la red de nuevo pero ahora con PLPCCLassifier.
#Se crea el clasificador con la función de activación relu,con 10k iteraciones y tiene capaz ocultas 4,2
KNC = MLPClassifier(activation='tanh', max_iter=10000, hidden_layer_sizes=(4,2))
```
In [17]:
```python
#Se entrena la red neuronal pasando los arreglos de entrada y de salida
KNC.fit(datos_entrada, datos_salida)
```
Out[17]:
```python
MLPClassifier(activation='tanh', alpha=0.0001, batch_size='auto', beta_1=0.9,
       beta_2=0.999, early_stopping=False, epsilon=1e-08,
       hidden_layer_sizes=(4, 2), learning_rate='constant',
       learning_rate_init=0.001, max_iter=10000, momentum=0.9,
       nesterovs_momentum=True, power_t=0.5, random_state=None,
       shuffle=True, solver='adam', tol=0.0001, validation_fraction=0.1,
       verbose=False, warm_start=False)
```
In [18]:
```python
#Se predice el valor de 1,0,0 que da como resultado el mismo del artículo anterior.
print(KNC.predict([[1, 0,0]]))
[1]
```

En el siguiente artículo se explicará otro ejemplo de Árbol de decisión usando scikit-learn.

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)


