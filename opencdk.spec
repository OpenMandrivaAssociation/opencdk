%define	name	opencdk
%define	version	0.5.8
%define release	%mkrel 1

%define libgcrypt_version 1.1.94

%define major	8
%define libname %mklibname %{name} %{major}
%define libname_orig lib%{name}

Summary:	Open Crypto Development Kit
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Libraries
URL:		http://www.gnutls.org/
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

Source0:	ftp://ftp.gnupg.org/gcrypt/alpha/gnutls/opencdk/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.gnupg.org/gcrypt/alpha/gnutls/opencdk/%{name}-%{version}.tar.gz.sig
#Patch0:		opencdk-0.5.4-automake18.patch.bz2

BuildRequires:	zlib-devel
BuildRequires:	libgcrypt-devel >= %{libgcrypt_version}

%description
%{name} library provides basic parts of the OpenPGP message format.
Due to some possible security problems, the library also implements
parts of draft-ietf-openpgp-rfc2440bis-08.txt.

The aim of the library is *not* to replace any available OpenPGP version.
There will be no real support for key management (sign, revoke,
alter preferences, ...) and some other parts are only rudimentary
available. The main purpose is to handle and understand OpenPGP
packets and to use basic operations. For example to encrypt/decrypt
or to sign/verify and packet routines.


%package -n	%{libname}
Summary:	Open Crypto Development Kit
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Provides:	%{libname_orig} = %{version}-%{release}

%description -n	%{libname}
%{name} library provides basic parts of the OpenPGP message format.
Due to some possible security problems, the library also implements
parts of draft-ietf-openpgp-rfc2440bis-08.txt.

The aim of the library is *not* to replace any available OpenPGP version.
There will be no real support for key management (sign, revoke,
alter preferences, ...) and some other parts are only rudimentary
available. The main purpose is to handle and understand OpenPGP
packets and to use basic operations. For example to encrypt/decrypt
or to sign/verify and packet routines.


%package -n	%{libname}-devel
Summary:	Development files for %{name}
Group:		Development/Other
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{libname_orig}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Requires:	libgcrypt-devel >= %{libgcrypt_version}

%description -n	%{libname}-devel
%{name} library provides basic parts of the OpenPGP message format.

You will need to install this package if you want to develop or 
compile any applications/libraries that use %{name}.

%prep
%setup -q
#%patch0 -p1 -b .automake18

%build
%configure2_5x
%make
make check

%install
rm -rf %{buildroot}
%makeinstall_std

install -D -m 644 src/opencdk.m4 %{buildroot}%{_datadir}/aclocal/opencdk.m4

%multiarch_binaries %{buildroot}%{_bindir}/*-config

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/lib*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%doc doc/DETAILS doc/opencdk-api.html
%{_bindir}/*-config
%multiarch %{multiarch_bindir}/*-config
%{_datadir}/aclocal/*.m4
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_libdir}/lib*.la