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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

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

strip --strip-unneeded c2ps

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*/*
%doc README.gz
