# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("RedditNews")
        MainWindow.resize(1800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 451, 121))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(200, 110, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.NewsTable = QtWidgets.QTableWidget(self.centralwidget)
        self.NewsTable.setGeometry(QtCore.QRect(10, 160, 1551, 421))
        self.NewsTable.setObjectName("NewsTable")
        self.NewsTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("RedditNews", "RedditNews"))
        MainWindow.setWindowTitle(_translate("RedditNews", "RedditNews"))
        self.label.setText(_translate("MainWindow", "Breaking news!"))
        self.comboBox.setCurrentText(_translate("MainWindow", "Today"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Today"))
        self.comboBox.setItemText(1, _translate("MainWindow", "This week"))
        self.comboBox.setItemText(2, _translate("MainWindow", "This month"))
        self.comboBox.setItemText(3, _translate("MainWindow", "This year"))
        self.label_2.setText(_translate("MainWindow", "Top news of"))
