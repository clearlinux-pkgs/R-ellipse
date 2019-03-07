#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ellipse
Version  : 0.4.1
Release  : 12
URL      : https://cran.r-project.org/src/contrib/ellipse_0.4.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ellipse_0.4.1.tar.gz
Summary  : Functions for Drawing Ellipses and Ellipse-Like Confidence
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : clr-R-helpers

%description
ellipses and ellipse-like confidence regions, implementing the plots
    described in Murdoch and Chow (1996), A graphical display of large
    correlation matrices, The American Statistician 50, 178-180. There are
    also routines implementing the profile plots described in Bates and
    Watts (1988), Nonlinear Regression Analysis and its Applications.

%prep
%setup -q -c -n ellipse

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521205960

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521205960
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ellipse
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ellipse
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ellipse
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library ellipse|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ellipse/DESCRIPTION
/usr/lib64/R/library/ellipse/INDEX
/usr/lib64/R/library/ellipse/Meta/Rd.rds
/usr/lib64/R/library/ellipse/Meta/features.rds
/usr/lib64/R/library/ellipse/Meta/hsearch.rds
/usr/lib64/R/library/ellipse/Meta/links.rds
/usr/lib64/R/library/ellipse/Meta/nsInfo.rds
/usr/lib64/R/library/ellipse/Meta/package.rds
/usr/lib64/R/library/ellipse/NAMESPACE
/usr/lib64/R/library/ellipse/R/ellipse
/usr/lib64/R/library/ellipse/R/ellipse.rdb
/usr/lib64/R/library/ellipse/R/ellipse.rdx
/usr/lib64/R/library/ellipse/help/AnIndex
/usr/lib64/R/library/ellipse/help/aliases.rds
/usr/lib64/R/library/ellipse/help/ellipse.rdb
/usr/lib64/R/library/ellipse/help/ellipse.rdx
/usr/lib64/R/library/ellipse/help/paths.rds
/usr/lib64/R/library/ellipse/html/00Index.html
/usr/lib64/R/library/ellipse/html/R.css
