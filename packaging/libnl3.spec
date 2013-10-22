Name:       libnl3
Summary:    Library for netlink sockets
Version:    3.2.22
Release:    1
Group:      System/Network
License:    LGPL-2.1
Source0:    %{name}-%{version}.tar.gz
Source1001: 	libnl3.manifest
BuildRequires:  bison
BuildRequires:  flex

%description
This is a library for applications dealing with netlink sockets.
The library provides an interface for raw netlink messaging and various
netlink family specific interfaces.

%package devel
Summary:    Development library and headers for libnl3
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
This is a library for applications dealing with netlink sockets.
The library provides an interface for raw netlink messaging and various
netlink family specific interfaces.
This package contains all files that are needed to build applications using
libnl3.

%package cli
Summary:   Command line interface utils for libnl3
Group:     Development/Libraries
Requires:  %{name} = %{version}-%{release}

%description cli
This package contains various libnl3 utils and additional
libraries on which they depend

%prep
%setup -q
cp %{SOURCE1001} .


%build
chmod +x autogen.sh
%autogen.sh
%configure

make -j1

%install
%make_install
rm -f %{buildroot}/etc/libnl/pktloc

%post -p /sbin/ldconfig
%post cli -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%postun cli -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/libnl*.so.*
%exclude %{_libdir}/libnl-cli*.so.*
%config(noreplace) %{_sysconfdir}/*

%files devel
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/libnl*.so

%files cli
%defattr(-,root,root,-)
%{_libdir}/libnl-cli*.so.*
%{_libdir}/libnl/
%{_sbindir}/*
%{_mandir}/man8/*
