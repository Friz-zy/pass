# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_pass.ui'
#
# Created: Tue Jun 18 13:13:28 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Pass(object):
    def setupUi(self, Pass):
        Pass.setObjectName(_fromUtf8("Pass"))
        Pass.resize(763, 553)
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
        self.checkBox = QtGui.QCheckBox(self.QWidget)
        self.checkBox.setEnabled(True)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout.addWidget(self.checkBox)
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
        self.menubar.setGeometry(QtCore.QRect(0, 0, 763, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Pass.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Pass)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Pass.setStatusBar(self.statusbar)

        self.retranslateUi(Pass)
        QtCore.QMetaObject.connectSlotsByName(Pass)

    def retranslateUi(self, Pass):
        Pass.setWindowTitle(_translate("Pass", "Pass", None))
        self.labelUser.setText(_translate("Pass", "User:", None))
        self.labelURL.setText(_translate("Pass", "Url:", None))
        self.labelPass.setText(_translate("Pass", "Pass:", None))
        self.pushButton.setText(_translate("Pass", "Give It!", None))
        self.checkBox.setText(_translate("Pass", "Hide password", None))
        self.deliteButton.setText(_translate("Pass", "Delite", None))
        self.saveButton.setText(_translate("Pass", "Save", None))

