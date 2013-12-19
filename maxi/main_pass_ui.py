# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_pass.ui'
#
# Created: Mon Jul 22 00:58:17 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

import sys
try:
  from PySide import QtCore, QtGui
except:
    try:
        from PyQt4 import QtCore, QtGui
    except:
        print >> sys.stderr, "Error: can't load PySide or PyQT"
        sys.exit()

class Ui_Pass(object):
    def setupUi(self, Pass):
        Pass.setObjectName("Pass")
        Pass.resize(763, 553)
        self.QWidget = QtGui.QWidget(Pass)
        self.QWidget.setObjectName("QWidget")
        self.gridLayout = QtGui.QGridLayout(self.QWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelUser = QtGui.QLabel(self.QWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelUser.sizePolicy().hasHeightForWidth())
        self.labelUser.setSizePolicy(sizePolicy)
        self.labelUser.setObjectName("labelUser")
        self.verticalLayout.addWidget(self.labelUser)
        self.lineEditUser = QtGui.QLineEdit(self.QWidget)
        self.lineEditUser.setObjectName("lineEditUser")
        self.verticalLayout.addWidget(self.lineEditUser)
        self.labelURL = QtGui.QLabel(self.QWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelURL.sizePolicy().hasHeightForWidth())
        self.labelURL.setSizePolicy(sizePolicy)
        self.labelURL.setObjectName("labelURL")
        self.verticalLayout.addWidget(self.labelURL)
        self.lineEditURL = QtGui.QLineEdit(self.QWidget)
        self.lineEditURL.setObjectName("lineEditURL")
        self.verticalLayout.addWidget(self.lineEditURL)
        self.labelPass = QtGui.QLabel(self.QWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPass.sizePolicy().hasHeightForWidth())
        self.labelPass.setSizePolicy(sizePolicy)
        self.labelPass.setObjectName("labelPass")
        self.verticalLayout.addWidget(self.labelPass)
        self.lineEditPass = QtGui.QLineEdit(self.QWidget)
        self.lineEditPass.setObjectName("lineEditPass")
        self.verticalLayout.addWidget(self.lineEditPass)
        self.pushButton = QtGui.QPushButton(self.QWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        spacerItem = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.checkBox = QtGui.QCheckBox(self.QWidget)
        self.checkBox.setEnabled(True)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.lineEditGive = QtGui.QLineEdit(self.QWidget)
        self.lineEditGive.setObjectName("lineEditGive")
        self.verticalLayout.addWidget(self.lineEditGive)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listWidget = QtGui.QListWidget(self.QWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.deliteButton = QtGui.QPushButton(self.QWidget)
        self.deliteButton.setObjectName("deliteButton")
        self.horizontalLayout.addWidget(self.deliteButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.saveButton = QtGui.QPushButton(self.QWidget)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        Pass.setCentralWidget(self.QWidget)
        self.menubar = QtGui.QMenuBar(Pass)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 763, 21))
        self.menubar.setObjectName("menubar")
        Pass.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Pass)
        self.statusbar.setObjectName("statusbar")
        Pass.setStatusBar(self.statusbar)

        self.retranslateUi(Pass)
        QtCore.QMetaObject.connectSlotsByName(Pass)

    def retranslateUi(self, Pass):
        Pass.setWindowTitle(QtGui.QApplication.translate("Pass", "Pass", None, QtGui.QApplication.UnicodeUTF8))
        self.labelUser.setText(QtGui.QApplication.translate("Pass", "User:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelURL.setText(QtGui.QApplication.translate("Pass", "Url:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPass.setText(QtGui.QApplication.translate("Pass", "Pass:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Pass", "Give It!", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("Pass", "Hide password", None, QtGui.QApplication.UnicodeUTF8))
        self.deliteButton.setText(QtGui.QApplication.translate("Pass", "Delite", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("Pass", "Save", None, QtGui.QApplication.UnicodeUTF8))

