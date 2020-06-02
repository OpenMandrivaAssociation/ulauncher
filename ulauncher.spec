Name:           ulauncher
Version:        5.7.5
Release:        2%{?dist}
Summary:        Linux Application Launcher
BuildArch:      noarch

License:        GPLv3+
URL:            https://github.com/Ulauncher/Ulauncher
Source0:        %{url}/releases/download/%{version}/%{name}_%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  keybinder3-devel
BuildRequires:  python3-dbus
BuildRequires:  python3-devel
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-gobject-devel >= 3.30
BuildRequires:  python3-inotify
BuildRequires:  python3-Levenshtein
BuildRequires:  python3-pyxdg
BuildRequires:  python3-websocket-client
BuildRequires:  python3dist(requests)
BuildRequires:  pkgconfig(gtk+-3.0)

Requires:       hicolor-icon-theme
Requires:       keybinder3
Requires:       webkitgtk4
Requires:       python3-cairo
Requires:       python3-dbus
Requires:       python3-gobject
Requires:       python3-inotify
Requires:       python3-Levenshtein
Requires:       python3-pyxdg
Requires:       python3-websocket-client

Recommends:     libappindicator-gtk3

%description
Ulauncher is a fast application launcher for Linux. It's is written in Python,
using GTK+.


%prep
%autosetup -n %{name} -p1
sed -i "s|version='%%VERSION%'|version='%{version}'|g" setup.py


%build
%py3_build


%install

# https://github.com/Ulauncher/Ulauncher/issues/521
install -m 0644 -Dp build/share/applications/ulauncher.desktop \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

%py3_install


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
%{python3_sitelib}/%{name}-*-py*.egg-info
%{python3_sitelib}/%{name}/
