%define 	module elixir
Summary:	Declarative layer on top of the SQLAlchemy library
Summary(pl.UTF-8):	Warstwa nad biblioteką SQLAlchemy.
Name:		python-%{module}
Version:	0.7.1
Release:	1
License:	MIT
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/E/Elixir/Elixir-%{version}.tar.gz
# Source0-md5:	5615ec9693e3a8e44f69623d58f54116
URL:		http://elixir.ematia.de/trac/wiki
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
# if py_postclean is used
BuildRequires:	rpmbuild(macros) >= 1.219
#Requires:		python-libs
Requires:	python-SQLAlchemy
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A declarative layer on top of SQLAlchemy. It is a fairly thin wrapper,
which provides the ability to create simple Python classes that map
directly to relational database tables (this pattern is often referred
to as the Active Record design pattern), providing many of the
benefits of traditional databases without losing the convenience of
Python objects.

%description -l pl.UTF-8
Cienka dodatkowa warstwa ponad SQLAlchemy. Pozwala tworzyć proste
klasy Pythonowe bezpośrednio mapowane do tabel relacyjnej bazy danych
(często nazywane też wzorcem projektowym Active Record) dając wiele
z zalet tradycyjnych baz danych bez straty wygody obiektów
Pythonowych.

%prep
%setup -q -n Elixir-%{version}

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
## %doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
##%{py_sitedir}/*.py[co]
## %attr(755,root,root) %{py_sitedir}/*.so
%{py_sitescriptdir}/%{module}
##%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/Elixir-*.egg-info
##%endif
