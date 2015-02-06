%define name	ocaml-bitstring
%define version	2.0.2
%define release	2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Bitstrings and bitstring matching for OCaml
License:	LGPLv2+ with exceptions and GPLv2+
Group:		Development/Other
URL:		http://code.google.com/p/bitstring
Source:	    http://bitstring.googlecode.com/files/%{name}-%{version}.tar.gz	
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


%changelog
* Mon Jan 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.2-1mdv2010.1
+ Revision: 496354
- new version

  + Florent Monnier <blue_prawn@mandriva.org>
    - rebuild
    - fixed license

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.0-5mdv2010.0
+ Revision: 389903
- rebuild

* Mon Dec 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.0-4mdv2009.1
+ Revision: 321224
- install at standard ocaml library root
- install binary

* Mon Dec 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.0-3mdv2009.1
+ Revision: 317604
- Fixes from Florent Monnier fmonnier@linux-nantes.org>:
- move non-devel files in main package
- fix build with latest ocaml

  + Pixel <pixel@mandriva.com>
    - rebuild

* Mon Nov 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.0-1mdv2009.1
+ Revision: 299452
- update to new version 2.0.0

* Tue Sep 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.9.8-1mdv2009.0
+ Revision: 279045
- new version

* Thu Aug 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.9.7-1mdv2009.0
+ Revision: 271756
- import ocaml-bitstring


* Thu Aug 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.9.7-1mdv2009.0
- first mdv release 
