#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	AI
%define		pnam	NeuralNet-BackProp
Summary:	A simple back-prop neural net that uses Delta's and Hebbs' rule
Summary(pl):	Prosta sie� neuronowa ze wsteczn� propagacj� u�ywaj�ca zasady Delty i Hebbsa
Name:		perl-AI-NeuralNet-BackProp
Version:	0.89
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.zip
# Source0-md5:	1791f9f8f178ef67d2814fd8ff46fa11
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AI::NeuralNet::BackProp is a simply back-propagation, feed-foward
neural network designed to learn using a generalization of the Delta
rule and a bit of Hopefield theory.

%description -l pl
AI::NeuralNet::BackProp to prosta sie� neuronowa ze wsteczn�
propagacj� i przednim sprz�eniem zaprojektowana do nauki przy u�yciu
uog�lnienia zasady Delty i cz�ci teorii Hopefielda.

%prep
%setup -q -c

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes *.htm README
%{perl_vendorlib}/AI/NeuralNet/*.pm
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%{_examplesdir}/%{name}-%{version}/*.dat
%{_mandir}/man3/*
