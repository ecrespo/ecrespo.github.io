Title: Manteniendo un paquete Debian con mercurial
Date: 2009-04-11 08:00
Category: Linux
Tags: Debian,Empaquetado,Mercurial
lang: es
translation: true

Para mantener un paquete Debian con mercurial es necesario tener un repositorio
mercurial, este se crea con el comando hg init.

```
hg init repositorio
```

Luego es necesario crear 2 directorios, uno es del paquete fuente de debian y el otro
del paquete fuente del upstream.

```
cd repositorio
hg init sshguard
hg init sshguard.upstream
```

Luego se importa las fuentes de Debian:

```
hg-importdsc /home/ecrespo/paquetes/sshguard/sshguard_1.3-1.dsc
ecrespo@canaima:~/repositorio/repositorio/sshguard$ hg-importdsc /home/ecrespo/paquetes/sshguard/sshguard_1.3-1.dsc
*** Processing upstream file /home/ecrespo/paquetes/sshguard/sshguard_1.3.orig.tar.gz
VCSCMD: hg
LOGTEXT Imported sshguard_1.3.orig.tar.gz
into Mercurial repository



adding Changes
adding Makefile.am
adding Makefile.in
adding README
adding aclocal.m4
adding config.h.in
adding configure
adding configure.ac
adding depcomp
adding examples/whitelistfile.example
adding install-sh
adding man/Makefile.am
adding man/Makefile.in
adding man/sshguard.8
adding missing
adding mkinstalldirs
adding scripts/sshguard_backendgen.sh
adding src/Makefile.am
adding src/Makefile.in
adding src/attack_parser.c
adding src/attack_parser.h
adding src/attack_parser.y
adding src/attack_scanner.c
adding src/attack_scanner.l
adding src/config.h.in
adding src/fwalls/Makefile.am
adding src/fwalls/Makefile.in
adding src/fwalls/command.c
adding src/fwalls/command_aix.h
adding src/fwalls/command_ipfilter.h
adding src/fwalls/command_iptables.h
adding src/fwalls/command_null.h
adding src/fwalls/command_pf.h
adding src/fwalls/hosts.c
adding src/fwalls/ipfw.c
adding src/parser.h
adding src/simclist.c
adding src/simclist.h
adding src/sshguard.c
adding src/sshguard.h
adding src/sshguard_addresskind.h
adding src/sshguard_fw.h
adding src/sshguard_log.c
adding src/sshguard_log.h
adding src/sshguard_procauth.c
adding src/sshguard_procauth.h
adding src/sshguard_services.h
adding src/sshguard_whitelist.c
adding src/sshguard_whitelist.h
adding stamp-h1
adding ylwrap
No username found, using 'ecrespo@canaima' instead
No username found, using 'ecrespo@canaima' instead
No username found, using 'ecrespo@canaima' instead

/home/ecrespo/paquetes/sshguard/sshguard_1.3.orig.tar.gz imported into /home/ecrespo/repositorio/repositorio/sshguard.upstream
Remember to run hg fetch /home/ecrespo/repositorio/repositorio/sshguard.upstream
*** Done processing upstream file /home/ecrespo/paquetes/sshguard/sshguard_1.3.orig.tar.gz
*** Processing Debian source tree for /home/ecrespo/paquetes/sshguard/sshguard_1.3-1.dsc
0:b438c8517fe7
1:f61bc4db3564
2:85a24e090d85
pulling from /home/ecrespo/repositorio/repositorio/sshguard.upstream
requesting all changes
adding changesets
adding manifests
adding file changes
added 3 changesets with 53 changes to 52 files
(run 'hg update' to get a working copy)
52 files updated, 0 files merged, 0 files removed, 0 files unresolved
dpkg-source: extracting sshguard in sshguard-1.3
dpkg-source: info: unpacking sshguard_1.3.orig.tar.gz
dpkg-source: info: applying sshguard_1.3-1.diff.gz
VCSCMD: hg
LOGTEXT Imported sshguard-1.3
into Mercurial repository



adding debian/changelog
adding debian/compat
adding debian/control
adding debian/copyright
adding debian/dirs
adding debian/docs
adding debian/rules
adding src/fwalls/command.h
No username found, using 'ecrespo@canaima' instead
No username found, using 'ecrespo@canaima' instead

```

Ahora se tienen los directorios sshguard y sshguard.upstream con archivos y directorios.

```
ecrespo@canaima:~/repositorio/repositorio/sshguard$ ls
aclocal.m4 config.h.in configure.ac depcomp install-sh Makefile.in missing README src ylwrap
Changes configure debian examples Makefile.am man mkinstalldirs scripts stamp-h1

ecrespo@canaima:~/repositorio/repositorio/sshguard.upstream$ ls
aclocal.m4 config.h.in configure.ac examples Makefile.am man mkinstalldirs scripts stamp-h1
Changes configure depcomp install-sh Makefile.in missing README src ylwrap
```

Se nota que el primer directorio es del paquete fuente de Debian por que tiene dentro un directorio debian y sshguard.upstream es el paquete fuente.
Ahora se harán cambios en los archivos del directorio debian. Se va a cambiar el archivo
rules en el configure que en vez de sorportar iptables use hosts; y en el archivo control
quitarla dependencia de iptables en build-depends y colocar en las dependencias tcpd ya
que ese es el paquete para usar hosts.allow y hosts.deny.

Archivo debian/rules:

```
./configure $(CROSS) --prefix=/usr --mandir=\$${prefix}/share/man --with-firewall=hosts --infodir=\$${prefix}/share/info CFLAGS="$(CFLAGS)" LDFLAGS="-Wl,-z,defs"
```

Archivo debian/control:

```
Source: sshguard
Section: net
Priority: optional
Maintainer: Ernesto Nadir Crespo Avila
Build-Depends: debhelper (>= 7), autotools-dev
Standards-Version: 3.8.0
Homepage: http://sshguard.sourceforge.net/

Package: sshguard
Architecture: any
Depends: ${shlibs:Depends}, ${misc:Depends}, tcpd
Description: Protects from brute force attacks against ssh
Protects networked hosts from the today's widespread
brute force attacks against ssh servers. It detects such attacks
and blocks the author's address with a firewall rule.
```

Se exportan las variables de ambiente DEBFULLNAME y DEBEMAIL:

```
export DEBFULLNAME="Ernesto Nadir Crespo Avila"
export DEBEMAIL="ecrespo@debianvenezuela.org"
```

Cambiar el archivo debian/changelo agregando los cambios que se realizaron:

```
dch -i

sshguard (1.3-2) unstable; urgency=low

* Remove iptables depend in build-depends in debian/control file.
* Add tcpd depend in depends in debian/control file.
* Change configure option in debian/rules to hosts.

-- Ernesto Nadir Crespo Avila Tue, 14 Apr 2009 14:06:01 -0430

```

Para agregar los cambios al repositorio se ejecuta un commit:


```
ecrespo@canaima:~/repositorio/repositorio/sshguard$ hg commit -m"Change control and rules files" -u "Ernesto Nadir Crespo Avila "
```

Al ejecutar hg log se muestra los cambios realizados:

```
changeset: 5:7a64e00a1c05
tag: tip
user: Ernesto Nadir Crespo Avila
date: Tue Apr 14 14:11:19 2009 -0430
summary: Change control and rules files

changeset: 4:19b2688f71ec
user: ecrespo@canaima
date: Tue Apr 14 13:57:26 2009 -0430
summary: Added tag DEBIAN_sshguard_1.3-1 for changeset a7094766c4e6

changeset: 3:a7094766c4e6
tag: DEBIAN_sshguard_1.3-1
user: ecrespo@canaima
date: Tue Apr 14 13:57:25 2009 -0430
summary: Import Debian sshguard 1.3-1

changeset: 2:85a24e090d85
user: ecrespo@canaima
date: Tue Apr 14 13:57:24 2009 -0430
summary: Added tag UPSTREAM_sshguard_1.3_TAG for changeset f61bc4db3564

changeset: 1:f61bc4db3564
tag: UPSTREAM_sshguard_1.3_TAG
user: ecrespo@canaima
date: Tue Apr 14 13:57:24 2009 -0430
summary: Added tag UPSTREAM_sshguard_1.3 for changeset b438c8517fe7

changeset: 0:b438c8517fe7
tag: UPSTREAM_sshguard_1.3
user: ecrespo@canaima
date: Tue Apr 14 13:57:24 2009 -0430
summary: Import upstream sshguard version 1.3
```

Se suben los cambios al repositorio:

```
ecrespo@canaima:~/repositorio/repositorio$ hg pull sshguard
pulling from sshguard
requesting all changes
adding changesets
adding manifests
adding file changes
added 7 changesets with 66 changes to 60 files
(run 'hg update' to get a working copy)
```

Se actualiza el repositorio:

```
ecrespo@canaima:~/repositorio/repositorio$ hg update
60 files updated, 0 files merged, 0 files removed, 0 files unresolved

```

Ahora se crea el paquete:

```
ecrespo@canaima:~/repositorio/repositorio$ hg-buildpackage -rfakeroot -k
Building ../sshguard_1.3.orig.tar.gz from Mercurial history
dpkg-buildpackage -rfakeroot -D -us -uc -i.hg -I.hg
dpkg-buildpackage: set CFLAGS to default value: -g -O2
dpkg-buildpackage: set CPPFLAGS to default value:
dpkg-buildpackage: set LDFLAGS to default value:
dpkg-buildpackage: set FFLAGS to default value: -g -O2
dpkg-buildpackage: set CXXFLAGS to default value: -g -O2
dpkg-buildpackage: source package sshguard
dpkg-buildpackage: source version 1.3-2
dpkg-buildpackage: source changed by Ernesto Nadir Crespo Avila
dpkg-buildpackage: host architecture i386
fakeroot debian/rules clean
dh_testdir
dh_testroot
rm -f build-stamp
# Add here commands to clean up after the build process.
[ ! -f Makefile ] || /usr/bin/make distclean
rm -f config.sub config.guess config.status config.status.lineno config.log
dh_clean
dpkg-source -i.hg -I.hg -b repositorio
dpkg-source: warning: source directory 'repositorio' is not - 'sshguard-1.3'
dpkg-source: warning: .orig directory name repositorio.orig is not - (wanted sshguard-1.3.orig)
dpkg-source: info: using source format `1.0'
dpkg-source: info: building sshguard using existing sshguard_1.3.orig.tar.gz
dpkg-source: info: building sshguard in sshguard_1.3-2.diff.gz
dpkg-source: info: building sshguard in sshguard_1.3-2.dsc
debian/rules build
dh_testdir
# Add here commands to configure the package.
cp -f /usr/share/misc/config.sub config.sub
cp -f /usr/share/misc/config.guess config.guess
./configure --build i486-linux-gnu --prefix=/usr --mandir=\${prefix}/share/man --with-firewall=hosts --infodir=\${prefix}/share/info CFLAGS="-g -O2" LDFLAGS="-Wl,-z,defs"
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
checking for a thread-safe mkdir -p... /bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking for gcc... gcc
checking for C compiler default output file name... a.out
checking whether the C compiler works... yes
checking whether we are cross compiling... no
checking for suffix of executables...
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether gcc accepts -g... yes
checking for gcc option to accept ISO C89... none needed
checking for style of include used by make... GNU
checking dependency style of gcc... gcc3
checking for ranlib... ranlib
checking for bison... bison -y
checking for flex... flex
checking lex output file root... lex.yy
checking lex library... -lfl
checking whether yytext is a pointer... yes
checking for pthread_create in -lpthread... yes
checking how to run the C preprocessor... gcc -E
checking for grep that handles long lines and -e... /bin/grep
checking for egrep... /bin/grep -E
checking for ANSI C header files... yes
checking for sys/wait.h that is POSIX.1 compatible... yes
checking for sys/types.h... yes
checking for sys/stat.h... yes
checking for stdlib.h... yes
checking for string.h... yes
checking for memory.h... yes
checking for strings.h... yes
checking for inttypes.h... yes
checking for stdint.h... yes
checking for unistd.h... yes
checking arpa/inet.h usability... yes
checking arpa/inet.h presence... yes
checking for arpa/inet.h... yes
checking malloc.h usability... yes
checking malloc.h presence... yes
checking for malloc.h... yes
checking netdb.h usability... yes
checking netdb.h presence... yes
checking for netdb.h... yes
checking netinet/in.h usability... yes
checking netinet/in.h presence... yes
checking for netinet/in.h... yes
checking for stdlib.h... (cached) yes
checking for string.h... (cached) yes
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking syslog.h usability... yes
checking syslog.h presence... yes
checking for syslog.h... yes
checking for unistd.h... (cached) yes
checking for an ANSI C-conforming const... yes
checking for inline... inline
checking for off_t... yes
checking for pid_t... yes
checking for size_t... yes
checking vfork.h usability... no
checking vfork.h presence... no
checking for vfork.h... no
checking for fork... yes
checking for vfork... yes
checking for working fork... yes
checking for working vfork... (cached) yes
checking for stdlib.h... (cached) yes
checking for GNU libc compatible malloc... yes
checking return type of signal handlers... void
checking for gethostbyname... yes
checking for inet_ntoa... yes
checking for strerror... yes
checking for strstr... yes
checking for strtol... yes
configure: Using /etc/hosts.allow as hosts.allow file
configure: creating ./config.status
config.status: creating Makefile
config.status: creating man/Makefile
config.status: creating src/Makefile
config.status: creating src/fwalls/Makefile
config.status: creating src/config.h
config.status: executing depfiles commands
dh_testdir
# Add here commands to compile the package.
/usr/bin/make
make[1]: se ingresa al directorio `/home/ecrespo/repositorio/repositorio'
cd . && /bin/sh /home/ecrespo/repositorio/repositorio/missing --run aclocal-1.10
cd . && /bin/sh /home/ecrespo/repositorio/repositorio/missing --run automake-1.10 --foreign
cd . && /bin/sh /home/ecrespo/repositorio/repositorio/missing --run autoconf
/bin/sh ./config.status --recheck
running CONFIG_SHELL=/bin/sh /bin/sh ./configure --build i486-linux-gnu --prefix=/usr --mandir=${prefix}/share/man --with-firewall=hosts --infodir=${prefix}/share/info CFLAGS=-g -O2 LDFLAGS=-Wl,-z,defs build_alias=i486-linux-gnu CPPFLAGS= --no-create --no-recursion
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
checking for a thread-safe mkdir -p... /bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking for gcc... gcc
checking for C compiler default output file name... a.out
checking whether the C compiler works... yes
checking whether we are cross compiling... no
checking for suffix of executables...
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether gcc accepts -g... yes
checking for gcc option to accept ISO C89... none needed
checking for style of include used by make... GNU
checking dependency style of gcc... gcc3
checking for ranlib... ranlib
checking for bison... bison -y
checking for flex... flex
checking lex output file root... lex.yy
checking lex library... -lfl
checking whether yytext is a pointer... yes
checking for pthread_create in -lpthread... yes
checking how to run the C preprocessor... gcc -E
checking for grep that handles long lines and -e... /bin/grep
checking for egrep... /bin/grep -E
checking for ANSI C header files... yes
checking for sys/wait.h that is POSIX.1 compatible... yes
checking for sys/types.h... yes
checking for sys/stat.h... yes
checking for stdlib.h... yes
checking for string.h... yes
checking for memory.h... yes
checking for strings.h... yes
checking for inttypes.h... yes
checking for stdint.h... yes
checking for unistd.h... yes
checking arpa/inet.h usability... yes
checking arpa/inet.h presence... yes
checking for arpa/inet.h... yes
checking malloc.h usability... yes
checking malloc.h presence... yes
checking for malloc.h... yes
checking netdb.h usability... yes
checking netdb.h presence... yes
checking for netdb.h... yes
checking netinet/in.h usability... yes
checking netinet/in.h presence... yes
checking for netinet/in.h... yes
checking for stdlib.h... (cached) yes
checking for string.h... (cached) yes
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking syslog.h usability... yes
checking syslog.h presence... yes
checking for syslog.h... yes
checking for unistd.h... (cached) yes
checking for an ANSI C-conforming const... yes
checking for inline... inline
checking for off_t... yes
checking for pid_t... yes
checking for size_t... yes
checking vfork.h usability... no
checking vfork.h presence... no
checking for vfork.h... no
checking for fork... yes
checking for vfork... yes
checking for working fork... yes
checking for working vfork... (cached) yes
checking for stdlib.h... (cached) yes
checking for GNU libc compatible malloc... yes
checking return type of signal handlers... void
checking for gethostbyname... yes
checking for inet_ntoa... yes
checking for strerror... yes
checking for strstr... yes
checking for strtol... yes
configure: Using /etc/hosts.allow as hosts.allow file
configure: creating ./config.status
/bin/sh ./config.status
config.status: creating Makefile
config.status: creating man/Makefile
config.status: creating src/Makefile
config.status: creating src/fwalls/Makefile
config.status: creating src/config.h
config.status: src/config.h is unchanged
config.status: executing depfiles commands
make[1]: se sale del directorio `/home/ecrespo/repositorio/repositorio'
make[1]: se ingresa al directorio `/home/ecrespo/repositorio/repositorio'
Making all in src
make[2]: se ingresa al directorio `/home/ecrespo/repositorio/repositorio/src'
cd .. && /bin/sh /home/ecrespo/repositorio/repositorio/missing --run autoheader
rm -f stamp-h1
touch config.h.in
cd .. && /bin/sh ./config.status src/config.h
config.status: creating src/config.h
config.status: src/config.h is unchanged
/usr/bin/make all-recursive
make[3]: se ingresa al directorio `/home/ecrespo/repositorio/repositorio/src'
Making all in fwalls
make[4]: se ingresa al directorio `/home/ecrespo/repositorio/repositorio/src/fwalls'
gcc -DHAVE_CONFIG_H -I. -I../../src -I. -I.. -O2 -g -O2 -MT hosts.o -MD -MP -MF .deps/hosts.Tpo -c -o hosts.o hosts.c
mv -f .deps/hosts.Tpo .deps/hosts.Po
rm -f libfwall.a
ar cru libfwall.a hosts.o
ranlib libfwall.a
make[4]: se sale del directorio `/home/ecrespo/repositorio/repositorio/src/fwalls'
make[4]: se ingresa al directorio `/home/ecrespo/repositorio/repositorio/src'
gcc -DHAVE_CONFIG_H -I. -I. -O2 -g -O2 -MT attack_parser.o -MD -MP -MF .deps/attack_parser.Tpo -c -o attack_parser.o attack_parser.c
mv -f .deps/attack_parser.Tpo .deps/attack_parser.Po
gcc -DHAVE_CONFIG_H -I. -I. -O2 -g -O2 -MT attack_scanner.o -MD -MP -MF .deps/attack_scanner.Tpo -c -o attack_scanner.o attack_scanner.c
mv -f .deps/attack_scanner.Tpo .deps/attack_scanner.Po
gcc -DHAVE_CONFIG_H -I. -I. -O2 -g -O2 -MT sshguard.o -MD -MP -MF .deps/sshguard.Tpo -c -o sshguard.o sshguard.c
mv -f .deps/sshguard.Tpo .deps/sshguard.Po
gcc -DHAVE_CONFIG_H -I. -I. -O2 -g -O2 -MT sshguard_whitelist.o -MD -MP -MF .deps/sshguard_whitelist.Tpo -c -o sshguard_whitelist.o sshguard_whitelist.c
mv -f .deps/sshguard_whitelist.Tpo .deps/sshguard_whitelist.Po
gcc -DHAVE_CONFIG_H -I. -I. -O2 -g -O2 -MT sshguard_log.o -MD -MP -MF .deps/sshguard_log.Tpo -c -o sshguard_log.o sshguard_log.c
mv -f .deps/sshguard_log.Tpo .deps/sshguard_log.Po
gcc -DHAVE_CONFIG_H -I. -I. -O2 -g -O2 -MT sshguard_procauth.o -MD -MP -MF .deps/sshguard_procauth.Tpo -c -o sshguard_procauth.o sshguard_procauth.c
mv -f .deps/sshguard_procauth.Tpo .deps/sshguard_procauth.Po
gcc -DHAVE_CONFIG_H -I. -I. -O2 -g -O2 -MT simclist.o -MD -MP -MF .deps/simclist.Tpo -c -o simclist.o simclist.c
mv -f .deps/simclist.Tpo .deps/simclist.Po
gcc -I. -O2 -g -O2 -Wl,-z,defs -o sshguard attack_parser.o attack_scanner.o sshguard.o sshguard_whitelist.o sshguard_log.o sshguard_procauth.o simclist.o fwalls/libfwall.a -lpthread
make[4]: se sale del directorio `/home/ecrespo/repositorio/repositorio/src'
make[3]: se sale del directorio `/home/ecrespo/repositorio/repositorio/src'
make[2]: se sale del directorio `/home/ecrespo/repositorio/repositorio/src'
Making all in man
make[2]: se ingresa al directorio `/home/ecrespo/repositorio/repositorio/man'
make[2]: No se hace nada para `all'.
make[2]: se sale del directorio `/home/ecrespo/repositorio/repositorio/man'
make[2]: se ingresa al directorio `/home/ecrespo/repositorio/repositorio'
make[2]: No se hace nada para `all-am'.
make[2]: se sale del directorio `/home/ecrespo/repositorio/repositorio'
make[1]: se sale del directorio `/home/ecrespo/repositorio/repositorio'
#docbook-to-man debian/sshguard.sgml > sshguard.1
touch build-stamp
fakeroot debian/rules binary
dh_testdir
dh_testroot
dh_prep
dh_installdirs
# Add here commands to install the package into debian/sshguard.
/usr/bin/make DESTDIR=/home/ecrespo/repositorio/repositorio/debian/sshguard install
make[1]: se ingresa al directorio `/home/ecrespo/repositorio/repositorio'
Making install in src
make[2]: se ingresa al directorio `/home/ecrespo/repositorio/repositorio/src'
/usr/bin/make install-recursive
make[3]: se ingresa al directorio `/home/ecrespo/repositorio/repositorio/src'
Making install in fwalls
make[4]: se ingresa al directorio `/home/ecrespo/repositorio/repositorio/src/fwalls'
make[5]: se ingresa al directorio `/home/ecrespo/repositorio/repositorio/src/fwalls'
make[5]: No se hace nada para `install-exec-am'.
make[5]: No se hace nada para `install-data-am'.
make[5]: se sale del directorio `/home/ecrespo/repositorio/repositorio/src/fwalls'
make[4]: se sale del directorio `/home/ecrespo/repositorio/repositorio/src/fwalls'
make[4]: se ingresa al directorio `/home/ecrespo/repositorio/repositorio/src'
make[5]: se ingresa al directorio `/home/ecrespo/repositorio/repositorio/src'
test -z "/usr/sbin" || /bin/mkdir -p "/home/ecrespo/repositorio/repositorio/debian/sshguard/usr/sbin"
/usr/bin/install -c 'sshguard' '/home/ecrespo/repositorio/repositorio/debian/sshguard/usr/sbin/sshguard'
make[5]: No se hace nada para `install-data-am'.
make[5]: se sale del directorio `/home/ecrespo/repositorio/repositorio/src'
make[4]: se sale del directorio `/home/ecrespo/repositorio/repositorio/src'
make[3]: se sale del directorio `/home/ecrespo/repositorio/repositorio/src'
make[2]: se sale del directorio `/home/ecrespo/repositorio/repositorio/src'
Making install in man
make[2]: se ingresa al directorio `/home/ecrespo/repositorio/repositorio/man'
make[3]: se ingresa al directorio `/home/ecrespo/repositorio/repositorio/man'
make[3]: No se hace nada para `install-exec-am'.
test -z "/usr/share/man/man8" || /bin/mkdir -p "/home/ecrespo/repositorio/repositorio/debian/sshguard/usr/share/man/man8"
/usr/bin/install -c -m 644 './sshguard.8' '/home/ecrespo/repositorio/repositorio/debian/sshguard/usr/share/man/man8/sshguard.8'
make[3]: se sale del directorio `/home/ecrespo/repositorio/repositorio/man'
make[2]: se sale del directorio `/home/ecrespo/repositorio/repositorio/man'
make[2]: se ingresa al directorio `/home/ecrespo/repositorio/repositorio'
make[3]: se ingresa al directorio `/home/ecrespo/repositorio/repositorio'
make[3]: No se hace nada para `install-exec-am'.
make[3]: No se hace nada para `install-data-am'.
make[3]: se sale del directorio `/home/ecrespo/repositorio/repositorio'
make[2]: se sale del directorio `/home/ecrespo/repositorio/repositorio'
make[1]: se sale del directorio `/home/ecrespo/repositorio/repositorio'
dh_testdir
dh_testroot
dh_installchangelogs Changes
dh_installdocs
dh_installexamples
dh_installman
dh_link
dh_strip
dh_compress
dh_fixperms
dh_installdeb
dh_shlibdeps
dh_gencontrol
dpkg-gencontrol: warning: unknown substitution variable ${misc:Depends}
dh_md5sums
dh_builddeb
dpkg-deb: construyendo el paquete `sshguard' en `../sshguard_1.3-2_i386.deb'.
dpkg-genchanges >../sshguard_1.3-2_i386.changes
dpkg-genchanges: not including original source code in upload
dpkg-buildpackage: binary and diff upload (original source NOT included)
Now running lintian...
Finished running lintian.
Now signing changes and any dsc files...
signfile sshguard_1.3-2.dsc C97E7015

Necesita una frase contraseña para desbloquear la clave secreta
del usuario: "Ernesto Nadir Crespo Avila (seraph1) "
clave DSA de 1024 bits, ID C97E7015, creada el 2005-08-15


signfile sshguard_1.3-2_i386.changes C97E7015

Necesita una frase contraseña para desbloquear la clave secreta
del usuario: "Ernesto Nadir Crespo Avila (seraph1) "
clave DSA de 1024 bits, ID C97E7015, creada el 2005-08-15


Successfully signed dsc and changes files
```

En este momento se tiene el paquete .deb y los archivos creados en el momento del empaquetado:

```
ecrespo@canaima:~/repositorio$ ls
sshguard_1.3-2.diff.gz sshguard_1
.3-2_i386.build sshguard_1.3-2_i386.deb
repositorio sshguard_1.3-2.dsc sshguard_1.3-2_i386.changes sshguard_1.3.orig.tar.gz
```




===

¡Haz tu donativo!
Si te gustó el artículo puedes realizar un donativo con Bitcoin (BTC)
usando la billetera digital de tu preferencia a la siguiente
dirección: 17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV

O Escaneando el código QR desde billetera:

![17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV](./imagenes/17MtNybhdkA9GV3UNS6BTwPcuhjXoPrSzV.png)
