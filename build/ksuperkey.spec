Name:		ksuperkey
Version:	0.4
Release:	1%{?dist}
Summary:	KDE Super key launcher

License:	GPLv3
URL:		https://github.com/hanschen/ksuperkey
Source0:	https://github.com/hanschen/ksuperkey/archive/v%version.zip

BuildRequires:	gcc make libX11-devel libXtst-devel pkgconfig

%description
ksuperkey allows you to open the application launcher
in KDE Plasma Desktop using the Super key


%prep
%setup -q


%build
make %{?_smp_mflags}


%install
%make_install


%files
%{_bindir}/%name


%changelog


