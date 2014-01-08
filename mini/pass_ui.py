# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pass.ui'
#
# Created: Sat Oct 13 15:48:59 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

import sys
import six

try:
  from PySide import QtCore, QtGui
except:
    try:
        from PyQt4 import QtCore, QtGui
    except:
        six.print_(("Error: can't load PySide or PyQT"), file=sys.stderr, end="\n", sep=" ")
        sys.exit()


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Pass(object):
    def setupUi(self, Pass):
        Pass.setObjectName(_fromUtf8("Pass"))
        Pass.resize(361, 313)
        self.gridLayout = QtGui.QGridLayout(Pass)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelUser = QtGui.QLabel(Pass)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelUser.sizePolicy().hasHeightForWidth())
        self.labelUser.setSizePolicy(sizePolicy)
        self.labelUser.setObjectName(_fromUtf8("labelUser"))
        self.verticalLayout.addWidget(self.labelUser)
        self.lineEditUser = QtGui.QLineEdit(Pass)
        self.lineEditUser.setObjectName(_fromUtf8("lineEditUser"))
        self.verticalLayout.addWidget(self.lineEditUser)
        self.labelURL = QtGui.QLabel(Pass)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelURL.sizePolicy().hasHeightForWidth())
        self.labelURL.setSizePolicy(sizePolicy)
        self.labelURL.setObjectName(_fromUtf8("labelURL"))
        self.verticalLayout.addWidget(self.labelURL)
        self.lineEditURL = QtGui.QLineEdit(Pass)
        self.lineEditURL.setObjectName(_fromUtf8("lineEditURL"))
        self.verticalLayout.addWidget(self.lineEditURL)
        self.labelPass = QtGui.QLabel(Pass)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelPass.sizePolicy().hasHeightForWidth())
        self.labelPass.setSizePolicy(sizePolicy)
        self.labelPass.setObjectName(_fromUtf8("labelPass"))
        self.verticalLayout.addWidget(self.labelPass)
        self.lineEditPass = QtGui.QLineEdit(Pass)
        self.lineEditPass.setObjectName(_fromUtf8("lineEditPass"))
        self.verticalLayout.addWidget(self.lineEditPass)
        self.pushButton = QtGui.QPushButton(Pass)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        spacerItem = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.lineEditGive = QtGui.QLineEdit(Pass)
        self.lineEditGive.setObjectName(_fromUtf8("lineEditGive"))
        self.verticalLayout.addWidget(self.lineEditGive)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(Pass)
        QtCore.QMetaObject.connectSlotsByName(Pass)

    def retranslateUi(self, Pass):
        Pass.setWindowTitle(QtGui.QApplication.translate("Pass", "Pass", None, QtGui.QApplication.UnicodeUTF8))
        self.labelUser.setText(QtGui.QApplication.translate("Pass", "User:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelURL.setText(QtGui.QApplication.translate("Pass", "Url:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPass.setText(QtGui.QApplication.translate("Pass", "Pass:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Pass", "Give It!", None, QtGui.QApplication.UnicodeUTF8))

