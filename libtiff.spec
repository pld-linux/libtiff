#
# _without_lzw - without LZW compression (was patented in some countries)
Summary:	Library for handling TIFF files
Summary(de):	Library zum Verwalten von TIFF-Dateien
Summary(fr):	Bibliothèque de gestion des fichiers TIFF
Summary(pl):	Bibliteka do manipulacji plikami w formacie TIFF
Summary(tr):	TIFF dosyalarýný iþleme kitaplýðý
Name:		libtiff
Version:	3.5.7
Release:	2
License:	distributable
Group:		Libraries
Source0:	ftp://ftp.remotesensing.org/pub/libtiff/tiff-v%{version}.tar.gz
# Source0-md5:	82243b5ae9b7c9e492aeebc501680990
Source1:	ftp://ftp.remotesensing.org/pub/libtiff/%{name}-lzw-compression-kit-1.2.tar.gz
# Source1-md5:	bb8d85b3f29b78edf8a06a7831b4df31
Patch0:		tiff-shlib.patch
Patch1:		%{name}-libmess.patch
Patch2:		%{name}-security.patch
URL:		http://www.libtiff.org/
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is a library of functions that manipulate TIFF images.

%description -l de
Eine Library von Funktionen zur Manipulation von TIFFs.

%description -l fr
Bibliothèque de fonctions pour manipuler des images TIFF.

%description -l pl
Ten pakiet zawiera bibliotekê pozalaj±ce manipulowaæ plikami w
formacie TIFF.

%description -l tr
Bu paket TIFF resimlerini iþleyen fonksiyonlardan oluþan bir
kitaplýktýr.

%package devel
Summary:	header files for developing programs using libtiff
Summary(de):	Header zur Entwicklung von Programmen unter Verwendung von libtiff
Summary(pl):	Pliki nag³ówkowe do biblioteki libtiff
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

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

%package static
Summary:	Static version libtiff library
Summary(pl):	Biblioteka statyczna libtiff
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libtiff library.

%description static -l pl
Statyczna biblioteka libtiff.

%prep
%setup -q -n tiff-v%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%if %{?_without_lzw:0}%{!?_without_lzw:1}
tar xzf %{SOURCE1}
cp -f libtiff-lzw-compression-kit/*.c libtiff
cp -f libtiff-lzw-compression-kit/README-LZW-COMPRESSION .
libtiff-lzw-compression-kit/mangle-src.sh `pwd`
%endif

%build
install /usr/share/automake/config.* .
./configure %{_target_platform} \
	--with-ZIP \
	--with-JPEG \
	--noninteractive \
	--prefix=$RPM_BUILD_ROOT%{_prefix} \
	--with-DIR_MAN=$RPM_BUILD_ROOT%{_mandir} \
	--with-DIR_HTML=$RPM_BUILD_ROOT/fake \
	--with-MANSCHEME=bsd-source-cat

ln -sf libtiff.so.%{version} libtiff/libtiff.so
%{__make} -C libtiff \
	OPTIMIZER="%{rpmcflags}" \
	CC="%{__cc}" \
	COPTS=""
%{__make} -C tools \
	OPTIMIZER="%{rpmcflags}" \
	CC="%{__cc}" \
	COPTS=""

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir},%{_bindir},%{_mandir}/man1}

%{__make} install
install libtiff/lib*.so.*.* $RPM_BUILD_ROOT%{_libdir}

ln -sf libtiff.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libtiff.so

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
