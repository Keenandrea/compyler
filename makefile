
PY=python2.7
ZIP=PY1.zip
MAIN=main
DIR=$(PWD)
.SUFFIXES: .py
FILES = \
	main.py
All:
	echo " $(PY) $(DIR)/$(FILES) " \"'$$1'\" > main
	chmod 777 main
