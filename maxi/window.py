#!/usr/bin/env python2
# coding=utf-8
# http://habrahabr.ru/post/31426/
from main_pass_ui import Ui_Pass
from PyQt4 import QtCore, QtGui
from listFiles import getFiles
from kppy import KPDB, KPError
from time import clock
from itertools import cycle, izip
import sys
import random
import time
import hashlib
import os.path

class Pass(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.ui = Ui_Pass()
		self.ui.setupUi(self)
		self.ui.lineEditPass.setEchoMode(self.ui.lineEditPass.Password)
		self.ui.deliteButton.setEnabled(False)
		self.ui.saveButton.setEnabled(False)

		QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL("clicked()"), self.add)
		QtCore.QObject.connect(self.ui.deliteButton,QtCore.SIGNAL("clicked()"), self.delete)
		QtCore.QObject.connect(self.ui.saveButton,QtCore.SIGNAL("clicked()"), self.save)
		QtCore.QObject.connect(self.ui.listWidget, QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem*)"), self.getLoginFromList)

		self.password = ""
		self.getPassword()

		# tray & menu
		self.createNewAction = QtGui.QAction('&Create new database', self)
		self.loadAction = QtGui.QAction('&Load database', self)
		self.saveAction = QtGui.QAction('&Save database', self)
		self.saveAsAction = QtGui.QAction('&Save database as', self)
		self.changePasswordAction = QtGui.QAction('&Change Password', self)
		self.aboutAction = QtGui.QAction('&About', self)

		self.quitAction = QtGui.QAction(QtGui.QIcon('images/exit.png'),'&Quit', self)

		self.createNewAction.triggered.connect(self.createDatabase)
		self.loadAction.triggered.connect(self.setDatabase)
		self.saveAction.triggered.connect(self.saveDatabase)
		self.saveAsAction.triggered.connect(self.saveAsDatabase)
		self.changePasswordAction.triggered.connect(self.getPassword)
		self.aboutAction.triggered.connect(self.about)

		self.quitAction.setShortcut('Ctrl+Q')
		self.quitAction.setStatusTip('Exit application')
		self.quitAction.triggered.connect(self.close)

		self.fileMenu = self.ui.menubar.addMenu('&File')
		self.fileMenu.addAction(self.createNewAction)
		self.fileMenu.addAction(self.loadAction)
		self.fileMenu.addAction(self.saveAction)
		self.fileMenu.addAction(self.saveAsAction)
		self.fileMenu.addAction(self.changePasswordAction)
		self.fileMenu.addAction(self.aboutAction)
		self.fileMenu.addAction(self.quitAction)

		self.trayIconMenu = QtGui.QMenu(self)
		self.trayIconMenu.addAction(self.createNewAction)
		self.trayIconMenu.addAction(self.loadAction)
		self.trayIconMenu.addAction(self.saveAction)
		self.trayIconMenu.addAction(self.saveAsAction)
		self.trayIconMenu.addAction(self.changePasswordAction)
		self.trayIconMenu.addAction(self.aboutAction)
		self.trayIconMenu.addAction(self.quitAction)
		self.trayIconPixmap = QtGui.QPixmap('images/ps.png')
		self.trayIcon = QtGui.QSystemTrayIcon(self)
		self.trayIcon.setContextMenu(self.trayIconMenu)
		self.trayIcon.setIcon(QtGui.QIcon(self.trayIconPixmap))
		self.trayIcon.show()

		self.setWindowIcon(QtGui.QIcon('images/ps.png'))

		# check the unique salt
		salt = "##"
		with open('pass.py') as f:
			salt = f.readlines()
		# if salt isn't unique: add some unique string to it
		if "#" in salt[-1][1]:
			try:
				os.popen("(dmesg;env;head -c16 /dev/random)|sha512sum >> ./pass.py")
				with open('pass.py', "r") as f:
					salt = f.readlines()
				salt[-1]="#" + salt[-1]
				with open('pass.py', "w") as f:
					f.writelines(salt)
				os.popen("chmod 400 ./pass.py") # only your user can read this file
			except IOError, OSError:
				# it is works in all OS, but clock() is most efficient in Windows
				with open('pass.py', "a") as f:
					f.writeline("#" + hashlib.sha512(clock()).hexdigest())

		# Get list user's urls
		urls = []
		with open("urls") as f:
			self.urls = f.readlines()
		for S in self.urls:
			self.ui.listWidget.insertItem(0, S)

		# Enable buttons
		if self.urls:
			self.ui.deliteButton.setEnabled(True)
			self.ui.saveButton.setEnabled(True)


	def showFileDialog(self):
		return QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')

	def showMessage(self, title, text):
		QtGui.QMessageBox.information(self, title, text)

	def showCritical(self, title, text):
		QtGui.QMessageBox.critical(self, title, text)

	def createDatabase(self):
		self.db = KPDB(new=True)

	def setDatabase(self):
		file = self.showFileDialog()
		self.getPassword(file)
		try:
			db = KPDB(file, self.password)
		except KPError as err:
		  self.showCritical("Some error occurred when opening %s" %(file), err)

	def saveDatabase(self):pass

	def saveAsDatabase(self):pass

	def getPassword(self, databaseName = None):
		if not databaseName:
			text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Enter your password:')
		else:
			text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Enter password for %s:') % (databaseName)
		if ok:
			self.password = str(text)
			self.ui.lineEditPass.setText(self.password)

	def about(self):
		about = ""
		self.showMessage("About paSs", about)

	def getLoginFromList(self):
		item = self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
		text = str(item.text())
		#hack
		for u in self.urls:
			if str(text) == u:
				self.urls.remove(u)

		b = text.find(" : ")
		self.ui.lineEditUser.setText(text[:b])
		self.ui.lineEditURL.setText(text[b+3:])
		self.ui.lineEditPass.setFocus()

	def save(self):
		with open("urls", "w") as f:
			f.write('\n'.join(self.urls))

	def delete(self):
		# dirty hack
		item = self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
		text = item.text()
		for u in self.urls:
			if str(text) == u:
				self.urls.remove(u)
		self.ui.listWidget.removeItemWidget(item)
		# Check if the list is empty - if yes, disable the deletebutton.
		if not self.ui.listWidget.count():
			self.ui.deliteButton.setEnabled(False)

	def add(self):
		with open('pass.py') as f:
			salt = f.read()
		nick = str(self.ui.lineEditUser.text()) + " : " + str(self.ui.lineEditURL.text())
		firstXor = self.xor(salt, nick)
		self.ui.lineEditURL.clear()
		self.ui.lineEditUser.clear()
		firstSha = hashlib.sha512(firstXor).hexdigest()
		password = hashlib.sha512(self.xor(firstSha, str(self.password))).hexdigest()[:32]
		self.ui.lineEditPass.clear()
		self.ui.lineEditGive.setText(password)
		if nick != " : " and nick not in self.urls:
			self.urls.append(nick)
			self.ui.listWidget.insertItem(0, nick)
			# enable buttons
			self.ui.deliteButton.setEnabled(True)
			self.ui.saveButton.setEnabled(True)

	# XOR function, thk The Internet
	def xor(self, ss, key):
		key = cycle(key)
		return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(ss, key))


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	myapp = Pass()
	myapp.setFixedSize(600, 400)
	randImage = random.choice(getFiles("./images"))
	if randImage:
		br = QtGui.QBrush()
		Image = QtGui.QImage(randImage)
		br.setTextureImage(Image.scaled(600, 400))
		plt = myapp.palette()
		plt.setBrush(plt.Background, br)
		myapp.setPalette(plt)
	myapp.show()

	sys.exit(app.exec_())

