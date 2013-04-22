# Pass - «associate password so simple»

Implementation of an algorithm generating and storing a passwords like this: "cf83e1357eefb8bdf1542850d66d8007". Written on python 2.7 and PyQT.
Used `sha512(sha512("salt" XOR "nick : site") XOR "pass")[:32]` algorithm, created by [Gist](https://gist.github.com/3334991) and modified [here](http://news.ycombinator.com/item?id=4374888).

Minimalistic interface -> mini
Maximalistic interface with background images and saving authentications data -> maxi

##How to:##
This programs helps you generate unique passwords for sites, programs, etc...
Run window.py from one of the folders.
At first start python will record unique salt in pass.py and run generating password. You need to enter nick, url of site and master password. New password will be displayed in bottom form. Just copy it.

##How to install:##
If you know about python [easy_install](http://www.google.com/search?q=python+egg+install) and [pip](http://pypi.python.org/pypi/pip) - use it! Else expect packages or read about pip.


Src on [Github](http://friz-zy.github.com)
Code under **MIT license** and Images and Photo under **Creative Commons license**

For quick use copy to bash:
`python pass.py`
Or change 'pass.py' to you'r salt file and use:
`python -c "import hashlib, getpass;from itertools import cycle, izip;f = open('pass.py');salt = f.read();f.close();print hashlib.sha512(''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(hashlib.sha512(''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(salt, cycle(raw_input('nick:') + ' : ' + raw_input('site:'))))).hexdigest(), cycle(getpass.getpass())))).hexdigest()[:32]"`

*Filipp Frizzy aka filipp.s.frizzy@gmail.com*
