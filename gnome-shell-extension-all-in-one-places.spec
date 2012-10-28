%define		extname		all-in-one-places
Summary:	All-in-one quick navigation to places and devices
Name:		gnome-shell-extension-%{extname}
Version:	20121027
Release:	0.1
License:	Unknown
Group:		X11/Applications
# $ git clone git://github.com/jferrao/gtk.git
# $ cd gtk/gnome-shell/extensions/all-in-one-places@jofer
# $ git archive --format=tar --prefix=%{extname}-%{version}/ master | xz > ../../../../%{extname}-%{version}.tar.xz
Source0:	%{extname}-%{version}.tar.xz
# Source0-md5:	f68f81a93ddc2de4627c646e45a12698
URL:		http://jferrao.github.com/gtk/
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	gnome-shell >= 3.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
All-in-one quick navigation to places and devices with a few extra
configuration options to customize and change the look and feel of the
extension.

%prep
%setup -q -n %{extname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas \
	$RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/all-in-one-places@jofer

cp -p schemas/org.gnome.shell.extensions.AllInOnePlaces.gschema.xml $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas
cp -p *.js* $RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/all-in-one-places@jofer
cp -p *.css $RPM_BUILD_ROOT%{_datadir}/gnome-shell/extensions/all-in-one-places@jofer

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files
%defattr(644,root,root,755)
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.AllInOnePlaces.gschema.xml
%{_datadir}/gnome-shell/extensions/all-in-one-places*
