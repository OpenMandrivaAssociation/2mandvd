%define srcname	2ManDVD

Name:		2mandvd
Version:	1.3.3
Release:	%mkrel 4
Summary:	Video DVD creation tool
URL:		http://2mandvd.tuxfamily.org/
# GPLv2 and LGPL for some icons
License:	GPLv2 and LGPL
Group:		Video
Source:		http://download.tuxfamily.org/2mandvd/%{srcname}-%{version}.tar.gz
Source1:	%{srcname}.desktop
Patch0:		jpegtopnm_1.3.3_wrong_detection.patch

BuildRequires:  qt4-devel >= 4.6

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
Suggests:	transcode
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
Obsoletes:	2ManDVD

%description
ManDVD is a graphical tool for creating Video DVDs, including menus.

%prep
%setup -q -n %{srcname}
%patch0

%build
%qmake_qt4 2ManDVD.pro
%make

%install
rm -rf %{buildroot}

# put the executable in %{_datadir}/%{name} and symlink it to %_bindir
# otherwise the UI localizations don't work
install -D -m 755 %{srcname} %{buildroot}%{_datadir}/%{srcname}/%{srcname}

mkdir %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
	ln -s %{_datadir}/%{srcname}/%{srcname} 2ManDVD
popd

install -m 644 2mandvd_*.qm %{buildroot}%{_datadir}/%{srcname}
install -m 644 fake.pl %{buildroot}%{_datadir}/%{srcname}

install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{srcname}.desktop
install -D -m 644 Interface/mandvd.png %{buildroot}%{_datadir}/pixmaps/%{srcname}.png

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{srcname}
%dir %{_datadir}/%{srcname}
%{_datadir}/%{srcname}/%{srcname}
%{_datadir}/%{srcname}/2mandvd_*.qm
%{_datadir}/%{srcname}/fake.pl
%{_datadir}/applications/%{srcname}.desktop
%{_datadir}/pixmaps/%{srcname}.png
