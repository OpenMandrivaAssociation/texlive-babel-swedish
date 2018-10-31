# revision 30296
# category Package
# catalog-ctan /macros/latex/contrib/babel-contrib/swedish
# catalog-date 2013-05-06 23:49:45 +0200
# catalog-license lppl1.3
# catalog-version 2.3d
Name:		texlive-babel-swedish
Version:	2.3d
Release:	10
Summary:	Babel support for typesetting Swedish
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/swedish
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-swedish.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-swedish.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-swedish.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the language definition file for Swedish.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-swedish/swedish.ldf
%doc %{_texmfdistdir}/doc/generic/babel-swedish/swedish.pdf
#- source
%doc %{_texmfdistdir}/source/generic/babel-swedish/swedish.dtx
%doc %{_texmfdistdir}/source/generic/babel-swedish/swedish.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
