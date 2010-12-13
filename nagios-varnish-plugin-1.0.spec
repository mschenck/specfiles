%global BaseName nagios-varnish-plugin
Name:           nagios-varnish-plugin
BuildRequires:  make gcc varnish-libs-devel
License:        GPLv2
Group:          Server Configuration Tools
Summary:        Nagios plugin for Varnish
Version:        1.0
Release:        1
URL:            http://sourceforge.net/projects/varnish/files/nagios-varnish-plugin/
Source:         http://downloads.sourceforge.net/project/varnish/nagios-varnish-plugin/1.0/nagios-varnish-plugin-1.0.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}
Requires:	varnish-libs
Patch0:		nagios-varnish-plugin-1.0-strncmp_and_2.0update.patch


%description
Nagios plugin for Varnish

%prep 
rm -rf %{buildroot}
%setup -q -n %{name}-%{version}
%patch -p0

%build
./configure --prefix=%{buildroot} --libexecdir=%{buildroot}/usr/lib64/nagios/plugins/

%install
make
make install

%clean
rm -rf %{buildroot}

%files
/usr/lib64/nagios/plugins/*

%changelog
* Mon Dec  13 2010 Michael Schenck <michael@tumblr.com>
- Initial build
