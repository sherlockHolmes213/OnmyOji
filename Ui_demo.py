# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'f:\python\Onmyoji\demo.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import configData
import init
import ctypes
import sys

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(486, 379)
        self.wareTypeTitle = QtWidgets.QLabel(Dialog)
        self.wareTypeTitle.setGeometry(QtCore.QRect(110, 60, 51, 21))
        self.wareTypeTitle.setObjectName("wareTypeTitle")
        self.wareTimeTitle = QtWidgets.QLabel(Dialog)
        self.wareTimeTitle.setGeometry(QtCore.QRect(110, 100, 51, 21))
        self.wareTimeTitle.setObjectName("wareTimeTitle")
        self.wareTime = QtWidgets.QComboBox(Dialog)
        self.wareTime.setGeometry(QtCore.QRect(200, 100, 69, 22))
        self.wareTime.setObjectName("wareTime")
        self.wareTime.addItem("")
        self.wareTime.addItem("")
        self.wareTime.addItem("")
        self.isTeam = QtWidgets.QComboBox(Dialog)
        self.isTeam.setEnabled(True)
        self.isTeam.setGeometry(QtCore.QRect(200, 140, 69, 22))
        self.isTeam.setObjectName("isTeam")
        self.isTeam.addItem("")
        self.isTeam.addItem("")
        self.isTeamTitle = QtWidgets.QLabel(Dialog)
        self.isTeamTitle.setEnabled(True)
        self.isTeamTitle.setGeometry(QtCore.QRect(110, 140, 54, 21))
        self.isTeamTitle.setObjectName("isTeamTitle")
        self.roleTitle = QtWidgets.QLabel(Dialog)
        self.roleTitle.setGeometry(QtCore.QRect(110, 180, 51, 21))
        self.roleTitle.setObjectName("roleTitle")
        self.role = QtWidgets.QComboBox(Dialog)
        self.role.setEnabled(True)
        self.role.setGeometry(QtCore.QRect(200, 180, 69, 22))
        self.role.setObjectName("role")
        self.role.addItem("")
        self.role.addItem("")
        self.runButton = QtWidgets.QPushButton(Dialog)
        self.runButton.setGeometry(QtCore.QRect(110, 230, 75, 23))
        self.runButton.setObjectName("runButton")
        self.exitButton = QtWidgets.QPushButton(Dialog)
        self.exitButton.setGeometry(QtCore.QRect(200, 230, 75, 23))
        self.exitButton.setObjectName("exitButton")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(190, 30, 191, 51))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.yhRadio = QtWidgets.QRadioButton(self.groupBox)
        self.yhRadio.setChecked(True)
        self.yhRadio.setGeometry(QtCore.QRect(0, 30, 41, 21))
        self.yhRadio.setObjectName("yhRadio")
        self.ylRadio = QtWidgets.QRadioButton(self.groupBox)
        self.ylRadio.setGeometry(QtCore.QRect(50, 30, 41, 21))
        self.ylRadio.setObjectName("ylRadio")
        self.yyhRadio = QtWidgets.QRadioButton(self.groupBox)
        self.yyhRadio.setGeometry(QtCore.QRect(100, 30, 91, 21))
        self.yyhRadio.setObjectName("yyhRadio")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.wareTypeTitle.setText(_translate("Dialog", "战斗类型"))
        self.wareTimeTitle.setText(_translate("Dialog", "战斗时间"))
        self.wareTime.setItemText(0, _translate("Dialog", "19秒"))
        self.wareTime.setItemText(1, _translate("Dialog", "30秒"))
        self.wareTime.setItemText(2, _translate("Dialog", "60秒"))
        self.isTeam.setItemText(0, _translate("Dialog", "单人"))
        self.isTeam.setItemText(1, _translate("Dialog", "组队"))
        self.isTeamTitle.setText(_translate("Dialog", "是否组队"))
        self.roleTitle.setText(_translate("Dialog", "身   份"))
        self.role.setItemText(0, _translate("Dialog", "队长"))
        self.role.setItemText(1, _translate("Dialog", "队员"))
        self.runButton.setText(_translate("Dialog", "运行"))
        self.runButton.clicked.connect(self.exeStart)
        self.exitButton.setText(_translate("Dialog", "停止"))
        self.exitButton.clicked.connect(self.exeExit)
        self.yhRadio.setText(_translate("Dialog", "御魂"))
        self.ylRadio.setText(_translate("Dialog", "御灵"))
        self.yyhRadio.setText(_translate("Dialog", "业原火"))
    def exeStart(self, Dialog):
        init.window_capture("a.png")
    def exeExit(self, Dialog):
        exit()
