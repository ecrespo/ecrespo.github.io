Title: Manejar información de un archivo csv con csvkit
Date: 2013-02-19 10:00
Category: Tutorial Python
Tags: General,Python,csv,csvkit
lang: es
translation: true

El programa `csvkit` es una herramienta desarrollada en Python que facilita la manipulación de la información contenida en un archivo con formato `csv`.

Se utilizará como ejemplo los datos de la página data.gov. Los datos que se utilizará son del Departamento de Asuntos de Veteranos de beneficios educativos de los Estatos Unidos (disculpen la traducción) del año 2009.

Es necesario instalar `csvkit`, en este caso se usa el comando `pip` de python:  
```python
pip install csvkit
```
Obtener los datos:
```
mkdir beneficios

cd beneficios 
```
Bajar archivo `2009.csv` con el comando `wget`:
```
wget -O 2009.csv -U "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.16 (JHTML, like Gecko) chrome/10.0.648.205 Safari/534.16" http://www.data.gob/download/4029/csv 
```
Verificar las primeras 5 líneas del archivo:
```
head -n 5 2009.csv 

State Name,State Abbreviate,Code,Montgomery GI Bill-Active Duty,Montgomery GI Bill- Selective Reserve,Dependents' Educational Assistance,Reserve Educational Assistance Program,Post-Vietnam Era Veteran's Educational Assistance Program,TOTAL,

ALABAMA,AL,01,"6,718","1,728","2,703","1,269",8,"12,426",

ALASKA,AK,02,776,154,166,60,2,"1,158",

ARIZONA,AZ,04,"26,822","2,005","3,137","2,011",11,"33,986",

ARKANSAS,AR,05,"2,061",988,"1,575",886,3,"5,513",
```
Se puede usar el mismo comando `wget` para bajar los archivos de los años 2010.csv, 2011.csv y 2012.csv.

Obtener la información de las columnas con `csvcut`:
```
csvcut -n 2009.csv

  1: State Name

  2: State Abbreviate

  3: Code

  4: Montgomery GI Bill-Active Duty

  5: Montgomery GI Bill- Selective Reserve

  6: Dependents' Educational Assistance

  7: Reserve Educational Assistance Program

  8: Post-Vietnam Era Veteran's Educational Assistance Program

  9: TOTAL

 10: 
```

Como se puede observar, el archivo `csv` maneja 9 columnas. 

Con el comando `csvcut` se puede obtener información entre la fila 2 y 3 (State Abbreviate y Code), sólo se desea mostrar las primeras 5 líneas del archivo: 
```
csvcut -c 2,3 2009.csv | head -n 5

State Abbreviate,Code
AL,01
AK,02
AZ,04
AR,05
```

Se puede también manejar estadisticas bajo demanda con `csvstat`. Se genera la estadistica de la información de las columnas 1,4,9 y 10. Para este caso se utiliza `csvcut` y se pasa la información a `csvstat`:
```
csvcut -c 1,4,9,10 2009.csv | csvstat

  1. State Name
	<type 'unicode'>
	Nulls: True
	Unique values: 52
	Max length: 17
  2. Montgomery GI Bill-Active Duty
	<type 'int'>
	Nulls: True
	Min: 435
	Max: 34942
	Sum: 325723
	Mean: 6263.90384615
	Median: 3548.0
	Standard Deviation: 7537.86225373
	Unique values: 52
  3. TOTAL
	<type 'int'>
	Nulls: True
	Min: 768
	Max: 46897
	Sum: 506914
	Mean: 9748.34615385
	Median: 6520.0
	Standard Deviation: 10070.4022127
	Unique values: 52
  4. _unnamed
	<type 'NoneType'>
	Nulls: True
	Values: 
```

Se puede realizar busquedas por filas con `csvgrep`. En este caso la información total del Estado de Illinois:
```
csvcut -c 1,"TOTAL" 2009.csv | csvgrep -c 1 -m ILLINOIS

State Name,TOTAL

ILLINOIS,"21,964"
```

Voltear orden de las columnas con `csvcut`: 
```
csvcut -c 9,1 2009.csv | head -n 5

TOTAL,State Name
"12,426",ALABAMA
"1,158",ALASKA
"33,986",ARIZONA
"5,513",ARKANSAS
```
En este caso se cambia el orden de las columnas al decirle a csvcut el orden de las columnas. 

Ordenar con `csvsort`: 
```
csvcut -c 9,1 2009.csv | csvsort -r | head -n 5

TOTAL,State Name
46897,CALIFORNIA
40402,TEXAS
36394,FLORIDA
33986,ARIZONA
```
Se puede dar un formato para que sea legible la información con `csvlook`:
```
csvcut -c 9,1 2009.csv | csvsort -r -l | csvlook

|--------------+-------+--------------------|
|  line_number | TOTAL | State Name         |
|--------------+-------+--------------------|
|  1           | 46897 | CALIFORNIA         |
|  2           | 40402 | TEXAS              |
|  3           | 36394 | FLORIDA            |
|  4           | 33986 | ARIZONA            |
|  5           | 21964 | ILLINOIS           |
|  6           | 20541 | VIRGINIA           |
|  7           | 18236 | GEORGIA            |
|  8           | 15730 | NORTH CAROLINA     |
|  9           | 13967 | NEW YORK           |
|  10          | 13962 | MISSOURI           |
|  11          | 13614 | COLORADO           |
|  12          | 13314 | OHIO               |
|  13          | 13011 | PENNSYLVANIA       |
|  14          | 12426 | ALABAMA            |
|  15          | 11492 | WASHINGTON         |
|  16          | 10085 | MARYLAND           |
|  17          | 9791  | MINNESOTA          |
|  18          | 9344  | MICHIGAN           |
|  19          | 9206  | OKLAHOMA           |
|  20          | 9013  | IOWA               |
|  21          | 8840  | WEST VIRGINIA      |
|  22          | 8757  | TENNESSEE          |
|  23          | 8081  | WISCONSIN          |
|  24          | 7872  | SOUTH CAROLINA     |
|  25          | 7809  | INDIANA            |
|  26          | 6652  | LOUISIANA          |
|  27          | 6388  | KENTUCKY           |
|  28          | 6009  | MASSACHUSETTS      |
|  29          | 5870  | OREGON             |
|  30          | 5513  | ARKANSAS           |
|  31          | 5511  | NEW JERSEY         |
|  32          | 5416  | NEBRASKA           |
|  33          | 5345  | UTAH               |
|  34          | 4947  | KANSAS             |
|  35          | 4551  | NEW MEXICO         |
|  36          | 4424  | PUERTO RICO        |
|  37          | 4299  | MISSISSIPPI        |
|  38          | 3728  | NEVADA             |
|  39          | 2997  | CONNECTICUT        |
|  40          | 2751  | IDAHO              |
|  41          | 2521  | HAWAII             |
|  42          | 1992  | SOUTH DAKOTA       |
|  43          | 1920  | MAINE              |
|  44          | 1795  | MONTANA            |
|  45          | 1778  | NORTH DAKOTA       |
|  46          | 1326  | NEW HAMPSHIRE      |
|  47          | 1175  | RHODE ISLAND       |
|  48          | 1158  | ALASKA             |
|  49          | 1145  | DELAWARE           |
|  50          | 1117  | WYOMING            |
|  51          | 1084  | DIST. OF COLUMBIA  |
|  52          | 768   | VERMONT            |
|  53          |       |                    |
|--------------+-------+--------------------|
```

Para finalizar se puede salvar el trabajo en un nuevo archivo csv:
```
csvcut -c 9,1 2009.csv | csvsort -r -l > 2009_ranking.csv
```

 Si se desea aprender más de la herramienta `csvkit` se puede revisar la página de la [documentación](https://csvkit.readthedocs.io/en/latest/index.html). 

En próximo artículo se mostrará como usar `csvkit` desde un programa en Python.

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)