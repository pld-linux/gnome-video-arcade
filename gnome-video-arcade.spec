#
# Conditional build:
%bcond_without	glade		# Glade catalog
#
Summary:	GNOME Video Arcade - a simple MAME frontend for the GNOME desktop
Summary(pl.UTF-8):	GNOME Video Arcade - prosty interfejs użytkownika do MAME dla środowiska GNOME
Name:		gnome-video-arcade
Version:	0.8.5
Release:	1
License:	LGPL v2+
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-video-arcade/0.8/%{name}-%{version}.tar.xz
# Source0-md5:	bbf14f2362c31a62d18684ce48b0a8aa
URL:		http://mbarnes.github.com/gnome-video-arcade/
BuildRequires:	GConf2-devel >= 2.0.0
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.11
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools
%{?with_glade:BuildRequires:	glade-devel >= 3.10.0}
BuildRequires:	glib2-devel >= 1:2.28
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	gtk-doc >= 1.6
BuildRequires:	intltool
BuildRequires:	libsoup-devel >= 2.34
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= 3.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	sqlite3-devel >= 3.0.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	yelp-tools
BuildRequires:	xz
Requires(post,preun):	glib2 >= 1:2.28
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	glib2 >= 1:2.28
Requires:	mame
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Video Arcade is a simple MAME frontend for the GNOME desktop.

%description -l pl.UTF-8
GNOME Video Arcade to prosty interfejs użytkownika do MAME dla
środowiska GNOME.

%package glade
Summary:	GNOME Video Arcade catalog file for Glade
Summary(pl.UTF-8):	Plik katalogu GNOME Video Arcade dla Glade
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glade >= 3.10.0

%description glade
GNOME Video Arcade catalog file for Glade.

%description glade -l pl.UTF-8
Plik katalogu GNOME Video Arcade dla Glade.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	MAME=/usr/bin/mame \
	--disable-silent-rules \
	--disable-static \
	%{?with_glade:--with-glade-catalog} \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with glade}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/glade/modules/libgladegva.la
%endif

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gnome-video-arcade
%{_datadir}/GConf/gsettings/gnome-video-arcade.convert
%{_datadir}/glib-2.0/schemas/org.gnome.VideoArcade.gschema.xml
%{_datadir}/gnome-video-arcade
%{_desktopdir}/gnome-video-arcade.desktop
%{_iconsdir}/hicolor/scalable/apps/gnome-video-arcade.svg
%{_mandir}/man1/gnome-video-arcade.1*
%{_gtkdocdir}/gnome-video-arcade

%if %{with glade}
%files glade
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/glade/modules/libgladegva.so
%{_datadir}/glade/catalogs/gva.xml
%{_datadir}/glade/pixmaps/hicolor/22x22/actions/widget-gva-*.png
%endif
