Summary:	Set of tools which creates and checks cramfs filesytem
Summary(pl):	Zestaw narzêdzi do tworzenia i sprawdzania systemu plików cramfs
Name:		cramfs
Version:	1.1
Release:	1
License:	GPL
Group:		Base/Utilities
Source0:	http://telia.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
Requires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
Set of tools which creates and checks cramfs filesytem

%description -l pl
Zestaw narzêdzi do tworzenia i sprawdzania systemu plików cramfs

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_docdir}}

install mkcramfs $RPM_BUILD_ROOT%{_sbindir}
install cramfsck $RPM_BUILD_ROOT%{_sbindir}
install README  $RPM_BUILD_ROOT%{_docdir}
install NOTES   $RPM_BUILD_ROOT%{_docdir}
install COPYING $RPM_BUILD_ROOT%{_docdir}
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}
%doc %{_docdir}
