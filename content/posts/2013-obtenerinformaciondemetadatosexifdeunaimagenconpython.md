Title: Obtener información de metadatos EXIF de una imagen con Python
Date: 2013-10-14 9:00
Category: Tutorial Python
Tags: Canaima,Debian,General,Linux,Python,Ubuntu,exif
lang: es
translation: true

Se probará con un simple script como obtener metadatos EXIF de dos imágenes, son dos fotos, la primera directamente del dispositivo móvil con que se tomó la foto, la segunda imagen se bajó desde Google+.

La idea es notar la diferencia de información que se obtiene de los metadatos de dos fotos idénticas para obtenidas de dos formas diferentes.

Lo primero que se tiene que hacer es instalar el módulo python llamado `pyexiv2`. Su documentación la pueden encontrar [aquí](tilloy.net/dev/pyexiv2/index.html).
Se puede instalar en Debian wheezy de la siguiente forma:
```
#apt-get install python-pyexiv2 python-pyexiv2-doc
```
La imagen original fue tomada desde un celular Motorola Razr XT910 y la segunda imagen se bajo desde Google+.
Imagen original con md5:
md5sum ecrespo-orig.jpg
a74977dbbd40d228658435b03db9a4c3  ecrespo-orig.jpg

El tamaño de la imagen es de 248k:
du  ecrespo-orig.jpg
248	ecrespo-orig.jpg

![](./images/obtenerinformaciondemetadatosexifdeunaimagenconpython-1.jpg) 
ecrespo-orig.jpg

Imagen bajada de Google+ con md5:
md5sum ecrespo.jpg
d1d41f5865bbb8360e6a748e38ae5ee1  ecrespo.jpg
El tamaño de la imagen es de 32k:
du ecrespo.jpg
32	ecrespo.jpg

![](./images/obtenerinformaciondemetadatosexifdeunaimagenconpython-2.jpg) 

ecrespo.jpg

El código que muestra los metadatos de exif de cada imagen es el siguiente:
```python
#!/usr/bin/env python

#Se importa el modulo para analisis de metadatos de exif

import pyexiv2

#Se crea una funcion que devuelve en pantalla la informacion exif

def Meta(archivo):

    #Se crea la instancia metadata al pasarle el archivo que se quiere analizar

    metadata = pyexiv2.ImageMetadata(archivo)

    #Se lee el metadato

    metadata.read()

    #Se muestra en pantalla un mensaje

    print "Se muestra la informacion exif del archivo %s" %archivo

    print  "---------------------------------------------"

    #Se despliega la informacion de metadatos exif que contiene la imagen

    for metadato in metadata.exif_keys:

        texto = metadato + ": " + metadata[metadato].raw_value

        print texto


if __name__ == "__main__":

    Meta("ecrespo-orig.jpg")

    print "********************************************"

    Meta("ecrespo.jpg")
```
La salida del script es la siguiente:
```python
Se muestra la informacion exif del archivo ecrespo-orig.jpg

---------------------------------------------

Exif.Image.YCbCrPositioning: 1

Exif.Image.XResolution: 72/1

Exif.Image.YResolution: 72/1

Exif.Image.ResolutionUnit: 2

Exif.Image.DateTime: 2013:09:08 13:10:00

Exif.Image.Make: Motorola

Exif.Image.Model: XT910

Exif.Image.ExifTag: 449

Exif.Photo.ExifVersion: 48 50 50 48

Exif.Photo.FlashpixVersion: 48 48 48 48

Exif.Photo.ColorSpace: 1

Exif.Photo.ComponentsConfiguration: 1 2 3 0

Exif.Photo.CompressedBitsPerPixel: 0/1

Exif.Photo.ExposureTime: 0/1000000

Exif.Photo.FNumber: 24/10

Exif.Photo.ExposureProgram: 0

Exif.Photo.ISOSpeedRatings: 0

Exif.Photo.ShutterSpeedValue: 0/1

Exif.Photo.ApertureValue: 3/1

Exif.Photo.BrightnessValue: 0/1

Exif.Photo.ExposureBiasValue: 0/10

Exif.Photo.MaxApertureValue: 3/1

Exif.Photo.SubjectDistance: 0/1

Exif.Photo.MeteringMode: 1

Exif.Photo.LightSource: 3

Exif.Photo.Flash: 24

Exif.Photo.FocalLength: 460/100

Exif.Photo.FlashEnergy: 0/1

Exif.Photo.ExposureIndex: 0/0

Exif.Photo.SceneType: 1

Exif.Photo.CustomRendered: 1

Exif.Photo.ExposureMode: 0

Exif.Photo.WhiteBalance: 0

Exif.Photo.DigitalZoomRatio: 65536/65535

Exif.Photo.SceneCaptureType: 0

Exif.Photo.GainControl: 0

Exif.Photo.Contrast: 0

Exif.Photo.Saturation: 0

Exif.Photo.Sharpness: 0

Exif.Photo.SubjectDistanceRange: 0

Exif.Image.GPSTag: 1243

Exif.Thumbnail.ImageWidth: 200

Exif.Thumbnail.ImageLength: 120

Exif.Thumbnail.Compression: 6

Exif.Thumbnail.XResolution: 72/1

Exif.Thumbnail.YResolution: 72/1

Exif.Thumbnail.ResolutionUnit: 2

Exif.Thumbnail.JPEGInterchangeFormat: 2027

Exif.Thumbnail.JPEGInterchangeFormatLength: 8033

********************************************

Se muestra la informacion exif del archivo ecrespo.jpg

---------------------------------------------

Exif.Image.Software: Google

Exif.Image.ExifTag: 46

Exif.Photo.ExifVersion: 48 50 50 48

Exif.Photo.0x9009: 10 39 8 1 16 1 24 0 32 0 40 0 48 0 56 0 64 0 72 1 80 0 88 0 96 1 104 1 112 0 120 1 128 1 1 136 1 1 144 1 1

```

Como se puede observar la imagen original bajada del dispositivo con Android tiene más información de metadatos exif que la imagen bajada de Google+, la primera foto tiene información del dispositivo, modelo entre otras cosas mientras que la segunda foto maneja información del software que proceso la imagen que es de Google.

##  ##
¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde la billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)