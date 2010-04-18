Name:		songwrite2
Summary:	Guitar tabulature editor with playing and printing
Version:	0.2
Release:	%mkrel 1
Source:		http://download.gna.org/songwrite/Songwrite2-%{version}.tar.gz
URL:		http://home.gna.org/oomadness/en/songwrite
License:	GPLv2
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libpython2.6-devel libpython2.6
Requires:	python editobj TiMidity++ lilypond
BuildArch:	noarch

%description
Songwrite is a tablature (guitar partition) editor.
Songwrite is coded in Python and uses Tk (Tkinter); it relies on Timidity to
play midi and on GNU Lilypond for printing. 

%prep
%setup -q -n Songwrite2-%version

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

#menu

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Songwrite2
Comment=Guitar TAB editor
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=AudioVideo;Audio;
Encoding=UTF-8
EOF


%find_lang %name

# remove unpackaged files
rm -f $RPM_BUILD_ROOT%{_datadir}/locale/*/*/*.po

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc README CHANGES AUTHORS 
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/*.egg-info

