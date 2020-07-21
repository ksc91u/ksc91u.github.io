Title: Turbo Boost Switcher, Free
Date: 2020-07-21 15:10
Modified: 2020-07-21 15:10
Category: osx
Tags: osx, turboboost
Slug: tb-free
Authors: Me
Summary: disable turbo boost on os x, free


# Turbo Boost Switcher

### Download from [GitHub](https://github.com/rugarciap/Turbo-Boost-Switcher) 


* Installed to /Application

```
user@localhost ~ $ ls -l /Applications/Turbo\ Boost\ Switcher.app/Contents/MacOS/Turbo\ Boost\ Switcher
-rwxr-xr-x@ 1 user  staff  141312 11 23  2019 /Applications/Turbo Boost Switcher.app/Contents/MacOS/Turbo Boost Switcher
```

* Create launch script at ```/Users/user/bin/turbo.sh```

```
#!/bin/bash
nohup "/Applications/Turbo Boost Switcher.app/Contents/MacOS/Turbo Boost Switcher" 1>/dev/null 2>/dev/null &

```

* Enable sudo without password for script ```sudo visudo```

```
user       ALL = (ALL) NOPASSWD:/Users/user/bin/turbo.sh

```

* Use Automator.app to create launch app to run script when login

	* Search for Run Shell Script from library
	
	```
	/usr/bin/sudo /Users/user/bin/turbo.sh
	```

	* Save app to ```~/bin/turbo_disable.app```

	* Add app to user Login Items

	* When Turbo Boost Switcher launch, check **Disable TB at Launch** from menu. Done

