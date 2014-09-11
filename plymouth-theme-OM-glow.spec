# noarch package but uses _lib macro in post scripts
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	"Openmandriva Glow" Plymouth theme
Name:		plymouth-theme-OM-glow
Version:	1.0
Release:	0
License:	Creative Commons Attribution-ShareAlike
Group:		System/Kernel and hardware
Source0:	openmandriva-glow.tar.gz
Requires:	plymouth
Requires:	plymouth-two-step
Requires(post,postun):	plymouth-scripts


%description
This package contains the "OpenMandriva Glow" Plymouth theme.

%files
%{_datadir}/plymouth/themes/OpenMandriva-glow

%post
if [ -x %{_sbindir}/plymouth-set-default-theme ]; then
    export LIB=%{_lib}
    if [ $1 -eq 1 ]; then
        %{_sbindir}/plymouth-set-default-theme --rebuild-initrd OpenMandriva-glow
    else
        THEME=$(%{_sbindir}/plymouth-set-default-theme)
        if [ "$THEME" == "text" -o "$THEME" == "OpenMandriva-glow" ]; then
            %{_sbindir}/plymouth-set-default-theme --rebuild-initrd OpenMandriva-glow
        fi
    fi
fi

%postun
export LIB=%{_lib}
if [ $1 -eq 0 -a -x %{_sbindir}/plymouth-set-default-theme ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "OpenMandriva-glow" ]; then
        %{_sbindir}/plymouth-set-default-theme --reset --rebuild-initrd
    fi
fi

#----------------------------------------------------------------------------

%prep
%setup -q -c
find . -type f | xargs chmod 0644

%build
# nothing

%install
mkdir -p %{buildroot}%{_datadir}/plymouth/themes/

cp -r OpenMandriva-glow %{buildroot}%{_datadir}/plymouth/themes/
