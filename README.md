Expyriment Android Runtime
==========================

*GNU General Public License v3*

Florian Krause (florian@expyriment.org) & Oliver Lindemann (oliver@expyriment.org)

Installation
------------

The easiest way is to install the Expyriment Android Runtime on you Android device is to download and istall [the latest release of our APK] (https://github.com/expyriment/expyriment-android-runtime/releases/latest).

Altenatively, you can build the Expyriment Android Runtime yourself as describe below:
* Installed the JAVA JDK: http://www.oracle.com/technetwork/java/javase/downloads/index.html
* Download PGS4A (version 0.94) from http://pygame.renpy.org/dl
* Run `./android.py installsdk`
* Run `./android-sdk/tools/android` and install the API vesion 8 (Android 2.2) (you need to install the updates first)
* Copy the folder 'expyriment_app' inside the PGS4A folder
* Download the latest Expyriment release (zip file) from http://www.expyriment.org/getit
* Extract only the 'expyriment' subfolder into the 'expyriment_app' folder
* Run `./android.py configure expyriment_app`
* Run `./android.py build expyriment_app release`

Note 
----
**Expyriment** is an open-source and platform-independent lightweight Python
library for designing and conducting behavioral experiments: http://www.expyriment.org, https://github.com/expyriment/expyriment
