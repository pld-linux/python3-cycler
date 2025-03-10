#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		cycler
Summary:	Composable style cycles
Summary(pl.UTF-8):	Komponowalne cykle styli
Name:		python-%{module}
# keep 0.10.x here for python2 support
Version:	0.10.0
Release:	9
License:	BSD
Group:		Libraries/Python
#Source0Download: https://github.com/matplotlib/cycler/releases
# FIXME: use
#Source0:	https://github.com/matplotlib/cycler/archive/v%{version}/%{module}-%{version}.tar.gz
Source0:	https://github.com/matplotlib/cycler/archive/v%{version}.tar.gz
# Source0-md5:	83dd0df7810e838b59e4dd9fa6e2d198
URL:		https://matplotlib.org/cycler/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-nose
BuildRequires:	python-six
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-nose
BuildRequires:	python3-six
%endif
%endif
%if %{with doc}
BuildRequires:	python-ipython
BuildRequires:	python-matplotlib
BuildRequires:	python-numpydoc
BuildRequires:	sphinx-pdg-2
%endif
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Composable style cycles.

%description -l pl.UTF-8.
Komponowalne cykle styli.

%package -n python3-%{module}
Summary:	Composable style cycles
Summary(pl.UTF-8):	Komponowalne cykle styli
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-%{module}
Composable style cycles.

%description -n python3-%{module} -l pl.UTF-8.
Komponowalne cykle styli.

%package apidocs
Summary:	%{module} API documentation
Summary(pl.UTF-8):	Dokumentacja API modułu %{module}
Group:		Documentation

%description apidocs
API documentation for %{module}.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu %{module}.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
nosetests-%{py_ver} test_cycler.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
nosetests-%{py3_ver} test_cycler.py
%endif
%endif

%if %{with doc}
%{__make} -C doc html \
	SPHINXBUILD=sphinx-build-2
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/cycler.py[co]
%{py_sitescriptdir}/cycler-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/cycler.py
%{py3_sitescriptdir}/__pycache__/cycler.cpython-*.py[co]
%{py3_sitescriptdir}/cycler-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/build/html/{_images,_modules,_static,generated,*.html,*.js,*.png}
%endif
