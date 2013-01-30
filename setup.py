from setuptools import setup, find_packages
from os.path import join, dirname
import maxi as module # import mini or maxi

setup(
    name='pass',
    version = module.__version__,
    author = module.__autor__,
    author_email = module.__email__,
    description = module.__description__,
    license = module.__license__,
    keywords = module.__keywords__,
    url = module.__url__,   # project home page, if any
    install_requires = ['PyQt4>=4.0'],
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    include_package_data=True,
    test_suite='tests',
    entry_points={
        'console_scripts':
            ['pass = module.window',],
        'gui_scripts':
            ['pass = module.window',],
        'setuptools.installation':
            ['eggsecutable = module.window',],
        }
)

