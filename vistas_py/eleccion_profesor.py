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
        eleccion_profesor.resize(429, 289)
        eleccion_profesor.setFocusPolicy(QtCore.Qt.NoFocus)
        eleccion_profesor.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.elegirbtn = QtWidgets.QPushButton(eleccion_profesor)
        self.elegirbtn.setGeometry(QtCore.QRect(310, 240, 99, 27))
        self.elegirbtn.setObjectName("elegirbtn")
        self.disculpasLb = QtWidgets.QLabel(eleccion_profesor)
        self.disculpasLb.setGeometry(QtCore.QRect(20, 16, 391, 31))
        self.disculpasLb.setObjectName("disculpasLb")
        self.groupBox = QtWidgets.QGroupBox(eleccion_profesor)
        self.groupBox.setGeometry(QtCore.QRect(50, 50, 341, 181))
        self.groupBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setObjectName("groupBox")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 30, 321, 136))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.celiaBtn = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.celiaBtn.setObjectName("celiaBtn")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.celiaBtn)
        self.gloriaBtn = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.gloriaBtn.setObjectName("gloriaBtn")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.gloriaBtn)
        self.diegoFBtn = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.diegoFBtn.setObjectName("diegoFBtn")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.diegoFBtn)
        self.marceloGBtn = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.marceloGBtn.setObjectName("marceloGBtn")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.marceloGBtn)
        self.martaBtn = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.martaBtn.setObjectName("martaBtn")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.martaBtn)
        self.nahuelBtn = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.nahuelBtn.setObjectName("nahuelBtn")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.nahuelBtn)
        self.marcelosBtn = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.marcelosBtn.setObjectName("marcelosBtn")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.marcelosBtn)
        self.sebastianBtn = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.sebastianBtn.setObjectName("sebastianBtn")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.sebastianBtn)
        self.diegoVHBtn = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.diegoVHBtn.setObjectName("diegoVHBtn")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.diegoVHBtn)
        self.ricardoBtn = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.ricardoBtn.setObjectName("ricardoBtn")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.ricardoBtn)

        self.retranslateUi(eleccion_profesor)
        QtCore.QMetaObject.connectSlotsByName(eleccion_profesor)

    def retranslateUi(self, eleccion_profesor):
        _translate = QtCore.QCoreApplication.translate
        eleccion_profesor.setWindowTitle(_translate("eleccion_profesor", "Elegir Profesor"))
        self.elegirbtn.setText(_translate("eleccion_profesor", "Elegir"))
        self.disculpasLb.setText(_translate("eleccion_profesor", "<html><head/><body><p><span style=\" font-weight:600;\">¡Lo Sentimos! ¿En qué profesor estabas pensando?</span></p></body></html>"))
        self.groupBox.setTitle(_translate("eleccion_profesor", "Profesores"))
        self.celiaBtn.setText(_translate("eleccion_profesor", "Celia Cintas"))
        self.gloriaBtn.setText(_translate("eleccion_profesor", "Gloria Bianchi"))
        self.diegoFBtn.setText(_translate("eleccion_profesor", "Diego Firmenich"))
        self.marceloGBtn.setText(_translate("eleccion_profesor", "Marcelo Gomez"))
        self.martaBtn.setText(_translate("eleccion_profesor", "Marta Saenz"))
        self.nahuelBtn.setText(_translate("eleccion_profesor", "Nahuel Defosse"))
        self.marcelosBtn.setText(_translate("eleccion_profesor", "Marcelo Santander"))
        self.sebastianBtn.setText(_translate("eleccion_profesor", "Sebastian Schanz"))
        self.diegoVHBtn.setText(_translate("eleccion_profesor", "Diego Van Haaster"))
        self.ricardoBtn.setText(_translate("eleccion_profesor", "Ricardo Lopez"))

