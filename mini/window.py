#!/usr/bin/env python2
# coding=utf-8
# http://habrahabr.ru/post/31426/
from pass_ui import Ui_Pass
import six
import sys, hashlib
if six.PY3:
    from itertools import cycle
    izip = zip
else:
    from itertools import cycle, izip

try:
  from PySide import QtCore, QtGui
except:
    try:
        from PyQt4 import QtCore, QtGui
    except:
        six.print_(("Error: can't load PySide or PyQT"), file=sys.stderr, end="\n", sep=" ")
        sys.exit()

class Pass(QtGui.QWidget):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui = Ui_Pass()
		self.ui.setupUi(self)
		self.ui.lineEditPass.setEchoMode(self.ui.lineEditPass.Password)
		QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL("clicked()"), self.add)

		# use pass.py as salt and check the unique
		with open('pass.py') as f:
			salt = f.readlines()
		# if salt isn't unique: add some unique string to it
		if "#" in salt[-1][1]:
			import os.path
			try:
				os.popen("(dmesg;env;head -c16 /dev/random)|sha512sum >> ./pass.py")
				with open('pass.py', "r") as f:
					salt = f.readlines()
				salt[-1]="#" + salt[-1]
				with open('pass.py', "w") as f:
					f.writelines(salt)
				os.popen("chmod 400 ./pass.py") # only your user can read this file
			except (IOError, OSError):
				# it is works in all OS, but clock() is most efficient in Windows
				from time import clock
				with open('pass.py', "a") as f:
					f.writeline("#" + hashlib.sha512(clock()).hexdigest())


	def add(self):
		with open('pass.py') as f:
			salt = f.read()
		nick = str(self.ui.lineEditUser.text()) + " : " + str(self.ui.lineEditURL.text())
		firstXor = self.xor(salt, nick)
		self.ui.lineEditURL.clear()
		self.ui.lineEditUser.clear()
		firstSha = hashlib.sha512(firstXor).hexdigest()
		password = hashlib.sha512(self.xor(firstSha, str(self.ui.lineEditPass.text()))).hexdigest()[:32]
		self.ui.lineEditPass.clear()
		self.ui.lineEditGive.setText(password)

	# XOR function, thk The Internet
	def xor(self, ss, key):
		key = cycle(key)
		return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(ss, key))

def main():
    app = QtGui.QApplication(sys.argv)
    myapp = Pass()
    myapp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

