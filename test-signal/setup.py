# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

__version__ = '0.1.1'


setup(
    name='test_signal',
    version=__version__,
    description='read data from modbus',
    author='Anusha',
    author_email='anusha.nss@gmail.com',
    include_package_data=True,
    url='git@gitlab.com:anusha_ahe/test_signal.git',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: AHE License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)

# Usage of setup.py:
# $> python setup.py register             # registering package on PYPI
# $> python setup.py build sdist upload   # build, make source dist and upload to PYPI
