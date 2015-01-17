from setuptools import setup
from os.path import join, dirname

import ps as module
setup(
    name='ps',
    version = module.__version__,
    author = module.__author__,
    author_email = module.__email__,
    description = module.__description__,
    license = module.__license__,
    keywords = module.__keywords__,
    url = module.__url__,   # project home page, if any
    install_requires = ['PySide', 'pycrypto', 'six', 'keepass'],
    packages=['ps'],
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    include_package_data=True,
    classifiers=[
        'License :: OSI Approved :: MIT',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts':
            ['pass = ps.window:main',],
        'gui_scripts':
            ['pass = ps.window:main',],
        }
)