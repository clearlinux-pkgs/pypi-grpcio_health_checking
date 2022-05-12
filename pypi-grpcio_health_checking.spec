#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-grpcio_health_checking
Version  : 1.46.1
Release  : 21
URL      : https://files.pythonhosted.org/packages/58/87/d886547b5d3efe019b91ff34eff7beb983da25e3423b1cf367707a21945c/grpcio-health-checking-1.46.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/58/87/d886547b5d3efe019b91ff34eff7beb983da25e3423b1cf367707a21945c/grpcio-health-checking-1.46.1.tar.gz
Summary  : Standard Health Checking Service for gRPC
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-grpcio_health_checking-license = %{version}-%{release}
Requires: pypi-grpcio_health_checking-python = %{version}-%{release}
Requires: pypi-grpcio_health_checking-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(grpcio)
BuildRequires : pypi(protobuf)

%description
gRPC Python Health Checking
===========================
Reference package for GRPC Python health checking.

%package license
Summary: license components for the pypi-grpcio_health_checking package.
Group: Default

%description license
license components for the pypi-grpcio_health_checking package.


%package python
Summary: python components for the pypi-grpcio_health_checking package.
Group: Default
Requires: pypi-grpcio_health_checking-python3 = %{version}-%{release}

%description python
python components for the pypi-grpcio_health_checking package.


%package python3
Summary: python3 components for the pypi-grpcio_health_checking package.
Group: Default
Requires: python3-core
Provides: pypi(grpcio_health_checking)
Requires: pypi(grpcio)
Requires: pypi(protobuf)

%description python3
python3 components for the pypi-grpcio_health_checking package.


%prep
%setup -q -n grpcio-health-checking-1.46.1
cd %{_builddir}/grpcio-health-checking-1.46.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1652397985
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-grpcio_health_checking
cp %{_builddir}/grpcio-health-checking-1.46.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-grpcio_health_checking/34ac89724cb7e3fb36bcfe93efabfd012c569a0e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-grpcio_health_checking/34ac89724cb7e3fb36bcfe93efabfd012c569a0e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
