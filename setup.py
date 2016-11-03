from setuptools import setup, find_packages

# Convert markdown README to rst format for PyPI.
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name='apimatic-cli',
    version='1.3',
    description='A command line interface for APIMatic.',
    long_description=long_description,
    author='Shahid Khaliq',
    author_email='shahid.khaliq@apimatic.io',
    url='https://apimatic.io/',
    packages=find_packages(),
    install_requires=[
        'requests>=2.9.1, <3.0',
        'jsonpickle>=0.7.1, <1.0'
    ],
    tests_require=[
        'nose>=1.3.7',
        'mock>=2.0.0'
    ],
    test_suite = 'nose.collector',
    entry_points={
        'console_scripts': [
            'apimatic-cli = apimaticcli.__main__:main'
        ]
    }
)