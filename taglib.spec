%define major 1
%define minor 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d
%define libnametagc %mklibname %{name}_c %{minor}

Summary:	Library for reading and editing audio meta data
Name:		taglib
Version:	1.12
Release:	1
License:	LGPLv2+
Group:		File tools
Url:		http://www.taglib.org
Source0:	http://taglib.github.io/releases/%{name}-%{version}.tar.gz
# (tpg) fix broken pc files
Patch0:	taglib-1.5rc1-multilib.patch
## upstream patches
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(cppunit)

%description
TagLib, is well, a library for reading and editing audio meta data, 
commonly know as tags.

Some goals of TagLib:
- A clean, high level, C++ API to handling audio meta data.
- Support for at least ID3v1, ID3v2 and Ogg Vorbis comments.
- A generic, simple API for the most common tagging related functions.
- Binary compatibility between minor releases using the standard KDE/Qt
  techniques for C++ binary compatibility.
- Make the tagging framework extensible by library users; i.e. it will be
  possible for libarary users to implement additional ID3v2 frames,
  without modifying the TagLib source.

Because TagLib desires to be toolkit agnostic, in hope of being widely
adopted and the most flexible in licensing TagLib provides many of its
own toolkit classes; in fact the only external dependency that TagLib has,
it a semi-sane STL implementation.

#---------------------------------------------------------------------

%package -n %{libname}
Group:		System/Libraries
Summary:	Library for reading and editing audio meta data

%description -n %{libname}
Main taglib library.

%files -n %{libname}
%{_libdir}/libtag.so.%{major}*

#---------------------------------------------------------------------

%package -n %{libnametagc}
Group:		System/Libraries
Summary:	A C bindings for taglib library

%description -n %{libnametagc}
TagLib, is well, a library for reading and editing audio meta data.

%files -n %{libnametagc}
%{_libdir}/libtag_c.so.%{minor}*

#---------------------------------------------------------------------

%package -n %{devname}
Group:		Development/C
Summary:	Headers and other files for taglib development
Requires:	%{libname} = %{EVRD}
Requires:	%{libnametagc} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Provides:	lib%{name}-devel = %{EVRD}

%description -n %{devname}
Install this package if you want do compile applications
using the libtag library.

%files -n %{devname}
%{_bindir}/taglib-config
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

#---------------------------------------------------------------------

%prep
%autosetup -p1

%build
%cmake -DEXEC_INSTALL_PREFIX="%{_prefix}" -DLIB_INSTALL_DIR="%{_libdir}" -DWITH_ASF=ON -DWITH_MP4=ON -G Ninja
%ninja

%install
%ninja_install -C build
