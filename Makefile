.PHONY: build

all: build 

build: build/pgs4a-0.9.4.tar.bz2 build/expyriment
	@rm -rf build/pgs4a
	@tar xjf build/pgs4a-0.9.4.tar.bz2; mv pgs4a-0.9.4 build/pgs4a;
	@cp -ra expyriment_app build/pgs4a
	@cp -ra build/expyriment build/pgs4a/expyriment_app
	@cd build/pgs4a;\
		python android.py configure expyriment_app ;\
		python android.py build expyriment_app release;\

build/pgs4a-0.9.4.tar.bz2:
	@mkdir -p build
	wget -P build 'http://pygame.renpy.org/dl/pgs4a-0.9.4.tar.bz2'

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
