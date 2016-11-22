from pathlib import Path

from setuptools import setup

requirements_path = str(Path().resolve() / 'requirements.txt')
with open(requirements_path) as f:
    requirements = f.read().splitlines()

setup(
    name='flask_bcolz',
    install_requires=requirements, )
