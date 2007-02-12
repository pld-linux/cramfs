Summary:	Set of tools which creates and checks cramfs filesytem
Summary(pl.UTF-8):	Zestaw narzędzi do tworzenia i sprawdzania systemu plików cramfs
Name:		cramfs
Version:	1.1
Release:	1
License:	GPL
Group:		Base/Utilities
Source0:	http://dl.sourceforge.net/cramfs/%{name}-%{version}.tar.gz
# Source0-md5:	d3912b9f7bf745fbfea68f6a9b9de30f
URL:		http://sourceforge.net/projects/cramfs/
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
Set of tools which creates and checks cramfs filesystem.

%description -l pl.UTF-8
Zestaw narzędzi do tworzenia i sprawdzania systemu plików cramfs.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install mkcramfs cramfsck $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NOTES
%attr(755,root,root) %{_sbindir}/*
