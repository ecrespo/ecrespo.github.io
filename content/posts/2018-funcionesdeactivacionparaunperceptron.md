Title: Funciones de activación para un perceptron  
Date: 2018-02-13 09:00  
Category: Tutorial Python  
Tags: Scikit-learn,Python,Inteligencia Artificial,
lang: es  
translation: true  

En el artículo ([introducción al perceptron](https://www.seraph.to/introduccion-al-perceptron-con-python.html)), se muestra el perceptron con la función de activación que en la figura es una onda cuadrada, pero puede ser también otro tipo de función.

![](./images/funcionesdeactivacionparaunperceptron-1.png) 

En el artículo  ([construir una red neuronal en pocos minutos](https://www.seraph.to/construir-una-red-neuronal-en-pocos-minutos.html)), se muestra la función de activación llamada sigmoide.

![](./images/funcionesdeactivacionparaunperceptron-2.png) 

Y en el artículo ([Una red Neuronal para aprendizaje supervisado usando Scikit-learn](https://www.seraph.to/una-red-neuronal-para-aprendizaje-supervisado-usando-scikit-learn.html)) se usa la función tanh.

Scikit-learn para  multi-layer perceptron maneja varios tipos de funciones de activación ([documentación](http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html)) como lo son:

- identity: La función de activación es `f(x)=x`.
- logistic: La función de activación es la función sigmoide `f(x)=1/(1+exp(-x))`.
- tanh: La función de activación es la función tangente hiperbolico `f(x)=tanh(x)`.
- relu: La función de activación es función rectificada de recta unitaria `f(x)=max(0,x)`.

El código mostrará las distintas funciones y sus gráficas, luego se toma la red neuronal del artículo [Una red Neuronal para aprendizaje supervisado usando Scikit-learn](https://www.seraph.to/una-red-neuronal-para-aprendizaje-supervisado-usando-scikit-learn.html), usando distintas funciones de activación, se entrena a la neurona con cada función de activación y se busca predecir el resultado.

A continuación el código:

In [1]:
```python
#Se importa numpy y matplotlib
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline
```
In [2]:
```python
#Se define el rango de valores
z = np.linspace(-10,10,100)
```
In [3]:
```python
#Onda cuadrada
def cuadrada(z):
    return 1*(z>0)
```
In [4]:
```python
#Se calcula la onda cuadrada a partir del rango de valores
a = cuadrada(z)
```
In [5]:
```python
#Se gráfica la onda cuadrada
plt.plot(z,a)
```
Out[5]:
```python
[<matplotlib.lines.Line2D at 0x7f90ba52c278>]
```
![](./images/funcionesdeactivacionparaunperceptron-3.png) 

In [6]:
```python
#Se define la función Identidad
def identidad(z):
    return z
```
In [7]:
```python
#Se calcula la función identidad a partir del rango de valores
b = identidad(z)
```
In [8]:
```python
#Se gráfica.
plt.plot(z,b)
```
Out[8]:
```python
[<matplotlib.lines.Line2D at 0x7f90ba49e7f0>]
```
![](./images/funcionesdeactivacionparaunperceptron-4.png) 

In [9]:
```python
#Función ReLU
def ReLU(z):
    return z * (z > 0)
```
In [10]:
```python
#Se calcula la función ReLU a partir del rango de valores
c = ReLU(z)
```
In [11]:
```python
#Se gráfica la función
plt.plot(z,c)
```
Out[11]:
```python
[<matplotlib.lines.Line2D at 0x7f90ba46c6d8>]
```
![](./images/funcionesdeactivacionparaunperceptron-5.png) 

In [12]:
```python
#Función tangente hiperbolico
def tanh(z):
    return(np.exp(z)-np.exp(-z))/(np.exp(z)+np.exp(-z))
```
In [13]:
```python
#Se calcula la tangente hiperbolica a partir del rango de valores
d = tanh(z)
```
In [14]:
```python
#Se gráfica
plt.plot(z,d)
```
Out[14]:
```
[<matplotlib.lines.Line2D at 0x7f90ba42e550>]
```
![](./images/funcionesdeactivacionparaunperceptron-6.png) 

In [15]:
```python
#Función sigmoide
def sigmoide(z):
    return 1/(1+np.exp(-z))
```
In [16]:
```python
#Se calcula la sigmoide a partir del rango de valores
e = sigmoide(z)
```
In [17]:
```python
#Se gráfica la función
plt.plot(z,e)
```
Out[17]:
```python
[<matplotlib.lines.Line2D at 0x7f90ba3f0be0>]
```

![](./images/funcionesdeactivacionparaunperceptron-7.png) 

La diferencia entre las funciones de activación es lo suavizada o no de cada curva. Osea, que tan abrupta es su pendiente, o la derivada de la función.

A continuación se crea una red neuronal usando scikit-learn  

In [18]:
```python
#Se importa de la red neuronal MLPClassifier
from sklearn.neural_network import MLPClassifier
```
In [19]:
```python
#Se definen los datos de entrada
datos_entrada = np.array([
    0, 0,
    0, 1,
    1, 0,
    1, 1
]).reshape(4, 2)
```
In [20]:
```python
#Se definen los datos de salida
datos_salida = np.array([0, 1, 1, 0]).reshape(4,)
```
In [21]:
```python
#Se crea la red neuronal con función de activación relu y 100 mil iteraciones
model = MLPClassifier(activation='relu', max_iter=100000, hidden_layer_sizes=(4,2))
```
In [22]:
```python
#Se entrena a la red neuronal
model.fit(datos_entrada,datos_salida)
```
Out[22]:
```python
MLPClassifier(activation='relu', alpha=0.0001, batch_size='auto', beta_1=0.9,
       beta_2=0.999, early_stopping=False, epsilon=1e-08,
       hidden_layer_sizes=(4, 2), learning_rate='constant',
       learning_rate_init=0.001, max_iter=100000, momentum=0.9,
       nesterovs_momentum=True, power_t=0.5, random_state=None,
       shuffle=True, solver='adam', tol=0.0001, validation_fraction=0.1,
       verbose=False, warm_start=False)
```
In [23]:
```python
#Se hace la predicción
print('prediccion:', model.predict(datos_entrada))

prediccion: [0 1 0 1]
```
El resultado que devuelve la red neuronal debería ser [0,1,1,0] y devuelve [0,1,0,1] el cual es errado.
Se repite la construcción de la red neuronal, pero ahora usando la función de activación identity.

In [24]:
```python
model = MLPClassifier(activation='identity', max_iter=100000, hidden_layer_sizes=(4,2))
```
In [25]:
```python
#Se entrena a la red neuronal
model.fit(datos_entrada,datos_salida)
```
Out[25]:
```python
MLPClassifier(activation='identity', alpha=0.0001, batch_size='auto',
       beta_1=0.9, beta_2=0.999, early_stopping=False, epsilon=1e-08,
       hidden_layer_sizes=(4, 2), learning_rate='constant',
       learning_rate_init=0.001, max_iter=100000, momentum=0.9,
       nesterovs_momentum=True, power_t=0.5, random_state=None,
       shuffle=True, solver='adam', tol=0.0001, validation_fraction=0.1,
       verbose=False, warm_start=False)
```
In [26]:
```python
#Se hace la predicción
print('prediccion:', model.predict(datos_entrada))

prediccion: [0 0 0 0]
```
El resultado que devuelve la red neuronal debería ser [0,1,1,0] y devuelve [0,0,0,0] el cual es errado.
Se repite la construcción de la red neuronal, pero ahora usando la función de activación sigmoide (logistic).  

In [27]:
```python
model = MLPClassifier(activation='logistic', max_iter=100000, hidden_layer_sizes=(4,2))
```
In [28]:
```python
#Se entrena a la red neuronal
model.fit(datos_entrada,datos_salida)
```
Out[28]:
```python
MLPClassifier(activation='logistic', alpha=0.0001, batch_size='auto',
       beta_1=0.9, beta_2=0.999, early_stopping=False, epsilon=1e-08,
       hidden_layer_sizes=(4, 2), learning_rate='constant',
       learning_rate_init=0.001, max_iter=100000, momentum=0.9,
       nesterovs_momentum=True, power_t=0.5, random_state=None,
       shuffle=True, solver='adam', tol=0.0001, validation_fraction=0.1,
       verbose=False, warm_start=False)
```
In [29]:
```python
#Se hace la predicción
print('prediccion:', model.predict(datos_entrada))

prediccion: [1 1 1 1]
```
El resultado que devuelve la red neuronal debería ser [0,1,1,0] y devuelve [1,1,1,1] el cual es errado.
Se repite la construcción de la red neuronal, pero ahora usando la función de activación tanh.  

In [33]:
```python
model = MLPClassifier(activation='tanh', max_iter=100000, hidden_layer_sizes=(4,2))
```
In [34]:
```python
#Se entrena a la red neuronal
model.fit(datos_entrada,datos_salida)
```
Out[34]:
```python
MLPClassifier(activation='tanh', alpha=0.0001, batch_size='auto', beta_1=0.9,
       beta_2=0.999, early_stopping=False, epsilon=1e-08,
       hidden_layer_sizes=(4, 2), learning_rate='constant',
       learning_rate_init=0.001, max_iter=100000, momentum=0.9,
       nesterovs_momentum=True, power_t=0.5, random_state=None,
       shuffle=True, solver='adam', tol=0.0001, validation_fraction=0.1,
       verbose=False, warm_start=False)
```
In [35]:
```python
#Se hace la predicción
print('prediccion:', model.predict(datos_entrada))

prediccion: [0 1 1 0]
```
El resultado que devuelve la red neuronal debería ser [0,1,1,0] y devuelve [0,1,1,0] el cual es el resultado esperado. Esto demuestra que es muy importante seleccionar la función de activación correcta a la hora de definir una red neuronal y entrenarla.


##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
