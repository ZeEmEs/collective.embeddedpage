# -*- coding: utf-8 -*-
"""Installer for the collective.embeddedpage package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='collective.embeddedpage',
    version='2.2.2.dev0',
    description="Add-on to embed remote HTML pages into the Plone CMS",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Framework :: Plone :: 5.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone',
    author='kitconcept GmbH',
    author_email='info@kitconcept.com',
    url='https://pypi.python.org/pypi/collective.embeddedpage',
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['collective'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'chardet',
        'lxml',
        'plone.api',
        'plone.app.contenttypes',
        'plone.app.dexterity',
        'plone.app.lockingbehavior',
        'plone.app.relationfield',
        'plone.app.versioningbehavior',
        'plone.restapi',
        'Products.GenericSetup>=1.8.2',
        'requests',
        'setuptools',
        'z3c.jbot',
    ],
    extras_require={
        'test': [
            'cssselect',
            'httmock',
            'plone.app.testing',
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            'plone.testing',
            'plone.app.contenttypes',
            'plone.app.robotframework[debug]',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
