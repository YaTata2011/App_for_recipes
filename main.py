# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt5 import QtCore, QtGui, QtWidgets

import os
from PyQt5.QtWidgets import (
   QApplication, QWidget,
   QFileDialog, # Диалог открытия файлов (и папок)
   QLabel, QPushButton, QListWidget,
   QHBoxLayout, QVBoxLayout
)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Малюнки")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_text = QtWidgets.QLabel(self.centralwidget)
        self.label_text.setGeometry(QtCore.QRect(380, 80, 331, 341))
        self.label_text.setObjectName("label_text")
        self.listWidget_files = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_files.setGeometry(QtCore.QRect(30, 90, 201, 421))
        self.listWidget_files.setObjectName("listWidget_files")
        self.pushButton_folder = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_folder.setGeometry(QtCore.QRect(40, 30, 191, 41))
        self.pushButton_folder.setStyleSheet("background-color: rgb(255, 214, 62);")
        self.pushButton_folder.setObjectName("pushButton_folder")
        self.btn_bw = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bw.setGeometry(QtCore.QRect(250, 500, 120, 40))
        self.btn_bw.setStyleSheet("background-color: rgb(255, 214, 62);")
        self.btn_bw.setObjectName("pushButton_bw")
        self.btn_left = QtWidgets.QPushButton(self.centralwidget)
        self.btn_left.setGeometry(QtCore.QRect(390, 500, 80, 40))
        self.btn_left.setStyleSheet("background-color: rgb(255, 214, 62);")
        self.btn_left.setObjectName("pushButton_btn_left")
        self.btn_right = QtWidgets.QPushButton(self.centralwidget)
        self.btn_right.setGeometry(QtCore.QRect(480, 500, 80, 40))
        self.btn_right.setStyleSheet("background-color: rgb(255, 214, 62);")
        self.btn_right.setObjectName("pushButton_btn_right")
        self.btn_sharp = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sharp.setGeometry(QtCore.QRect(570, 500, 80, 40))
        self.btn_sharp.setStyleSheet("background-color: rgb(255, 214, 62);")
        self.btn_sharp.setObjectName("pushButton_btn_sharp")
        self.btn_flip = QtWidgets.QPushButton(self.centralwidget)
        self.btn_flip.setGeometry(QtCore.QRect(660, 500, 120, 40))
        self.btn_flip.setStyleSheet("background-color: rgb(255, 214, 62);")
        self.btn_flip.setObjectName("pushButton_flip")
        
        


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Малюнки"))
        self.label_text.setText(_translate("MainWindow", "   Картинка"))
        self.pushButton_folder.setText(_translate("MainWindow", "Папка"))
        self.btn_bw.setText(_translate("MainWindow", "Ч/Б"))
        self.btn_left.setText(_translate("MainWindow", "Ліворуч"))
        self.btn_right.setText(_translate("MainWindow", "Праворуч"))
        self.btn_sharp.setText(_translate("MainWindow", "Різкість"))
        self.btn_flip.setText(_translate("MainWindow", "Відзеркалити"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())