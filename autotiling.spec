Name     : autotiling
Version  : 1.8
Release  : 1
URL      : https://github.com/nwg-piotr/autotiling
Source0  : https://github.com/nwg-piotr/autotiling/archive/refs/tags/v%{version}.tar.gz
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


%build
unset https_proxy http_proxy no_proxy
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
mkdir buildir
python -m pip install autotiling i3ipc python-xlib six --target builddir
rm -rf builddir/*.dist-info
python -m zipapp builddir -m autotiling:main -p /usr/sbin/python -c -o autotiling


%install
install -Dm755 autotiling %{buildroot}/usr/bin/autotiling


%files
%defattr(-,root,root,-)
/usr/bin/autotiling
