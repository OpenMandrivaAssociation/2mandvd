Name:		2ManDVD
Version:	1.3
Release:	%mkrel 1
Summary:	Video DVD creation tool
URL:		http://2mandvd.tuxfamily.org/
# GPLv2 and LGPL for some icons
License:	GPLv2 and LGPL
Group:		Video
Source:		http://download.tuxfamily.org/2mandvd/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
BuildRequires:  qt4-devel
Requires:	dvdauthor
Requires:	dvdauthor
Requires:	ffmpeg >= 0.5
Requires:	ffmpegthumbnailer
Requires:	mencoder
Requires:	mjpegtools
Requires:	mkisofs
Requires:	mplayer
Requires:	netpbm
Requires:	sox
Requires:	transcode
BuildRoot:	%{_tmppath}/%{name}-%{version}-build


%description
ManDVD is a graphical tool for creating Video DVDs, including menus.

%prep
%setup -q -n %{name}

%build
%qmake_qt4 2ManDVD.pro
%make

%install
rm -rf %{buildroot}

# put the executable in %{_datadir}/%{name} and symlink it to %_bindir
# otherwise the UI localizations don't work
install -D -m 755 %{name} %{buildroot}%{_datadir}/%{name}/%{name}

mkdir %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
	ln -s %{_datadir}/%{name}/%{name} 2mandvd
popd

install -m 644 2mandvd_*.qm %{buildroot}%{_datadir}/%{name}

install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -D -m 644 Interface/mandvd.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/2mandvd
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{name}
%{_datadir}/%{name}/2mandvd_*.qm
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
