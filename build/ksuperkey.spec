Name:		ksuperkey
Version:	0.4
Release:	1%{?dist}
Summary:	KDE Super key launcher

License:	GPLv3
URL:		https://github.com/hanschen/ksuperkey
Source0:	https://github.com/hanschen/ksuperkey/archive/v%version.zip

BuildRequires:	gcc desktop-file-utils make libX11-devel libXtst-devel pkgconfig

%description
ksuperkey allows you to open the application launcher
in KDE Plasma Desktop using the Super key


%prep
%setup -q


%build
make %{?_smp_mflags}


%install
%{make_install}
mkdir -p %{buildroot}%{_datadir}/applications
install -m 644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop


%post
update-desktop-database &> /dev/null || :


%files
%{_bindir}/%name
%{_datadir}/applications/%{name}.desktop


%changelog
* Sat Jul 02 2016 Chris Smart <csmart@kororaproject.org> - 0.4-1
- Initial package

