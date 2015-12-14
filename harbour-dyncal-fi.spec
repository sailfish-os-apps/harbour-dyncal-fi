Name:          harbour-dyncal-fi
Version:       0.1.0
Release:       1
Summary:       DynCal Finland
Group:         System/Tools
Vendor:        fravaccaro
Distribution:  SailfishOS
Requires: harbour-dyncal >= 0.3.0-1
Packager: fravaccaro <fravaccaro@jollacommunity.it>
URL:           www.jollacommunity.it
License:       GPL

%description
Change Calendar icon accordingly with the day. It features Finland holidays.

%files
%defattr(-,root,root,-)
/usr/share/*

%post
mkdir /usr/share/harbour-dyncal-fi/backup
chmod +x /usr/share/harbour-dyncal-fi/*.sh
/usr/share/harbour-dyncal-fi/run.sh

%preun
/usr/share/harbour-dyncal-fi/restore.sh

%postun
if [ $1 = 0 ]; then
    // Do stuff specific to uninstalls
rm -rf /usr/share/harbour-dyncal-fi
else
if [ $1 = 1 ]; then
    // Do stuff specific to upgrades
echo "Upgrading"
/usr/share/harbour-dyncal/harbour-dyncal.sh
fi
fi

%changelog
* Mon Dec 14 2015 0.2
- Backup handling improved.

* Tue Dec 8 2015 0.1
- First build.
