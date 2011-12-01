%define version 47
Name:           migrationtools
Version:        %{version}
Release:        7%{?dist}
Summary:        Migration scripts for LDAP

Group:          System Environment/Daemons
License:        BSD
URL:            http://www.padl.com/OSS/MigrationTools.html
Source0:        http://www.padl.com/download/MigrationTools-%{version}.tar.gz
Source1:        migration-tools.txt
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       perl, openldap-clients, ldif2ldbm

Patch1: MigrationTools-38-instdir.patch
Patch2: MigrationTools-36-mktemp.patch
Patch3: MigrationTools-27-simple.patch
Patch4: MigrationTools-26-suffix.patch
Patch5: MigrationTools-46-schema.patch
Patch6: MigrationTools-45-noaliases.patch
Patch7: MigrationTools-46-ddp.patch
Patch8: MigrationTools-46-unique-hosts.patch
Patch9: MigrationTools-46-shadow-numbers.patch
Patch10: MigrationTools-46-gen-one-domain.patch

%description
The MigrationTools are a set of Perl scripts for migrating users, groups,
aliases, hosts, netgroups, networks, protocols, RPCs, and services from 
existing nameservices (flat files, NIS, and NetInfo) to LDAP.

%prep
%setup -q -n MigrationTools-47

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

%build
# nothing to build
cp %SOURCE1 .

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}
install -m 755 migrate_* $RPM_BUILD_ROOT/%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%attr(0755,root,root) %dir /%{_datadir}/%{name}
%attr(0644,root,root) /%{_datadir}/%{name}/*.ph
%attr(0755,root,root) /%{_datadir}/%{name}/*.pl
%attr(0755,root,root) /%{_datadir}/%{name}/*.sh
%doc README
%doc migration-tools.txt

%changelog
* Tue Apr 27 2010 Jan Safranek <jsafrane@redhat.com> - 47-7
- Fixed import of fields with value '0' of shadowFlag in /etc/passwd
  (#563172)

* Mon Feb 22 2010 Jan Safranek <jsafrane@redhat.com> - 47-6
- Spec file cleanup

* Tue Feb  9 2010 Jan Safranek <jsafrane@redhat.com> - 47-5
- Fixed import of fields with value '0' in /etc/passwd (#563172)
- Fixed import of three-level base domains (#563155)

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 47-4.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 47-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 47-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 29 2008 Jan Safranek <jsafrane@redhat.com> 47-2
- added support for Fedora DS (when it provides ldif2ldbm)
- rediffed all patches to get rid of patch fuzz

* Thu Feb 28 2008 Jan Safranek <jsafrane@redhat.com> 47-1
- package carved out of openldap-servers

