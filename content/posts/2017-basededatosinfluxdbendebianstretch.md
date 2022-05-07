Title: Base de datos InfluxDB en Debian Stretch
Date: 2017-06-24 12:00
Category: Tutorial de Linux
Tags: Linux,Debian,Ubuntu,InfluxDB
lang: es
translation: true

InfluxDB es una base de datos opensource de series de tiempo, para manejo de eventos,monitoreo, métricas, Internet de las cosas y Analítica en tiempo real. Desarrollada por [InfluxData](https://www.influxdata.com/) en Lenguaje Go. Pueden ver más información en [wikipedia](https://en.wikipedia.org/wiki/InfluxDB).

Para instalar en Debian simplemente se usa `apt-get`:
```
# apt-cache search influxdb 
golang-github-influxdb-enterprise-client-dev - Golang client for speaking to the InfluxDB Enterprise application
golang-github-influxdb-usage-client-dev - library for speaking to the InfluxDB Anonymous Usage Reporting API
golang-gopkg-alexcesaro-statsd.v1-dev - simple and efficient Golang StatsD client
golang-github-influxdb-influxdb-dev - Scalable datastore for metrics, events, and real-time analytics. Dev package
influxdb - Scalable datastore for metrics, events, and real-time analytics
influxdb-client - command line interface for InfluxDB
influxdb-dev - Transitional package for golang-github-influxdb-influxdb-dev
ruby-influxdb - library for InfluxDB
```

Para instalar:
```
# apt-get install influxdb influxdb-client
```
Para probar que está en funcionamiento:
```
# influx
Visit https://enterprise.influxdata.com to register for updates, InfluxDB server management, and monitoring.
Connected to http://localhost:8086 version 1.0.2
InfluxDB shell version: 1.0.2
> 
```


Para crear una base de datos llamada `mydb`:
```
> create database mydb
```
Listar las bases de datos:
```
> show databases
name: databases
---------------
name
_internal
mydb

```

Insertar datos y consultarlos en la base de datos `mydb`:
```
> use mydb
Using database mydb
> INSERT cpu,host=ServerA,region=us_west value=0.64
> SELECT host, region, value FROM cpu
name: cpu
---------
time                   host         region value
1498340879346347895 ServerA us_west 0.64
```
Por lo que se ve, la clave primaria de los datos siempre es el tiempo. 

Ahora una pequeña prueba con Python.

Para instalar la librería en Python:
```python
# pip3 install influxdb
```


Se tiene el siguiente script:

```python


#!/usr/bin/env python3





#Se importa influxdb


from influxdb import InfluxDBClient





#Se define un json con los datos a insertar


json_body = [


    {


        "measurement": "cpu_load_short",


        "tags": {


            "host": "server01",


            "region": "us-west"


        },


        "time": "2009-11-10T23:00:00Z",


        "fields": {


            "value": 0.64


        }


    },


    {


        "measurement": "cpu_load_short",


        "tags": {


            "host": "server02",


            "region": "us-west"


        },


        "time": "2009-12-10T23:00:00Z",


        "fields": {


            "value": 0.65


        }


    }


]


#Se conecta a la base de datos


client = InfluxDBClient('localhost', 8086, 'root', 'root', 'mydb')


#Se crea la base de datos mydb


client.create_database('mydb')





#Se inserta los datos


client.write_points(json_body)


#Se consulta y se muestra en pantalla


result = client.query('select value from cpu_load_short;')


print("Result: {0}".format(result))

```

Al ejecutar el script, este devuelve lo siguiente:
```python
./prueba-influxdb.py 
Result: ResultSet({'('cpu_load_short', None)': [{'value': 0.64, 'time': '2009-11-10T23:00:00Z'}, {'value': 0.65, 'time': '2009-12-10T23:00:00Z'}]})
```

O desde el cliente de `influxdb`:
```
> use mydb
Using database mydb
> select value from cpu_load_short;
name: cpu_load_short
--------------------
time   value
1257894000000000000 0.64
1260486000000000000 0.65
```

Como se muestra, la clave que maneja las consultas es el tiempo.

Para más información se tienen los siguientes enlaces:

- Grafana, influxdb y python.  
- influxdb-python y su documentación.   
- Documentación de influxdata.  
- Plataforma de Influxdata  



##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)

