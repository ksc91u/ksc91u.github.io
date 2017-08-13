Title: AMD OSX86 Post Install
Date: 2017-08-13 22:10
Modified: 2017-08-13 22:10
Category: osx
Tags: osx, osx86, amd
Slug: amd-osx86
Authors: Me
Summary: AMD OSX86 post install issues and fix


I migrate from and Intel system, here are my steps.

1. Prepare usb disk with [TransMac](https://forum.amd-osx.com/viewtopic.php?f=24&t=1213)
2. Boot USB Disk, BIOS set to UEFI+Legacy mode.
3. Launch terminal from installer
 
 ```
 sh /Volumes/SierraAMD/PostInstall/post.sh
 ```
 The script will ask for your OSX volume, but volume name may not contains spaces. If your OSX volume name contains spaces, make soft link first
 
 ```
 cd /Volumes/
 ln -s OS\ X OSX
 ```
 
4. Reboot, first time boot with USB.
5. Install CLOVER
6. Make kernel caches

 ```
 sudo kextcache -system-prelinked-kernel
 sudo kextcache -system-caches
 ```
 Then you should be able to boot with clover

7. If you have monitor color blinking issue, install [ResXtream](http://resxtreme.com/) and set 8-bits color 
8. If your system clock runs too fast/slow, adjust [busratio](http://www.insanelymac.com/forum/topic/240542-guide-getting-your-busratio/) in clover boot arg 
9. I found there is a process assistantd keeps writing to my disk, stopping Siri does not help. Thus I disable the service directly
 
 ```
 sudo vim /System/Library/LaunchAgents/com.apple.assistantd.plist
 
 #change RunAtLoad to false and reboot
 ```

10. Other issue: playing video with VLC got crappy audio output. Use [mpv](https://mpv.io/) or [mplayer](http://brewformulas.org/Mplayer)
