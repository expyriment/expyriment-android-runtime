.PHONY: build

all: build 

build: build/pgs4a build/expyriment
	@mkdir -p build/pgs4a/expyriment_app
	@cp -a *.py build/pgs4a/expyriment_app
	@cp -a android-icon.png build/pgs4a/expyriment_app
	@cp build/expyriment build/pgs4a -ra
	@cd build/pgs4a;\
	python android.py configure expyriment_app ;\
	python android.py build expyriment_app release;\

build/pgs4a:
	@mkdir -p build
	wget -P build 'http://pygame.renpy.org/dl/pgs4a-0.9.4.tar.bz2'
	@cd build; tar xjf pgs4a-0.9.4.tar.bz2; rm pgs4a-0.9.4.tar.bz2; \
		mv pgs4a-0.9.4 pgs4a;
	@cp *.py build/pgs4a

build/expyriment:
	@DIR=build;\
	mkdir -p $$DIR;\
	wget -P $$DIR https://raw.github.com/expyriment/expyriment/master/CHANGES.md;\
	VER=`awk 'BEGIN{FS=" "}{ if ($$1 ~ /Version/){ print $$2;exit}}' $$DIR/CHANGES.md`;\
	wget -P $$DIR https://github.com/expyriment/expyriment/releases/download/v$$VER/expyriment-$$VER.zip;\
	cd $$DIR;\
	unzip expyriment-$$VER.zip;\
	mv expyriment-$$VER/expyriment expyriment;\
	rm expyriment-$$VER.zip expyriment-$$VER -rf;\

clean:
	rm -rf build
