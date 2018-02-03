# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='translate_api',
    version='0.1',
    author='Nil Portugués Calderó',
    author_email='contact@nilportugues.com',
    url='http://nilportugues.com/',
    license='BSD',
    packages=find_packages(exclude=('tests', 'docs', 'venv')),
    install_requires=[
        'googletrans==2.1.3',
        'virtualenv',
        'flask-restplus==0.9.2',
        'flask-restful-swagger-2==0.35',
        'Flask-SQLAlchemy==2.1',
    ],
    include_package_data=True, 
)

# EOF
