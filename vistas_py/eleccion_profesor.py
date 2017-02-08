# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eleccion_profesor.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_eleccion_profesor(object):
    def setupUi(self, eleccion_profesor):
        eleccion_profesor.setObjectName("eleccion_profesor")
        eleccion_profesor.resize(492, 261)
        self.elegirbtn = QtWidgets.QPushButton(eleccion_profesor)
        self.elegirbtn.setGeometry(QtCore.QRect(180, 220, 99, 27))
        self.elegirbtn.setObjectName("elegirbtn")
        self.disculpasLb = QtWidgets.QLabel(eleccion_profesor)
        self.disculpasLb.setGeometry(QtCore.QRect(20, 16, 361, 31))
        self.disculpasLb.setObjectName("disculpasLb")
        self.groupBox = QtWidgets.QGroupBox(eleccion_profesor)
        self.groupBox.setGeometry(QtCore.QRect(30, 60, 431, 151))
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.celiaBtn = QtWidgets.QRadioButton(self.groupBox)
        self.celiaBtn.setGeometry(QtCore.QRect(0, 30, 150, 22))
        self.celiaBtn.setObjectName("celiaBtn")
        self.diegoFBtn = QtWidgets.QRadioButton(self.groupBox)
        self.diegoFBtn.setGeometry(QtCore.QRect(120, 30, 149, 22))
        self.diegoFBtn.setObjectName("diegoFBtn")
        self.diegoVHBtn = QtWidgets.QRadioButton(self.groupBox)
        self.diegoVHBtn.setGeometry(QtCore.QRect(260, 30, 160, 22))
        self.diegoVHBtn.setObjectName("diegoVHBtn")
        self.gloriaBtn = QtWidgets.QRadioButton(self.groupBox)
        self.gloriaBtn.setGeometry(QtCore.QRect(0, 60, 150, 22))
        self.gloriaBtn.setObjectName("gloriaBtn")
        self.martaBtn = QtWidgets.QRadioButton(self.groupBox)
        self.martaBtn.setGeometry(QtCore.QRect(0, 90, 150, 22))
        self.martaBtn.setObjectName("martaBtn")
        self.nahuelBtn = QtWidgets.QRadioButton(self.groupBox)
        self.nahuelBtn.setGeometry(QtCore.QRect(120, 90, 149, 22))
        self.nahuelBtn.setObjectName("nahuelBtn")
        self.ricardoBtn = QtWidgets.QRadioButton(self.groupBox)
        self.ricardoBtn.setGeometry(QtCore.QRect(260, 90, 160, 22))
        self.ricardoBtn.setObjectName("ricardoBtn")
        self.marcelosBtn = QtWidgets.QRadioButton(self.groupBox)
        self.marcelosBtn.setGeometry(QtCore.QRect(260, 60, 160, 22))
        self.marcelosBtn.setObjectName("marcelosBtn")
        self.marceloGBtn = QtWidgets.QRadioButton(self.groupBox)
        self.marceloGBtn.setGeometry(QtCore.QRect(120, 60, 232, 22))
        self.marceloGBtn.setObjectName("marceloGBtn")
        self.sebastianBtn = QtWidgets.QRadioButton(self.groupBox)
        self.sebastianBtn.setGeometry(QtCore.QRect(120, 120, 471, 22))
        self.sebastianBtn.setObjectName("sebastianBtn")

        self.retranslateUi(eleccion_profesor)
        QtCore.QMetaObject.connectSlotsByName(eleccion_profesor)

    def retranslateUi(self, eleccion_profesor):
        _translate = QtCore.QCoreApplication.translate
        eleccion_profesor.setWindowTitle(_translate("eleccion_profesor", "Elegir Profesor"))
        self.elegirbtn.setText(_translate("eleccion_profesor", "Elegir"))
        self.disculpasLb.setText(_translate("eleccion_profesor", "<html><head/><body><p>¡Lo Sentimos! ¿En qué profesor estabas pensando?</p></body></html>"))
        self.groupBox.setTitle(_translate("eleccion_profesor", "Profesores"))
        self.celiaBtn.setText(_translate("eleccion_profesor", "Celia Cintas"))
        self.diegoFBtn.setText(_translate("eleccion_profesor", "Diego Firmenich"))
        self.diegoVHBtn.setText(_translate("eleccion_profesor", "Diego Van Haaster"))
        self.gloriaBtn.setText(_translate("eleccion_profesor", "Gloria Bianchi"))
        self.martaBtn.setText(_translate("eleccion_profesor", "Marta Saenz"))
        self.nahuelBtn.setText(_translate("eleccion_profesor", "Nahuel Defosse"))
        self.ricardoBtn.setText(_translate("eleccion_profesor", "Ricardo Lopez"))
        self.marcelosBtn.setText(_translate("eleccion_profesor", "Marcelo Santander"))
        self.marceloGBtn.setText(_translate("eleccion_profesor", "Marcelo Gomez"))
        self.sebastianBtn.setText(_translate("eleccion_profesor", "Sebastian Schanz"))

