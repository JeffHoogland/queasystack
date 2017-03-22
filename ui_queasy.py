# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'queasy.ui'
#
# Created: Wed Mar 22 10:24:36 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.deckNameEntry = QtGui.QLineEdit(self.centralwidget)
        self.deckNameEntry.setObjectName("deckNameEntry")
        self.verticalLayout.addWidget(self.deckNameEntry)
        self.deckListEntry = QtGui.QPlainTextEdit(self.centralwidget)
        self.deckListEntry.setObjectName("deckListEntry")
        self.verticalLayout.addWidget(self.deckListEntry)
        self.generateImage = QtGui.QPushButton(self.centralwidget)
        self.generateImage.setObjectName("generateImage")
        self.verticalLayout.addWidget(self.generateImage)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Queasy Stack", None, QtGui.QApplication.UnicodeUTF8))
        self.generateImage.setText(QtGui.QApplication.translate("MainWindow", "Generate Image", None, QtGui.QApplication.UnicodeUTF8))

