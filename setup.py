#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
try:
    import multiprocessing  # atexit exception
except:
    pass


def setup_python3():
    # Taken from "distribute" setup.py
    from distutils.filelist import FileList
    from distutils import dir_util, file_util, util, log
    from os.path import join

    tmp_src = join("build", "src")
    log.set_verbosity(1)
    fl = FileList()
    for line in open("MANIFEST.in"):
        if not line.strip():
            continue
        fl.process_template_line(line)
    dir_util.create_tree(tmp_src, fl.files)
    outfiles_2to3 = []
    for f in fl.files:
        outf, copied = file_util.copy_file(f, join(tmp_src, f), update=1)
        if copied and outf.endswith(".py"):
            outfiles_2to3.append(outf)

    util.run_2to3(outfiles_2to3)

    # arrange setup to use the copy
    sys.path.insert(0, tmp_src)

    return tmp_src

# Find version. We have to do this because we can't import it in Python 3 until
# its been automatically converted in the setup process.


def find_version(filename):
    _version_re = re.compile(r'__version__ = "(.*)"')
    for line in open(filename):
        version_match = _version_re.match(line)
        if version_match:
            return version_match.group(1)

__version__ = find_version('rdflib_mysql/__init__.py')

config = dict(
    name='rdflib-mysql',
    version=__version__,
    description="rdflib extension adding MySQL as back-end store",
    author="RDFLib Team",
    maintainer="Graham Higgins",
    maintainer_email="gjhiggins@gmail.com",
    url="http://github.com/RDFLib/rdflib-mysql",
    packages=["rdflib_mysql"],
    download_url="https://github.com/RDFLib/rdflib-mysql/zipball/master",
    license="BSD",
    platforms=["any"],
    long_description="""
    MySQL implementation of FOPL Relational Model as an RDFLib Store.

    The MySQL store's relational schema incorporates hashes of terms for
    efficient interning as well as other normalizations. Very little of
    it is written specifically for MySQL and thus theoretically it can
    be very easily ported to other back-ends (with the possible exception
    of issues with its use of foreign keys).
    """,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: BSD License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        ],
    test_suite="test",
    install_requires=[
            "rdflib>=3.0",
            "rdfextras>=0.1",
            "MySQL-python>=1.2.3"
            ],
    entry_points={
        'rdf.plugins.store': [
            'MySQL = rdflib_mysql.MySQL:MySQL',
        ],
    }
)

if sys.version_info[0] >= 3:
    from setuptools import setup
    config.update({'use_2to3': True})
    config.update({'src_root': setup_python3()})
else:
    try:
        from setuptools import setup
        config.update({'test_suite': "nose.collector"})
    except ImportError:
        from distutils.core import setup


setup(**config)
