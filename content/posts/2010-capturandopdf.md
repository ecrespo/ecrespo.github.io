Title: Capturando el contenido de un pdf desde python
Date: 2010-03-29 11:00
Category: Accesibilidad
Tags: Linux,Python,pypdf
lang: es
translation: true


Desde hace tiempo conocía de la posibilidad de capturar información de un pdf, la idea final es lograr tomar esta información y reproducirla con espeak.

El siguiente ejemplo muestra el uso del módulo pypdf.

```python

#Importar modulo de lectura de pypdf
from pyPdf import PdfFileReader

#Capturar el archivo pdf a leer
input1 = PdfFileReader(file("tut.pdf", "rb"))

#Capturar la cantidad de paginas que tiene el documento
paginas = input1.getNumPages()
#Capturar el titulo del pdf
titulo =input1.getDocumentInfo().title
#Captura la pagina inicial del pdf
pagina1 = input1.getPage(0)
#Captura el autor del documento pdf
autor =input1.getDocumentInfo().author
#Extrae el texto de la pagina inicial del documento pdf
texto = pagina1.extractText()
print "El libro se llama : %s" %titulo
print "El autor es: %s" %autor
print "La cantidad de paginas del libro es: %s " %paginas
print "El contenido de la pagina inicial es:"
print texto

```

El resultado de este script es el siguiente:
```
El libro se llama : Guía de aprendizaje de Python
El autor es: Guido van Rossum, Fred L. Drake, Jr., editor
La cantidad de paginas del libro es: 77 
El contenido de la pagina inicial es:
GuíadeaprendizajedePythonRelease2.0GuidovanRossumFredL.Drake,Jr.,editor16deoctubrede2000BeOpenPythonLabsCorreoelectrónico:python-docs@python.org
```

En el siguiente artículo explicare ya el uso del conversor de audio de la información capturada del pdf.

===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)