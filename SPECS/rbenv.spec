Name:     	rbenv
Version:  	0.4.0
Release:  	1%{?dist:%{dist}}
Group: 	  	Applications/System
Summary:  	The rbenv program for running multiple Ruby instances.
BuildArch: 	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot
License:  	MIT
URL:      	https://github.com/sstephenson/rbenv    
Source0: 	rbenv-0.4.0.tar.gz
BuildRequires:	redhat-rpm-config

%description
Installs rbenv in shared location for all users to use.  Install the rvm-ruby packages with ruby versions you want.

%prep
%setup -q

%build

%install
# for now files will live in /opt
install -m 0755 -d $RPM_BUILD_ROOT/opt/%{name}-%{version}
cp -r * $RPM_BUILD_ROOT/opt/%{name}-%{version}
#install -m 0755 * $RPM_BUILD_ROOT/opt/%{name}-%{version}
cd $RPM_BUILD_ROOT/opt
ln -s %{name}-%{version} %{name}

# adding config to global profile
install -m 0755 -d $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d
cat > $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d/%{name}.sh <<END_OF_RBENV_PROFILE
# rbenv path update and initialisation
#
export PATH="/opt/%{name}/bin:\$PATH"
eval "\$(rbenv init -)"
END_OF_RBENV_PROFILE

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo " "
echo "rbenv have been installed in /opt/%{name}.  Please install rbenv-ruby packages you need and tell rbenv which version to use."

%files
%dir /opt/%{name}-%{version}
/opt/%{name}-%{version}/*
/opt/%{name}
/%{_sysconfdir}/profile.d/%{name}.sh

%changelog
* Wed Mar 19 2014 Guy Gershoni <guy@conchus.com> - 1-0.4.0
- Initial version of the package

