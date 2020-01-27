Title: Contar palabras de un texto usando Spark con PySpark  
Date: 2018-07-03 09:00  
Category: Tutorial Python  
Tags: Python, Spark, PySpark
lang: es  
translation: true 


En el artículo anterior se explicó el [procedimiento de instalación de Spark usando Docker](https://www.seraph.to/como-correr-apache-spark-desde-una-imagen-docker.html).  En este artículo se usará un texto tomado de la página de la ONU, de ahí se extrae las líneas y se cuentan las palabras.

A continuación el texto que se va a utilizar (lo pueden bajar desde el repositorio [gitlab](https://gitlab.com/mangoosta/articulos-cienciasdedatos/blob/master/datos/declaracion_onut.text)):

```
1942: La Declaración de las Naciones Unidas
Representantes de 26 Estados que lucharon contra las potencias del Eje Roma-Berlín-Tokio manifestaron su apoyo a la Carta del Atlántico mediante su firma de la « Declaración de las Naciones Unidas ». En este trascendental documento, los signatarios se comprometían a poner su máximo empeño en la guerra y a no firmar una paz por separado. 


Declaración de las Naciones Unidas prometiendo "emplear todos sus recursos, militares o económicos" en "la lucha por la victoria sobre el hitlerismo".
El día de año nuevo de 1942, el señor presidente Roosevelt y los señores Winston Churchill, Maxim Litvinov, de la Unión Soviética, y T. V. Soong, de China, firmaron un breve documento que luego se conocería como la Declaración de las Naciones Unidas. Al día siguiente se sumaron los representantes de otras 22 naciones más. En este trascendental documento, los signatarios se comprometían a poner su máximo empeño en la guerra y a no firmar una paz por separado.

La Declaración de las Naciones Unidas
La alianza completa a que se llegó en esta forma concordaba con los principios enunciados en la Carta del Atlántico, y la primera cláusula de la declaración de las Naciones Unidas reza que los países signatarios 

« . . . han suscrito un programa común de propósitos y principios enunciados en la declaración conjunta del presidente de los Estados Unidos de América y del primer ministro del Reino Unido de la Gran Bretaña e Irlanda del Norte, fechada el 14 de agosto de 1941, y conocida como la Carta del Atlántico. ».

Cuando tres años después se iniciaban los preparativos para la conferencia de San Francisco, únicamente se invitó a participar a aquellos estados que, en marzo de 1945, habían declarado la guerra a Alemania y al Japón y que habían firmado la Declaración de las Naciones Unidas.

Signatarios Originales de la Declaración de la ONU
Los 26 signatarios originales fueron: Los Estados Unidos de América, el Reino Unido de la Gran Bretaña e Irlanda del Norte, la Unión de Repúblicas Socialistas Soviéticas, China, Australia, Bélgica, Canadá, Costa Rica, Checoeslovaquia, El Salvador, Grecia, Guatemala, Haití, Honduras, India, Luxemburgo, Nicaragua, Noruega, Nueva Zelandia, Países Bajos, Panamá, Polonia, República Dominicana, Unión Sudafricana, Yugoeslavia .

Los firmantes posteriores
Más tarde se adhirieron a la Declaración los siguientes países (en el orden de las firmas): México, Colombia, Iraq, Irán, Liberia, Paraguay, Chile, Uruguay, Egipto, Siria, Francia, Filipinas, Brasil, Bolivia, Etiopía, Ecuador, Perú, Venezuela, Turquía, Arabia Saudita, Líbano.

```

A continuación se muestra la ejecución del código (si quieren bajar el archivo `jupyter notebook` lo pueden descargar desde [gitlab](https://gitlab.com/mangoosta/articulos-cienciasdedatos/blob/master/spark1.ipynb)):

In [1]:
```python
#Se importa SparkContext y SparkConf
from pyspark import SparkContext, SparkConf
```
In [2]:
```python
#Se crea la instancia de la configuración con el nombre de la aplicación contador
conf1 = SparkConf().setAppName("contador").setMaster("local[3]")
```
In [3]:
```python
#Se crea el contexto pasando la instancia de la configuración
sc = SparkContext(conf = conf1)
```
In [4]:
```python
#Se extrae las líneas del texto 
lineas = sc.textFile("data/declaracion_onut.text")
```
In [6]:
```python
#Se extrae las palabras del texto y se cuentan
contarPalabras = lineas.flatMap(lambda linea: linea.split(" ")).countByValue()
```
In [7]:
```python
#Se muestra las palabras con la cantidad de veces que tiene su aparición
for palabra, contador in contarPalabras.items():
    print("{} : {}".format(palabra, contador))
```

```
1942: : 1
La : 3
Declaración : 8
de : 29
las : 9
Naciones : 7
Unidas : 5
Representantes : 1
26 : 2
Estados : 3
que : 5
lucharon : 1
contra : 1
potencias : 1
del : 9
Eje : 1
Roma-Berlín-Tokio : 1
manifestaron : 1
su : 4
apoyo : 1
a : 10
la : 21
Carta : 3
Atlántico : 1
mediante : 1
firma : 1
« : 2
». : 2
En : 2
este : 2
trascendental : 2
documento, : 2
los : 9
signatarios : 4
se : 8
comprometían : 2
poner : 2
máximo : 2
empeño : 2
en : 7
guerra : 3
y : 10
no : 2
firmar : 2
una : 2
paz : 2
por : 3
separado. : 2
 : 9
prometiendo : 1
"emplear : 1
todos : 1
sus : 1
recursos, : 1
militares : 1
o : 1
económicos" : 1
"la : 1
lucha : 1
victoria : 1
sobre : 1
el : 5
hitlerismo". : 1
El : 2
día : 2
año : 1
nuevo : 1
1942, : 1
señor : 1
presidente : 2
Roosevelt : 1
señores : 1
Winston : 1
Churchill, : 1
Maxim : 1
Litvinov, : 1
Unión : 3
Soviética, : 1
T. : 1
V. : 1
Soong, : 1
China, : 2
firmaron : 1
un : 2
breve : 1
documento : 1
luego : 1
conocería : 1
como : 2
Unidas. : 2
Al : 1
siguiente : 1
sumaron : 1
representantes : 1
otras : 1
22 : 1
naciones : 1
más. : 1
alianza : 1
completa : 1
llegó : 1
esta : 1
forma : 1
concordaba : 1
con : 1
principios : 2
enunciados : 2
Atlántico, : 1
primera : 1
cláusula : 1
declaración : 2
reza : 1
países : 2
. : 4
han : 1
suscrito : 1
programa : 1
común : 1
propósitos : 1
conjunta : 1
Unidos : 2
América : 1
primer : 1
ministro : 1
Reino : 2
Unido : 2
Gran : 2
Bretaña : 2
e : 2
Irlanda : 2
Norte, : 2
fechada : 1
14 : 1
agosto : 1
1941, : 1
conocida : 1
Atlántico. : 1
Cuando : 1
tres : 1
años : 1
después : 1
iniciaban : 1
preparativos : 1
para : 1
conferencia : 1
San : 1
Francisco, : 1
únicamente : 1
invitó : 1
participar : 1
aquellos : 1
estados : 1
que, : 1
marzo : 1
1945, : 1
habían : 2
declarado : 1
Alemania : 1
al : 1
Japón : 1
firmado : 1
Signatarios : 1
Originales : 1
ONU : 1
Los : 3
originales : 1
fueron: : 1
América, : 1
Repúblicas : 1
Socialistas : 1
Soviéticas, : 1
Australia, : 1
Bélgica, : 1
Canadá, : 1
Costa : 1
Rica, : 1
Checoeslovaquia, : 1
Salvador, : 1
Grecia, : 1
Guatemala, : 1
Haití, : 1
Honduras, : 1
India, : 1
Luxemburgo, : 1
Nicaragua, : 1
Noruega, : 1
Nueva : 1
Zelandia, : 1
Países : 1
Bajos, : 1
Panamá, : 1
Polonia, : 1
República : 1
Dominicana, : 1
Sudafricana, : 1
Yugoeslavia : 1
firmantes : 1
posteriores : 1
Más : 1
tarde : 1
adhirieron : 1
siguientes : 1
(en : 1
orden : 1
firmas): : 1
México, : 1
Colombia, : 1
Iraq, : 1
Irán, : 1
Liberia, : 1
Paraguay, : 1
Chile, : 1
Uruguay, : 1
Egipto, : 1
Siria, : 1
Francia, : 1
Filipinas, : 1
Brasil, : 1
Bolivia, : 1
Etiopía, : 1
Ecuador, : 1
Perú, : 1
Venezuela, : 1
Turquía, : 1
Arabia : 1
Saudita, : 1
Líbano. : 1

```




Como se puede ver, se logra obtener la cantidad de veces que aparecen las palabras en el texto.

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
