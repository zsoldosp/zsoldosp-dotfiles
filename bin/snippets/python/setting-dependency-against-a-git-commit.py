# in setup.py

from setuptools import setup

setup(
    ...,
    install_requires = [ 'django-offline-messages == 0.3.1-imadeitup' ],
    dependency_links = [ 
        'https://github.com/dym/django-offline-messages/zipball/e22735cbdedbe3b32520d76790c05497bc0d1a07#egg=django-offline-messages-0.3.1-imadeitup',
    ]
)
