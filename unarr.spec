%define major	1
%define libname	%mklibname unarr %{major}
%define devname %mklibname -d unarr
%define date	20160923

Name:		unarr
Version:	0
Release:	1.%{date}
Group:		Development/C
Summary:	A decompression library
License:	LGPLv2+
Url:            https://github.com/zeniko/unarr
Source0:	https://github.com/zeniko/unarr/archive/master.zip
Source1:        https://raw.githubusercontent.com/selmf/unarr/master/CMakeLists.txt
Patch0:		unarr-install.patch
BuildRequires: 	cmake
BuildRequires: 	pkgconfig(zlib)
BuildRequires: 	bzip2-devel

%description
A lightweight decompression library with support for rar, tar and zip
archives.
#---------------------------------------------------------------
%package -n %{libname}
Summary:        A decompression library

%description -n %{libname}
A lightweight decompression library with support for rar, tar and zip
archives.

%files -n %{libname}
%doc AUTHORS COPYING README
%{_libdir}/*.so.%{major}*
#---------------------------------------------------------------


%package -n %{devname}
Summary:	Development files for %{name}
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%files -n %{devname}
%doc AUTHORS COPYING README
%{_includedir}/*
%{_libdir}/lib%{name}.so
#---------------------------------------------------------------

%prep
%setup -qn %{name}-master
cp -p %{SOURCE1} .
%patch0	-p0

%build
export CFLAGS+="%{optflags} -DDEBUG -g"
%cmake 
%make

%install
%makeinstall_std -C build LIB_INSTALL_DIR=%{_libdir}
find %{buildroot} -name '*.a' -exec rm -f {} ';'



