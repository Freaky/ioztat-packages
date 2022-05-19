Name: ioztat
Version: 2.0.1
Release: 1%{?dist}
Summary: Storage load analysis tool for OpenZFS datasets
Group: Applications/System
License: BSD
URL: https://github.com/jimsalterjrs/%{name}/
Source0: https://github.com/jimsalterjrs/%{name}/archive/refs/tags/v%{version}.tar.gz
Requires: python3 >= 3.7
BuildArch: noarch

%description
ioztat is a storage load analysis tool for OpenZFS. It provides iostat-like
statistics at an individual dataset/zvol level.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/%{_bindir} %{buildroot}/%{_mandir}/man8
install -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}
install -m 0444 %{name}.8 %{buildroot}/%{_mandir}/man8/%{name}.8

%files
%license LICENSE
%doc CHANGELOG.md
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8*

%changelog
* Thu May 19 2022 Thomas Hurst <tom@hur.st> - 2.0.1-1
- Initial draft of RPM
