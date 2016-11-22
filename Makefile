clean:
	find . -name '*.pyc' -delete
	find . -name __pycache__ -delete
	find . -name '*.pyo' -delete
	find . -name '*~' -delete

clean-build:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info

run:
	python flask_bcolz/app.py

test:
	py.test --cov-report html --cov flask_bcolz flask_bcolz/tests

isort:
	sh -c "isort --skip-glob=.tox --recursive . "
