from setuptools import setup

setup(
    name = 'rdflib-mysql',
    version = '0.1',
    description = "rdflib extension adding MySQL as back-end store",
    author = "Graham Higgins",
    author_email = "gjhiggins@gmail.com",
    url = "http://github.com/RDFLib/rdflib-mysql",
    py_modules = ["rdflib_mysql"],
    test_suite = "test",
    install_requires = ["rdflib>=3.0", "rdfextras>=0.1", "MySQL-python>=1.2.3"],
    entry_points = {
    	'rdf.plugins.store': [
            'MySQL = rdfextras.store.MySQL:MySQL',
        ],
    }

)
