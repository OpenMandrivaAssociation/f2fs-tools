%define major 10
%define format_major 9
%define libname %mklibname f2fs %{major}
%define libformat %mklibname f2fs_format %{format_major}
%define devname %mklibname f2fs -d
%global optflags %{optflags} -Oz

Summary:	Tools for Flash-Friendly File System (F2FS)
Name:		f2fs-tools
Version:	1.16.0
Release:	1
License:	GPLv2+
Group:		System/Kernel and hardware
URL:		https://sourceforge.net/projects/f2fs-tools/
Source0:	http://git.kernel.org/cgit/linux/kernel/git/jaegeuk/f2fs-tools.git/snapshot/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(ossp-uuid)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(blkid)
BuildRequires:	pkgconfig(libsepol)
BuildRequires:	pkgconfig(libacl)
Requires:	%{libname} = %{EVRD}
Requires:	%{libformat} = %{EVRD}

%description
NAND flash memory-based storage devices, such as SSD, and SD cards,
have been widely being used for ranging from mobile to server systems.
Since they are known to have different characteristics from the
conventional rotational disks,a file system, an upper layer to
the storage device, should adapt to the changes
from the sketch.

F2FS is a new file system carefully designed for the
NAND flash memory-based storage devices.
We chose a log structure file system approach,
but we tried to adapt it to the new form of storage.
Also we remedy some known issues of the very old log
structured file system, such as snowball effect
of wandering tree and high cleaning overhead.

Because a NAND-based storage device shows different characteristics
according to its internal geometry or flash memory management
scheme aka FTL, we add various parameters not only for configuring
on-disk layout, but also for selecting allocation
and cleaning algorithms.

%package -n %{libname}
Summary:	Libraries for Flash-Friendly File System (F2FS)
Group:		System/Libraries
Obsoletes:	%{mklibname f2fs 0} < 1.9.0
Obsoletes:	%{mklibname f2fs 1} < 1.9.0
Obsoletes:	%{mklibname f2fs 2} < 1.9.0

%description -n %{libname}
This package contains the libraries for Flash-Friendly File System (F2FS).

%package -n %{libformat}
Summary:	Format library for Flash-Friendly File System (F2FS)
Group:		System/Libraries
Obsoletes:	%{mklibname f2fs_format 0} < 1.9.0
Obsoletes:	%{mklibname f2fs_format 1} < 1.9.0

%description -n %{libformat}
This package contains the format library for Flash-Friendly File System (F2FS).

%package -n %{devname}
Summary:	Development files for %{name}
Group:		System/Libraries
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}
Requires:	%{libformat} = %{EVRD}

%description -n %{devname}
This package contains the libraries needed to develop applications
that use %{name}.

%prep
%autosetup -p1

%build
./autogen.sh

%configure \
	--disable-static \
	--without-selinux

%make_build

%install
%make_install

mkdir -m 755 -p %{buildroot}%{_includedir}
install -m 644 include/f2fs_fs.h %{buildroot}%{_includedir}
install -m 644 mkfs/f2fs_format_utils.h %{buildroot}%{_includedir}
rm -f %{buildroot}/%{_libdir}/*.la

%files
%doc AUTHORS
%{_sbindir}/f2fscrypt
%{_sbindir}/defrag.f2fs
%{_sbindir}/mkfs.f2fs
%{_sbindir}/fibmap.f2fs
%{_sbindir}/fsck.f2fs
%{_sbindir}/dump.f2fs
%{_sbindir}/parse.f2fs
%{_sbindir}/resize.f2fs
%{_sbindir}/sload.f2fs
%{_sbindir}/f2fs_io
%{_sbindir}/f2fslabel
%doc %{_mandir}/man8/*.8.*

%files -n %{libname}
%{_libdir}/libf2fs.so.%{major}*

%files -n %{libformat}
%{_libdir}/libf2fs_format.so.%{format_major}*

%files -n %{devname}
%{_includedir}/*.h
%{_libdir}/*.so
