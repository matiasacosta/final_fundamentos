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
        eleccion_profesor.resize(492, 300)
        self.elegirbtn = QtWidgets.QPushButton(eleccion_profesor)
        self.elegirbtn.setGeometry(QtCore.QRect(200, 260, 99, 27))
        self.elegirbtn.setObjectName("elegirbtn")
        self.gridLayoutWidget = QtWidgets.QWidget(eleccion_profesor)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 60, 473, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.martaBtn = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.martaBtn.setObjectName("martaBtn")
        self.gridLayout.addWidget(self.martaBtn, 2, 0, 1, 1)
        self.gloriaBtn = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.gloriaBtn.setObjectName("gloriaBtn")
        self.gridLayout.addWidget(self.gloriaBtn, 1, 0, 1, 1)
        self.ricardoBtn = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.ricardoBtn.setObjectName("ricardoBtn")
        self.gridLayout.addWidget(self.ricardoBtn, 2, 2, 1, 1)
        self.celiaBtn = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.celiaBtn.setObjectName("celiaBtn")
        self.gridLayout.addWidget(self.celiaBtn, 0, 0, 1, 1)
        self.diegoFBtn = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.diegoFBtn.setObjectName("diegoFBtn")
        self.gridLayout.addWidget(self.diegoFBtn, 0, 1, 1, 1)
        self.marceloGBtn = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.marceloGBtn.setObjectName("marceloGBtn")
        self.gridLayout.addWidget(self.marceloGBtn, 1, 1, 1, 1)
        self.marcelosBtn = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.marcelosBtn.setObjectName("marcelosBtn")
        self.gridLayout.addWidget(self.marcelosBtn, 1, 2, 1, 1)
        self.diegoVHBtn = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.diegoVHBtn.setObjectName("diegoVHBtn")
        self.gridLayout.addWidget(self.diegoVHBtn, 0, 2, 1, 1)
        self.nahuelBtn = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.nahuelBtn.setObjectName("nahuelBtn")
        self.gridLayout.addWidget(self.nahuelBtn, 2, 1, 1, 1)
        self.sebastianBtn = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.sebastianBtn.setObjectName("sebastianBtn")
        self.gridLayout.addWidget(self.sebastianBtn, 3, 0, 1, 1)
        self.disculpasLb = QtWidgets.QLabel(eleccion_profesor)
        self.disculpasLb.setGeometry(QtCore.QRect(20, 16, 361, 31))
        self.disculpasLb.setObjectName("disculpasLb")

        self.retranslateUi(eleccion_profesor)
        QtCore.QMetaObject.connectSlotsByName(eleccion_profesor)

    def retranslateUi(self, eleccion_profesor):
        _translate = QtCore.QCoreApplication.translate
        eleccion_profesor.setWindowTitle(_translate("eleccion_profesor", "Elegir Profesor"))
        self.elegirbtn.setText(_translate("eleccion_profesor", "Elegir"))
        self.martaBtn.setText(_translate("eleccion_profesor", "Marta Sanz"))
        self.gloriaBtn.setText(_translate("eleccion_profesor", "Gloria Bianchi"))
        self.ricardoBtn.setText(_translate("eleccion_profesor", "Ricardo Lopez"))
        self.celiaBtn.setText(_translate("eleccion_profesor", "Celia Cintas"))
        self.diegoFBtn.setText(_translate("eleccion_profesor", "Diego Firmenich"))
        self.marceloGBtn.setText(_translate("eleccion_profesor", "Marcelo Gomez"))
        self.marcelosBtn.setText(_translate("eleccion_profesor", "Marcelo Santander"))
        self.diegoVHBtn.setText(_translate("eleccion_profesor", "Diego Van Haaster"))
        self.nahuelBtn.setText(_translate("eleccion_profesor", "Nahuel Defossé"))
        self.sebastianBtn.setText(_translate("eleccion_profesor", "Sebastian Schanz"))
        self.disculpasLb.setText(_translate("eleccion_profesor", "<html><head/><body><p>¡Lo Sentimos! ¿En qué profesor estabas pensando?</p></body></html>"))

