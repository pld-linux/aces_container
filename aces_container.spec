Summary:	Implementation of ACES Image Container File
Summary(pl.UTF-8):	Implementacja pliku kontenera obrazów ACES
Name:		aces_container
Version:	1.0.2
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/ampas/aces_container/releases
Source0:	https://github.com/ampas/aces_container/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	b82364639768d650dd45e6085b429fb6
Patch0:		%{name}-libdir.patch
URL:		https://github.com/ampas/aces_container
BuildRequires:	cmake >= 2.6
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains a reference implementation for an ACES container
file writer intended to be used with the Academy Color Encoding System
(ACES). The resulting file is compliant with the ACES container
specification (SMPTE S2065-4).

%description -l pl.UTF-8
Ten pakiet zawiera wzorcową implementację biblioteki zapisującej pliki
kontenerów ACES. Jest przeznaczona do wykorzystania wraz z systemem
ACES (Academy Color Encoding System). Wynikowe pliki są zgodne ze
specyfikacją kontenerów ACES (SMPTE S2065-4).

%package devel
Summary:	Header files for AcesContainer library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki AcesContainer
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for AcesContainer library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki AcesContainer.

%prep
%setup -q
%patch0 -p1

%build
%cmake . \
	-DINSTALL_CMAKE_DIR=%{_libdir}/cmake/AcesContainer \
	-DINSTALL_LIB_DIR=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%attr(755,root,root) %{_libdir}/libAcesContainer.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/aces
%{_pkgconfigdir}/AcesContainer.pc
%{_libdir}/cmake/AcesContainer
