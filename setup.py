#!/usr/bin/env python
import os
from django_dropbox import version
from setuptools import setup

def get_packages():
    # setuptools can't do the job :(
    packages = []
    for root, dirnames, filenames in os.walk('django_dropbox'):
        if '__init__.py' in filenames:
            packages.append(".".join(os.path.split(root)).strip("."))

    return packages

requires = [r for r in open('requirements.txt').read().split('\n') if r]

setup(name='django-dropbox',
    version=version,
    description='A Django App that contains a Django Storage which uses Dropbox.',
    author=u'Andres Torres Marroquin',
    author_email='andres.torres.marroquin@gmail.com',
    url='https://github.com/andres-torres-marroquin/django-dropbox',
    packages=get_packages(),
    install_requires=requires,
)
