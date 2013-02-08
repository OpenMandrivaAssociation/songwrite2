Name:		songwrite2
Summary:	Guitar tabulature editor with playing and printing
Version:	0.2.1
Release:	4
Source:		http://download.gna.org/songwrite/Songwrite2-%{version}.tar.gz
URL:		http://home.gna.org/oomadness/en/songwrite
License:	GPLv2
Group:		Sound
%py_requires -d
Requires:	editobj2 TiMidity++ lilypond
BuildArch:	noarch
Obsoletes:	songwrite

%description
Songwrite2 is a tablature (guitar partition) editor. It's the successor of
songwrite. Songwrite2 is coded in Python and uses Tk (Tkinter); it relies
on Timidity to play midi and on GNU Lilypond for printing.

%prep
%setup -q -n Songwrite2-%version

%build
#only to fix rpmlint's warning

%install
python setup.py install --root=%{buildroot}

#menu

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
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
rm -f %{buildroot}%{_datadir}/locale/*/*/*.po


%files -f %name.lang
%defattr(-,root,root)
%doc README CHANGES AUTHORS 
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/*.egg-info



%changelog
* Mon Nov 01 2010 Funda Wang <fwang@mandriva.org> 0.2.1-3mdv2011.0
+ Revision: 591341
- rebuild for py 2.7

* Sun Apr 18 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.2.1-2mdv2010.1
+ Revision: 536484
- fix requires (with importation of editobj2)
- add an obsoletes on songwrite

* Sun Apr 18 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.2.1-1mdv2010.1
+ Revision: 536444
- new version 0.2.1

* Sun Apr 18 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.2-2mdv2010.1
+ Revision: 536208
- fix summary
- add a build section for fix a rpmlint's warning
- use %%py_requires

* Sun Apr 18 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.2-1mdv2010.1
+ Revision: 536173
- try to fix rebuild with an additional BR
- fix BR
- import songwrite2


