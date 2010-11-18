%global BaseName greenlet
Name:           python26-%{BaseName}
BuildRequires:  python26
License:        MIT License
Group:          Development
Summary:        greenlet
Version:        0.3.1
Release:        1
URL:            http://bitbucket.org/ambroff/greenlet
Source:         http://pypi.python.org/packages/source/g/greenlet/greenlet-0.3.1.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Lightweight in-process concurrent programming

The greenlet package is a spin-off of Stackless, a version of CPython that supports micro-threads called "tasklets". Tasklets run pseudo-concurrently (typically in a single or a few OS-level threads) and are synchronized with data exchanges on "channels".

A "greenlet", on the other hand, is a still more primitive notion of micro- thread with no implicit scheduling; coroutines, in other words. This is useful when you want to control exactly when your code runs. You can build custom scheduled micro-threads on top of greenlet; however, it seems that greenlets are useful on their own as a way to make advanced control flow structures. For example, we can recreate generators; the difference with Python's own generators is that our generators can call nested functions and the nested functions can yield values too. Additionally, you don't need a "yield" keyword. See the example in tests/test_generator.py.

Greenlets are provided as a C extension module for the regular unmodified interpreter.

%prep
%setup -q -n %{BaseName}-%{version}

%build
python26 setup.py build

%install
rm -rf %{buildroot}

python26 setup.py install --no-compile --root %{buildroot} --install-lib %{_libdir}/python2.6/site-packages/

find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -f %{buildroot}%{_infodir}/dir

%clean
rm -rf %{buildroot}

%files
%{_libdir}/*

%changelog
* Thu Nov  18 2010 Michael Schenck <mschenck@tek-ops.com>
- Initial build
