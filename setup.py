from setuptools import setup, find_packages
from os.path import join, dirname
import shutil, errno, os

import Pass as module
setup(
    name='Pass',
    version = module.__version__,
    author = module.__author__,
    author_email = module.__email__,
    description = module.__description__,
    license = module.__license__,
    keywords = module.__keywords__,
    url = module.__url__,   # project home page, if any
    install_requires = ['PySide', 'pycrypto', 'six'],
    packages=['Pass'],
    package_data = {
        '.': ['*.txt', '*.rst', '*.md'],
        "Pass" : ['images/*', 'icons/*', 'keepass/*', '*.*'],
    },
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    include_package_data=True,
    classifiers=[
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts':
            ['pass = paSs.window:main',],
        'gui_scripts':
            ['pass = paSs.window:main',],
        }
)