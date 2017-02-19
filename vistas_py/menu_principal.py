# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu_principal.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_menu_principal(object):
    def setupUi(self, menu_principal):
        menu_principal.setObjectName("menu_principal")
        menu_principal.setWindowModality(QtCore.Qt.NonModal)
        menu_principal.resize(800, 600)
        menu_principal.setMinimumSize(QtCore.QSize(800, 600))
        menu_principal.setMaximumSize(QtCore.QSize(800, 600))
        menu_principal.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.centralwidget = QtWidgets.QWidget(menu_principal)
        self.centralwidget.setObjectName("centralwidget")
        self.infoLb = QtWidgets.QLabel(self.centralwidget)
        self.infoLb.setGeometry(QtCore.QRect(210, 430, 411, 131))
        self.infoLb.setTextFormat(QtCore.Qt.RichText)
        self.infoLb.setAlignment(QtCore.Qt.AlignCenter)
        self.infoLb.setObjectName("infoLb")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 761, 371))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.preguntasLb = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.preguntasLb.setText("")
        self.preguntasLb.setTextFormat(QtCore.Qt.RichText)
        self.preguntasLb.setScaledContents(False)
        self.preguntasLb.setAlignment(QtCore.Qt.AlignCenter)
        self.preguntasLb.setWordWrap(True)
        self.preguntasLb.setObjectName("preguntasLb")
        self.horizontalLayout.addWidget(self.preguntasLb)
        self.fotoLb = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.fotoLb.setText("")
        self.fotoLb.setTextFormat(QtCore.Qt.RichText)
        self.fotoLb.setAlignment(QtCore.Qt.AlignCenter)
        self.fotoLb.setObjectName("fotoLb")
        self.horizontalLayout.addWidget(self.fotoLb)
        self.sipreguntaBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sipreguntaBtn.setGeometry(QtCore.QRect(50, 390, 99, 27))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sipreguntaBtn.setFont(font)
        self.sipreguntaBtn.setObjectName("sipreguntaBtn")
        self.nopreguntaBtn = QtWidgets.QPushButton(self.centralwidget)
        self.nopreguntaBtn.setGeometry(QtCore.QRect(190, 390, 99, 27))
        self.nopreguntaBtn.setObjectName("nopreguntaBtn")
        self.siprofesorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.siprofesorBtn.setGeometry(QtCore.QRect(500, 390, 99, 27))
        self.siprofesorBtn.setObjectName("siprofesorBtn")
        self.noprofesorBtn = QtWidgets.QPushButton(self.centralwidget)
        self.noprofesorBtn.setGeometry(QtCore.QRect(630, 390, 99, 27))
        self.noprofesorBtn.setObjectName("noprofesorBtn")
        self.comenzarBtn = QtWidgets.QPushButton(self.centralwidget)
        self.comenzarBtn.setEnabled(True)
        self.comenzarBtn.setGeometry(QtCore.QRect(370, 390, 99, 27))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.comenzarBtn.setFont(font)
        self.comenzarBtn.setObjectName("comenzarBtn")
        menu_principal.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(menu_principal)
        self.statusbar.setObjectName("statusbar")
        menu_principal.setStatusBar(self.statusbar)
        self.action_Que_son = QtWidgets.QAction(menu_principal)
        self.action_Que_son.setObjectName("action_Que_son")
        self.action_arbol_de_Profesores = QtWidgets.QAction(menu_principal)
        self.action_arbol_de_Profesores.setObjectName("action_arbol_de_Profesores")

        self.retranslateUi(menu_principal)
        QtCore.QMetaObject.connectSlotsByName(menu_principal)

    def retranslateUi(self, menu_principal):
        _translate = QtCore.QCoreApplication.translate
        menu_principal.setWindowTitle(_translate("menu_principal", "Adivinador Profesores"))
        self.infoLb.setText(_translate("menu_principal", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-style:italic;\">Materia: Fundamentos Teóricos de Informática</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-style:italic;\">Profesoras: Bianchi, Gloria. Cintas, Celia.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-style:italic;\">Alumnos: Acosta, Matías. Mazzaglia Ian.</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-style:italic;\">Trabajo Final 2017</span></p></body></html>"))
        self.sipreguntaBtn.setText(_translate("menu_principal", "SI"))
        self.nopreguntaBtn.setText(_translate("menu_principal", "NO"))
        self.siprofesorBtn.setText(_translate("menu_principal", "SI"))
        self.noprofesorBtn.setText(_translate("menu_principal", "NO"))
        self.comenzarBtn.setText(_translate("menu_principal", "¡Comenzar!"))
        self.action_Que_son.setText(_translate("menu_principal", "¿Qué son?"))
        self.action_arbol_de_Profesores.setText(_translate("menu_principal", "Árbol de Profesores"))

