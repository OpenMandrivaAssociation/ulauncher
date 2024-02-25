# don't require because it uses Ayatana Appindicator
%global __requires_exclude ^typelib\\(AppIndicator3\\).*$

Name:		ulauncher
Version:	5.15.6
Release:	1
Summary:	Linux Application Launcher
BuildArch:	noarch

License:	GPLv3+
URL:		https://github.com/Ulauncher/Ulauncher
Source0:	https://github.com/Ulauncher/Ulauncher/releases/download/%{version}/%{name}_%{version}.tar.gz
#Patch0:	 ulauncher-5.9.0-fix-usr-bin-sh-openmandriva.patch

BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	pkgconfig(keybinder-3.0)
BuildRequires:	pkgconfig(dbus-python)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(pygobject-3.0)
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(dbus-python)
BuildRequires:	python%{pyver}dist(requests)
BuildRequires:	python%{pyver}dist(python-distutils-extra)
BuildRequires:	python%{pyver}dist(pyinotify)
BuildRequires:	python%{pyver}dist(python-levenshtein)
BuildRequires:	python%{pyver}dist(pyxdg)
BuildRequires:	python%{pyver}dist(websocket-client)
BuildRequires:	systemd-rpm-macros

Requires:	hicolor-icon-theme
Requires:	keybinder3.0
Requires:	webkit
Requires:	python-cairo
Requires:	python-dbus
Requires:	python-gobject
Requires:	python-pyinotify
Requires:	python-Levenshtein
Requires:	python-pyxdg
Requires:	python-websocket-client
Requires:	wmctrl

%description
Ulauncher is a fast application launcher for Linux. It's is written in Python,
using GTK+.

%prep
%autosetup -p1 -n %{name}

%build
%py_build

%install
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
%{_userunitdir}/%{name}.service
%{python_sitelib}/%{name}-*-py*.egg-info
%{python_sitelib}/%{name}/

