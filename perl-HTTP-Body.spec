#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTTP
%define	pnam	Body
Summary:	HTTP::Body - HTTP Body Parser
Summary(pl.UTF-8):	HTTP::Body - parser ciała odpowiedzi HTTP
Name:		perl-HTTP-Body
Version:	1.22
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	81a38eab683d8750b78ad0d4845ef0d5
URL:		http://search.cpan.org/dist/HTTP-Body/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Path-Class
BuildRequires:	perl-Test-Deep
BuildRequires:	perl-YAML >= 0.39
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTTP Body Parser.

%description -l pl.UTF-8
Parser ciała odpowiedzi HTTP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/HTTP/*.pm
%{perl_vendorlib}/HTTP/Body
%{_mandir}/man3/*
