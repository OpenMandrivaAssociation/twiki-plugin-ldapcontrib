%define _provides_exceptions perl(.*)
%define _requires_exceptions perl(\\(TWiki.*\\|Assert\\))

Name:       twiki-plugin-ldapcontrib
Version:    2.99.7
Release:    %mkrel 1
Summary:    LDAP services for TWiki
License:    GPL
Group:      System/Servers
URL:        http://twiki.org/cgi-bin/view/Plugins/LdapContrib
Source:     http://twiki.org/p/pub/Plugins/LdapContribDev/LdapContrib.zip
Requires:   twiki
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This package offers basic LDAP services for TWiki and offers authentication of
TWiki users by binding to an LDAP server as well as incorporate LDAP user
groups into TWiki's access control. Note, however that you need at least
TWiki-4.0.3 for that. Optionally, if you need an interface to query your LDAP
directory and display the results in a TWiki topic install the
TWiki:Plugins/LdapNgPlugin which will make use of the LdapContrib services.
This work is a rewrite of the TWiki:Plugins/LdapPlugin by
TWiki:Main/GerardHickey while bringing authentication, user management and
other LDAP applications onto a common base.

%prep
%setup -q -c

%build

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/twiki/lib/TWiki
cp -r lib/TWiki/* %{buildroot}%{_datadir}/twiki/lib/TWiki

install -d -m 755 %{buildroot}%{_localstatedir}/lib/twiki/data/Twiki
install -m 644 data/TWiki/LdapContrib.txt \
    %{buildroot}%{_localstatedir}/lib/twiki/data/Twiki

install -d -m 755 %{buildroot}%{_localstatedir}/lib/twiki/pub/Twiki
cp -r pub/TWiki/LdapContrib %{buildroot}%{_localstatedir}/lib/twiki/pub/Twiki

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/twiki/lib/TWiki/*
%attr(-,apache,apache) %{_localstatedir}/lib/twiki/data/Twiki/*
%attr(-,apache,apache) %{_localstatedir}/lib/twiki/pub/Twiki/*