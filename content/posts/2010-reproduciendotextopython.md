Title: Reproduciendo texto desde python
Date: 2010-03-30 11:00
Category: Accesibilidad
Tags: Linux,Python,pypdf, pyttsx
lang: es
translation: true


Existe un módulo en python que permite reproducir texto directamente desde el código python sin necesidad de ejecutar un comando externo; este módulo se llama pyttsx.

Para instalarlo se ejecuta easy_install:
easy_install pyttsx

Ahora ya se puede probar el módulo:


```python

#!/usr/bin/env python
#Se importa el modulo
import pyttsx
#Se inicia el motor de voz
engine = pyttsx.init()
#Se selecciona el idioma a utilizar
engine.setProperty('voice', "spanish-latin-american")
#Se genera la voz a partir de un texto
engine.say('Esta es una prueba de reproduccion de texto')
engine.say('fin')
#Se reproduce la voz
engine.runAndWait()
```

Esto reproducirá el contenido definido en el código, a continuación se reproducirá el contenido de un pdf basandose en la publicación anterior y esta:


```python

#!/usr/bin/env python
"""
Nombre: pdf2voz
Descripcion: Programa que reproduce el contenido de un pdf 
Autor: Ernesto Crespo
Correo: ernesto@crespo.org.ve
Licencia: GPL v3
Version de prueba para definir la construccion del reproductor
"""
import pyttsx
#Importar modulo de lectura de pypdf
from pyPdf import PdfFileReader
#Inicia el motor de reproduccion de texto a voz
engine = pyttsx.init()
#Se define el Idioma a reproducir
engine.setProperty('voice', "spanish-latin-american")
#Capturar el archivo pdf a leer
input1 = PdfFileReader(file("tut.pdf", "rb"))
#Capturar la cantidad de paginas que tiene el documento
paginas = input1.getNumPages()
titulo =input1.getDocumentInfo().title
#Captura la pagina inicial del pdf
pagina1 = input1.getPage(0)
#Captura el autor del documento pdf
autor =input1.getDocumentInfo().author
#Extrae el texto de la pagina inicial del documento pdf
texto = pagina1.extractText()
#Reproduccion de la informacion del pdf
engine.say("El titulo de libro es %s" %titulo)
engine.say("La cantidad de paginas del libro son %s" %paginas)
engine.say("El autor del documento es %s" %autor)
engine.say("El texto de la pagina inicial es")
engine.say(texto)
engine.runAndWait()


```

Ahora queda trabajar en el programa que generalice la reproducción de documentos pdf, defina las páginas que quiera reproducir, el volumen, el idioma entre otras opciones.


===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)