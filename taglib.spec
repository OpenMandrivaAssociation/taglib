%define major 1
%define minor 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d
%define libnametagc %mklibname %{name}_c %{minor}
%define libold %mklibname %{name} 0
%define libolddev %mklibname %{name} 0 -d

Summary:	Library for reading and editing audio meta data
Name:		taglib
Version:	1.6.1
Release:	%mkrel 1
License:	LGPLv2+
Group:		File tools
URL:		http://developer.kde.org/~wheeler/taglib.html
Source:		http://ftp.musicbrainz.org/pub/musicbrainz/users/luks/taglib//%{name}-%{version}.tar.gz
#(tpg) http://foetida.jaist.ac.jp:37565/~yaz/diary/2006/07/taglib-1.4_wchar.diff
Patch0:		taglib-1.4_wchar.diff
Conflicts:	taglib <= 0.96-1mdk
BuildRequires:	zlib-devel
BuildRequires:	cppunit-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
TagLib, is well, a library for reading and editing audio meta data, 
commonly know as tags.
Some goals of TagLib:
A clean, high level, C++ API to handling audio meta data.
Support for at least ID3v1, ID3v2 and Ogg Vorbis comments.
A generic, simple API for the most common tagging related functions.
Binary compatibility between minor releases using the standard KDE/Qt 
techniques for C++ binary compatibility.
Make the tagging framework extensible by library users; i.e. it will be 
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
Conflicts:	taglib <= 0.96-1mdk
Obsoletes:	%{libold} < 1.5.0
Obsoletes:	taglib < 1.5.0

%description -n %{libname}
Main taglib library.


%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libtag.so.%{major}*

#---------------------------------------------------------------------

%package -n %{libnametagc}
Group:		System/Libraries
Summary:	A C bindings for taglib library
Conflicts:	taglib <= 0.96-1mdk
Conflicts:	%{libold} < 1.5.0
Obsoletes:	taglib < 1.5.0

%description	-n %{libnametagc}
TagLib, is well, a library for reading and editing audio meta data.

%files -n %{libnametagc}
%defattr(-,root,root)
%{_libdir}/libtag_c.so.%{minor}*

#---------------------------------------------------------------------

%package -n %{develname}
Group:		Development/C
Summary:	Headers and static lib for taglib development
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libnametagc} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Conflicts:	taglib <= 0.96-1mdk
Obsoletes:	%{libolddev}

%description -n %{develname}
Install this package if you want do compile applications i
using the libtag library.

%files -n %{develname}
%defattr(-,root,root)
%{_bindir}/taglib-config
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%multiarch %{multiarch_bindir}/taglib-config

#---------------------------------------------------------------------

%prep
%setup -q 
%patch0 -p1

%build
#(tpg) taglib have to be linked against -ldl, otherwise check fails
export LDFLAGS="%{optflags} -ldl"

%cmake_kde4 -DWITH_ASF=ON -DWITH_MP4=ON

%make

%install
rm -rf %{buildroot}
cd build
%makeinstall_std

%multiarch_binaries %{buildroot}%{_bindir}/taglib-config

%clean
rm -rf %{buildroot}
