#
# _without_lzw - without LZW compression (patented in some countries)
Summary:	Library for handling TIFF files
Summary(de):	Library zum Verwalten von TIFF-Dateien
Summary(fr):	BibliothËque de gestion des fichiers TIFF
Summary(pl):	Bibliteka do manipulacji plikami w formacie TIFF 
Summary(tr):	TIFF dosyalar˝n˝ i˛leme kitapl˝˝
Name:		libtiff
%define		ver	3.5.6
Version:	%{ver}beta
Release:	1
License:	distributable
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	ftp://ftp.remotesensing.org/pub/libtiff/tiff-v%{ver}-beta.tar.gz
Source1:	ftp://ftp.remotesensing.org/pub/libtiff/%{name}-lzw-compression-kit-1.2.tar.gz
Patch0:		tiff-shlib.patch
Patch1:		%{name}-arm.patch
Patch2:		tiff-config.patch
Patch3:		%{name}-libmess.patch
URL:		http://www.libtiff.org/
BuildRequires:	zlib-devel
BuildRequires:	libjpeg-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is a library of functions that manipulate TIFF images.

%description -l de
Eine Library von Funktionen zur Manipulation von TIFFs.

%description -l fr
BibliothËque de fonctions pour manipuler des images TIFF.

%description -l pl
Ten pakiet zawiera bibliotekÍ pozalaj±ce manipulowaÊ plikami w
formacie TIFF.

%description -l tr
Bu paket TIFF resimlerini i˛leyen fonksiyonlardan olu˛an bir
kitapl˝kt˝r.

%package devel
Summary:	header files for developing programs using libtiff
Summary(de):	Header zur Entwicklung von Programmen unter Verwendung von libtiff 
Summary(pl):	Pliki nag≥Ûwkowe do biblioteki libtiff
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
This package is all you need to develop programs that manipulate tiff
images.

%description -l de devel
Dieses Paket enth‰lt alles, was Sie zum Entwickeln von Programmen zum
Bearbeiten von tiff-Bildern benˆtigen.

%description -l fr devel
Ce package contient tout le nÈcessaire pour rÈaliser des programmes
manipulant des images au format tiff.

%description -l pl devel
Pakiet ten zawiera wszystko co potrzebujesz przy pisaniu programÛw
operuj±cych na formacie tiff.

%description -l tr devel
tiff resimlerini i˛leyen programlar yazmak iÁin gerekli dosyalar bu
pakette yer al˝r.

%package progs
Summary:	Simple clients for manipulating tiff images
Summary(de):	Einfachen Clients zur Manipulation von tiff
Summary(fr):	Clients simples pour manipuler de telles images
Summary(pl):	Kilka prostych programÛw do manipulowania na plikach tiff
Group:		Applications/Graphics
Group(de):	Applikationen/Grafik
Group(pl):	Aplikacje/Grafika
Requires:	%{name} = %{version}

%description progs
Simple clients for manipulating tiff images.

%description progs -l de
Einfachen Clients zur Manipulation von tiff.

%description progs -l fr
Clients simples pour manipuler de telles images.

%description progs -l pl
Kilka prostych programÛw do manipulowania na plikach tiff.

%package static
Summary:	Static version libtiff library
Summary(pl):	Biblioteka statyczna libtiff
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Static libtiff library.

%description static -l pl
Statyczna bibliteka libtiff.

%prep
%setup  -q -n tiff-v%{ver}-beta
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%if %{?_without_lzw:0}%{!?_without_lzw:1}
tar xzf %{SOURCE1}
cp -f libtiff-lzw-compression-kit/*.c libtiff
cp -f libtiff-lzw-compression-kit/README-LZW-COMPRESSION .
libtiff-lzw-compression-kit/mangle-src.sh `pwd`
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
	
(cd libtiff ; ln -sf libtiff.so.3.5.6 libtiff.so)
%{__make} COPTS="%{rpmcflags}" LDOPTS="%{rpmldflags}" OPTIMIZER=""

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir},%{_bindir},%{_mandir}/man1}

%{__make} install
install libtiff/lib*.so.*.* $RPM_BUILD_ROOT%{_libdir}

ln -sf libtiff.so.3.5.6 $RPM_BUILD_ROOT%{_libdir}/libtiff.so

gzip -9nf COPYRIGHT README* TODO

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {COPYRIGHT,README*,TODO}.gz
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
