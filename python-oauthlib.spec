# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-oauthlib
Epoch: 100
Version: 3.2.2
Release: 1%{?dist}
BuildArch: noarch
Summary: Generic implementation of the OAuth request-signing logic
License: BSD-3-Clause
URL: https://github.com/oauthlib/oauthlib/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
OAuthLib is a generic utility which implements the logic of OAuth
without assuming a specific HTTP request object. It can be used to graft
OAuth support onto HTTP libraries.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-oauthlib
Summary: Generic implementation of the OAuth request-signing logic
Requires: python3
Requires: python3-blinker >= 1.4.0
Requires: python3-cryptography >= 3.0.0
Requires: python3-jwt >= 2.0.0
Provides: python3-oauthlib = %{epoch}:%{version}-%{release}
Provides: python3dist(oauthlib) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-oauthlib = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(oauthlib) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-oauthlib = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(oauthlib) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-oauthlib
OAuthLib is a generic utility which implements the logic of OAuth
without assuming a specific HTTP request object. It can be used to graft
OAuth support onto HTTP libraries.

%files -n python%{python3_version_nodots}-oauthlib
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-oauthlib
Summary: Generic implementation of the OAuth request-signing logic
Requires: python3
Requires: python3-blinker >= 1.4.0
Requires: python3-cryptography >= 3.0.0
Requires: python3-jwt >= 2.0.0
Provides: python3-oauthlib = %{epoch}:%{version}-%{release}
Provides: python3dist(oauthlib) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-oauthlib = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(oauthlib) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-oauthlib = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(oauthlib) = %{epoch}:%{version}-%{release}

%description -n python3-oauthlib
OAuthLib is a generic utility which implements the logic of OAuth
without assuming a specific HTTP request object. It can be used to graft
OAuth support onto HTTP libraries.

%files -n python3-oauthlib
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
