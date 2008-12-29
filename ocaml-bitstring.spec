%define name	ocaml-bitstring
%define version	2.0.0
%define release	%mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Bitstrings and bitstring matching for OCaml
License:	LGPL
Group:		Development/Other
URL:		http://code.google.com/p/bitstring
Source:	    http://bitstring.googlecode.com/files/%{name}-%{version}.tar.gz	
Patch:      ocaml-bitstring-2.0.0-dynlink.patch
BuildRequires:	ocaml
BuildRequires:	camlp4
BuildRequires:  ocaml-findlib
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
make doc

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{_libdir}/ocaml/stublibs
make install OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml

install -d -m 755 %{buildroot}/%{_bindir}
install -m 755 bitstring-objinfo %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README TODO COPYING COPYING.LIB CHANGES
%dir %{_libdir}/ocaml/bitstring
%{_libdir}/ocaml/bitstring/*.cmi
%{_libdir}/ocaml/bitstring/*.cma
%{_libdir}/ocaml/bitstring/META
%{_libdir}/ocaml/stublibs/*.so
%{_libdir}/ocaml/stublibs/*.so.owner

%files devel
%defattr(-,root,root)
%{_bindir}/bitstring-objinfo
%{_libdir}/ocaml/bitstring/*.a
%{_libdir}/ocaml/bitstring/*.cmx
%{_libdir}/ocaml/bitstring/*.cmxa
%{_libdir}/ocaml/bitstring/*.cmo
%{_libdir}/ocaml/bitstring/*.mli
