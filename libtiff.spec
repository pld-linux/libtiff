Summary:	Library for handling TIFF files.
Summary(de):	Library zum Verwalten von TIFF-Dateien
Summary(fr):	Bibliothèque de gestion des fichiers TIFF
Summary(pl):	Bibliteka do manipulacji plikami w formacie TIFF 
Summary(tr):	TIFF dosyalarýný iþleme kitaplýðý
Name:		libtiff
Version:	3.4
Release:	9
Copyright:	distributable
Group:		Libraries
Group(pl):	Biblioteki
Source:		ftp://ftp.sgi.com/graphics/tiff/tiff-v%{version}-tar.gz
Patch0:		tiff-glibc.patch
Patch1:		tiff-shlib.patch
Patch2:		libtiff-arm.patch
URL:		http://www-mipl.jpl.nasa.gov/~ndr/tiff/
Buildroot:	/tmp/%{name}-%{version}-root

%description
This package is a library of functions that manipulate TIFF images.

%description -l de
Eine Library von Funktionen zur Manipulation von TIFFs. 

%description -l fr
Bibliothèque de fonctions pour manipuler des images TIFF."

%description -l pl
Ten pakiet zawiera bibliotekê pozalaj±ce manipulowaæ formatem TIFF.

%description -l tr
Bu paket TIFF resimlerini iþleyen fonksiyonlardan oluþan bir kitaplýktýr.

%package devel
Summary:	header files for developing programs using libtiff
Summary(de):	Header zur Entwicklung von Programmen  unter Verwendung von libtiff 
Summary(pl):	Pliki nag³ówkowe do biblioteki libtiff
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
This package is all you need to develop programs that manipulate tiff
images.

%description -l pl devel
Pakiet ten zawiera wszystko co potrzebujesz przy pisaniu programów
operuj±cych na formacie tiff.

%description -l de devel
Dieses Paket enthält alles, was Sie zum Entwickeln von Programmen
zum Bearbeiten von tiff-Bildern benötigen.

%description -l fr devel
Ce package contient tout le nécessaire pour réaliser des programmes
manipulant des images au format tiff.

%description -l tr devel
tiff resimlerini iþleyen programlar yazmak için gerekli dosyalar bu pakette
yer alýr.

%package progs
Summary:	Simple clients for manipulating tiff images
Summary(de):	Einfachen Clients zur Manipulation von tiff
Summary(fr):	Clients simples pour manipuler de telles images
Summary(pl):	Kilka prostych programów do manipulowania na plikach tiff
Group:		Applications/Graphics
Group(pl):	Aplikacje/Grafika
Requires:	%{name} = %{version}

%description progs
Simple clients for manipulating tiff images.

%description progs -l de
Einfachen Clients zur Manipulation von tiff.

%description progs -l fr
Clients simples pour manipuler de telles images.

%description progs -l pl
Kilka prostych programów do manipulowania na plikach tiff.

%package static
Summary:	Static version libtiff library
Summary(pl):	Biblioteka statyczna libtiff
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libtiff library.

%description static -l pl
Statyczna bibliteka libtiff.

%prep
%setup -q -n tiff-v%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
GCOPTS=" " \
./configure %{_target} << EOF
no
$RPM_BUILD_ROOT/usr/bin
$RPM_BUILD_ROOT/usr/lib
$RPM_BUILD_ROOT/usr/include
$RPM_BUILD_ROOT%{_mandir}
bsd-source-cat
yes
EOF
make OPTIMIZER="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{lib,include,bin,man/man1}

make install
install -s libtiff/lib*.so.*.* $RPM_BUILD_ROOT/usr/lib

ln -sf libtiff.so.%{version} $RPM_BUILD_ROOT/usr/lib/libtiff.so

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	COPYRIGHT README TODO

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/lib/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc {COPYRIGHT,README,TODO}.gz html/*
/usr/lib/lib*.so
/usr/include/*
%{_mandir}/man3/*

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) /usr/bin/*
%{_mandir}/man1/*

%files static
%defattr(644,root,root,755)
/usr/lib/lib*.a

%changelog
* Sat Apr 24 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.4-8]
- recompiles on new rpm.

* Sun Mar 14 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [3.4-7]
- added Group(pl)
- added gzipping documentation and man pages
- minor changes

* Sat Aug  8 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.4-6]
- modified pl translation,
- added -q %setup parameter and added using %%{version} in -n,
- added using $RPM_OPT_FLAGS during compile,
- added static an progs subpackages,
- Buildroot changed to /tmp/%%{name}-%%{version}-root,
- removed VERSION from devel %doc,
- changed Requires to "Requires: %%{name}-%%{version}",
- added stripping shared libs,
- removed using LIBVER macro.

* Thu Jul 16 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [3.4-5]
- added pl translation,
- added %defattr mafros in %files (for build from not root's account),
- changed permision of *.so library to 755.

* Tue Jun 30 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
- build against glibc-2.1

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Oct 13 1997 Donnie Barnes <djb@redhat.com>
- new version to replace the one from libgr
- patched for glibc
- added shlib support
