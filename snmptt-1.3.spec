Name:           snmptt
BuildRequires:  net-snmp-perl perl-Config-IniFiles
License:        GPLv2
Group:          Administration Tools
Summary:        SNMPTT (SNMP Trap Translator) is an SNMP trap handler written in Perl for use with the Net-SNMP / UCD-SNMP snmptrapd program (www.net-snmp.org).
Version:        1.3
Release:        1
URL:            http://www.snmptt.org/
Source:         http://downloads.sourceforge.net/project/snmptt/snmptt/snmptt_1.3/snmptt_1.3.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}
BuildArch:	noarch
Requires:	net-snmp

%description
SNMPTT (SNMP Trap Translator) is an SNMP trap handler written in Perl for use with the Net-SNMP / UCD-SNMP snmptrapd program (www.net-snmp.org).

%prep 
rm -rf %{buildroot}
%setup -q -n %{name}_%{version}

%build

%install
mkdir -p %{buildroot}/usr/sbin
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share/snmptt
mkdir -p %{buildroot}/etc/snmp
mkdir -p %{buildroot}/etc/logrotate.d
mkdir -p %{buildroot}/etc/rc.d/init.d
mkdir -p %{buildroot}/var/log/snmptt
mkdir -p %{buildroot}/var/spool/snmptt

cp snmptt %{buildroot}/usr/sbin
cp snmptthandler %{buildroot}/usr/sbin
cp snmpttconvert %{buildroot}/usr/bin
cp snmpttconvertmib %{buildroot}/usr/bin
cp snmptt-net-snmp-test %{buildroot}/usr/bin
cp snmptt.ini %{buildroot}/etc/snmp
cp snmptt-init.d %{buildroot}/etc/rc.d/init.d/snmptt
cp snmptt.logrotate %{buildroot}/etc/logrotate.d/snmptt
cp -r contrib %{buildroot}/usr/share/snmptt/
cp -r docs %{buildroot}/usr/share/snmptt/
cp -r examples %{buildroot}/usr/share/snmptt/
cp sample* %{buildroot}/usr/share/snmptt/
cp README %{buildroot}/usr/share/snmptt/

%post
echo "+------------------------------------------------------------------------------+"
echo "| SNMPTT installation successful!                                              |"
echo "+------------------------------------------------------------------------------+"
echo "| For standlone mode:                                                          |"
echo "|     Modify the Net-SNMP snmptrapd.conf file by adding the following line:    |"
echo "|                                                                              |"
echo "|          traphandle default /usr/sbin/snmptt                                 |"
echo "|                                                                              |"
echo "|                                                                              |"
echo "| For daemon mode:                                                             |"
echo "|     Modify /etc/snmp/snmptt.ini file by change the following line:           |"
echo "|         mode = standalone                                                    |"
echo "|     To:                                                                      |"
echo "|         mode = daemon                                                        |"
echo "|                                                                              |"
echo "|     Modify the Net-SNMP snmptrapd.conf file by adding the following line:    |"
echo "|                                                                              |"
echo "|         traphandle default /usr/sbin/snmptthandler                           |"
echo "|                                                                              |"
echo "|     Add the service using chkconfig:                                         |"
echo "|         chkconfig --add snmptt                                               |"
echo "|                                                                              |"
echo "|     Configure the service to start at runlevel 2345:                         |"
echo "|         chkconfig --level 2345 snmptt on                                     |"
echo "|                                                                              |"
echo "|     Start service:                                                           |"
echo "|         service snmptt start                                                 |"
echo "+------------------------------------------------------------------------------+"

%clean
rm -rf %{buildroot}

%files
/usr/sbin/snmptt
/usr/sbin/snmptthandler
/usr/bin/snmpttconvert
/usr/bin/snmpttconvertmib
/usr/bin/snmptt-net-snmp-test
/usr/share/snmptt/*
/etc/snmp/snmptt.ini
/etc/rc.d/init.d/snmptt
/etc/logrotate.d/snmptt

%changelog
* Thu Dec 16 2010 Michael Schenck <michael@tumblr.com>
- Initial build
