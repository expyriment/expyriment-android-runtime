Expyriment Runtime for Android (ERA)
==========================

**Expyriment** Runtime for Android

*GNU General Public License v3*

Florian Krause (florian@expyriment.org) & Oliver Lindemann (oliver@expyriment.org)

Building the Android app
------------------------

Please, ensure that you have installed the Android JDK: http://www.oracle.com/technetwork/java/javase/downloads/index.html

You can build ERA by using the Makefie (`make configure build`) or manually as describe below:
* Download PGS4A (version 0.94) from http://pygame.renpy.org/dl
* Run `./android.py installsdk`
* Copy the folder 'expyriment_app' inside the PGS4A folder
* Download the latest Expyriment release (zip file) from http://www.expyriment.org/getit
* Extract only the 'expyriment' subfolder into the 'expyriment_app' folder
* Run `./android.py configure expyriment_app`
* Run `./android.py build expyriment_app release`

Note 
----
**Expyriment** is an open-source and platform-independent lightweight Python
library for designing and conducting behavioral experiments: http://www.expyriment.org, https://github.com/expyriment/expyriment
