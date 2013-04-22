from setuptools import setup, find_packages
from os.path import join, dirname
import shutil, errno, os
target = "maxi" # import mini or maxi

root, dirs, files = os.walk('.').next() 

dotDirs=[]
for D in dirs:
    if D[0] != ".":
        shutil.move(D, "." + D)
        dotDirs.append(D)

shutil.copytree("." + target, "paSs")

if not os.path.exists("pass.egg-info"):
    os.makedirs("pass.egg-info")
for F in files:
    if ".md" in F:
        shutil.copy(F, "pass.egg-info")


import paSs as module
setup(
    name='pass',
    version = module.__version__,
    author = module.__author__,
    author_email = module.__email__,
    description = module.__description__,
    license = module.__license__,
    keywords = module.__keywords__,
    url = module.__url__,   # project home page, if any
    install_requires = ['PyQt4>=4.0'],
    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst', '*.md'],
        # And include any *.msg files found in the 'hello' package, too:
        "paSs" : ['images/*', '*.*'],
    },
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    include_package_data=True,
    test_suite='tests',
    entry_points={
        'console_scripts':
            ['pass = paSs.window',],
        'gui_scripts':
            ['pass = paSs.window',],
#        'setuptools.installation':
#            ['eggsecutable = ' + md + '.window',],
        }
)

shutil.rmtree("paSs")
shutil.rmtree("build")
shutil.rmtree("pass.egg-info")

for D in dotDirs:
    shutil.move("." + D, D)

root, dirs, files = os.walk('.').next()
for F in files:
    if ".pyc" in F:
        os.remove(F)

