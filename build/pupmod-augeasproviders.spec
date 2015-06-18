Summary: Alternative Augeas-based providers for Puppet
Name: pupmod-augeasproviders
Version: 2.1.3
Release: 0
License: Apache License, 2.0
Group: Applications/System
URL: https://github.com/hercules-team/augeasproviders
Source: %{name}-%{version}-%{release}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildarch: noarch
Requires: simp-bootstrap >= 4.2.0
Requires: puppet
Obsoletes: pupmod-augeasproviders-test

Prefix: /etc/puppet/environments/simp/modules

%description
Alternative Augeas-based providers for Puppet with local fixes.

%prep
%setup -q

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{prefix}/augeasproviders

dirs='files lib manifests templates'
for dir in $dirs; do
  test -d $dir && cp -r $dir %{buildroot}/%{prefix}/augeasproviders
done

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

mkdir -p %{buildroot}/%{prefix}/augeasproviders

%files
%defattr(0640,root,puppet,0750)
%{prefix}/augeasproviders

%post
#!/bin/sh

%postun
# Post uninstall stuff

%changelog
* Thu Feb 19 2015 Trevor Vaughan <tvaughan@onyxpoint.com> - 2.1.3-0
- Updated to 2.1.3

* Fri Jan 16 2015 Trevor Vaughan <tvaughan@onyxpoint.com> - 1.0.2-2
- Updated to require Puppet

* Thu Jul 10 2014 - Trevor Vaughan <tvaughan@onyxpoint.com> - 1.0.2-1
- Fixed a bug in augeasproviders that prevented the default Grub2 boot
  options from being able to be written.
- Incorporated bug fixes from the upstream community repository.

* Mon Jan 13 2014 - Trevor Vaughan <tvaughan@onyxpoint.com> - 1.0.2-0
- Initial release.
