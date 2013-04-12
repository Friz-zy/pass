#!/usr/bin/env python2
# coding=utf-8
# http://habrahabr.ru/post/31426/

"""
db = KPDB("foo.kdb", "bar")
db.lock()

db.groups[] # internet, mail
db.create_group("foobar", db.groups[0]) # Internet: -foobar
db.create_group(self, id_=None, title=None, image=1, db=None, level=0, parent=None, children=[], entries=[], creation=None, last_mod=None, last_access=None, expire=None, flags=None)
create_entry(self, group=None, title='', image=1, url='', username='', password='', comment='', y=2999, mon=12, d=28, h=23, min_=59, s=59)

remove_entry(self, entry=None)
remove_group(self, group=None)

db.save("foo.kdb", "bar")
db.unlock("bar")
db.close() 
del db
"""


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

		self.ui.pushButton.clicked.connect(self.add)
		self.ui.deliteButton.clicked.connect(self.delete)
		self.ui.saveButton.clicked.connect(self.save)
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

		self.quitAction = QtGui.QAction(QtGui.QIcon('icons/exit.png'),'&Quit', self)

		self.createNewAction.triggered.connect(self.createDatabase)
		self.loadAction.setShortcut('Ctrl+O')
		self.loadAction.setStatusTip('Opening Database')
		self.loadAction.triggered.connect(self.setDatabase)
		self.saveAction.setShortcut('Ctrl+S')
		self.saveAction.setStatusTip('Saving Database')
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
		self.trayIconPixmap = QtGui.QPixmap('icons/ps.png')
		self.trayIcon = QtGui.QSystemTrayIcon(self)
		self.trayIcon.setContextMenu(self.trayIconMenu)
		self.trayIcon.setIcon(QtGui.QIcon(self.trayIconPixmap))
		self.trayIcon.show()

		self.setWindowIcon(QtGui.QIcon('icons/ps.png'))

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


	def showFileOnenDialog(self):
	# QStringList 	getOpenFileNames ( QWidget * parent = 0, const QString & caption = QString(), const QString & dir = QString(), const QString & filter = QString(), QString * selectedFilter = 0, Options options = 0 )
		return QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')

	def showFileSaveDialog(self):
	# QString 	getSaveFileName ( QWidget * parent = 0, const QString & caption = QString(), const QString & dir = QString(), const QString & filter = QString(), QString * selectedFilter = 0, Options options = 0 )
		return QtGui.QFileDialog.getSaveFileName(self, 'Save file as:', '/home')

	def showMessage(self, title, text):
		QtGui.QMessageBox.information(self, title, text)

	def showCritical(self, title, text):
		QtGui.QMessageBox.critical(self, title, text)

	def createDatabase(self):
		file = self.showFileSaveDialog()
		try:
			self.db = KPDB(filepath=file, password=self.password, new=True)
			self.db.lock()
		except KPError as err:
			self.showCritical("Some error occurred when opening %s" %(file), err)

	def setDatabase(self, file=None):
		if self.db:
			self.db.saveDatabase
			self.db.unlock(self.password)
			self.db.close()
		if not file:
			file = self.showFileOnenDialog()
		self.getPassword(file)
		try:
			self.db = KPDB(file, self.password)
			self.db.lock()
		except KPError as err:
			self.showCritical("Some error occurred when opening %s" %(file), err)

	def saveDatabase(self):
		if self.db:
			self.db.save(password=self.password)
			
	def saveAsDatabase(self):
		file = self.showFileSaveDialog()
		if self.db and file:
			self.db.save(filepath=file, password=self.password)
			
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

