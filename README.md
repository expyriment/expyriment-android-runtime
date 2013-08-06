expyriment-android-runtime
==========================

Main repository of Expyriment Android Runtime


Building the Android app
------------------------

* Download PGS4A (version 0.94) from http://pygame.renpy.org/dl
* Copy all files in this repository into a folder called 'expyriment_app', inside the PGS4A folder
* Copy the (released!) Expyriment source code (the 'expyriment' folder) into the 'expyriment_app' folder
* Run
    ./android.py configure expyriment
* Run
    ./android.py build expyriment release
