%define libnametag	%mklibname %{name} 1
%define libnametagc	%mklibname %{name}_c 0
%define libdev %mklibname %{name} -d
%define libold %mklibname %{name} 0
%define libolddev %mklibname %{name} 0 -d

Name: taglib
Version: 1.5
Release: %mkrel 1
Summary: Library for reading and editing audio meta data
License: GPL
Group: File tools
Source: %name-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
URL: http://ktown.kde.org/~wheeler/taglib/
Conflicts:	taglib <= 0.96-1mdk

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

%package	-n %{libnametag}
Group:		System/Libraries
Summary:	Library for reading and editing audio meta data
Conflicts:  taglib <= 0.96-1mdk
Obsoletes: %{libold} < 1.5.0
Obsoletes: taglib < 1.5.0

%description	-n %{libnametag}
Library for taglib

%post -n %{libnametag} -p /sbin/ldconfig
%postun -n %{libnametag} -p /sbin/ldconfig

%files -n %{libnametag}
%defattr(-,root,root)
%_libdir/libtag.la
%_libdir/libtag.so.*

#---------------------------------------------------------------------

%package	-n %{libnametagc}
Group: System/Libraries
Summary: Library for reading and editing audio meta data
Conflicts: taglib <= 0.96-1mdk
Conflicts: %{libold} < 1.5.0
Obsoletes: taglib < 1.5.0

%description	-n %{libnametagc}
TagLib, is well, a library for reading and editing audio meta data.

%post -n %{libnametagc} -p /sbin/ldconfig
%postun -n %{libnametagc} -p /sbin/ldconfig

%files -n %{libnametagc}
%defattr(-,root,root)
%_libdir/libtag_c.la
%_libdir/libtag_c.so.*

#---------------------------------------------------------------------

%package -n %{libdev}
Group: Development/C
Summary: Headers and static lib for taglib development
Requires: %{libnametag} = %version-%release
Requires: %{libnametagc} = %version-%release
Provides: %{name}-devel = %{version}-%{release}
Conflicts: taglib <= 0.96-1mdk
Obsoletes: %{libolddev}

%description -n %{libdev}
Install this package if you want do compile applications i
using the libtag library.

%files -n %{libdev}
%defattr(-,root,root)
%_bindir/taglib-config
%_libdir/*.so
%_libdir/pkgconfig/*
%_includedir/*
%multiarch %{multiarch_bindir}/taglib-config

#---------------------------------------------------------------------

%prep
%setup -q 

%build
%configure2_5x

%make

%install
rm -rf %buildroot
%makeinstall_std

%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/taglib-config

%clean
rm -rf %buildroot


