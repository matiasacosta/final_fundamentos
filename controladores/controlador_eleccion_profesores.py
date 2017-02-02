from PyQt5.QtWidgets import QDialog
from vistas_py.eleccion_profesor import Ui_eleccion_profesor

class ControladorEleccionProfesor(QDialog):

    def __init__(self):
        super(ControladorEleccionProfesor, self).__init__()
        self.eleccion_profesor = Ui_eleccion_profesor()
        self.eleccion_profesor.setupUi(self)
