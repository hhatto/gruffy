all: test

.PHONY: test
test:
	cd test && python test_area.py
	cd test && python test_bar.py
	cd test && python test_base.py
	cd test && python test_dot.py
	cd test && python test_line.py
	cd test && python test_pie.py
	cd test && python test_side_bar.py

pypireg:
	python setup.py register
	python setup.py sdist upload

clean:
	rm -f gruffy/*.pyc
	rm -f *.png
	rm -rf build dist gruffy.egg-info temp
	cd test && rm -f gruffy_*.png && cd -
