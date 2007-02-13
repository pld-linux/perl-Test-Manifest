#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Manifest
Summary:	Test::Manifest - interact with a t/test_manifest file
Summary(pl.UTF-8):	Test::Manifest - współpraca z plikiem t/test_manifest
Name:		perl-Test-Manifest
Version:	1.14
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4b0a8c9789b65647024e62cd1ee1fb8f
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MakeMaker assumes that you want to run all of the .t files in the t/
directory in ascii-betical order during make test unless you say
otherwise.  This leads to some interesting naming schemes for test files
to get them in the desired order.

%description -l pl.UTF-8
MakeMaker zakłada, że chcemy podczas make test uruchamiać wszystkie
pliki .t z katalogu t/ w kolejności asciibetycznej, o ile nie podamy
innej kolejności. To prowadzi do interesujących schematów nazywania
plików z testami, aby były wykonywane we właściwej kolejności.

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
%{perl_vendorlib}/Test/*.pm
%{_mandir}/man3/*
