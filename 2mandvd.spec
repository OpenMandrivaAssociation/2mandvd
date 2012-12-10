%define srcname	2ManDVD

Name:		2mandvd
Version:	1.8.2
Release:	1
Summary:	Video DVD creation tool, successor to ManDVD
URL:		http://2mandvd.tuxfamily.org/
# GPLv2 and LGPL for some icons
License:	GPLv2 and LGPL
Group:		Video
Source:		http://download.tuxfamily.org/2mandvd/%{srcname}-%{version}.tar.gz
Patch:		2ManDVD-ffmpeg-0.11.patch

BuildRequires:	qt4-devel >= 4.6
BuildRequires:	ffmpeg-devel
BuildRequires:	SDL-devel

Requires:	dvd+rw-tools
Requires:	dvdauthor
Requires:	ffmpeg >= 0.5
Requires:	ffmpegthumbnailer
Requires:	mencoder
Requires:	mjpegtools
Requires:	mkisofs
Requires:	mplayer
Requires:	netpbm
Requires:	sox
Requires:	exif
Suggests:	transcode
Obsoletes:	2ManDVD

%description
2ManDVD is a graphical tool for creating Video DVDs and slideshows, including
menus.

N.B. Executable name is 2ManDVD

%prep
%setup -q -n %{srcname}
%patch -p1 -b .compile~

%build
%qmake_qt4 2ManDVD.pro
%make

%install
%__rm -rf %{buildroot}

# put the executable in %{_datadir}/%{name} and symlink it to %_bindir
# otherwise the UI localizations don't work
%__install -D -m 755 %{srcname} %{buildroot}%{_datadir}/%{srcname}/%{srcname}

%__mkdir_p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
	ln -s %{_datadir}/%{srcname}/%{srcname} 2ManDVD
popd

%__install -m 644 2mandvd_*.qm %{buildroot}%{_datadir}/%{srcname}
%__install -m 644 fake.pl %{buildroot}%{_datadir}/%{srcname}

# create .desktop file
%__mkdir_p %{buildroot}%{_datadir}/applications/

%__cat > %{buildroot}%{_datadir}/applications/%{srcname}.desktop << EOF
[Desktop Entry]
Type=Application
Exec=2ManDVD -graphicssystem raster
Icon=2ManDVD
GenericName=2ManDVD
Comment=Video DVD Creator
Name=2ManDVD
Terminal=false
Categories=AudioVideo;DiscBurning;
X-KDE-StartupNotify=true
EOF

%__install -D -m 644 Interface/mandvd.png %{buildroot}%{_datadir}/pixmaps/%{srcname}.png

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{srcname}
%dir %{_datadir}/%{srcname}
%{_datadir}/%{srcname}/%{srcname}
%{_datadir}/%{srcname}/2mandvd_*.qm
%{_datadir}/%{srcname}/fake.pl
%{_datadir}/applications/%{srcname}.desktop
%{_datadir}/pixmaps/%{srcname}.png



%changelog
* Fri Jun 08 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.8.2-1
+ Revision: 803396
- Make it compile with ffmpeg 0.11
- Update to 1.8.2
- Build for ffmpeg 0.11.x

  + Andrey Bondrov <abondrov@mandriva.org>
    - Update BuildRequires

* Sun Jan 08 2012 Andrey Bondrov <abondrov@mandriva.org> 1.7.3-1
+ Revision: 758682
- New version 1.7.3, require Exif

* Tue May 31 2011 Sandro Cazzaniga <kharec@mandriva.org> 1.5.5-1
+ Revision: 682088
- 1.5.5

* Mon Mar 14 2011 Stéphane Téletchéa <steletch@mandriva.org> 1.5.3-1
+ Revision: 644731
- update to new version 1.5.3

* Sat Oct 09 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.4-1mdv2011.0
+ Revision: 584384
- Update to new version

* Fri Jul 30 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.3.5-1mdv2011.0
+ Revision: 563290
- update to 1.3.5
- drop patch0, merged upstream
- improve description
- Exec in the .desktop file must be 2ManDVD, lower case doesn't work
- drop the .desktop file from SOURCES and create it in the spec instead, this way
  it's easier to spot necessary changes

* Mon Apr 19 2010 Stéphane Téletchéa <steletch@mandriva.org> 1.3.3-4mdv2010.1
+ Revision: 536759
- Adjust ppegtopnm detection, fixes #58695

* Mon Apr 19 2010 Stéphane Téletchéa <steletch@mandriva.org> 1.3.3-3mdv2010.1
+ Revision: 536729
- Add missing fake.pl script

* Sun Mar 28 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.3.3-2mdv2010.1
+ Revision: 528474
- rebuild
- Update to 1.3.3

* Sat Mar 13 2010 Funda Wang <fwang@mandriva.org> 1.3.2-1mdv2010.1
+ Revision: 518684
- new version 1.3.2

* Mon Mar 08 2010 Stéphane Téletchéa <steletch@mandriva.org> 1.3.1-2mdv2010.1
+ Revision: 515906
- Correct growisofs requires

* Mon Mar 01 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.3.1-1mdv2010.1
+ Revision: 513035
- Update to 1.3.1

* Thu Feb 25 2010 Stéphane Téletchéa <steletch@mandriva.org> 1.3-2mdv2010.1
+ Revision: 511190
- Forgot to bump rel
- Add missing Requires
- Transform trancode requires into suggests since this package is not available in official mandriva repositories

  + Ahmad Samir <ahmadsamir@mandriva.org>
    - 1.3 now requires qt >= 4.6

* Wed Feb 24 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.3-1mdv2010.1
+ Revision: 510789
- rename back the symlink in bindir, otherwise it doesn't work??
- adapt spec for package renaming
- rename to lowercase
- clean spec
- fix license
- update to 1.3
- name the executable 2mandvd, more robust this way
- use "EXEC=2mandvd -graphicssystem raster" as per upstream's recomendation
- fix requires (again)
- fix requires

* Wed Jan 27 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.2-3mdv2010.1
+ Revision: 497157
- only suggest transcode

* Wed Jan 27 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.2-2mdv2010.1
+ Revision: 496931
- use %%qmake_qt4 and %%make macors (the latter to enable parallel build
  which seems to work)
- make .desktop file compliant with xdg specs

* Mon Jan 18 2010 Stéphane Téletchéa <steletch@mandriva.org> 1.2-1mdv2010.1
+ Revision: 493378
- import 2ManDVD

