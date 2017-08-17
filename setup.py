"""Setup script

For details: https://packaging.python.org/en/latest/distributing.html
"""
import os
import setuptools


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'readme.rst'), encoding='utf-8') as fd:
    long_description = fd.read()


setuptools.setup(
    name='r5',
    version='0.5.0',

    description='Re-run, Repeat, Reproduce, Reuse, Replicate',
    long_description=long_description,

    url='https://github.com/benureau/r5',

    author='Fabien C. Y. Benureau and Nicolas P. Rougier',
    author_email='fabien.benureau@gmail.com',

    license='BSD',

    keywords='replicable reproducible research',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',

        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Testing'


        'License :: OSI Approved :: BSD License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    # where is our code
    packages=['r5', 'r5.tests'],

    # required dependencies
    install_requires=['gitpython'],

    # you can install extras_require with
    # $ pip install -e .[test]
    extras_require={'test': ['pytest', 'pytest-cov']},
)
