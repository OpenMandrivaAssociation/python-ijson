%define module ijson
%bcond tests 1

Name:		python-ijson
Version:	3.5.1
Release:	1
Summary:	Iterative JSON parser with standard Python iterator interfaces
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://pypi.org/project/ijson/
Source0:	https://files.pythonhosted.org/packages/source/i/ijson/ijson-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildRequires:	pkgconfig(yajl)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
%endif

%description
Iterative JSON parser with standard Python iterator interfaces

%prep -a
# Remove bundled egg-info
rm -rf src/%{module}.egg-info

%build -p
export LDFLAGS="%{ldflags} -lpython%{py_ver}"

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitearch}:${PWD}"
pytest
%endif

%files
%doc README.rst
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}.dist-info
