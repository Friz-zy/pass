# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_pass.ui'
#
# Created: Mon Apr  8 17:02:09 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Pass(object):
    def setupUi(self, Pass):
        Pass.setObjectName(_fromUtf8("Pass"))
        Pass.resize(800, 600)
        self.QWidget = QtGui.QWidget(Pass)
        self.QWidget.setObjectName(_fromUtf8("QWidget"))
        self.gridLayout = QtGui.QGridLayout(self.QWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelUser = QtGui.QLabel(self.QWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelUser.sizePolicy().hasHeightForWidth())
        self.labelUser.setSizePolicy(sizePolicy)
        self.labelUser.setObjectName(_fromUtf8("labelUser"))
        self.verticalLayout.addWidget(self.labelUser)
        self.lineEditUser = QtGui.QLineEdit(self.QWidget)
        self.lineEditUser.setObjectName(_fromUtf8("lineEditUser"))
        self.verticalLayout.addWidget(self.lineEditUser)
        self.labelURL = QtGui.QLabel(self.QWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelURL.sizePolicy().hasHeightForWidth())
        self.labelURL.setSizePolicy(sizePolicy)
        self.labelURL.setObjectName(_fromUtf8("labelURL"))
        self.verticalLayout.addWidget(self.labelURL)
        self.lineEditURL = QtGui.QLineEdit(self.QWidget)
        self.lineEditURL.setObjectName(_fromUtf8("lineEditURL"))
        self.verticalLayout.addWidget(self.lineEditURL)
        self.labelPass = QtGui.QLabel(self.QWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPass.sizePolicy().hasHeightForWidth())
        self.labelPass.setSizePolicy(sizePolicy)
        self.labelPass.setObjectName(_fromUtf8("labelPass"))
        self.verticalLayout.addWidget(self.labelPass)
        self.lineEditPass = QtGui.QLineEdit(self.QWidget)
        self.lineEditPass.setObjectName(_fromUtf8("lineEditPass"))
        self.verticalLayout.addWidget(self.lineEditPass)
        self.pushButton = QtGui.QPushButton(self.QWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        spacerItem = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.lineEditGive = QtGui.QLineEdit(self.QWidget)
        self.lineEditGive.setObjectName(_fromUtf8("lineEditGive"))
        self.verticalLayout.addWidget(self.lineEditGive)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.listWidget = QtGui.QListWidget(self.QWidget)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.deliteButton = QtGui.QPushButton(self.QWidget)
        self.deliteButton.setObjectName(_fromUtf8("deliteButton"))
        self.horizontalLayout.addWidget(self.deliteButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.saveButton = QtGui.QPushButton(self.QWidget)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.horizontalLayout.addWidget(self.saveButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        Pass.setCentralWidget(self.QWidget)
        self.menubar = QtGui.QMenuBar(Pass)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Pass.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Pass)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Pass.setStatusBar(self.statusbar)

        self.retranslateUi(Pass)
        QtCore.QMetaObject.connectSlotsByName(Pass)

    def retranslateUi(self, Pass):
        Pass.setWindowTitle(QtGui.QApplication.translate("Pass", "Pass", None, QtGui.QApplication.UnicodeUTF8))
        self.labelUser.setText(QtGui.QApplication.translate("Pass", "User:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelURL.setText(QtGui.QApplication.translate("Pass", "Url:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPass.setText(QtGui.QApplication.translate("Pass", "Pass:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Pass", "Give It!", None, QtGui.QApplication.UnicodeUTF8))
        self.deliteButton.setText(QtGui.QApplication.translate("Pass", "Delite", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("Pass", "Save", None, QtGui.QApplication.UnicodeUTF8))

