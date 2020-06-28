Title: Generación de esquema JSON de un archivo XML con genson,lxml y xmltodict.
Date:  2020-06-28 10:55
Category: Tutorial de Python
Tags: Python, Genson,lxml, xmltodict
lang: es
translation: true
Slug: python-genson-xml-json_schema
Authors: Ernesto Crespo
Summary: Se explicará como usar genson para obtener un esquema json a partir de un archivo json o un archivo xml.


La página de genson es la [siguiente](https://pypi.org/project/genson/) y en [github](https://github.com/wolverdude/genson/).  Lo primero que se hará es instalar genson , así como lxml y xmltodict . 


# Instalación

Se instala genson, lxml y xmltodict:

```bash 

pip install genson lxml xmltodict

```

# CLI Tool 

Genson puede ser usado como un comando para generar un esquema json. A continuación se muestra la salida de su ayuda: 

```bash 

$ genson --help

usage: genson.py [-h] [-d DELIM] [-i SPACES] [-s SCHEMA] [-$ URI] ...

Generate one, unified JSON Schema from one or more JSON objects and/or JSON
Schemas. It's compatible with Draft 6 and above.

positional arguments:
  object                files containing JSON objects (defaults to stdin if no
                        arguments are passed)

optional arguments:
  -h, --help            show this help message and exit
  -d DELIM, --delimiter DELIM
                        set a delimiter - Use this option if the input files
                        contain multiple JSON objects/schemas. You can pass
                        any string. A few cases ('newline', 'tab', 'space')
                        will get converted to a whitespace character. If this
                        option is omitted, the parser will try to auto-detect
                        boundaries
  -i SPACES, --indent SPACES
                        pretty-print the output, indenting SPACES spaces
  -s SCHEMA, --schema SCHEMA
                        file containing a JSON Schema (can be specified
                        multiple times to merge schemas)
  -$ URI, --schema-uri URI
                        the value of the '$schema' keyword (defaults to
                        'http://json-schema.org/schema#' or can be specified
                        in a schema with the -s option). If 'NULL' is passed,
                        the "$schema" keyword will not be included in the
                        result.

```

# GenSON Python API

Ahora se mostrará el uso del API de genSON para Python.

## Ejemplos

Para todos los ejemplos se importará una lista de módulos de Python: 

* json
* lxml parse
* lxml XMLParse
* xmltodict 
* genson SchemaBuilder

```python 

import json
from lxml.etree import parse
from lxml.etree import XMLParser
import xmltodict
import genson
from genson import SchemaBuilder
```


### Una lista de diccionarios

Se tiene una lista de diccionarios de la siguiente forma: 

```python 

templist = [{
 'name':'Sam',
},
{
 'name':'Jack',
}]

templist
[{'name': 'Sam'}, {'name': 'Jack'}]

```

Convertir a JSON la lista: 

```python 

jsonf = json.dumps(templist)
jsonf 

'[{"name": "Sam"}, {"name": "Jack"}]'

```

Se crea la instancia del SchemaBuilder, se agrega el objeto  y se muestra el esquema de ese objecto:

```python

builder = SchemaBuilder()
builder.add_object(json.loads(jsonf))
builder.to_schema()

{'$schema': 'http://json-schema.org/schema#',
 'type': 'array',
 'items': {'type': 'object',
  'properties': {'name': {'type': 'string'}},
  'required': ['name']}}

```

El esquema muestra que el objeto es de tipo arreglo, que tiene items que son del tipo object, y que tiene un campo requerido como nombre, y ese nombre es de tipo string.


### Diccionarios agregados como objetos individuales

Se agregarán dos diccionarios que tiene como clave "hi" con diferentes valores (tipo string y entero):

```python 

builder = SchemaBuilder()
builder.add_object({"hi": "there"})
builder.add_object({"hi": 5})
builder.to_schema()

{'$schema': 'http://json-schema.org/schema#',
 'type': 'object',
 'properties': {'hi': {'type': ['integer', 'string']}},
 'required': ['hi']}
```

Ahora el esquema devuelve que es de tipo objeto, y que tiene un campo requerido con nombre "hi", pero de tipo entero y string.

### Se tiene una lista con dos items de distinto tipo (String, entero)

```python 

builder = SchemaBuilder()
builder.add_object(['one', 1])
builder.to_schema()

{'$schema': 'http://json-schema.org/schema#',
 'type': 'array',
 'items': {'type': ['integer', 'string']}}

```

El esquema que genera es de tipo arreglo, con item de dipo entero y string.


### Caso real datos de la NASA

En el siguiente [enlace](http://aiweb.cs.washington.edu/research/projects/xmltk/xmldata/www/repository.html#nasa) encontrarán el data set de la NASA convertido en archivo plano en xml. El archivo xml lo pueden descargar directamente desde [acá](http://aiweb.cs.washington.edu/research/projects/xmltk/xmldata/data/nasa/nasa.xml).

No se va a procesar o restructurar los datos, ya que sería necesario conocer el modelo de datos de la investigación. 

Los pasos son los siguientes: 

1. Creación del parser xml con encoding UTF-8

```python 

parser = XMLParser(encoding='UTF-8')

```

2. Leer los datos xml del archivo y convertirlos en un diccionario: 

```python 

with open("../datos/nasa.xml", "r") as f:
  xx = xmltodict.parse(f.read())
```

3. Crear la instancia de SchemaBuilder, pasarle el diccionario y generar el esquema:

```python 
sb = genson.SchemaBuilder()
sb.add_object(xx)
sb.to_schema()

{'$schema': 'http://json-schema.org/schema#',
 'type': 'object',
 'properties': {'datasets': {'type': 'object',
   'properties': {'dataset': {'type': 'array',
     'items': {'type': 'object',
      'properties': {'@subject': {'type': 'string'},
       '@xmlns:xlink': {'type': 'string'},
       'title': {'type': 'string'},
       'altname': {'type': 'array',
        'items': {'type': 'object',
         'properties': {'@type': {'type': 'string'},
          '#text': {'type': 'string'}},
         'required': ['#text', '@type']}},
       'reference': {'type': 'object',
................
```
Sólo se muestra una parte del esquema, lo que se hará a continuación es eliminar el "@" que en algunos datos aparecen.

Para ello se tiene una función de postprocesamiento:

```python 

def postprocessor(path,key,value):
    try: 
        if key.startswith("@"):
            key = "_" + key[1:]
        return key,value 
    except (ValueError, TypeError):
        return key,value
``` 
Toma las claves del diccionario y los que comiencen por "@" los cambia por "_". 

4. Se vuelve a leer los datos del archivo xml pasando la función: 

```python 

with open("../datos/nasa.xml", "r") as f:
    xx = xmltodict.parse(f.read(),encoding="utf-8",postprocessor=postprocessor)

```

5. Se crea la instancia de SchemaBuilder, se agrega el diccionario y se genera el esquema:

```python
sb = genson.SchemaBuilder()
sb.add_object(xx)
sb.to_schema()

{'$schema': 'http://json-schema.org/schema#',
 'type': 'object',
 'properties': {'datasets': {'type': 'object',
   'properties': {'dataset': {'type': 'array',
     'items': {'type': 'object',
      'properties': {'_subject': {'type': 'string'},
       '_xmlns:xlink': {'type': 'string'},
       'title': {'type': 'string'},
       'altname': {'type': 'array',
        'items': {'type': 'object',
         'properties': {'_type': {'type': 'string'},
          '#text': {'type': 'string'}},
         'required': ['#text', '_type']}}

..................

```

Ahora se nota que cambiaron algunas claves con un "_". 

Con xmltodict, lxl y genson se puede procesar conjunto de datos y restructurarlos a lo que se requiere para facilitar su análisis.



####


¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
