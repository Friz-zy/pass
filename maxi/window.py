#!/usr/bin/env python2
# coding=utf-8

import os
import sys
import random
from keeper import Keeper
from listFiles import getFiles
from generator import Generator
from configobj import ConfigObj
from main_pass_ui import Ui_Pass
from config import Config
from dialogs import Password
try:
  from PySide import QtCore, QtGui
except:
    try:
        from PyQt4 import QtCore, QtGui
    except:
        print >> sys.stderr, "Error: can't load PySide or PyQT"
        sys.exit()

class Pass(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_Pass()
        self.ui.setupUi(self)
        self.loadConfig()
        
        # set size and background
        self.setFixedSize(600, 400)
        randImage = random.choice(getFiles(self.images))
        if randImage:
            br = QtGui.QBrush()
            Image = QtGui.QImage(randImage)
            br.setTextureImage(Image.scaled(600, 400))
            plt = self.palette()
            plt.setBrush(plt.Background, br)
            self.setPalette(plt)
        self.setWindowIcon(QtGui.QIcon(os.path.join(self.icons, 'ps.png')))

        self.ui.lineEditPass.setEchoMode(self.ui.lineEditPass.Password)
        self.ui.deliteButton.setEnabled(False)
        self.ui.saveButton.setEnabled(False)
        self.ui.lineEditGive.setEchoMode(self.ui.lineEditGive.Password)
        self.ui.listWidget.setSortingEnabled(True)

        self.ui.pushButton.clicked.connect(self.add)
        self.ui.deliteButton.clicked.connect(self.delete)
        self.ui.saveButton.clicked.connect(self.saveDatabase)
        QtCore.QObject.connect(self.ui.listWidget, 
              QtCore.SIGNAL("itemDoubleClicked(QListWidgetItem*)"),
                              self.getLoginFromList)
        self.ui.checkBox.stateChanged.connect(self.setPasswordVisible)
        
        # clipboard
        self.globalClipboard = QtGui.QApplication.clipboard()
        self.clipboard = QtGui.QClipboard

        # tray & menu
        self.createNewAction = QtGui.QAction(QtGui.QIcon.fromTheme("document-new"),
                                  '&Create new database', self)
        self.createNewAction.triggered.connect(self.createDatabase)

        self.loadAction = QtGui.QAction(QtGui.QIcon.fromTheme("document-open"),
                                '&Load database', self)
        self.loadAction.setShortcut('Ctrl+O')
        self.loadAction.setStatusTip('Opening Database')
        self.loadAction.triggered.connect(self.setDatabase)

        self.saveAction = QtGui.QAction(QtGui.QIcon.fromTheme("document-save"),
                                 '&Save database', self)
        self.saveAction.setShortcut('Ctrl+S')
        self.saveAction.setStatusTip('Saving Database')
        self.saveAction.triggered.connect(self.saveDatabase)

        self.saveAsAction = QtGui.QAction(QtGui.QIcon.fromTheme("document-save-as"),
                                  '&Save database as', self)
        self.saveAsAction.triggered.connect(self.saveAsDatabase)
        
        self.changePasswordAction = QtGui.QAction('&Change Password', self)
        self.changePasswordAction.triggered.connect(self.setPassword)

        self.aboutAction = QtGui.QAction(QtGui.QIcon.fromTheme("help-about"),
                                    '&About', self)
        self.aboutAction.triggered.connect(self.about)

        self.quitAction = QtGui.QAction(QtGui.QIcon.fromTheme("application-exit"),
                                        '&Quit', self)
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
        self.trayIconMenu.addAction(self.saveAction)
        self.trayIconMenu.addAction(self.saveAsAction)
        self.trayIconMenu.addAction(self.quitAction)
        self.trayIconPixmap = QtGui.QPixmap(os.path.join(self.icons, "ps.png"))
        self.trayIcon = QtGui.QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(self.trayIconMenu)
        self.trayIcon.setIcon(QtGui.QIcon(self.trayIconPixmap))
        self.trayIcon.show()
        self.trayIcon.activated.connect(self.changeVisible)

    def loadConfig(self):
    # initialization of variables
        self.keeper = Keeper()
        if not self.keeper.isKdb:
            self.showMessage("Warning!", "".join(("Can't load keepass module.",
                      " Nickname will be saved in plain text,",
                             " passwords will be not saved.")))

        self.password = ""
        self.file = ""
        self.salt = ""
        self.icons = ""
        self.images = ""
        self.config = Config(self, "pass") # self.homeDir
        self.config.createUserConfig(["icons", "images", "pass.py"])
        self.config.loadConfig() # self.file, self.salt, self.icons, self.images

        if self.file:
            self.setDatabase(self.file)
        else:
            self.setPassword()

        if not self.salt:
            self.salt = os.path.join(self.homeDir, "pass.py")
            if not os.path.exists(self.salt):
                with open(os.path.join(self.homeDir, "salt")) as f:
                    f.write("##")

        if not self.icons:
            self.icons = os.path.join(self.homeDir, "icons")
            if not os.path.isdir(self.icons):
                self.icons = "./icons"

        if not self.images:
            self.images = os.path.join(self.homeDir, "images")
            if not os.path.isdir(self.images):
                self.images = "./images"

        self.generator = Generator(self)
        self.generator.set_salt(self.salt)

    def saveConfig(self):
        if not self.file:
            self.file = ""
        self.config.saveConfig(["file", "salt", "icons", "images"])

    def createDatabase(self):
        if self.file and self.savePageBeforeClose() == -1:
            return 0
        try:
            self.file = str(self.showFileSaveDialog()[0])
            if file:
                self.keeper = Keeper()
        except: self.showCritical("Error","Can't create %s" % file)

    def setDatabase(self, file=""):
        if self.file and self.savePageBeforeClose() == -1:
            return 0
        back_file = self.file
        back_password = self.password
        if not file:
            self.file = self.showFileOpenDialog()[0]
        else:
            self.file = file
        self.setPassword(self.file)
        if self.file and self.password: 
            try:
                self.keeper.load(self.file, self.password)
                self.setUsersUrls()
            except:
                self.showCritical("Some error with set db", "Some error occurred when opening %s as database" 
                        %(self.file))
                self.file = back_file
                self.password = back_password
        else:
            self.file = back_file
            self.password = back_password

    def setUsersUrls(self):
        self.ui.listWidget.clear()
        for url in self.keeper.urls.keys():
            for name in self.keeper.urls[url].keys():
                if name != "SUSTEM" and url != "$":
                    self.ui.listWidget.insertItem(0, 
                          str(url) + " : " + str(name))
        if self.ui.listWidget.count():
            self.ui.deliteButton.setEnabled(True)
            self.ui.saveButton.setEnabled(True)

    def saveDatabase(self):
        if  self.file:
            self.keeper.save(self.file, self.password)
        else:
            self.saveAsDatabase()

    def saveAsDatabase(self):
        if self.ui.listWidget.count():
            try:
                file = self.showFileSaveDialog()[0]
                if file:
                    self.file = self.keeper.save(file, self.password)
            except: self.showCritical("Error","Can't save %s" % file)

    def setPassword(self, databaseName = None):
        if not databaseName:
            dlg = Password('Input Password',
                           'Input your password here:', self)
            dlg.exec_()
            text, ok = dlg.getPassword()
        else:
            text = 'Input your password for %s here:' % (str(databaseName))
            dlg = Password('Input Password', text, self)
            dlg.exec_()
            text, ok = dlg.getPassword()
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
        password = self.generator.generate_simple(str(self.ui.lineEditUser.text()),
                      str(self.ui.lineEditURL.text()), self.password, 32)
        self.ui.lineEditURL.clear()
        self.ui.lineEditUser.clear()
        self.ui.lineEditGive.setText(password)
        self.clipboard.setText(self.globalClipboard, password)
        if name and url and (url not in self.keeper.urls.keys() \
          or name not in self.keeper.urls[url].keys() \
            or password != self.keeper.urls[url][name][0]):
            self.keeper.urls[url] = {name : [password, "simple 32"]}
            self.ui.listWidget.insertItem(0, nick)
            # enable buttons
            self.ui.deliteButton.setEnabled(True)
            self.ui.saveButton.setEnabled(True)

    def savePageBeforeClose(self):
        if self.ui.listWidget.count():
            q = "Do you want to save your changes?"
            if self.file:
                q = "Do you want to save your changes as %s?" % self.file
            choice = self.showChoice("?!", q)
            if choice == -1:
                return -1
            elif choice:
                self.saveDatabase()
            return 1

    def showChoice(self, title, text):
        q = QtGui.QMessageBox.question(self, 
                  title,
                  text,
                  QtGui.QMessageBox.No |
                  QtGui.QMessageBox.Cancel |
                  QtGui.QMessageBox.Yes,)
        if q == QtGui.QMessageBox.Yes:
            return True
        elif q == QtGui.QMessageBox.No:
            return False
        return -1

    def setPasswordVisible(self, e):
        if e:
            self.ui.lineEditGive.setEchoMode(self.ui.lineEditGive.Password)
        else:
            self.ui.lineEditGive.setEchoMode(self.ui.lineEditGive.Normal)

    def showFileOpenDialog(self, path="", filer=""):
        if not path:
            path = self.homeDir
        return QtGui.QFileDialog.getOpenFileName(self,
                      'Open file', path, filer)

    def showFileSaveDialog(self, path="", filer=""):
        if not path:
            path = self.homeDir
        return QtGui.QFileDialog.getSaveFileName(self,
                    'Save file as:', path, filer)

    def showMessage(self, title, text):
        QtGui.QMessageBox.information(self, str(title), str(text))

    def showCritical(self, title, text):
        QtGui.QMessageBox.critical(self, str(title), str(text))

    def changeVisible(self,r):
        if r == QtGui.QSystemTrayIcon.Trigger:
            if self.isHidden():
                self.showNormal()
            else:
                self.hide()
    
    def changeEvent(self, e):
        # to tray
        if self.isMinimized():
            self.hide()
            e.ignore()

    def closeEvent(self, e):
        if self.savePageBeforeClose() != -1:
            self.saveDatabase()
        self.saveConfig()
        print "bye!"
        self.close()

def main():
    app = QtGui.QApplication(sys.argv)
    myapp = Pass()
    myapp.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
