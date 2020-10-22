# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in company_wise_naming_series/__init__.py
from company_wise_naming_series import __version__ as version

setup(
	name='company_wise_naming_series',
	version=version,
	description='define in Company doctype naming series for each doctype  which needs to be fetched in (e.g.  SO, SI, DN,SE,JE ) and set on  new / on selection of company',
	author='GreyCube Technologies',
	author_email='admin@greycube.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
