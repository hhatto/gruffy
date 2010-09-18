all: test

.PHONY: test
test:
	python test/test_base.py
	python test/test_area.py
	python test/test_bar.py
	python test/test_dot.py
	python test/test_side_bar.py
	python test/test_line.py
	rm graph.png

pypireg:
	python setup.py register
	python setup.py sdist upload

clean:
	rm -f gruffy/*.pyc
	rm -f *.png
	rm -rf build dist
