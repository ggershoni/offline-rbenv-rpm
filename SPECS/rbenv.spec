Name:     rbenv
Version:  0.4.0
Release:  1%{?dist:%{dist}}
Summary:  The rbenv program for running multiple Ruby instances.
BuildArch: noarch
License:  MIT
URL:      https://github.com/sstephenson/rbenv    
Source0:  https://github.com/sstephenson/rbenv/archive/v0.4.0.tar.gz

%description
Installs rbenv in shared location for all users to use.

%prep
%setup

# no building required.

%install
# for now files will live in /opt
rm -rf %{buildroot}
mkdir -p %{buildroot}/opt/%{name}-%{version}
cp -r * %{buildroot}/opt/%{name}-%{version}
cd %{buildroot}/opt
ln -s %{name}-%{version} %{name}

# adding config to global profile
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
cat > %{buildroot}%{_sysconfdir}/profile.d/rbenv.sh <<END_OF_RBENV_PROFILE
# rbenv path update and initialisation
#
export PATH="/opt/%{name}/bin:\$PATH"
eval "\$(rbenv init -)"
END_OF_RBENV_PROFILE

%clean
rm -rf %{buildroot}

%files
/opt/%{name}-%{version}/*
/etc/profile.d/rbenv.sh
/opt/rbenv

%changelog
* Wed Mar 19 2014 Guy Gershoni <guy@conchus.com> - 1-0.4.0
- Initial version of the package

