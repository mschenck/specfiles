Name:           zookeeper
BuildRequires:  jdk make gcc
License:        Apache License 2.0
Group:          Development
Summary:        open-source coordination service for distributed applications
Version:        3.2.2
Release:        1
URL:            http://hadoop.apache.org/zookeeper/
Source:         http://mirror.cloudera.com/apache//hadoop/zookeeper/zookeeper-3.3.1/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Patch0: zkpython-build.xml-3.2.2.patch

%description 
ZooKeeper is a distributed, open-source coordination service for distributed applications. It exposes a simple set of primitives that distributed applications can build upon to implement higher level services for synchronization, configuration maintenance, and groups and naming. It is designed to be easy to program to, and uses a data model styled after the familiar directory tree structure of file systems. It runs in Java and has bindings for both Java and C.

Coordination services are notoriously hard to get right. They are especially prone to errors such as race conditions and deadlock. The motivation behind ZooKeeper is to relieve distributed applications the responsibility of implementing coordination services from scratch.

%package server
Summary: Zookeeper server
Group: Applications/System

%description server
Zookeeper server

%package client
Summary: Zookeeper C client (multithreaded)
Group: Development

%description client
Zookeeper client

%prep 
rm -rf %{buildroot}
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
cd src/c
./configure --prefix=%{buildroot}
make cli_st

%install 
# Server
mkdir -p %{buildroot}/opt/zookeeper/
cp -r bin %{buildroot}/opt/zookeeper/
cp -r build.xml %{buildroot}/opt/zookeeper/
cp -r conf %{buildroot}/opt/zookeeper/
cp -r contrib %{buildroot}/opt/zookeeper/
cp -r docs %{buildroot}/opt/zookeeper/
cp -r lib %{buildroot}/opt/zookeeper/
cp -r LICENSE.txt %{buildroot}/opt/zookeeper/
cp -r NOTICE.txt %{buildroot}/opt/zookeeper/
cp -r recipes %{buildroot}/opt/zookeeper/
cp -r zookeeper*jar* %{buildroot}/opt/zookeeper/

# Client
cd src/c
make install
export LD_LIBRARY_PATH=%{buildroot}/lib
cd ../contrib/zkpython
ant install
mv usr %{buildroot}/

%post client
/sbin/ldconfig

%clean
rm -rf %{buildroot}

%files server
/opt/zookeeper/*

%files client
/bin/*
/lib/*
/usr/lib64/*
/include/*

%changelog
* Thu Nov  18 2010 Michael Schenck <mschenck@tek-ops.com>
- Initial build
