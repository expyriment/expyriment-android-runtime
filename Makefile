PGS4A=pgs4a-0.9.4

.PHONY: build configure

build: 
	@cd build/$(PGS4A);\
		python android.py build expyriment_app release;\

configure: build/$(PGS4A).tar.bz2 build/expyriment
	@rm -rf build/$(PGS4A)
	@tar xjf build/$(PGS4A).tar.bz2; mv $(PGS4A) build/$(PGS4A);
	@cp -ra expyriment_app build/$(PGS4A)
	@cp -ra build/expyriment build/$(PGS4A)/expyriment_app
	@cd build/$(PGS4A);\
		python ./android.py installsdk;\
		python android.py configure expyriment_app ;\
		./android-sdk/tools/android

build/pgs4a-%.tar.bz2:
	@mkdir -p build
	wget -P build 'http://pygame.renpy.org/dl/pgs4a-$*.tar.bz2'

build/expyriment:
	@mkdir -p build
	wget -P build https://raw.github.com/expyriment/expyriment/master/CHANGES.md;
	@VER=`awk 'BEGIN{FS=" "}{ if ($$1 ~ /Version/){ print $$2;exit}}' build/CHANGES.md`;\
		wget -P build https://github.com/expyriment/expyriment/releases/download/v$$VER/expyriment-$$VER.zip;\
		cd build;\
		unzip expyriment-$$VER.zip;\
		mv expyriment-$$VER/expyriment expyriment;\
		rm expyriment-$$VER -rf;\

clean:
	rm -rf build
