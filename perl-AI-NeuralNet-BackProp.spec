%include	/usr/lib/rpm/macros.perl
%define	pdir	AI
%define	pnam	NeuralNet-BackProp
Summary:	A simple back-prop neural net that uses Delta's and Hebbs' rule.
Name:		perl-%{pdir}-%{pnam}
Version:	0.89
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.zip
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AI::NeuralNet::BackProp is a simply back-propagation, feed-foward neural
network designed to learn using a generalization of the Delta rule and
a bit of Hopefield theory.

# %description -l pl
# TODO

%prep
%setup -q -n %{name}-%{version} -c

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/AI/NeuralNet/*.pm
%doc Changes *.htm README
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%{_examplesdir}/%{name}-%{version}/*.dat
%{_mandir}/man3/*
