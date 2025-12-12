Name:		python-ijson
Version:	3.3.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/i/ijson/ijson-%{version}.tar.gz
Summary:	Iterative JSON parser with standard Python iterator interfaces
URL:		https://pypi.org/project/ijson/
License:	BSD
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	pkgconfig(yajl)
BuildRequires:	pkgconfig(python3)

%description
Iterative JSON parser with standard Python iterator interfaces

%prep
%autosetup -p1 -n ijson-%{version}

%build
%py_build

%install
%py_install

%files
%{python_sitearch}/ijson
%{python_sitearch}/ijson-*.*-info
