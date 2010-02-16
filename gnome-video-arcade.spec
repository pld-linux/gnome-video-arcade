Summary:	GNOME Video Arcade - a simple MAME frontend for the GNOME desktop
Name:		gnome-video-arcade
Version:	0.6.8
Release:	1
License:	LGPL v2+
Group:		Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-video-arcade/0.6/%{name}-%{version}.tar.bz2
# Source0-md5:	1f9d8ca7c56757fe0ffde789b65269cb
URL:		http://mbarnes.github.com/gnome-video-arcade/
BuildRequires:	GConf2
BuildRequires:	GConf2-devel >= 2.0.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	gnome-doc-utils
BuildRequires:	gnome-icon-theme
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	gtk-doc-automake
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 2.16.0
BuildRequires:	libxml2-progs
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel >= 3.0.0
Requires(post,postun):	hicolor-icon-theme
Requires(post,preun):	GConf2
Requires:	sdlmame
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Video Arcade is a simple MAME frontend for the GNOME desktop.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
export SDLMAME=/usr/bin/sdlmame
%configure \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gnome-video-arcade.schemas
%update_desktop_database_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall gnome-video-arcade.schemas

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gnome-video-arcade
%{_desktopdir}/gnome-video-arcade.desktop
%{_datadir}/gnome-video-arcade
%{_iconsdir}/hicolor/*/*/*.svg
%{_mandir}/man1/*.1*
%{_gtkdocdir}/gnome-video-arcade
%{_sysconfdir}/gconf/schemas/gnome-video-arcade.schemas
