%define major 1
%define minor 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d
%define libnametagc %mklibname %{name}_c %{minor}

Summary:	Library for reading and editing audio meta data
Name:		taglib
Version:	1.8
Release:	4
License:	LGPLv2+
Group:		File tools
URL:		http://developer.kde.org/~wheeler/taglib.html
Source0:	taglib-%{version}.tar.gz
#(tpg) http://foetida.jaist.ac.jp:37565/~yaz/diary/2006/07/taglib-1.4_wchar.diff
Patch0:		taglib-1.4_wchar.diff
Patch1:		taglib-1.8-librcc.patch
BuildRequires:	zlib-devel
BuildRequires:	cppunit-devel
BuildRequires:	kde4-macros
BuildRequires:	librcc-devel

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

%description -n %{libname}
Main taglib library.


%files -n %{libname}
%{_libdir}/libtag.so.%{major}*

#---------------------------------------------------------------------

%package -n %{libnametagc}
Group:		System/Libraries
Summary:	A C bindings for taglib library

%description	-n %{libnametagc}
TagLib, is well, a library for reading and editing audio meta data.

%files -n %{libnametagc}
%{_libdir}/libtag_c.so.%{minor}*

#---------------------------------------------------------------------

%package -n %{develname}
Group:		Development/C
Summary:	Headers and static lib for taglib development
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libnametagc} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %{develname}
Install this package if you want do compile applications i
using the libtag library.

%files -n %{develname}
%{_bindir}/taglib-config
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{multiarch_bindir}/taglib-config

#---------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%cmake_kde4 -DWITH_ASF=ON -DWITH_MP4=ON
%make

%install
%makeinstall_std -C build

%multiarch_binaries %{buildroot}%{_bindir}/taglib-config



%changelog
* Wed Nov  7 2012 Arkady L. Shane <ashejn@rosalab.ru> 1.8-1
- update to 1.8
- apply patch to recode russian tags via librcc

* Wed Jul 11 2012 Andrey Bondrov <abondrov@mandriva.org> 1.7.2-1
+ Revision: 808821
- New version 1.7.2, drop no longer needed Conflicts and Obsoletes

* Mon Mar 26 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.7.1-1
+ Revision: 787123
- version update 1.7.1

* Mon Mar 05 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.7-1
+ Revision: 782254
- Update to 1.7

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.6.3-2
+ Revision: 661752
- multiarch fixes

* Fri Oct 01 2010 Funda Wang <fwang@mandriva.org> 1.6.3-1mdv2011.0
+ Revision: 582221
- update to new version 1.6.3

* Sat Apr 10 2010 Funda Wang <fwang@mandriva.org> 1.6.2-1mdv2010.1
+ Revision: 533551
- new version 1.6.2

* Sat Mar 13 2010 Funda Wang <fwang@mandriva.org> 1.6.1-1mdv2010.1
+ Revision: 518719
- BR kde4-macros
- update url

  + Emmanuel Andry <eandry@mandriva.org>
    - New version 1.6.1

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Use CMake to build
      Fix file list
      Remove old macros

* Fri Sep 18 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.6-3mdv2010.0
+ Revision: 444460
- Rebuild
- enable asf and mp4 support ( needed for amarok)

* Tue Sep 15 2009 Frederik Himpe <fhimpe@mandriva.org> 1.6-1mdv2010.0
+ Revision: 443191
- Update to new version 1.6
- Remove gcc 4.3 tests patch: not needed anymore

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.5-6mdv2010.0
+ Revision: 427224
- rebuild

* Mon Aug 18 2008 Emmanuel Andry <eandry@mandriva.org> 1.5-5mdv2009.0
+ Revision: 273257
- add P1 from gentoo to pass check with gcc4.3

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Mar 11 2008 Götz Waschk <waschk@mandriva.org> 1.5-4mdv2008.1
+ Revision: 185173
- rebuild for missing package

* Mon Feb 25 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.5-3mdv2008.1
+ Revision: 175106
- enable checks
- add cppunit-devel as a buildrequires, used by checks
- link with -ldl

* Mon Feb 25 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.5-2mdv2008.1
+ Revision: 174957
- new license policy
- add missing buildrequires on zlib-devel
- Patch0: convert cjk chars into utf8
- add explicit provides on libtaglib-devel
- use standard macros and defines
- make use of %%major in file list

* Thu Feb 21 2008 Helio Chissini de Castro <helio@mandriva.com> 1.5-1mdv2008.1
+ Revision: 173556
- New final upstream release 1.5

  + Thierry Vignaud <tv@mandriva.org>
    - fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Thu Feb 14 2008 Helio Chissini de Castro <helio@mandriva.com> 1.5-0.rc1.2mdv2008.1
+ Revision: 168652
- Obsolete taglib package, as they have no files inside, just a wrong explicit requires

* Wed Feb 13 2008 Helio Chissini de Castro <helio@mandriva.com> 1.5-0.rc1.1mdv2008.1
+ Revision: 167117
- Release Candidate 1 of new Taglib. Major bugfixes, but keeps ABI and API compatible.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon May 28 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.4-3mdv2008.0
+ Revision: 31990
- Add Patch2 (close bug #30620)


* Tue Apr 03 2007 Laurent Montel <lmontel@mandriva.com> 1.4-3mdv2007.1
+ Revision: 150241
- Fix mem leak

* Wed Dec 13 2006 Götz Waschk <waschk@mandriva.org> 1.4-2mdv2007.1
+ Revision: 96488
- Import taglib

* Wed Dec 13 2006 Götz Waschk <waschk@mandriva.org> 1.4-2mdv2007.1
- use the right configure macro

* Thu Jul 28 2005 Laurent MONTEL <lmontel@mandriva.com> 1.4-1mdk
- 1.4

* Wed Jan 26 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3.1-3mdk
- Add for multiarch

* Fri Jan 14 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3.1-2mdk
- Add patch1: fix kde bug #96926

* Mon Nov 08 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3.1-1mdk
- 1.3.1

* Sat Oct 02 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3-1mdk
- 1.3

* Wed Sep 29 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.2-2mdk
- merge lost changes from amd64-branch:
  * mklibnamification fixes

* Thu Jul 29 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.2-1mdk
- 1.2
- Desactivate doc

* Tue Jul 27 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.1-3mdk
- Compile doc

* Fri Jun 04 2004 Montel Laurent <lmontel@mandrakesoft.com> 1.1-2mdk
- Rebuild with new gcc

* Tue Apr 06 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.1-1mdk
- 1.1

