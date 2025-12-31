Name:          	elara-desktop
Version:        1.0.0
Release:        1%{?dist}
Summary:        Elara Desktop Metapackage

License:        MIT
URL:            https://github.com/joshm998/elara-desktop
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch

Requires:       labwc
Requires:       network-manager-applet
Requires:       waybar
Requires:	    wlr-randr
Requires:       elara-launcher
Requires:	    kitty
Requires:	    pcmanfm
Requires:	    mako
Requires:	    swayidle
Requires:	    sddm
Requires:       mousepad

%description
A metapackage that installs labwc Wayland compositor with nm-applet
and provides default configuration files in /etc/xdg/labwc.

%prep
%autosetup

%build
# No build needed

%install
# Create directory structure
mkdir -p %{buildroot}%{_sysconfdir}/xdg/labwc
mkdir -p %{buildroot}%{_datadir}/wayland-sessions
mkdir -p %{buildroot}%{_datadir}/themes

# Install configuration files
install -Dm644 data/etc/xdg/labwc/rc.xml %{buildroot}%{_sysconfdir}/xdg/labwc/rc.xml
install -Dm755 data/etc/xdg/labwc/autostart %{buildroot}%{_sysconfdir}/xdg/labwc/autostart
install -Dm644 data/etc/xdg/labwc/environment %{buildroot}%{_sysconfdir}/xdg/labwc/environment
install -Dm644 data/etc/xdg/labwc/menu.xml %{buildroot}%{_sysconfdir}/xdg/labwc/menu.xml

# Install session file
install -Dm644 data/usr/share/wayland-sessions/labwc.desktop %{buildroot}%{_datadir}/wayland-sessions/labwc.desktop

# Install Themes
cp -a data/usr/share/themes/* %{buildroot}%{_datadir}/themes/

%files
%license LICENSE
%doc README.md
%{_sysconfdir}/xdg/labwc/rc.xml
%{_sysconfdir}/xdg/labwc/autostart
%{_sysconfdir}/xdg/labwc/environment
%{_sysconfdir}/xdg/labwc/menu.xml
%{_datadir}/wayland-sessions/labwc.desktop
%{_datadir}/themes

%changelog
* Tue Dec 31 2025 Josh Mangiola <contact@joshmangiola.com> - 1.0.0-1
- Initial release
