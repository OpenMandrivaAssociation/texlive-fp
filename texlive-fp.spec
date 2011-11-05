# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/fp
# catalog-date 2009-09-26 11:43:36 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-fp
Version:	20090926
Release:	1
Summary:	Fixed point arithmetic
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fp
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fp.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fp.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
An extensive collection of arithmetic operations for fixed
point real numbers of high precision.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fp/defpattern.sty
%{_texmfdistdir}/tex/latex/fp/fp-addons.sty
%{_texmfdistdir}/tex/latex/fp/fp-basic.sty
%{_texmfdistdir}/tex/latex/fp/fp-eqn.sty
%{_texmfdistdir}/tex/latex/fp/fp-eval.sty
%{_texmfdistdir}/tex/latex/fp/fp-exp.sty
%{_texmfdistdir}/tex/latex/fp/fp-pas.sty
%{_texmfdistdir}/tex/latex/fp/fp-random.sty
%{_texmfdistdir}/tex/latex/fp/fp-snap.sty
%{_texmfdistdir}/tex/latex/fp/fp-trigo.sty
%{_texmfdistdir}/tex/latex/fp/fp-upn.sty
%{_texmfdistdir}/tex/latex/fp/fp.sty
%{_texmfdistdir}/tex/latex/fp/lfp.sty
%{_texmfdistdir}/tex/plain/fp/fp.tex
%doc %{_texmfdistdir}/doc/latex/fp/README
%doc %{_texmfdistdir}/doc/latex/fp/fp.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
