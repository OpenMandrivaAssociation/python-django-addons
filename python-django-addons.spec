%define realname  django-addons
%define name      python-%{realname}
%define version   0.6.4
%define release   2

Name:           %{name}
Version:        0.6.6
Release:        2
Summary:        Addon framework to create pluggable Django addons
Group:          Development/Python
License:        BSD
URL:            http://pypi.python.org/pypi/django-addons
Source:         http://pypi.python.org/packages/source/d/django-addons/django-addons-%{version}.tar.gz
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
python setup.py install --root %{buildroot}
rm -f %{buildroot}/usr/django_addons/templates/addons.html

%clean

%files
%defattr(-,root,root,-)
%doc README LICENSE AUTHORS
%{py_puresitedir}/*


%changelog
* Fri Nov 12 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.6.4-1mdv2011.0
+ Revision: 596461
- Update to 0.6.4
- Update Summary, Source, URL and Description tags
- Add requires on python-django-staticfiles
- Add suggests on python-django-notification

* Tue Nov 02 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.1-1mdv2011.0
+ Revision: 591993
- add BR python-django
- import python-django-addons


