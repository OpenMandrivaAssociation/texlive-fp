Name:		texlive-fp
Version:	49719
Release:	2
Summary:	Fixed point arithmetic
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fp
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fp.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fp.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
An extensive collection of arithmetic operations for fixed
point real numbers of high precision.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fp
%{_texmfdistdir}/tex/plain/fp
%doc %{_texmfdistdir}/doc/latex/fp

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
