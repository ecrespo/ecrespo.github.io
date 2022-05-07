Title: Una red Neuronal para aprendizaje supervisado usando Scikit-learn  
Date: 2018-02-12 11:00  
Category: Tutorial de Python  
Tags: Python,Numpy,Red Neuronal, Inteligencia Artificial, Scikit-learn
lang: es  
translation: true  

Continuando con los artículos sobre Redes Neuronales, en este caso se usará la librería Scikit-learn.

Lo primero es instalar `scikit-learn` en Linux con `pip`:
```python
pip3 install  scikit-learn
```

Se tendrán dos ejemplos, el primero es entrenar la red neuronal con la tabla de la verdad de XOR y ver que devuelve la red, el segundo ejercicio es tomando los datos del artículo anterior ([construir una red neuronal en pocos minutos](https://www.seraph.to/construir-una-red-neuronal-en-pocos-minutos.html)) y ver si se logra el mismo resultado.

La resolución de XOR se hará con el algoritmo de [K nearest neighbor algorithm](http://www.codeday.top/2017/10/15/50798.html) y también se usará [multi-layer perceptron Classifier](http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier) con backpropagation ([redes neuronales supervisadas](http://scikit-learn.org/stable/modules/neural_networks_supervised.html)).

###Se crea una red neuronal clasificador para evaluar la tabla de la verdad para XOR  

In [1]:
```python
#Se importa Numpy, MLPCCLassifier y KNeighborsClassifier
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
```
In [2]:
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
```
In [3]:
```python
# Se muestra el arreglo
xs
```
Out[3]:
```python
array([[0, 0],
       [0, 1],
       [1, 0],
       [1, 1]])
```
In [4]:
```python
#Se muestra un arreglo conel resultado de hacer un XOR
ys = np.array([0, 1, 1, 0]).reshape(4,)
```
In [5]:
```python
ys
```
Out[5]:
```python
array([0, 1, 1, 0])
```
In [6]:
```python
#Se crea el clasificador con la función de activación relu,con 10k iteraciones y tiene capaz ocultas 4,2
model = MLPClassifier(activation='tanh', max_iter=10000, hidden_layer_sizes=(4,2))
```
In [7]:
```python
#Se entrena la red neuronal pasando los arreglos de entrada y de salida
model.fit(xs, ys)
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
print('prediccion:', model.predict(xs)) # salida 0110

prediccion: [0 1 1 0]
```
In [9]:
```python
print('Se espera:', np.array([0, 1, 1, 0]))
```
Se espera: [0 1 1 0]

####Datos de entrada y salida del artículo anterior  
```
Entrada 	Salida
001 	0
111 	1
101 	1
011 	0
100 	?
```
In [10]:
```python
#Se importa de numpy array
from numpy import array
```
In [11]:
```python
#Datos de entrada y de salida
datos_entrada = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]]).reshape(4, 3)
datos_salida = array([[0, 1, 1, 0]]).reshape(4, )
```
In [12]:
```python
#En este caso se usa KNeighborsClassifier con 2 capaz
KNC = KNeighborsClassifier(n_neighbors= 2)
```
In [13]:
```python
KNC.fit(datos_entrada,datos_salida)
```
Out[13]:
```python
KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
           metric_params=None, n_jobs=1, n_neighbors=2, p=2,
           weights='uniform')
```
In [14]:
```python
#Se predice el valor de 1,0,0 que da como resultado el mismo del artículo anterior.
print(KNC.predict([[1, 0,0]]))

[1]
```
In [15]:
```python
#Se crea la red de nuevo pero ahora con PLPCCLassifier.
#Se crea el clasificador con la función de activación relu,con 10k iteraciones y tiene capaz ocultas 4,2
KNC = MLPClassifier(activation='tanh', max_iter=10000, hidden_layer_sizes=(4,2))
```
In [16]:
```python
#Se entrena la red neuronal pasando los arreglos de entrada y de salida
KNC.fit(datos_entrada, datos_salida)
```
Out[16]:
```python
MLPClassifier(activation='tanh', alpha=0.0001, batch_size='auto', beta_1=0.9,
       beta_2=0.999, early_stopping=False, epsilon=1e-08,
       hidden_layer_sizes=(4, 2), learning_rate='constant',
       learning_rate_init=0.001, max_iter=10000, momentum=0.9,
       nesterovs_momentum=True, power_t=0.5, random_state=None,
       shuffle=True, solver='adam', tol=0.0001, validation_fraction=0.1,
       verbose=False, warm_start=False)
```
In [17]:
```python
print(KNC.predict([[1, 0,0]]))

[1]
```

El resultado es el mismo usando dos tipos distintas de redes neuronales, para el caso del multi-layer perceptron se usó la función de activación tanh. 

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
