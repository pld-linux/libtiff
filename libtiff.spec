Summary:	Library for handling TIFF files.
Summary(de):	Library zum Verwalten von TIFF-Dateien
Summary(fr):	Bibliothèque de gestion des fichiers TIFF
Summary(pl):	Bibliteka do manipulacji plikami w formacie TIFF 
Summary(tr):	TIFF dosyalarýný iþleme kitaplýðý
Name:		libtiff
Version:	3.4
Release:	10
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
./configure %{_target_platform} << EOF
no
$RPM_BUILD_ROOT%{_bindir}
$RPM_BUILD_ROOT%{_libdir}
$RPM_BUILD_ROOT%{_includedir}
$RPM_BUILD_ROOT%{_mandir}
bsd-source-cat
yes
EOF
make OPTIMIZER="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir},%{_bindir},%{_mandir}/man1}

make install
install -s libtiff/lib*.so.*.* $RPM_BUILD_ROOT%{_libdir}

ln -sf libtiff.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libtiff.so

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	COPYRIGHT README TODO

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc {COPYRIGHT,README,TODO}.gz html/*
%{_libdir}/lib*.so
%{_includedir}/*
%{_mandir}/man3/*

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%changelog
* Mon May 24 1999 Artur Frysiak <wiget@pld.org.pl>
  [3.4-10]
- based on RH spec
- rewrite to PLD style (by PLD team)
- pl translation by Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
