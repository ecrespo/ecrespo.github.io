Title: Manejo de calendario en python con la librería calendar 
Date:  2023-03-18 11:22
Category: Tutorial Python
Tags: python, calendar
lang: es
translation: true
Slug: python_calendar
Authors: Ernesto Crespo
Summary: Artículo sobre como manejar meses del calendario según el año

# Manejo de calendario en python con la librería calendar

El artículo se basa en el artículo en inglés de:
* [Python Engineer](https://www.python-engineer.com/posts/calendar-python/)

La librería calendar permite desplegar meses de un año, lo primero que tenemos que hacer es importar la librería.

```python
import calendar
```

## Desplegar el calendario del año y mes:

Se define las variables aÑo y mes, se llama a calendar al método month pasando estas variables, devuelve el calendario del mes y año definido.


```python
year = 2023
month = 3
print(calendar.month(year, month))
```
```output
     March 2023
Mo Tu We Th Fr Sa Su
       1  2  3  4 5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31
```
## Desplegar el calendario del año 2023:

Se define el aÑo del calendario y luego se muestra todos los meses.

```python
year = 2023 
print(calendar.calendar(year))
```
```output
2023

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                   1             1  2  3  4  5             1  2  3  4  5
 2  3  4  5  6  7  8       6  7  8  9 10 11 12       6  7  8  9 10 11 12
 9 10 11 12 13 14 15      13 14 15 16 17 18 19      13 14 15 16 17 18 19
16 17 18 19 20 21 22      20 21 22 23 24 25 26      20 21 22 23 24 25 26
23 24 25 26 27 28 29      27 28                     27 28 29 30 31
30 31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2       1  2  3  4  5  6  7                1  2  3  4
 3  4  5  6  7  8  9       8  9 10 11 12 13 14       5  6  7  8  9 10 11
10 11 12 13 14 15 16      15 16 17 18 19 20 21      12 13 14 15 16 17 18
17 18 19 20 21 22 23      22 23 24 25 26 27 28      19 20 21 22 23 24 25
24 25 26 27 28 29 30      29 30 31                  26 27 28 29 30

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6                   1  2  3
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       4  5  6  7  8  9 10
10 11 12 13 14 15 16      14 15 16 17 18 19 20      11 12 13 14 15 16 17
17 18 19 20 21 22 23      21 22 23 24 25 26 27      18 19 20 21 22 23 24
24 25 26 27 28 29 30      28 29 30 31               25 26 27 28 29 30
31

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                   1             1  2  3  4  5                   1  2  3
 2  3  4  5  6  7  8       6  7  8  9 10 11 12       4  5  6  7  8  9 10
 9 10 11 12 13 14 15      13 14 15 16 17 18 19      11 12 13 14 15 16 17
16 17 18 19 20 21 22      20 21 22 23 24 25 26      18 19 20 21 22 23 24
23 24 25 26 27 28 29      27 28 29 30               25 26 27 28 29 30 31
30 31
```

## Clase Calendar

La clase calendar permite crear un objecto calendario, el cual permite obtener información del calendario y darle formato
de salida.

Como usar la clase calendar:

1. El método iterweekdays():

Permite iterar sobre los días de la semana, el método devuelve un iterador que itera sobre los días de la semana, 
el primer día de la semana es el lunes, el último es el domingo.
```python
import calendar

cal = calendar.calendar()
for dia in cal.iterweekdays():
    print(dia,end=' ')
```

```output
0 1 2 3 4 5 6
```
Entonces devuelve lunes, martes, miércoles, jueves, viernes, sábado y domingo.


2. El método monthdayscalendar():

El método permite iterar sobre todo el mes, los días de cada semana.

```python
cal = calendar.Calendar()
for mes in cal.monthdayscalendar(2023,3):
    print(mes)
```

```output
[0, 0, 1, 2, 3, 4, 5]
[6, 7, 8, 9, 10, 11, 12]
[13, 14, 15, 16, 17, 18, 19]
[20, 21, 22, 23, 24, 25, 26]
[27, 28, 29, 30, 31, 0, 0]
```


## Clase TextCalendar

Esta es una clase que se usa para generar calendarios en formato texto.

1. El método formatmonth():

Generada la salida del mes en formato calendario pero en texto.

```python
textcal = calendar.TextCalendar()
year = 2023
month = 3
w = 4 # ancho de cada columna
l = 2 # número de líneas por semana
print(textcal.formatmonth(year, month, w, l))
```

```output
     March 2023
Mo Tu We Th Fr Sa Su
       1  2  3  4 5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30 31
```

2. El método prmonth():

Este método imprime el mes en formato calendario retornado por el método formatmonth. Toma los mismos argumentos
del método formatmonth.

```python
textcal.prmonth(year,month,6,3)
```

```ouput

March 2023


 Mon    Tue    Wed    Thu    Fri    Sat    Sun


                 1      2      3      4      5


   6      7      8      9     10     11     12


  13     14     15     16     17     18     19


  20     21     22     23     24     25     26


  27     28     29     30     31
  
```

## Clase HTMLCalendar

Se usa para generar los calendarios en formato html.

1. El método formatmonth():
```python
htmlcal = calendar.HTMLCalendar()
print(htmlcal.formatmonth(2023, 3))
```

```html

<table border="0" cellpadding="0" cellspacing="0" class="month">
<tr><th colspan="7" class="month">March 2023</th></tr>
<tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>
<tr><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="wed">1</td><td class="thu">2</td><td class="fri">3</td><td class="sat">4</td><td class="sun">5</td></tr>
<tr><td class="mon">6</td><td class="tue">7</td><td class="wed">8</td><td class="thu">9</td><td class="fri">10</td><td class="sat">11</td><td class="sun">12</td></tr>
<tr><td class="mon">13</td><td class="tue">14</td><td class="wed">15</td><td class="thu">16</td><td class="fri">17</td><td class="sat">18</td><td class="sun">19</td></tr>
<tr><td class="mon">20</td><td class="tue">21</td><td class="wed">22</td><td class="thu">23</td><td class="fri">24</td><td class="sat">25</td><td class="sun">26</td></tr>
<tr><td class="mon">27</td><td class="tue">28</td><td class="wed">29</td><td class="thu">30</td><td class="fri">31</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td></tr>
</table>

```

Al tomar el código y pasarlo por codepen se tiene:

![codepen](./images/codepen.png)


Esta librería facilita la visualización de calendarios anual y/o por mes.

