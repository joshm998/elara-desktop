Name:          	elara-desktop
Version:        1.0.1
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
Requires:       seatd
Requires:       xorg-x11-server-Xwayland
Requires:       firefox
Requires:       alsa-utils
Requires:       brightnessctl
Requires:       plymouth-system-theme

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
mkdir -p %{buildroot}%{_sysconfdir}/xdg/waybar
mkdir -p %{buildroot}%{_datadir}/wayland-sessions
mkdir -p %{buildroot}%{_datadir}/themes

# Install configuration files
install -Dm644 data/etc/xdg/labwc/rc.xml %{buildroot}%{_sysconfdir}/xdg/labwc/rc.xml
install -Dm755 data/etc/xdg/labwc/autostart %{buildroot}%{_sysconfdir}/xdg/labwc/autostart
install -Dm644 data/etc/xdg/labwc/environment %{buildroot}%{_sysconfdir}/xdg/labwc/environment
install -Dm644 data/etc/xdg/labwc/menu.xml %{buildroot}%{_sysconfdir}/xdg/labwc/menu.xml

install -Dm644 data/etc/xdg/waybar/colors.css %{buildroot}%{_sysconfdir}/xdg/waybar/colors.css
install -Dm644 data/etc/xdg/waybar/config.jsonc %{buildroot}%{_sysconfdir}/xdg/waybar/config.jsonc
install -Dm644 data/etc/xdg/waybar/style.css %{buildroot}%{_sysconfdir}/xdg/waybar/style.css

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
%{_sysconfdir}/xdg/waybar/colors.css
%{_sysconfdir}/xdg/waybar/config.jsonc
%{_sysconfdir}/xdg/waybar/style.css
%{_datadir}/wayland-sessions/labwc.desktop
%{_datadir}/themes

%changelog
* Fri Jan 1 2026 Josh Mangiola <contact@joshmangiola.com> - 1.0.1-1
- Adds Waybar config and fixes issues on Asahi
* Wed Dec 31 2025 Josh Mangiola <contact@joshmangiola.com> - 1.0.0-1
- Initial release
