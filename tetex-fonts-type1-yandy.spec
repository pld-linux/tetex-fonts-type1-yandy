# TODO:
# - review license...
# - use .pfb only (not .pfa) if possible
Summary:	TeX EC fonts, PostScript Type1 format
Summary(pl):	Fonty TeX EC w formacie PostScript Type1
%define		short_name	yandy
Name:		tetex-fonts-type1-%{short_name}
Version:	1
Release:	1
License:	non distributable
Group:		Fonts
Source0:	yandy-fonts.tar.bz2
NoSource:	0
Requires:	tetex
Requires:	tetex-dirs-fonts
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		texhash	[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;

%description
These are Type1 renderings of the EC variants of the standard CMR
family.

%description -l pl
Ten pakiet zawiera obrazy Type1 wariantów EC ze standardowej rodziny
CMR.

%prep
%setup -q -n %{short_name}-fonts

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/fonts/type1/%{short_name}

install *.pfa *.pfb $RPM_BUILD_ROOT%{_datadir}/texmf/fonts/type1/%{short_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2

%postun
[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2

%files
%defattr(644,root,root,755)
%doc *.txt
%dir %{_datadir}/texmf/fonts/type1/%{short_name}
%{_datadir}/texmf/fonts/type1/%{short_name}/*.pfa
%{_datadir}/texmf/fonts/type1/%{short_name}/*.pfb
