%define srcname 2ManDVD

Summary:	Video DVD creation tool, successor to ManDVD
Name:		2mandvd
Version:	1.8.5
Release:	5
# GPLv2 and LGPL for some icons
License:	GPLv2+ and LGPL
Group:		Video
Url:		http://2mandvd.tuxfamily.org/
Source0:	http://download.tuxfamily.org/2mandvd/%{srcname}-%{version}.tar.gz
Patch0:		2ManDVD-1.8.5-ffmpeg2.0.patch
Patch1:		2ManDVD-1.8.5-install.patch
BuildRequires:	qt4-devel >= 4.6
BuildRequires:	ffmpeg-devel >= 2.5.4
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(sdl)

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
Obsoletes:	2ManDVD < %{EVRD}

%description
2ManDVD is a graphical tool for creating Video DVDs and slideshows, including
menus.

N.B. Executable name is 2ManDVD.

%files
%{_bindir}/%{srcname}
%{_bindir}/fake.pl
%dir %{_datadir}/%{srcname}
%{_datadir}/%{srcname}/2mandvd_*.qm
%{_datadir}/%{srcname}/Bibliotheque
%{_datadir}/%{srcname}/mandvdico.png
%{_datadir}/applications/%{srcname}.desktop

#----------------------------------------------------------------------------

%prep
%setup -q -n %{srcname}
%patch0 -p1
%patch1 -p1

%build
%qmake_qt4 2ManDVD.pro
%make

%install
make INSTALL_ROOT=%{buildroot} install

