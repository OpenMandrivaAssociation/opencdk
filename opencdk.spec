%define libgcrypt_version 1.1.94

%define major	10
%define libname %mklibname %{name} %{major}
%define libname_orig lib%{name}
%define develname %mklibname %{name} -d

Summary:	Open Crypto Development Kit
Name:		opencdk
Version:	0.6.6
Release:	%mkrel 7
License:	GPLv2+
Group:		System/Libraries
URL:		http://www.gnutls.org/
Source0:	http://www.gnu.org/software/gnutls/releases/opencdk/%{name}-%{version}.tar.bz2
Source1:	http://www.gnu.org/software/gnutls/releases/opencdk/%{name}-%{version}.tar.bz2.sig
BuildRequires:	zlib-devel
BuildRequires:	libgcrypt-devel >= %{libgcrypt_version}
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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


%package -n	%{develname}
Summary:	Development files for %{name}
Group:		Development/Other
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{libname_orig}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	libgcrypt-devel >= %{libgcrypt_version}
Obsoletes:	%mklibname %{name} 8 -d

%description -n	%{develname}
%{name} library provides basic parts of the OpenPGP message format.

You will need to install this package if you want to develop or 
compile any applications/libraries that use %{name}.

%prep

%setup -q

%build
%configure2_5x
%make

%check
make check

%install
rm -rf %{buildroot}

%makeinstall_std

install -D -m 644 src/opencdk.m4 %{buildroot}%{_datadir}/aclocal/opencdk.m4

%multiarch_binaries %{buildroot}%{_bindir}/*-config

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%doc doc/opencdk-api.html
%{_bindir}/opencdk-config
%{multiarch_bindir}/*-config
%{_datadir}/aclocal/*.m4
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/pkgconfig/opencdk.pc
