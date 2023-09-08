#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-grpcio_health_checking
Version  : 1.58.0
Release  : 47
URL      : https://files.pythonhosted.org/packages/0d/44/5d6791f8b12f09529e3e42da9f4b0781cf0f61b76b20a2907cbe9c77eb48/grpcio-health-checking-1.58.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/0d/44/5d6791f8b12f09529e3e42da9f4b0781cf0f61b76b20a2907cbe9c77eb48/grpcio-health-checking-1.58.0.tar.gz
Summary  : Standard Health Checking Service for gRPC
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-grpcio_health_checking-license = %{version}-%{release}
Requires: pypi-grpcio_health_checking-python = %{version}-%{release}
Requires: pypi-grpcio_health_checking-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(grpcio)
BuildRequires : pypi(protobuf)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n grpcio-health-checking-1.58.0
cd %{_builddir}/grpcio-health-checking-1.58.0
pushd ..
cp -a grpcio-health-checking-1.58.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1694186808
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-grpcio_health_checking
cp %{_builddir}/grpcio-health-checking-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-grpcio_health_checking/242ec6abfdd8c114f2e803b84934469c299348fc || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-grpcio_health_checking/242ec6abfdd8c114f2e803b84934469c299348fc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
