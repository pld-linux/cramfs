Summary:	cramfs
Summary(pl):	cramfs
Name:		cramfs
Version:	1.1
Release:	1
License:	GPL
Group:		Base/Utilities
Source0:	http://telia.dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
Requires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_docdir}}

install mkcramfs $RPM_BUILD_ROOT%{_bindir}
install cramfsck $RPM_BUILD_ROOT%{_bindir}
install README  $RPM_BUILD_ROOT%{_docdir}
install NOTES   $RPM_BUILD_ROOT%{_docdir}
install COPYING $RPM_BUILD_ROOT%{_docdir}
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}
%doc %{_docdir}
