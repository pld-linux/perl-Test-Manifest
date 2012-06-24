#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Manifest
Summary:	Test::Manifest - interact with a t/test_manifest file
Summary(pl):	Test::Manifest - wsp�praca z plikiem t/test_manifest
Name:		perl-Test-Manifest
Version:	0.91
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MakeMaker assumes that you want to run all of the .t files in the t/
directory in ascii-betical order during make test unless you say
otherwise.  This leads to some interesting naming schemes for test files
to get them in the desired order.

%description -l pl
MakeMaker zak�ada, �e chcemy podczas make test uruchamia� wszystkie
pliki .t z katalogu t/ w kolejno�ci asciibetycznej, o ile nie podamy
innej kolejno�ci. To prowadzi do interesuj�cych schemat�w nazywania
plik�w z testami, aby by�y wykonywane we w�a�ciwej kolejno�ci.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/Test/*.pm
%{_mandir}/man3/*
