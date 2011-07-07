%define		theme	supermario
Summary:	Pidgin Sounds - Super Mario
Name:		libpurple-theme-%{theme}
Version:	1.0
Release:	1
License:	?
Group:		Applications/Publishing
Source0:	http://www.deviantart.com/download/145302959/Pidgin_Sound___Super_Mario_by_kidnoize.zip
# Source0-md5:	4d1bb4819711598a03c1731d664a60e5
URL:		http://kidnoize.deviantart.com/art/Pidgin-Sound-Super-Mario-145302959
BuildRequires:	unzip
Requires:	libpurple
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/themes/%{theme}

%description
I've developed Carbon theme for personal needs for Gallery 2. It is
based on Matrix theme. The theme works well in Firefox and IE6.

%prep
%setup -q -n Super\ Mario\ World

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a . $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
