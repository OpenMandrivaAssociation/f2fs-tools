%define major 0
%define libname %mklibname f2fs %{major}
%define devname %mklibname f2fs -d

Summary:	Tools for Flash-Friendly File System (F2FS)
Name:		f2fs-tools
Version:	1.7.0
Release:	1
License:	GPLv2+
Group:		System/Kernel and hardware
URL:		http://sourceforge.net/projects/f2fs-tools/
Source0:	http://git.kernel.org/cgit/linux/kernel/git/jaegeuk/f2fs-tools.git/snapshot/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(ossp-uuid)
BuildRequires:	pkgconfig(uuid)
BuildRequires:	pkgconfig(libselinux)

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

%package -n	%{libname}
Summary:	Libraries for Flash-Friendly File System (F2FS)
Group:		System/Libraries

%description -n	%{libname}
This package contains the libraries for Flash-Friendly File System (F2FS)

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		System/Libraries
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}

%description -n	%{devname}
This package contains the libraries needed to develop applications
that use %{name}

%prep
%setup -q

%build
./autogen.sh

%configure \
	--disable-static

%make

%install
%makeinstall_std

mkdir -m 755 -p %{buildroot}%{_includedir}
install -m 644 include/f2fs_fs.h %{buildroot}%{_includedir}
install -m 644 mkfs/f2fs_format_utils.h %{buildroot}%{_includedir}
rm -f %{buildroot}/%{_libdir}/*.la

%files
%doc COPYING AUTHORS ChangeLog
%{_sbindir}/defrag.f2fs
%{_sbindir}/mkfs.f2fs
%{_sbindir}/fibmap.f2fs
%{_sbindir}/fsck.f2fs
%{_sbindir}/dump.f2fs
%{_sbindir}/parse.f2fs
%{_sbindir}/f2fstat
%{_mandir}/man8/*.8.*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*.h
%{_libdir}/*.so
