Summary:	Tool for converting C/C++ sources to PostScript
Summary(pl.UTF-8):	Narzędzie do konwersji źródeł C/C++ na PostScript
Name:		c2ps
Version:	4.0
Release:	3
License:	GPL
Group:		Applications/Printing
Source0:	http://www.geocities.com/SiliconValley/Park/2055/%{name}-40.tgz
# Source0-md5:	195553258f2f18198f164ea8f66362dc
Patch0:		%{name}-OPT_FLAGS.patch
URL:		http://www.geocities.com/SiliconValley/Park/2055/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This small utility converts C/C++ sources to PostScript. It performs
syntax highlighting and can add many very useful informations to the
printout, such as line numbers, headers and indexes of functions on
each page. Great thing, if you waste too much time in traffic jams or
public transport ;)

%description -l pl.UTF-8
To małe narzędzie konwertuje pliki źródłowe C/C++ do PostScriptu.
Wykonuje wyróżnianie składni a także potrafi dodać do wydruku wiele
bardzo użytecznych informacji, takich jak numery linii, nagłówki oraz
indeksy funkcji znajdujących się na poszczególnych stronach. Świetna
rzecz, jeśli tracisz zbyt dużo czasu stojąc w korkach, albo w
komunikacji miejskiej ;)

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install c2ps	$RPM_BUILD_ROOT%{_bindir}
install c2ps.1	$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*
