Summary:	Tool for converting C/C++ sources to PostScript
Summary(pl):	Narzêdzie do konwersji ¼róde³ C/C++ na PostScript
Name:		c2ps
Version:	4.0
Release:	1
Group:		Utilities/Printing
Group(pl):	Narzêdzia/Drukowanie
License:	GPL
Source0:	http://www.geocities.com/SiliconValley/Park/2055/%{name}-40.tgz
Patch0:		c2ps-OPT_FLAGS.patch
URL:		http://www.geocities.com/SiliconValley/Park/2055/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This small utility converts C/C++ sources to PostScript. It performs syntax
highlighting and can add many, very usefull informations to the printout, such
as line numbers, headers and indexes of functions on each page. Great thing, if
you waste too much time in traffic jams or public transport ;)

%description -l pl
To ma³e na¿êdzie konwertuje pliki ¼ród³owe C/C++ do PostScriptu. Wykonuje
wyró¿nianie sk³adni a tak¿e potrafi dodaæ do wydruku wiele bardzo u¿ytecznych
informacji, takich jak numery linii, nag³ówki oraz indeksy funkcji znajduj±cych
siê na poszczególnych stronach. ¦wieta rzecz, je¶li tracisz zbyt du¿o czasu
stoj±c w korkach, albo w komunikacji miejskiej ;)

%prep
%setup -q
%patch0 -p1

%build
%{__make} OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install c2ps	$RPM_BUILD_ROOT%{_bindir}
install c2ps.1	$RPM_BUILD_ROOT%{_mandir}/man1

strip c2ps

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*
