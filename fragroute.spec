Summary:	Fragroute - intercept, modify, and rewrite egress traffic
Name:		fragroute
Version:	1.2
Release:	%mkrel 12
License:	BSD
# not sure about this one
Group:		System/Servers
URL:		http://monkey.org/~dugsong/fragroute/
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	dnet-devel
BuildRequires:	libpcap-devel
BuildRequires:	libevent-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
fragroute intercepts, modifies, and rewrites egress traffic,
implementing most of the attacks described in the Secure
Networks "Insertion, Evasion, and Denial of Service: Eluding
Network Intrusion Detection" paper. It features a simple ruleset
language to delay, duplicate, drop, fragment, overlap, print,
reorder, segment, source-route, or otherwise monkey with all
outbound packets destined for a target host, with minimal support
for randomized or probabilistic behaviour. This tool was written
in good faith to aid in the testing of intrusion detection
systems, firewalls, and basic TCP/IP stack behaviour. 

%prep

%setup -q

# lib64 fix
perl -pi -e "s|/lib\ |/%{_lib}\ |g" configure*
perl -pi -e "s|/lib/|/%{_lib}/|g" configure*

# anti recheck hack
touch * scripts/* win32/*

%build
#libtoolize --copy --force; aclocal-1.4; automake-1.4; autoconf-2.13
%serverbuild
export CFLAGS="%{optflags} -fPIC"
%configure 
%make

%install
rm -rf %{buildroot}

%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc INSTALL README TODO scripts
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_sbindir}/*
%{_mandir}/man8/*
