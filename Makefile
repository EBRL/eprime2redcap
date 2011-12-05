rebuild: clean uninstall install

test:

	nosetests;

clean:

	find . -type f -name "*.pyc" -exec rm -v {} \;

install:

	python setup.py install

uninstall:

	python setup.py develop -u
	
