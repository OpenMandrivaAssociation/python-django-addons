%define realname  django-addons
%define name      python-%{realname}
%define version   0.6.4
%define release   %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Addon framework to create pluggable Django addons
Group:          Development/Python
License:        BSD
URL:            http://pypi.python.org/pypi/django-addons
Source:         http://pypi.python.org/packages/source/d/django-addons/%{realname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
BuildRequires:  python-devel python-setuptools python-django
Requires:       python-django python-django-staticfiles
Suggests:       python-django-notification

%description
A Django app used to add true plug-n-play functionality to your own Django
applications and projects

Django-addons is a bunch of code that makes writing addon/plugins for your
Django project much easier. Add django-addons to your Django project and 
you can drop all the addons to '<projectdir>/addons' directory.

Features
========

* Addons overview page
* Automatic signal connecting of addons
* Automatic URL discovery of addons
* Template hooking system (inject code from addons to your main project)
* Django-staticfiles to serve site media from each addon
* Django-notifications support (automatic registration of noticetypes)
* Per addon localization
* Per addon settings
* Disabling addons via ./manage.py addons

%prep
%setup -q -n %{realname}-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root %{buildroot}
rm -f %{buildroot}/usr/django_addons/templates/addons.html

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README LICENSE AUTHORS
%{py_puresitedir}/*
