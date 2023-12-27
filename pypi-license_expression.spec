#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-license_expression
Version  : 30.1.1
Release  : 4
URL      : https://files.pythonhosted.org/packages/90/93/0fc8c72a5c9b65c2fd56154ef9e08c0c7a7fd0596ae69c65ce714ea5cd84/license-expression-30.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/90/93/0fc8c72a5c9b65c2fd56154ef9e08c0c7a7fd0596ae69c65ce714ea5cd84/license-expression-30.1.1.tar.gz
Summary  : license-expression is a comprehensive utility library to parse, compare, simplify and normalize license expressions (such as SPDX license expressions) using boolean logic.
Group    : Development/Tools
License  : Apache-2.0 CC-BY-4.0 MIT
Requires: pypi-license_expression-license = %{version}-%{release}
Requires: pypi-license_expression-python = %{version}-%{release}
Requires: pypi-license_expression-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wheel)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
==================
license-expression
==================
``license-expression`` is a comprehensive utility library to parse, compare,
simplify and normalize license expressions (such as SPDX license expressions)
using boolean logic.

%package license
Summary: license components for the pypi-license_expression package.
Group: Default

%description license
license components for the pypi-license_expression package.


%package python
Summary: python components for the pypi-license_expression package.
Group: Default
Requires: pypi-license_expression-python3 = %{version}-%{release}

%description python
python components for the pypi-license_expression package.


%package python3
Summary: python3 components for the pypi-license_expression package.
Group: Default
Requires: python3-core
Provides: pypi(license_expression)
Requires: pypi(boolean.py)

%description python3
python3 components for the pypi-license_expression package.


%prep
%setup -q -n license-expression-30.1.1
cd %{_builddir}/license-expression-30.1.1
pushd ..
cp -a license-expression-30.1.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695162982
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-license_expression
cp %{_builddir}/license-expression-%{version}/NOTICE %{buildroot}/usr/share/package-licenses/pypi-license_expression/9a61580943731f263c093243fd3fb2a7f8bf1185 || :
cp %{_builddir}/license-expression-%{version}/apache-2.0.LICENSE %{buildroot}/usr/share/package-licenses/pypi-license_expression/7df059597099bb7dcf25d2a9aedfaf4465f72d8d || :
cp %{_builddir}/license-expression-%{version}/etc/ci/mit.LICENSE %{buildroot}/usr/share/package-licenses/pypi-license_expression/3a7a80be859f41edcaf9989291d2f4b04231d186 || :
cp %{_builddir}/license-expression-%{version}/src/license_expression/data/cc-by-4.0.LICENSE %{buildroot}/usr/share/package-licenses/pypi-license_expression/6e55f0780239c6f263c1ab27a55205efb0204d6d || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-license_expression/3a7a80be859f41edcaf9989291d2f4b04231d186
/usr/share/package-licenses/pypi-license_expression/6e55f0780239c6f263c1ab27a55205efb0204d6d
/usr/share/package-licenses/pypi-license_expression/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
/usr/share/package-licenses/pypi-license_expression/9a61580943731f263c093243fd3fb2a7f8bf1185

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
