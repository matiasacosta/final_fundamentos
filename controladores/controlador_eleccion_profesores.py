from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QRadioButton
from vistas_py.eleccion_profesor import Ui_eleccion_profesor


class ControladorEleccionProfesor(QDialog):

    def __init__(self, profesor):
        super(ControladorEleccionProfesor, self).__init__()
        self.eleccion_profesor = Ui_eleccion_profesor()
        self.eleccion_profesor.setupUi(self)
        self.profesor_incognito = profesor

        self.eleccion_profesor.elegirbtn.clicked.connect(self.guardar_profesor)

    def guardar_profesor(self):
        profesor = None
        for boton in self.eleccion_profesor.groupBox.findChildren(QRadioButton):
            if boton.isChecked():
                profesor = boton.text()

        if profesor == None:
            self.eleccion_profesor.disculpasLb.setText(" < html > < head / > < body > < p > < span style = \" font-weight:600;\" > POR FAVOR ELIJA ALGUNO DE LOS PROFESORES < / span > < / p > < / body > < / html >")
        else:
            with open('muestras.txt', 'a') as f:
                f.write("{} {} {} {} {} {} {}\n".format(
                    self.profesor_incognito.pelo, self.profesor_incognito.sexo, self.profesor_incognito.año,
                    self.profesor_incognito.estatura, self.profesor_incognito.cargo, self.profesor_incognito.materia,
                    self.profesor_incognito.cuatrimestre))
                f.close()
            with open('profesores.txt', 'a') as f:
                f.write("{}\n".format(profesor))
                f.close()
            self.close()