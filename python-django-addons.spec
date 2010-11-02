%define realname    django-addons
%define name	    python-%{realname}
%define version     0.1
%define release %mkrel 1

Name: %{name}
Version: %{version}
Release: %{release}
Summary:        A simple project to make plugging functionality in your projects using external apps (addons or plugins) easier
Group:          Development/Python
License:        BSD
URL:            http://bitbucket.org/indifex/django-addons
Source:         %{realname}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
BuildRequires:  python-devel python-setuptools
Requires:       python-django

%description
A simple project to make plugging functionality in your projects 
using external apps (addons or plugins) easier.

%prep
%setup -q -n %{realname}-%{version}
find . -name \*._* -exec rm {} +
find . -name \*.buildinfo* -exec rm {} +

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/usr/django_addons/templates/addons.html

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{py_puresitedir}/*

