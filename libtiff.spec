#
# Conditional build:
# _without_lzw - without LZW compression (patented in some countries)
#
Summary:	Library for handling TIFF files
Summary(de):	Library zum Verwalten von TIFF-Dateien
Summary(fr):	Biblioth�que de gestion des fichiers TIFF
Summary(pl):	Bibliteka do manipulacji plikami w formacie TIFF
Summary(tr):	TIFF dosyalar�n� i�leme kitapl���
Name:		libtiff
Version:	3.6.0
Release:	0.beta2.2
License:	distributable
Group:		Libraries
Source0:	ftp://ftp.remotesensing.org/pub/libtiff/tiff-v%{version}-beta2.tar.gz
# Source0-md5:	647ba1a4c9a22ace5611d82de14cae10
Source1:	ftp://ftp.remotesensing.org/pub/libtiff/%{name}-lzw-compression-kit-1.4.tar.gz
# Source1-md5:	8e548335de1cf38898722943cc21e27b
URL:		http://www.libtiff.org/
BuildRequires:	libjpeg-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is a library of functions that manipulate TIFF images.

%description -l de
Eine Library von Funktionen zur Manipulation von TIFFs.

%description -l fr
Biblioth�que de fonctions pour manipuler des images TIFF.

%description -l pl
Ten pakiet zawiera bibliotek� pozalaj�ce manipulowa� plikami w
formacie TIFF.

%description -l tr
Bu paket TIFF resimlerini i�leyen fonksiyonlardan olu�an bir
kitapl�kt�r.

%package devel
Summary:	Header files for developing programs using libtiff
Summary(de):	Header zur Entwicklung von Programmen unter Verwendung von libtiff
Summary(pl):	Pliki nag��wkowe do biblioteki libtiff
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This package is all you need to develop programs that manipulate tiff
images.

%description devel -l de
Dieses Paket enth�lt alles, was Sie zum Entwickeln von Programmen zum
Bearbeiten von tiff-Bildern ben�tigen.

%description devel -l fr
Ce package contient tout le n�cessaire pour r�aliser des programmes
manipulant des images au format tiff.

%description devel -l pl
Pakiet ten zawiera wszystko co potrzebujesz przy pisaniu program�w
operuj�cych na formacie tiff.

%description devel -l tr
tiff resimlerini i�leyen programlar yazmak i�in gerekli dosyalar bu
pakette yer al�r.

%package progs
Summary:	Simple clients for manipulating tiff images
Summary(de):	Einfachen Clients zur Manipulation von tiff
Summary(fr):	Clients simples pour manipuler de telles images
Summary(pl):	Kilka prostych program�w do manipulowania na plikach tiff
Group:		Applications/Graphics
Requires:	%{name} = %{version}

%description progs
Simple clients for manipulating tiff images.

%description progs -l de
Einfachen Clients zur Manipulation von tiff.

%description progs -l fr
Clients simples pour manipuler de telles images.

%description progs -l pl
Kilka prostych program�w do manipulowania na plikach tiff.

%package static
Summary:	Static version libtiff library
Summary(pl):	Biblioteka statyczna libtiff
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libtiff library.

%description static -l pl
Statyczna biblioteka libtiff.

%prep
%setup  -q -n tiff-v%{version}-beta2

%if 0%{!?_without_lzw:1}
tar xzf %{SOURCE1}
cp -f libtiff-lzw-compression-kit-1.4/*.c libtiff
cp -f libtiff-lzw-compression-kit-1.4/README-LZW-COMPRESSION .
%endif

%build
./configure %{_target_platform} \
	--with-ZIP \
	--with-JPEG \
	--noninteractive \
	--prefix=$RPM_BUILD_ROOT%{_prefix} \
	--with-DIR_MAN=$RPM_BUILD_ROOT%{_mandir} \
	--with-DIR_HTML=$RPM_BUILD_ROOT/fake \
	--with-MANSCHEME=bsd-source-cat

%{__make} -C libtiff OPTIMIZER="%{rpmcflags}" CC=%{__cc} COPTS=""
%{__make} -C tools OPTIMIZER="%{rpmcflags}" CC=%{__cc} COPTS=""

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir},%{_bindir},%{_mandir}/man1}

%{__make} install

rm -rf html/{*/CVS,Makefile*}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYRIGHT README* TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc html/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*
%{_mandir}/man3/*

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
