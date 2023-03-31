# we don't want to provide private python extension libs
%define _exclude_files_from_autoprov %{python2_sitearch}/.*\\.so\\|%{python3_sitearch}/.*\\.so

Name:		libyui-bindings
Version:	4.2.22
Release:	2
Summary:	Bindings to the Libyui user interface abstraction layer
Group:		System/Libraries
License:	LGPLv2+
URL:		https://github.com/libyui/libyui-bindings
Source0:	https://github.com/libyui/libyui-bindings/archive/%{name}-%{version}.tar.xz
# Based on https://github.com/anaselli/libyui-bindings/tree/mageia
Patch0:		0001-Mageia-changes-to-get-also-libyui-mga.patch
Patch1:		0008-Fix-github-issue-15-Yitems-are-hard-to-manage-in-per.patch

BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	graphviz
#BuildRequires:	texlive
BuildRequires:	ghostscript
BuildRequires:	boost-devel
BuildRequires:	libtool
BuildRequires:	swig
BuildRequires:	pkgconfig(python3)
BuildRequires:	perl-devel
BuildRequires:	ruby-devel
BuildRequires:	pkgconfig(libyui)
Buildrequires:	pkgconfig(libyui-mga)

%description
libYUI is a library written entirely in C++ to provide an abstraction layer
for Qt, GTK and ncurses UI frameworks. This means that a single code in YUI
can be used to produce outputs using any of the 3 UI frameworks listed above.
This library was (and still is) used to create the YaST2 User Interface. 

#----------------------------------------------------------
%package -n python-libyui
Summary:	Python bindings for libyui
Group:		System/Libraries

%description -n python-libyui
Python bindings to the libyui UI wrapper library.

%files -n python-libyui
%{py_platsitedir}/yui.py
%{py_platsitedir}/_yui.so
# %{py_platsitedir}/__pycache__

#----------------------------------------------------------
%package -n perl-libyui
Summary:	Perl bindings for libyui
Group:		System/Libraries

%description -n perl-libyui
Perl bindings to the libyui UI wrapper library.

%files -n perl-libyui
%{_datadir}/perl*/vendor_perl/yui.pm
%{_libdir}/perl5/vendor_perl/yui.so

#----------------------------------------------------------
%package -n ruby-libyui
Summary:	Ruby bindings for libyui
Group:		System/Libraries

%description -n ruby-libyui
Ruby bindings to the libyui UI wrapper library.

%files -n ruby-libyui
%{_libdir}/ruby/vendor_ruby/_yui.so

#----------------------------------------------------------

%prep
%autosetup -p1

%build
# As of 1.1.2, can't use -G Ninja because of custom commands
# being written to Makefiles
%cmake \
	-DYPREFIX=%{_prefix}   \
	-DDOC_DIR=%{_docdir}   \
	-DLIB_DIR=%{_lib}      \
	-DSKIP_LATEX=yes       \
	-DENABLE_WERROR:BOOL=no \
	-DCMAKE_BUILD_TYPE=RELWITHDEBINFO \
	-DWITH_MGA=yes

%make_build

%install
%make_install -C build
