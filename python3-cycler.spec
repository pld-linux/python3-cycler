#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

%define		module		cycler
Summary:	Composable style cycles
Summary(pl.UTF-8):	Komponowalne cykle styli
Name:		python3-%{module}
Version:	0.12.1
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://github.com/matplotlib/cycler/releases
Source0:	https://github.com/matplotlib/cycler/archive/v%{version}/%{module}-%{version}.tar.gz
# Source0-md5:	1f6077c5e7adf8824d50c3a01c8104f6
URL:		https://matplotlib.org/cycler/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	python3-setuptools >= 1:61
%if %{with tests}
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.045
%if %{with doc}
BuildRequires:	python3-ipython
BuildRequires:	python3-matplotlib
BuildRequires:	python3-numpydoc
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Composable style cycles.

%description -l pl.UTF-8.
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
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest test_cycler.py
%endif

%if %{with doc}
%{__make} -C doc html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst SECURITY.md
%{py3_sitescriptdir}/cycler
%{py3_sitescriptdir}/cycler-%{version}.dist-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/build/html/{_images,_modules,_static,generated,*.html,*.js,*.png}
%endif
