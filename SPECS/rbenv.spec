Name:     rbenv
Version:  0.4.0
Release:  1%{?dist:%{dist}}
Group: 	  Applications/System
Summary:  The rbenv program for running multiple Ruby instances.
BuildArch: noarch
License:  MIT
URL:      https://github.com/sstephenson/rbenv    
Source0:  https://github.com/sstephenson/rbenv/archive/v0.4.0.tar.gz
BuildRequires:	redhat-rpm-config

%global buildroot %{_topdir}/BUILDROOT/%{name}-%{version}-%{release}.%{_arch}

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
%defattr(-,root,root)
%{buildroot}/etc/profile.d/rbenv.sh
%{buildroot}/opt/rbenv
%{buildroot}/opt/rbenv-0.4.0/LICENSE
%{buildroot}/opt/rbenv-0.4.0/README.md
%{buildroot}/opt/rbenv-0.4.0/bin/rbenv
%{buildroot}/opt/rbenv-0.4.0/bin/ruby-local-exec
%{buildroot}/opt/rbenv-0.4.0/completions/rbenv.bash
%{buildroot}/opt/rbenv-0.4.0/completions/rbenv.zsh
%{buildroot}/opt/rbenv-0.4.0/libexec/rbenv
%{buildroot}/opt/rbenv-0.4.0/libexec/rbenv---version
%{buildroot}/opt/rbenv-0.4.0/libexec/rbenv-commands
%{buildroot}/opt/rbenv-0.4.0/libexec/rbenv-completions
%{buildroot}/opt/rbenv-0.4.0/libexec/rbenv-exec
%{buildroot}/opt/rbenv-0.4.0/libexec/rbenv-global
%{buildroot}/opt/rbenv-0.4.0/libexec/rbenv-help
%{buildroot}/opt/rbenv-0.4.0/libexec/rbenv-hooks
%{buildroot}/opt/rbenv-0.4.0/libexec/rbenv-init
%{buildroot}/opt/rbenv-0.4.0/libexec/rbenv-local
%{buildroot}/opt/rbenv-0.4.0/libexec/rbenv-prefix
%{buildroot}/opt/rbenv-0.4.0/libexec/rbenv-rehash
%{buildroot}/opt/rbenv-0.4.0/libexec/rbenv-root
%{buildroot}/opt/rbenv-0.4.0/libexec/rbenv-sh-rehash
%{buildroot}/opt/rbenv-0.4.0/libexec/rbenv-sh-shell
%{buildroot}/opt/rbenv-0.4.0/libexec/rbenv-shims
%{buildroot}/opt/rbenv-0.4.0/libexec/rbenv-version
%{buildroot}/opt/rbenv-0.4.0/libexec/rbenv-version-file
%{buildroot}/opt/rbenv-0.4.0/libexec/rbenv-version-file-read
%{buildroot}/opt/rbenv-0.4.0/libexec/rbenv-version-file-write
%{buildroot}/opt/rbenv-0.4.0/libexec/rbenv-version-name
%{buildroot}/opt/rbenv-0.4.0/libexec/rbenv-version-origin
%{buildroot}/opt/rbenv-0.4.0/libexec/rbenv-versions
%{buildroot}/opt/rbenv-0.4.0/libexec/rbenv-whence
%{buildroot}/opt/rbenv-0.4.0/libexec/rbenv-which

%dir %{buildroot}/opt/rbenv-0.4.0

%changelog
* Wed Mar 19 2014 Guy Gershoni <guy@conchus.com> - 1-0.4.0
- Initial version of the package

