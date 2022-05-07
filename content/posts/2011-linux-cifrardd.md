Title: Como cifrar directorios/particiones con eCryptfs
Date: 2011-08-21 09:00
Category: Tutorial de Linux
Tags: Linux,Debian, Ubuntu, Canaima,Seguridad,eCryptfs
lang: es
translation: true

Este artículo se basa en el artículo de HowtoForge sobre el mismo [tema](http://www.howtoforge.net/how-to-encrypt-directories-partitions-with-ecryptfs-on-debian-squeeze).

La idea es cifrar el directorio home del usuario,se monte el directorio cifrado automáticamente al arrancar el equipo.

Es necesario tener un respaldo de la carpeta del usuario para evitar perdida de datos si olvida la clave.

1. Instalar eCryptfs:

Se ejecuta:

```
aptitude install ecryptfs-utils
```

2. Cifrar un directorio.

Respaldar los archivos y directorios del home del usuario:

```
cp -pfr /home/ecrespo /tmp/

```

Cifrar el directorio /home/ecrespo/ al montar el sistema de archivos ecryptfs:

Se selecciona aes, 16, no se habilita frase plana, no se habilita cifrado del nombre del archivo, así que con estas opciones sólo hay que presionar enter a la información que solicite al montar la partición cifrada.

```
mount -t ecryptfs /home/ecrespo /home/ecrespo

Passphrase:
Select cipher:
 1) aes: blocksize = 16; min keysize = 16; max keysize = 32 (not loaded)
 2) blowfish: blocksize = 16; min keysize = 16; max keysize = 56 (not loaded)
 3) des3_ede: blocksize = 8; min keysize = 24; max keysize = 24 (not loaded)
 4) twofish: blocksize = 16; min keysize = 16; max keysize = 32 (not loaded)
 5) cast6: blocksize = 16; min keysize = 16; max keysize = 32 (not loaded)
 6) cast5: blocksize = 8; min keysize = 5; max keysize = 16 (not loaded)
Selection [aes]:
Select key bytes:
 1) 16
 2) 32
 3) 24
Selection [16]:
Enable plaintext passthrough (y/n) [n]: Enter
Enable filename encryption (y/n) [n]: Enter
Attempting to mount with the following options:
  ecryptfs_unlink_sigs
  ecryptfs_key_bytes=16
  ecryptfs_cipher=aes
  ecryptfs_sig=162827f20fdadf4e
Mounted eCryptfs
```

3. Verificar que la partición se ha montado.

El comando mount sólo devuelve las particiones que se encuentran montadas en el Linux.

```
mount /home/ecrespo on /home/ecrespo type ecryptfs (rw,ecryptfs_sig=162827f20fdadf4e,ecryptfs_cipher=aes,ecryptfs_key_bytes=16,ecryptfs_unlink_sigs)
```

4. Recuperar el respaldo y borrar el respaldo del directorio /tmp/

```
cp -pfr /tmp/ecrespo /home/
rm -fr /tmp/ecrespo
```

5. Verificar el funcionamiento del cifrado de archivos.

Para propósitos de prueba se copia un archivo de /etc/ al home del usuario.
Mostrar la información que contiene el archivo hostname en /etc/

```
cat /etc/hostname 
canaima-popular
```

Copiar el archivo hostname al home del usuario:

```
cp /etc/hostname /home/ecrespo/
```

Mientras la partición cifrada se encuentra montada se puede visualizar los archivos:

```
cat /home/ecrespo/hostname 
canaima-popular
```

Desmontar la partición.

```
umount /home/ecrespo/
```

Verificar que el archivo está cifrado:

```
cat /home/ecrespo/hostname
4��ˉ�s|| � "3DUfw`�6���D �̬�����{� _CONSOLE ('��N�pD���-� \ٛn�Ś/��TD��xҝD[:�$] �wq�V��
�n /�k�a:�H.�{ USj�@u)�c ������T� �� �m�иや� � Z�&��0�Q��B�� /��q�e��E��li�"dx�tDs���k����h�J��20��&T�?R�x� �W�$�
                                                                                                                   �$�@ �&
                                                                                                                           ��� �G� /�.L���1d�� j����{cYRꄙZ`��t 8�4ԬZ~ ,)H
eb �� f ��?��
          �_' ��K&�d)����{y�z����ֆ�2x��h�� &j���tuq��a�JeJ�� ���\"~
                                                                   ��5`� V RCB`��������PU�&������X�
                                                                                                    9Ԥ[� 4O.� �� ̔�;/ �����#j V`Sf^��<�uB8 �ЭIx�4PR�� dml��`&c �
! ҟ&`�~�U?u�� �����쵮 @�)�8�Q U��杞M�e��="�}�V# ��>������ �>�F�� R�#ZgI���^J�� ,��0ݼR�rO�f��AxS��3�\�M���o�D �u�Av)�qq%�(F�/���%tL��w�U�k6~c��` “=�4N��E�= #� � a7�����v�(V�p�HlR�Y5����#^���K �~ :h��Z�Q�J�{�FC�N;*� 0Bő*���=�
�ՙ��R�mќet ���7B�_�Dz.[�6>�ĸؓ�� �Nc��#��NR��@� 4 �/���M?Om �|;/�Oe9�6��&6D*U�A�e��� �V
�ZM�<ɝ��"�0��0�WŸL�H�,r
                        �>��f��4�$�wA�rѫ� �0H�����CP�i��&���!b���-#
$ލ;�X!y�� ~� I5e��V|Y�\� �H^£�7�0�Z��{�}"!��͡�� 6�M�!LNȆXvF         )� ��G�Nuɍ� � ӧ��s���t ���t��o&� C������W�#��Cpk�><„
```

6. Montar automáticamente  la partición o directorio.

Conecte un pendrive y ejecute el comando fdisk -l donde aparecerá la partición del pendrive:

```
fdisk -l
 Disk /dev/sdb: 16.0 GB, 16011542528 bytes
32 heads, 63 sectors/track, 15512 cylinders, 31272544 sectores en total
Units = sectores of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Identificador del disco: 0x59a4123d

Disposit. Inicio    Comienzo      Fin      Bloques  Id  Sistema
/dev/sdb1   *          63    31272191    15636064+   b  W95 FAT32
```

Montar el pendrive:

```
mkdir /mnt/usb
mount /dev/sdb1 /mnt/usb
```

Al ejecutar mount sólo mostrará las particiones montadas en el equipo:

```
mount /dev/sdb1 on /mnt/usb type vfat (rw)
```

A diferencia del artículo original el pendrive y la partición cifrada no se monta automaticamente.



===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./images/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
