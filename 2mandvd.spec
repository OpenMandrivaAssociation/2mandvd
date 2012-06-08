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

