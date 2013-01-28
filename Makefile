all: test

.PHONY: test
test:
	cd test && python test_accumulator_bar.py
	cd test && python test_area.py
	cd test && python test_bar.py
	cd test && python test_base.py
	cd test && python test_bezier.py
	cd test && python test_dot.py
	cd test && python test_line.py
	cd test && python test_pie.py
	cd test && python test_sidebar.py
	cd test && python test_stacked_area.py
	cd test && python test_stacked_bar.py
	cd test && python test_stacked_sidebar.py

checkcode:
	clonedigger --cpd-output gruffy/*.py
	pylint --max-module-lines=1500 -f parseable gruffy/*.py | tee pylint.out

pypireg:
	python setup.py register
	python setup.py sdist bdist_egg upload

builddocs:
	cd docs/en && make html
	cd docs/ja && make html
	tar czf gruffy-docs.tar.gz docs/en/_build/html docs/ja/_build/html

coverage:
	coverage run --append test/test_accumulator_bar.py
	coverage run --append test/test_area.py
	coverage run --append test/test_bar.py
	coverage run --append test/test_base.py
	coverage run --append test/test_bezier.py
	coverage run --append test/test_dot.py
	coverage run --append test/test_line.py
	coverage run --append test/test_pie.py
	coverage run --append test/test_sidebar.py
	coverage run --append test/test_stacked_area.py
	coverage run --append test/test_stacked_bar.py
	coverage run --append test/test_stacked_sidebar.py
	coverage combine
	coverage report --omit="*pgmagick*,test*"
	coverage html
	coverage xml
	@rm .coverage

clean: cleandocs cleansrc

cleandocs:
	cd docs/en && make clean
	cd docs/ja && make clean

cleansrc:
	rm -f coverage.xml output.xml pylint.out
	rm -f gruffy/*.pyc test/*.pyc
	rm -f *.png test/*.png example/*.png
	rm -rf build dist gruffy.egg-info temp htmlcov
	cd test && rm -f gruffy_*.png && cd -
