#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Manifest
Summary:	Test::Manifest - interact with a t/test_manifest file
Summary(pl):	Test::Manifest - wspó³praca z plikiem t/test_manifest
Name:		perl-Test-Manifest
Version:	0.93
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a46b6185410c2fd8b1a2efd6fea94d9e
BuildRequires:	perl-devel >= 5.6
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

%description -l pl
MakeMaker zak³ada, ¿e chcemy podczas make test uruchamiaæ wszystkie
pliki .t z katalogu t/ w kolejno¶ci asciibetycznej, o ile nie podamy
innej kolejno¶ci. To prowadzi do interesuj±cych schematów nazywania
plików z testami, aby by³y wykonywane we w³a¶ciwej kolejno¶ci.

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
