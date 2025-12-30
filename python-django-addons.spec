%define realname  django-addons
%define name      python-%{realname}
%define version   0.6.4
%define release   3

Name:           %{name}
Version:        2.0.1
Release:        3
Summary:        Addon framework to create pluggable Django addons
Group:          Development/Python
License:        BSD
URL:            https://pypi.python.org/pypi/django-addons
Source:         https://pypi.python.org/packages/source/d/django-addons/django-addons-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-django
Requires:       python-django python-django-staticfiles
Suggests:       python-django-notification
BuildSystem:	python

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

%install -a
rm -f %{buildroot}/usr/django_addons/templates/addons.html

%files
%{py_puresitedir}/django_addons
%{py_puresitedir}/django_addons-%{version}-*-info
