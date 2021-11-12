Name:           ulauncher
Version:        5.14.1
Release:        1
Summary:        Linux Application Launcher
BuildArch:      noarch

License:        GPLv3+
URL:            https://github.com/Ulauncher/Ulauncher
Source0:        https://github.com/Ulauncher/Ulauncher/releases/download/%{version}/%{name}_%{version}.tar.gz
#Patch0:         ulauncher-5.9.0-fix-usr-bin-sh-openmandriva.patch

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  pkgconfig(keybinder-3.0)
BuildRequires:  pkgconfig(dbus-python)
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(python-distutils-extra)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  python3dist(pyinotify)
BuildRequires:  python3dist(python-levenshtein)
BuildRequires:  python3dist(pyxdg)
BuildRequires:  python3dist(websocket-client)
BuildRequires:  python3dist(requests)
BuildRequires:  pkgconfig(gtk+-3.0)

Requires:       hicolor-icon-theme
Requires:       keybinder3.0
Requires:       webkit
Requires:       python-cairo
Requires:       python-dbus
Requires:       python-gobject
Requires:       python-pyinotify
Requires:       python-Levenshtein
Requires:       python-pyxdg
Requires:       python-websocket-client

%description
Ulauncher is a fast application launcher for Linux. It's is written in Python,
using GTK+.

%prep
%autosetup -n %{name} -p1
sed -i "s|version='%%VERSION%'|version='%{version}'|g" setup.py

%build
%py_build

%install

# https://github.com/Ulauncher/Ulauncher/issues/521
install -m 0644 -Dp build/share/applications/ulauncher.desktop \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

%py_install


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license LICENSE
%doc README.md AUTHORS
%{_bindir}/%{name}
%{_bindir}/%{name}-toggle
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%dir %{_datadir}/icons/breeze/
%dir %{_datadir}/icons/elementary/
%dir %{_datadir}/icons/gnome/
%dir %{_datadir}/icons/ubuntu-mono-dark/
%dir %{_datadir}/icons/ubuntu-mono-light/
%{_datadir}/icons/breeze/apps/48/%{name}-indicator.svg
%{_datadir}/icons/elementary/scalable/apps/%{name}-indicator.svg
%{_datadir}/icons/gnome/scalable/apps/%{name}-indicator.svg
%{_datadir}/icons/gnome/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/*/apps/%{name}-indicator.svg
%{_datadir}/icons/hicolor/*/apps/%{name}.svg
%{_datadir}/icons/ubuntu-mono-*/scalable/apps/%{name}-indicator.svg
%{python_sitelib}/%{name}-*-py*.egg-info
%{python_sitelib}/%{name}/
