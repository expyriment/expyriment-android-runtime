Expyriment Android Runtime (EAR)
================================

The **Expyriment Android Runtime** (EAR) is a convinient way to run experiments created with [*Expyriment*] (http://www.expyriment.org) on an Android device. *Expyriment* is an open-source and platform-independent lightweight Python library for designing and conducting behavioral experiments: https://github.com/expyriment/expyriment


*GNU General Public License v3*

Florian Krause (florian@expyriment.org) & Oliver Lindemann (oliver@expyriment.org)



Installation
------------
The easiest way is to install EAR on you Android device is to download and install the latest release of our [Android application package] (https://github.com/expyriment/expyriment-android-runtime/releases).

You can build EAR yourself as describe below:

1. Installed the JAVA JDK: http://www.oracle.com/technetwork/java/javase/downloads/index.html
2. Download PGS4A (version 0.94) from http://pygame.renpy.org/dl
3. Run `./android.py installsdk`
4. Copy the folder 'expyriment_app' inside the PGS4A folder
5. Download the latest Expyriment release (zip file) from http://www.expyriment.org/getit
6. Extract only the 'expyriment' subfolder into the 'expyriment_app' folder
7. Run `./android.py configure expyriment_app`
8. Run `./android-sdk/tools/android` and install the API vesion 8 (Android 2.2) (you might need to install any pending updates first)
9. Run `./android.py build expyriment_app release`
* The resulting apk file will be available in the bin/ directory

Alternative, you can use the makefile: `make configure` (step 2 to 8) and `make build` (step 9). 


Usage
-----
Once installed, the application will look for Expyriment scripts (each in its own subdirectory) in a directory called ‘expyriment’, located at the root level of either storage device under ‘mnt’ (i.e. the internal or external SD card). Examples of correctly located Expyriment scripts include:
```
/mnt/sdcard0/expyriment/exp1/exp1.py

/mnt/sdcard0/expyriment/exp2/exp2.py

/mnt/extSdCard/expyriment/exp3/exp3.py

/mnt/extSdCard/expyriment/exp4/exp4.py
```
