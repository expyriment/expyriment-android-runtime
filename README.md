Expyriment Android Runtime
==========================

*GNU General Public License v3*

Florian Krause (florian@expyriment.org) & Oliver Lindemann (oliver@expyriment.org)

About
-----
The Expyriment Android Runtime is a convinient way to run experiments created with [Expyriment] (http://www.expyriment.org) on an Android device.


Installation
------------
The easiest way is to install the Expyriment Android Runtime on you Android device is to download and install the latest release of our [Android application package] (https://github.com/expyriment/expyriment-android-runtime/releases).

Altenatively, you can build the Expyriment Android Runtime yourself as describe below:
  1) Installed the JAVA JDK: http://www.oracle.com/technetwork/java/javase/downloads/index.html
  2) Download PGS4A (version 0.94) from http://pygame.renpy.org/dl
  3) Run `./android.py installsdk`
4) Run `./android-sdk/tools/android` and install the API vesion 8 (Android 2.2) (you might need to install any pending updates first)
5) Copy the folder 'expyriment_app' inside the PGS4A folder
6) Download the latest Expyriment release (zip file) from http://www.expyriment.org/getit
7) Extract only the 'expyriment' subfolder into the 'expyriment_app' folder
8) Run `./android.py configure expyriment_app`
9) Run `./android.py build expyriment_app release`
* The resulting apk file will be available in the bin/ directory

Usage
-----
Once installed, the application will look for Expyriment scripts (each in its own subdirectory) in a directory called ‘expyriment’, located at the root level of either storage device under ‘mnt’ (i.e. the internal or external SD card). Examples of correctly located Expyriment scripts include:
```
/mnt/sdcard0/expyriment/exp1/exp1.py

/mnt/sdcard0/expyriment/exp2/exp2.py

/mnt/extSdCard/expyriment/exp3/exp3.py

/mnt/extSdCard/expyriment/exp4/exp4.py
```

Note 
----
**Expyriment** is an open-source and platform-independent lightweight Python
library for designing and conducting behavioral experiments: http://www.expyriment.org, https://github.com/expyriment/expyriment
