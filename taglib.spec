
%define __libtoolize    /bin/true

%define compile_doc 0

%define name		taglib
%define major		0
%define libname_orig	lib%{name}
%define libname		%mklibname %{name} %{major}

Summary: 	TagLib, is well, a library for reading and editing audio meta data
Name:	 	%name
Version:	1.4
Release: %mkrel 3
License: 	GPL
Group: 		File tools
Source:		%name-%version.tar.bz2
URL: 		http://ktown.kde.org/~wheeler/taglib/
Requires: 	%{libname} = %{version}-%release
Conflicts:	taglib <= 0.96-1mdk
Patch1:		taglib-1.4-fix-mem-leak.patch
Patch2:         taglib-1.4-fix-rw.patch

BuildRequires:	multiarch-utils >= 1.0.3

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

%package	-n %{libname}
Group:		System/Libraries
Summary:	TagLib, is well, a library for reading and editing audio meta data
Provides:	%{libname_orig} = %{version}-%{release}
Conflicts:  taglib <= 0.96-1mdk

%description	-n %{libname}
Librairy for taglib

%package	-n %{libname}-devel
Group:		Development/C
Summary:	Headers and static lib for taglib development
Requires:	%{libname} = %version-%release
Provides:	%{libname_orig}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Conflicts:  taglib <= 0.96-1mdk

%description	-n %{libname}-devel
Install this package if you want do compile applications using the libtag
library.

%prep
%setup -q
%patch1 -p1 -b .fix_mem_leak
%patch2 -p0

%build
%configure2_5x
%make

%if %compile_doc
make doc
%endif

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/taglib-config

%if %compile_doc
(
install -d -m 0755 %buildroot/%_docdir/
cp -r taglib-api/  %buildroot/%_docdir/
)
%endif


%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
 
%files

#
%files -n %{libname}
%defattr(-,root,root)

%_libdir/libtag.la
%_libdir/libtag.so.*
%_libdir/libtag_c.la
%_libdir/libtag_c.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%_bindir/taglib-config
%multiarch %{multiarch_bindir}/taglib-config

%_libdir/libtag.so
%_libdir/libtag_c.so
%_libdir/pkgconfig/taglib.pc

%dir %_includedir/taglib/
%_includedir/taglib/*.h
%_includedir/taglib/*.tcc

%if %compile_doc
%dir %_docdir/taglib-api/
%dir %_docdir/taglib-api/html/
%doc %_docdir/taglib-api/html/*.html
%doc %_docdir/taglib-api/html/*.dot
%doc %_docdir/taglib-api/html/*.md5
%doc %_docdir/taglib-api/html/*.css
%doc %_docdir/taglib-api/html/*.png
%endif


