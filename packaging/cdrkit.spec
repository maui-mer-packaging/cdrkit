# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
# 
# >> macros
# << macros

Name:       cdrkit
Summary:    A collection of CD/DVD utilities
Version:    1.1.11
Release:    11
Group:      Applications/System
License:    GPLv2
URL:        http://cdrkit.org/
Source0:    http://cdrkit.org/releases/cdrkit-%{version}.tar.gz
Source100:  cdrkit.yaml
Patch0:     cdrkit-1.1.8-werror.patch
Patch1:     cdrkit-1.1.9-efi-boot.patch
Patch2:     cdrkit-1.1.9-no_mp3.patch
Patch3:     cdrkit-1.1.9-buffer_overflow.patch
Patch4:     cdrkit-1.1.10-build-fix.patch
Patch5:     cdrkit-1.1.10-msg-format.patch
Patch6:     cdrkit-1.1.11-cmakewarn.patch
Patch7:     cdrkit-1.1.11-memset.patch
BuildRequires:  pkgconfig(zlib)
BuildRequires:  cmake
BuildRequires:  libcap-devel
BuildRequires:  perl
BuildRequires:  file-devel
BuildRequires:  bzip2-devel


%description
cdrkit is a collection of CD/DVD utilities.


%package -n genisoimage
Summary:    Creates an image of an ISO9660 filesystem
Group:      Applications/System

%description -n genisoimage
The genisoimage program is used as a pre-mastering program; i.e., it
generates the ISO9660 filesystem. Genisoimage takes a snapshot of
a given directory tree and generates a binary image of the tree
which will correspond to an ISO9660 filesystem when written to
a block device. Genisoimage is used for writing CD-ROMs, and includes
support for creating bootable El Torito CD-ROMs.

Install the genisoimage package if you need a program for writing
CD-ROMs.


%package -n wodim
Summary:    A command line CD/DVD recording program
Group:      Applications/Archiving

%description -n wodim
Wodim is an application for creating audio and data CDs. Wodim
works with many different brands of CD recorders, fully supports
multi-sessions and provides human-readable error messages.


%package -n icedax
Summary:    A utility for sampling/copying .wav files from digital audio CDs
Group:      Applications/Multimedia
Requires:   vorbis-tools

%description -n icedax
Icedax is a sampling utility for CD-ROM drives that are capable of
providing a CD's audio data in digital form to your host. Audio data
read from the CD can be saved as .wav or .sun format sound files.
Recording formats include stereo/mono, 8/12/16 bits and different
rates. Icedax can also be used as a CD player.


%package -n dirsplit
Summary:    Splits directory into multiple volumes with equal size
Group:      Applications/System
Requires:   genisoimage = %{version}-%{release}

%description -n dirsplit
The displit utility is designed to for a simple purpose: convert a 
directory with many multiple files (which are all smaller than a
certain medium, eg.  DVD) and "splits" it into "volumes", looking 
for the optimal order to get  the  best  space/medium-
number efficiency.



%prep
%setup -q -n %{name}-%{version}

# cdrkit-1.1.8-werror.patch
%patch0 -p1
# cdrkit-1.1.9-efi-boot.patch
%patch1 -p1
# cdrkit-1.1.9-no_mp3.patch
%patch2 -p1
# cdrkit-1.1.9-buffer_overflow.patch
%patch3 -p1
# cdrkit-1.1.10-build-fix.patch
%patch4 -p1
# cdrkit-1.1.10-msg-format.patch
%patch5 -p1
# cdrkit-1.1.11-cmakewarn.patch
%patch6 -p1
# cdrkit-1.1.11-memset.patch
%patch7 -p1
# >> setup
find . -type f -print0 | xargs -0 perl -pi -e 's#/usr/local/bin/perl#/usr/bin/perl#g'
find doc -type f -print0 | xargs -0 chmod a-x
# << setup

%build
# >> build pre
export CFLAGS="$RPM_OPT_FLAGS -Wall -Werror -Wno-unused-function -Wno-unused-variable -fno-strict-aliasing -Wno-unused-but-set-variable -Wno-array-bounds"
export CXXFLAGS="$CFLAGS"
export FFLAGS="$CFLAGS"
# << build pre

mkdir meego-build
cd meego-build
cmake ..  \
    -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
    -DBUILD_SHARED_LIBS:BOOL=ON

make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
cd meego-build
%make_install

# >> install post
perl -pi -e 's#^require v5.8.1;##g' $RPM_BUILD_ROOT%{_bindir}/dirsplit
ln -s genisoimage $RPM_BUILD_ROOT%{_bindir}/mkisofs
ln -s genisoimage $RPM_BUILD_ROOT%{_bindir}/mkhybrid
ln -s icedax $RPM_BUILD_ROOT%{_bindir}/cdda2wav
ln -s wodim $RPM_BUILD_ROOT%{_bindir}/cdrecord
ln -s wodim $RPM_BUILD_ROOT%{_bindir}/dvdrecord
ln -sf wodim.1.gz $RPM_BUILD_ROOT/%{_mandir}/man1/netscsid.1.gz

# we don't need cdda2mp3 since we don't have any mp3 {en,de}coder
rm $RPM_BUILD_ROOT%{_bindir}/cdda2mp3

# << install post




















%files -n genisoimage
%defattr(-,root,root,-)
# >> files genisoimage
%doc doc/genisoimage COPYING
%{_bindir}/genisoimage
%ghost %{_bindir}/mkisofs
%ghost %{_bindir}/mkhybrid
%{_bindir}/isodebug
%{_bindir}/isodump
%{_bindir}/isoinfo
%{_bindir}/isovfy
%{_bindir}/pitchplay
%{_bindir}/readmult
%doc %{_mandir}/man5/genisoimagerc.*
%doc %{_mandir}/man1/genisoimage.*
%doc %{_mandir}/man1/isodebug.*
%doc %{_mandir}/man1/isodump.*
%doc %{_mandir}/man1/isoinfo.*
%doc %{_mandir}/man1/isovfy.*
%doc %{_mandir}/man1/pitchplay.*
%doc %{_mandir}/man1/readmult.*
# << files genisoimage

%files -n wodim
%defattr(-,root,root,-)
# >> files wodim
%doc Changelog COPYING FAQ FORK START
%doc doc/READMEs doc/wodim
%{_bindir}/devdump
%{_bindir}/wodim
%ghost %{_bindir}/cdrecord
%ghost %{_bindir}/dvdrecord
%{_bindir}/readom
%{_sbindir}/netscsid
%doc %{_mandir}/man1/devdump.*
%doc %{_mandir}/man1/wodim.*
%doc %{_mandir}/man1/netscsid.*
%doc %{_mandir}/man1/readom.*
# << files wodim

%files -n icedax
%defattr(-,root,root,-)
# >> files icedax
%doc doc/icedax COPYING
%{_bindir}/icedax
%ghost %{_bindir}/cdda2wav
%{_bindir}/cdda2ogg
%doc %{_mandir}/man1/icedax.*
%doc %{_mandir}/man1/cdda2ogg.*
%doc %{_mandir}/man1/list_audio_tracks.*
# << files icedax

%files -n dirsplit
%defattr(-,root,root,-)
# >> files dirsplit
%{_bindir}/dirsplit
%doc %{_mandir}/man1/dirsplit.*
# << files dirsplit

