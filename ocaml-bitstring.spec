%define name	ocaml-bitstring
%define version	1.9.7
%define release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Bitstrings and bitstring matching for OCaml
License:	LGPL
Group:		Development/Other
URL:		http://code.google.com/p/bitstring
Source:	    http://bitstring.googlecode.com/files/%{name}-%{version}.tar.gz	
Patch:      %{name}-1.9.7-install-flags.patch
BuildRequires:	ocaml
BuildRequires:	camlp4
BuildRequires:  findlib
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The ocaml-bitstring project adds Erlang-style bitstrings and matching over
bitstrings as a syntax extension and library for OCaml.

%package	devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the development files needed to build applications
using %{name}.

%prep
%setup -q
%patch -p 1

%build
%configure2_5x
make 

%install
rm -rf %{buildroot}
#%makeinstall_std
install -d -m 755 %{buildroot}/%{ocaml_sitelib}
make install OCAMLFIND_INSTFLAGS="-destdir %{buildroot}/%{ocaml_sitelib}"

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README TODO COPYING COPYING.LIB CHANGES
%dir %{ocaml_sitelib}/bitstring
%{ocaml_sitelib}/bitstring/*.cmi

%files devel
%defattr(-,root,root)
%{ocaml_sitelib}/bitstring/*
%exclude %{ocaml_sitelib}/bitstring/*.cmi

