Name:		songwrite2
Summary:	Guitar tabulature editor with playing and printing
Version:	0.4.1
Release:	2
Source:		http://download.gna.org/songwrite/Songwrite2-%{version}.tar.gz
URL:		http://home.gna.org/oomadness/en/%{name}
License:	GPLv3
Group:		Sound

BuildRequires:	desktop-file-utils
BuildRequires:  imagemagick
BuildRequires:  pkgconfig(python)
Requires:	pythonegg(editobj2)
Requires:	TiMidity++
Requires:	lilypond
Requires:       hicolor-icon-theme
BuildArch:	noarch
%rename		songwrite

%description
Songwrite2 is a tablature (guitar partition) editor. It's the successor of
songwrite. Songwrite2 is coded in Python and uses Tk (Tkinter); it relies on
Timidity to play midi and on GNU Lilypond for printing.


%prep
%setup -q -n Songwrite2-%{version}


%build

%install
python setup.py install --root=%{buildroot}
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*

#menu
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install	%{name}.desktop \
			--remove-key=Encoding \
			--set-icon=%{name} \
			--remove-category=Application \
			--dir=%{buildroot}%{_datadir}/applications
# icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{16x16,32x32,48x48,64x64}/apps
convert -scale 16 data/%{name}_64x64.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
convert -scale 32 data/%{name}_64x64.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
convert -scale 48 data/%{name}_64x64.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
convert -scale 64 data/%{name}_64x64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
			

%find_lang %{name}

# clean
rm -f %{buildroot}%{_datadir}/locale/*/*/*.po
mv %{buildroot}%{_datadir}/doc/%{name}/en/doc.pdf en-doc.pdf
mv %{buildroot}%{_datadir}/doc/%{name}/fr/doc.pdf fr-doc.pdf

%files -f %{name}.lang
%doc README CHANGES AUTHORS *.pdf
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/*.egg-info
%{_mandir}/man1/%{name}.1.xz