Summary:	Tool for converting C/C++ sources to PostScript
Summary(pl):	Narz�dzie do konwersji �r�de� C/C++ na PostScript
Name:		c2ps
Version:	4.0
Release:	2
Group:		Applications/Printing
Group(de):	Applikationen/Drucken
Group(pl):	Aplikacje/Drukowanie
License:	GPL
Source0:	http://www.geocities.com/SiliconValley/Park/2055/%{name}-40.tgz
Patch0:		%{name}-OPT_FLAGS.patch
URL:		http://www.geocities.com/SiliconValley/Park/2055/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This small utility converts C/C++ sources to PostScript. It performs
syntax highlighting and can add many, very usefull informations to the
printout, such as line numbers, headers and indexes of functions on
each page. Great thing, if you waste too much time in traffic jams or
public transport ;)

%description -l pl
To ma�e narz�dzie konwertuje pliki �r�d�owe C/C++ do PostScriptu.
Wykonuje wyr�nianie sk�adni a tak�e potrafi doda� do wydruku wiele
bardzo u�ytecznych informacji, takich jak numery linii, nag��wki oraz
indeksy funkcji znajduj�cych si� na poszczeg�lnych stronach. �wietna
rzecz, je�li tracisz zbyt du�o czasu stoj�c w korkach, albo w
komunikacji miejskiej ;)

%prep
%setup -q
%patch0 -p1

%build
%{__make} OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install c2ps	$RPM_BUILD_ROOT%{_bindir}
install c2ps.1	$RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*
