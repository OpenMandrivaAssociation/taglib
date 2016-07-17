%define major 1
%define minor 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d
%define libnametagc %mklibname %{name}_c %{minor}
%define debug_package %{nil}

Summary:	Library for reading and editing audio meta data
Name:		taglib
Version:	1.11
Release:	1
License:	LGPLv2+
Group:		File tools
Url:		http://developer.kde.org/~wheeler/taglib.html
Source0:	http://taglib.github.io/releases/%{name}-%{version}.tar.gz
#Patch1:		https://raw.github.com/RussianFedora/taglib/master/taglib-1.9.1-ds-rusxmms-r9.patch
BuildRequires:	kde4-macros
BuildRequires:	librcc-devel
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
%{multiarch_bindir}/taglib-config

#---------------------------------------------------------------------

%prep
%setup -q
%patch1 -p1 -b .rusxmms~

%build
export CC=gcc
export CXX=g++
%cmake_kde4 -DWITH_ASF=ON -DWITH_MP4=ON
%make

%install
%makeinstall_std -C build

%multiarch_binaries %{buildroot}%{_bindir}/taglib-config

