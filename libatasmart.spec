Summary:	Small and clean implementation of an ATA S.M.A.R.T
Name:		libatasmart
Version:	0.19
Release:	3
License:	LGPL
Group:		Applications
Source0:	http://0pointer.de/public/%{name}-%{version}.tar.xz
# Source0-md5:	53afe2b155c36f658e121fe6def33e77
Patch0:		0001-Dont-test-undefined-bits.patch
Patch1:		0002-Drop-our-own-many-bad-sectors-heuristic.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	udev-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small and clean implementation of an ATA S.M.A.R.T.

%package devel
Summary:	Header files for atasmart library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	udev-devel

%description devel
This is the package containing the header files for atasmart
library.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/skdump
%attr(755,root,root) %{_sbindir}/sktest
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*.h
%{_pkgconfigdir}/*.pc
%{_datadir}/vala/vapi/atasmart.vapi
