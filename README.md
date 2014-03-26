= offline-rbenv-rpm =

Create a stand alone RPM for rbenv so can be installed in prod envs.

This RPM does not download anything from the Internet.  The idea is to allow you to install rbenv on a production environment where internet access is limited.

== Building RPM ==

=== Centos/RHEL 5.x ===

==== Useful sites ====
http://wiki.centos.org/HowTos/SetupRpmBuildEnvironment
http://www.lamolabs.org/blog/164/centos-rpm-tutorial-1/
http://www.lamolabs.org/blog/6837/centos-rpm-tutorial-part-3-building-your-own-rpm-of-jboss/

==== Prepare ====
Need to install the following packages to allow you to build RPMs:
```
yum install rpm-build redhat-rpm-config
```
For EL5 you will also need:
```
yum install buildsys-macros
```
You may also want rpmdevtools for setting up new projects etc.  You will need to install EPEL repo first: 
```
yum install rpmdevtools
```
Building RPMs should never be done as root so:
```
adduser rpmbuild
su - rpmbuild
git clone https://github.com/ggershoni/offline-rbenv-rpm
echo '%_topdir %(echo $HOME)/offline-rbenv-rpm' > ~/.rpmmacros 
cd offline-rbenv-rpm
rpmbuild -ba SPECS/rbenv.spec
```

== Install RPM ==
```
wget --no-check-certificate https://github.com/ggershoni/offline-rbenv-rpm/raw/master/RPMS/noarch/rbenv-0.4.0-1.noarch.rpm
sudo yum install --nogpgcheck rbenv-0.4.0-1.noarch.rpm
```
