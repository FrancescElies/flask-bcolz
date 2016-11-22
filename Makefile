run:
	python flask_bcolz/app.py

test:
	py.test --cov-report html --cov flask_bcolz flask_bcolz/tests

isort:
	sh -c "isort --skip-glob=.tox --recursive . "
