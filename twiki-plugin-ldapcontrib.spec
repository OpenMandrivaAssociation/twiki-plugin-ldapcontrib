%if %{_use_internal_dependency_generator}
%define __noautoprov 'perl\\((.*)\\)'
%define __noautoreq 'perl\\(TWiki(.*)\\)|perl\\(Assert\\)'
%else
%define _provides_exceptions perl(.*)
%define _requires_exceptions perl(\\(TWiki.*\\|Assert\\))
%endif

Name:		twiki-plugin-ldapcontrib
Version:	2.99.7
Release:	3
Summary:	LDAP services for TWiki
License:	GPL
Group:		System/Servers
URL:		http://twiki.org/cgi-bin/view/Plugins/LdapContrib
Source:		http://twiki.org/p/pub/Plugins/LdapContribDev/LdapContrib.zip
Requires:	twiki
BuildArch:	noarch

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
install -d -m 755 %{buildroot}%{_datadir}/twiki/lib/TWiki
cp -r lib/TWiki/* %{buildroot}%{_datadir}/twiki/lib/TWiki

install -d -m 755 %{buildroot}%{_localstatedir}/lib/twiki/data/TWiki
install -m 644 data/TWiki/LdapContrib.txt \
    %{buildroot}%{_localstatedir}/lib/twiki/data/TWiki

install -d -m 755 %{buildroot}%{_localstatedir}/lib/twiki/pub/TWiki
cp -r pub/TWiki/LdapContrib %{buildroot}%{_localstatedir}/lib/twiki/pub/TWiki

%files
%{_datadir}/twiki/lib/TWiki/*
%attr(-,apache,apache) %{_localstatedir}/lib/twiki/data/TWiki/*
%attr(-,apache,apache) %{_localstatedir}/lib/twiki/pub/TWiki/*

