#!/usr/bin/env python2
# coding=utf-8
# http://habrahabr.ru/post/31426/



import sys
import random
from main_pass_ui import Ui_Pass
from PyQt4 import QtCore, QtGui
from listFiles import getFiles
from keeper import Keeper
from generator import Generator


class Pass(QtGui.QMainWindow):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		
		self.loadConfig()
		
		self.ui = Ui_Pass()
		self.ui.setupUi(self)
		self.ui.lineEditPass.setEchoMode(self.ui.lineEditPass.Password)
		self.ui.deliteButton.setEnabled(False)
		self.ui.saveButton.setEnabled(False)
		self.ui.listWidget.setSortingEnabled(True)

		self.ui.pushButton.clicked.connect(self.add)
		self.ui.deliteButton.clicked.connect(self.delete)
		self.ui.saveButton.clicked.connect(self.saveDatabase)
		QtCore.QObject.connect(self.ui.listWidget, QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem*)"), self.getLoginFromList)

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

		# initialization of variables
		self.file = None
		self.password = ""
		self.getPassword()
		self.keeper = Keeper()
		if not self.keeper.isKdb:
			self.showMessage("Warning!", "Can't load kpdb module. Nickname will be saved in plain text, passwords will be not saved.")

		#self.setDatabase()
		self.generator = Generator(self)
		self.generator.set_salt("./pass.py")

	def getUsersUrls(self):
		#self.urls = self.keeper.urls
		self.ui.listWidget.clear()
		for url in self.keeper.urls.keys():
			for name in self.keeper.urls[url].keys():
				if name != "SUSTEM" and url != "$":
					self.ui.listWidget.insertItem(0, str(url) + " : " + str(name))
		if self.ui.listWidget.count():
			self.ui.deliteButton.setEnabled(True)
			self.ui.saveButton.setEnabled(True)

	def loadConfig(self): pass

	def createDatabase(self):
		try:
			self.file = str(self.showFileSaveDialog())
			if file:
				self.keeper = Keeper()
		except: self.showCritical("","")

	def setDatabase(self, file=None):
		if self.file:
			self.keeper.save(file,password)
		if not file:
			file = self.file = self.showFileOnenDialog()
		else:
			self.file = file
		if file or not self.password:
			self.getPassword(file)
		try:
			self.keeper.load(file, self.password)
			self.getUsersUrls()
		except:
			self.showCritical("Some error occurred when opening %s" %(file), "Some error with set db")

	def saveDatabase(self):
		if  self.file:
			self.keeper.save(self.file, self.password)
		else:
			self.saveAsDatabase()

	def saveAsDatabase(self):
		file = self.showFileSaveDialog()
		if file:
			self.keeper.save(file, self.password)
			self.file = file

	def getPassword(self, databaseName = None):
		if not databaseName:
			text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Enter your password:')
		else:
			text = 'Enter password for %s:' % (str(databaseName))
			text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', text)
		if ok:
			self.password = str(text)
			self.ui.lineEditPass.setText(self.password)

	def about(self):
		about = ""
		self.showMessage("About paSs", about)

	def getLoginFromList(self):
		item = self.ui.listWidget.item(self.ui.listWidget.currentRow())
		text = str(item.text())
		b = text.find(" : ")
		self.ui.lineEditURL.setText(text[:b])
		self.ui.lineEditUser.setText(text[b+3:])
		self.ui.lineEditPass.setFocus()

	def delete(self):
		item = self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
		text = str(item.text())
		begin = text.find(" : ")
		url = text[:begin]
		name = text[begin + 3:]
		for u in self.keeper.urls.keys():
			if u in url and name in self.keeper.urls[u].keys():
				del self.keeper.urls[u][name]
		self.ui.listWidget.removeItemWidget(item)
		if not self.ui.listWidget.count():
			self.ui.deliteButton.setEnabled(False)

	def add(self):
		name = str(self.ui.lineEditUser.text())
		url = str(self.ui.lineEditURL.text())
		nick =  " : ".join((url, name)) 
		password = self.generator.generate_simple(str(self.ui.lineEditUser.text()), str(self.ui.lineEditURL.text()), self.password, 32)
		self.ui.lineEditURL.clear()
		self.ui.lineEditUser.clear()
		#self.ui.lineEditPass.clear()
		self.ui.lineEditGive.setText(password)
		if name and url and (url not in self.keeper.urls.keys() or name not in self.keeper.urls[url].keys() or password != self.keeper.urls[url][name][0]):
			self.keeper.urls[url] = {name : [password, "simple 32"]}
			self.ui.listWidget.insertItem(0, nick)
			# enable buttons
			self.ui.deliteButton.setEnabled(True)
			self.ui.saveButton.setEnabled(True)
			
	def showFileOnenDialog(self):
	# QStringList 	getOpenFileNames ( QWidget * parent = 0, const QString & caption = QString(), const QString & dir = QString(), const QString & filter = QString(), QString * selectedFilter = 0, Options options = 0 )
		return QtGui.QFileDialog.getOpenFileName(self, 'Open file', '.')

	def showFileSaveDialog(self):
	# QString 	getSaveFileName ( QWidget * parent = 0, const QString & caption = QString(), const QString & dir = QString(), const QString & filter = QString(), QString * selectedFilter = 0, Options options = 0 )
		return QtGui.QFileDialog.getSaveFileName(self, 'Save file as:', '.')

	def showMessage(self, title, text):
		QtGui.QMessageBox.information(self, str(title), str(text))

	def showCritical(self, title, text):
		QtGui.QMessageBox.critical(self, str(title), str(text))





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

