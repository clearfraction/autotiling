%global   abi_package %{nil}
%global   i3ipc_version 2.2.1

Name     : autotiling
Version  : 1.6
Release  : 1
URL      : https://github.com/nwg-piotr/autotiling
Source0  : https://github.com/nwg-piotr/autotiling/archive/refs/tags/v%{version}.tar.gz
Source1  : https://pypi.python.org/packages/source/i/i3ipc/i3ipc-%{i3ipc_version}.tar.gz
Summary  : Tiling script
Group    : Development/Tools
License  : MIT
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wheel)


%description
This script uses the i3ipc-python library to switch the layout splith/splitv depending on the currently focused window dimensions. It works on both sway and i3 window managers.

%prep
%setup -q -n autotiling-%{version} -a 1

%build
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1651591567
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
pushd i3ipc-%{i3ipc_version}
python3 setup.py build
python3 -tt setup.py build install --root=/
popd
make

%install
export MAKEFLAGS=%{?_smp_mflags}
python setup.py install --root=%{buildroot} --optimize=1
cp -pr /usr/lib/python*/site-packages/i3ipc %{buildroot}/usr/lib/python3*/site-packages/
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
rm -rf %{buildroot}/usr/lib/python3*/site-packages/*.egg-info

%files
%defattr(-,root,root,-)
/usr/lib/python3*/*
/usr/bin/autotiling
