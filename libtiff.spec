#
# Conditional build:
%bcond_without	opengl	# do not build OpenGL viewer
%bcond_with	jpeg12	# dual 8/12-bit libjpeg mode
#
Summary:	Library for handling TIFF files
Summary(de.UTF-8):	Library zum Verwalten von TIFF-Dateien
Summary(fr.UTF-8):	Bibliothèque de gestion des fichiers TIFF
Summary(pl.UTF-8):	Biblioteka do manipulacji plikami w formacie TIFF
Summary(tr.UTF-8):	TIFF dosyalarını işleme kitaplığı
Name:		libtiff
Version:	4.0.9
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://download.osgeo.org/libtiff/tiff-%{version}.tar.gz
# Source0-md5:	54bad211279cc93eb4fca31ba9bfdc79
Patch0:		%{name}-glut.patch
URL:		http://www.simplesystems.org/libtiff/
%{?with_opengl:BuildRequires:  OpenGL-glut-devel}
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11
BuildRequires:	jbigkit-devel
BuildRequires:	libjpeg-devel
%{?with_jpeg12:BuildRequires:	libjpeg12-devel}
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2.2
%{?with_opengl:BuildRequires:	xorg-lib-libX11-devel}
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is a library of functions that manipulate TIFF images.

%description -l de.UTF-8
Eine Library von Funktionen zur Manipulation von TIFFs.

%description -l fr.UTF-8
Bibliothèque de fonctions pour manipuler des images TIFF.

%description -l pl.UTF-8
Ten pakiet zawiera bibliotekę pozwalającą manipulować plikami w
formacie TIFF.

%description -l tr.UTF-8
Bu paket TIFF resimlerini işleyen fonksiyonlardan oluşan bir
kitaplıktır.

%package devel
Summary:	Header files for developing programs using libtiff
Summary(de.UTF-8):	Header zur Entwicklung von Programmen unter Verwendung von libtiff
Summary(pl.UTF-8):	Pliki nagłówkowe do biblioteki libtiff
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	jbigkit-devel
Requires:	libjpeg-devel
%{?with_jpeg12:Requires:	libjpeg12-devel}
Requires:	xz-devel
Requires:	zlib-devel

%description devel
This package is all you need to develop programs that manipulate tiff
images.

%description devel -l de.UTF-8
Dieses Paket enthält alles, was Sie zum Entwickeln von Programmen zum
Bearbeiten von tiff-Bildern benötigen.

%description devel -l fr.UTF-8
Ce package contient tout le nécessaire pour réaliser des programmes
manipulant des images au format tiff.

%description devel -l pl.UTF-8
Pakiet ten zawiera wszystko co potrzebujesz przy pisaniu programów
operujących na formacie tiff.

%description devel -l tr.UTF-8
tiff resimlerini işleyen programlar yazmak için gerekli dosyalar bu
pakette yer alır.

%package static
Summary:	Static version libtiff library
Summary(pl.UTF-8):	Biblioteka statyczna libtiff
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libtiff library.

%description static -l pl.UTF-8
Statyczna biblioteka libtiff.

%package cxx
Summary:	libtiff C++ streams library
Summary(pl.UTF-8):	Biblioteka strumieni C++ dla libtiff
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description cxx
libtiff C++ streams library.

%description cxx -l pl.UTF-8
Biblioteka strumieni C++ dla libtiff.

%package cxx-devel
Summary:	libtiff C++ streams API
Summary(pl.UTF-8):	API strumieni C++ dla libtiff
Group:		Development/Libraries
Requires:	%{name}-cxx = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description cxx-devel
libtiff C++ streams API.

%description cxx-devel -l pl.UTF-8
API strumieni C++ dla libtiff.

%package cxx-static
Summary:	libtiff C++ streams static library
Summary(pl.UTF-8):	Statyczna biblioteka strumieni C++ dla libtiff
Group:		Development/Libraries
Requires:	%{name}-cxx-devel = %{version}-%{release}

%description cxx-static
libtiff C++ streams static library.

%description cxx-static -l pl.UTF-8
Statyczna biblioteka strumieni C++ dla libtiff.

%package progs
Summary:	Simple clients for manipulating tiff images
Summary(de.UTF-8):	Einfachen Clients zur Manipulation von tiff
Summary(fr.UTF-8):	Clients simples pour manipuler de telles images
Summary(pl.UTF-8):	Kilka prostych programów do manipulowania na plikach tiff
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs
Simple clients for manipulating tiff images.

%description progs -l de.UTF-8
Einfachen Clients zur Manipulation von tiff.

%description progs -l fr.UTF-8
Clients simples pour manipuler de telles images.

%description progs -l pl.UTF-8
Kilka prostych programów do manipulowania na plikach tiff.

%package progs-gl
Summary:	tiffgt - OpenGL-based tiff viewer
Summary(pl.UTF-8):	tiffgt - program do oglądania plików tiff oparty o OpenGL
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs-gl
tiffgt - OpenGL-based tiff viewer.

%description progs-gl -l pl.UTF-8
tiffgt - program do oglądania plików tiff oparty o OpenGL.

%prep
%setup -q -n tiff-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_opengl:--without-x} \
	%{?with_jpeg12:--enable-jpeg12 --with-jpeg12-include-dir=%{_includedir}/libjpeg12 --with-jpeg12-lib=-ljpeg12}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r html{,/*}/Makefile* $RPM_BUILD_ROOT%{_docdir}/tiff-%{version}

# libtiff*.la kept - no .pc file for libtiffxx

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYRIGHT ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libtiff.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtiff.so.5

%files devel
%defattr(644,root,root,755)
%doc html/*
%attr(755,root,root) %{_libdir}/libtiff.so
%{_libdir}/libtiff.la
%{_includedir}/tiff*.h
%{_pkgconfigdir}/libtiff-4.pc
%{_mandir}/man3/TIFF*.3tiff*
%{_mandir}/man3/libtiff.3tiff*

%files static
%defattr(644,root,root,755)
%{_libdir}/libtiff.a

%files cxx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtiffxx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtiffxx.so.5

%files cxx-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtiffxx.so
%{_libdir}/libtiffxx.la
%{_includedir}/tiffio.hxx

%files cxx-static
%defattr(644,root,root,755)
%{_libdir}/libtiffxx.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fax2ps
%attr(755,root,root) %{_bindir}/fax2tiff
%attr(755,root,root) %{_bindir}/pal2rgb
%attr(755,root,root) %{_bindir}/ppm2tiff
%attr(755,root,root) %{_bindir}/raw2tiff
%attr(755,root,root) %{_bindir}/tiff[!g]*
%{_mandir}/man1/fax2ps.1*
%{_mandir}/man1/fax2tiff.1*
%{_mandir}/man1/pal2rgb.1*
%{_mandir}/man1/ppm2tiff.1*
%{_mandir}/man1/raw2tiff.1*
%{_mandir}/man1/tiff[!g]*.1*

%if %{with opengl}
%files progs-gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tiffgt
%{_mandir}/man1/tiffgt.1*
%endif
