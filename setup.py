try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'MMSA-AE',
    'author': '2015087d',
    'url': '.',
    'download_url': 'Where to download it.',
    'author_email': '2015087d@student.gla.ac.uk.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['mmsa-ae'],
    'scripts': [],
    'name': 'mmsa-ae'
}

setup(**config)
