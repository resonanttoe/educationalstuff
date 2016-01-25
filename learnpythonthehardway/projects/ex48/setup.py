try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'First project',
	'author': 'Pauldev',
	'url': 'https://www.github.com/resonanttoe/',
	'author_email': 'Empty',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'first'
}

setup(**config)