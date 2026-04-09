%define major 2
%define minor 2
%define oldlibname %mklibname %{name} 1
%define olddevname %mklibname %{name} -d
%define oldlibnametagc %mklibname %{name}_c 0
%define libname %mklibname tag
%define devname %mklibname tag -d
%define libnametagc %mklibname tag_c

Summary:	Library for reading and editing audio meta data
Name:		taglib
Version:	2.2.1
Release:	1
License:	LGPLv2+
Group:	File tools
Url:		https://www.taglib.org
Source0:	https://taglib.github.io/releases/%{name}-%{version}.tar.gz
Source100:	taglib.rpmlintrc
BuildRequires:		cmake >= 3.10
BuildRequires:		ninja
BuildRequires:		cmake(utf8cpp)
BuildRequires:		pkgconfig(cppunit)
BuildRequires:		pkgconfig(zlib)

%description
TagLib, is well, a library for reading and editing audio meta data, commonly
know as tags.
Some goals of the library:
- A clean, high level, C++ API to handling audio meta data.
- Support for at least ID3v1, ID3v2 and Ogg Vorbis comments.
- A generic, simple API for the most common tagging related functions.
- Binary compatibility between minor releases using the standard KDE/Qt
  techniques for C++ binary compatibility.
- Make the tagging framework extensible by library users; i.e. it will be
  possible for users to implement additional ID3v2 frames, without modifying
  the sources.
Because TagLib desires to be toolkit agnostic, in hope of being widely
adopted and the most flexible in licensing it provides many of its own toolkit
classes; in fact the only external dependency that TagLib has, it a semi-sane
STL implementation.

#---------------------------------------------------------------------

%package -n %{libname}
Summary:	Library for reading and editing audio meta data
Group:		System/Libraries
# Renamed before 6.0 2024-12-29
%rename %{oldlibname}

%description -n %{libname}
Library for reading and editing audio meta data. This package contains
the main library.

%files -n %{libname}
%{_libdir}/libtag.so.%{major}*

#---------------------------------------------------------------------

%package -n %{libnametagc}
Summary:	A C bindings for taglib library
Group:		System/Libraries
# Renamed before 6.0 2024-12-29
%rename %{oldlibnametagc}

%description -n %{libnametagc}
This is a library for reading and editing audio meta data.
This package contains the c bindings for the library,

%files -n %{libnametagc}
%{_libdir}/libtag_c.so.%{minor}*

#---------------------------------------------------------------------

%package -n %{devname}
Summary:	Headers and other files for taglib development
Group:		Development/C

Requires:	%{libname} = %{EVRD}
Requires:	%{libnametagc} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Provides:	lib%{name}-devel = %{EVRD}
# Renamed before 6.0 2024-12-29
%rename %{olddevname}

%description -n %{devname}
Headers and other files for taglib development. Install this package if you
want do compile applications using the taglib library.

%files -n %{devname}
%doc CHANGELOG.md README.md
%{_bindir}/%{name}-config
%{_includedir}/%{name}/*
%{_libdir}/*.so
%{_libdir}/cmake/%{name}/*.cmake
%{_libdir}/pkgconfig/*.pc

#---------------------------------------------------------------------

%prep
%autosetup -p1

#conf
%cmake -DEXEC_INSTALL_PREFIX="%{_prefix}" \
			-DLIB_INSTALL_DIR="%{_libdir}" \
			-DWITH_ASF=ON \
			-DWITH_MP4=ON \
			-G Ninja


%build
%ninja_build -C build


%install
%ninja_install -C build
