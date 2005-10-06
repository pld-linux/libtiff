Summary:	Library for handling TIFF files
Summary(de):	Library zum Verwalten von TIFF-Dateien
Summary(fr):	Bibliothèque de gestion des fichiers TIFF
Summary(pl):	Bibliteka do manipulacji plikami w formacie TIFF
Summary(tr):	TIFF dosyalarýný iþleme kitaplýðý
Name:		libtiff
Version:	3.7.4
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	ftp://ftp.remotesensing.org/pub/libtiff/tiff-%{version}.tar.gz
# Source0-md5:	f37a7907bca4e235da85eb0126caa2b0
URL:		http://www.remotesensing.org/libtiff/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	glut-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
This package is a library of functions that manipulate TIFF images.

%description -l de
Eine Library von Funktionen zur Manipulation von TIFFs.

%description -l fr
Bibliothèque de fonctions pour manipuler des images TIFF.

%description -l pl
Ten pakiet zawiera bibliotekê pozwalaj±c± manipulowaæ plikami w
formacie TIFF.

%description -l tr
Bu paket TIFF resimlerini iþleyen fonksiyonlardan oluþan bir
kitaplýktýr.

%package devel
Summary:	Header files for developing programs using libtiff
Summary(de):	Header zur Entwicklung von Programmen unter Verwendung von libtiff
Summary(pl):	Pliki nag³ówkowe do biblioteki libtiff
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libjpeg-devel
Requires:	zlib-devel

%description devel
This package is all you need to develop programs that manipulate tiff
images.

%description devel -l de
Dieses Paket enthält alles, was Sie zum Entwickeln von Programmen zum
Bearbeiten von tiff-Bildern benötigen.

%description devel -l fr
Ce package contient tout le nécessaire pour réaliser des programmes
manipulant des images au format tiff.

%description devel -l pl
Pakiet ten zawiera wszystko co potrzebujesz przy pisaniu programów
operuj±cych na formacie tiff.

%description devel -l tr
tiff resimlerini iþleyen programlar yazmak için gerekli dosyalar bu
pakette yer alýr.

%package static
Summary:	Static version libtiff library
Summary(pl):	Biblioteka statyczna libtiff
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libtiff library.

%description static -l pl
Statyczna biblioteka libtiff.

%package cxx
Summary:	libtiff C++ streams library
Summary(pl):	Biblioteka strumieni C++ dla libtiff
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description cxx
libtiff C++ streams library.

%description cxx -l pl
Biblioteka strumieni C++ dla libtiff.

%package cxx-devel
Summary:	libtiff C++ streams API
Summary(pl):	API strumieni C++ dla libtiff
Group:		Development/Libraries
Requires:	%{name}-cxx = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description cxx-devel
libtiff C++ streams API.

%description cxx-devel -l pl
API strumieni C++ dla libtiff.

%package cxx-static
Summary:	libtiff C++ streams static library
Summary(pl):	Statyczna biblioteka strumieni C++ dla libtiff
Group:		Development/Libraries
Requires:	%{name}-cxx-devel = %{version}-%{release}

%description cxx-static
libtiff C++ streams static library.

%description cxx-static -l pl
Statyczna biblioteka strumieni C++ dla libtiff.

%package progs
Summary:	Simple clients for manipulating tiff images
Summary(de):	Einfachen Clients zur Manipulation von tiff
Summary(fr):	Clients simples pour manipuler de telles images
Summary(pl):	Kilka prostych programów do manipulowania na plikach tiff
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs
Simple clients for manipulating tiff images.

%description progs -l de
Einfachen Clients zur Manipulation von tiff.

%description progs -l fr
Clients simples pour manipuler de telles images.

%description progs -l pl
Kilka prostych programów do manipulowania na plikach tiff.

%package progs-gl
Summary:	tiffgt - OpenGL-based tiff viewer
Summary(pl):	tiffgt - program do ogl±dania plików tiff oparty o OpenGL
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs-gl
tiffgt - OpenGL-based tiff viewer.

%description progs-gl -l pl
tiffgt - program do ogl±dania plików tiff oparty o OpenGL.

%prep
%setup -q -n tiff-%{version}

rm -f m4/libtool.m4

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir},%{_bindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf html{,/*}/Makefile* $RPM_BUILD_ROOT%{_docdir}/tiff-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYRIGHT ChangeLog README TODO
%attr(755,root,root) %{_libdir}/libtiff.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc html/*
%attr(755,root,root) %{_libdir}/libtiff.so
%{_libdir}/libtiff.la
%{_includedir}/tiff*.h
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libtiff.a

%files cxx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtiffxx.so.*.*.*

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
%attr(755,root,root) %{_bindir}/*
%exclude %{_bindir}/tiffgt
%{_mandir}/man1/*
%exclude %{_mandir}/man1/tiffgt.1*

%files progs-gl
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/tiffgt
%{_mandir}/man1/tiffgt.1*
