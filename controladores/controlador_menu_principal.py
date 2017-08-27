from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from vistas_py.menu_principal import Ui_menu_principal
from .controlador_eleccion_profesores import ControladorEleccionProfesor
from .adivinador import Adivinador
from modelo.bosque import Bosque
import os

class ControladorMenuPrincipal(QMainWindow):
    def __init__(self):
        super(ControladorMenuPrincipal, self).__init__()
        self.menu_principal = Ui_menu_principal()
        self.menu_principal.setupUi(self)
        self.menu_principal.sipreguntaBtn.setVisible(False)
        self.menu_principal.nopreguntaBtn.setVisible(False)
        self.menu_principal.siprofesorBtn.setVisible(False)
        self.menu_principal.noprofesorBtn.setVisible(False)
        str = "<html><head/><body><b><p align=\"center\">Bienvenido Al Adivinador de Profesores!</p><p align=\"center\">Mi tarea es adivinar el profesor</p><p align=\"center\">que usted está pensando</p><p align=\"center\">Las opciones son:</p><p align=\"center\">Celia Cintas </p><p align=\"center\">" \
              "Diego Firmenich</p><p align=\"center\">Diego Van Haaster</p><p align=\"center\">Gloria Bianchi</p><p align=\"center\">Marcelo Gomez</p><p align=\"center\">Marcelo Santander</p><p align=\"center\">Marta Sanz</p><p align=\"center\">Nahuel Defossé</p><p align=\"center\"" \
              ">Ricardo López</p><p align=\"center\">Sebastian Schanz</p><p align=\"center\"></b><br/></p></body></html>"
        self.menu_principal.preguntasLb.setText(str)
        path = os.path.abspath("controladores/imagenes/DIT.png")
        myPixmap = QPixmap(path)
        self.menu_principal.fotoLb.setPixmap(myPixmap)
        self.bosque = Bosque()
        self.bosque = self.bosque.entrenar()
        self.menu_principal.comenzarBtn.clicked.connect(self.comenzar)

    def comenzar(self):
        path = os.path.abspath("controladores/imagenes/adivinador.png")
        myPixmap = QPixmap(path)
        self.menu_principal.fotoLb.setPixmap(myPixmap)
        self.menu_principal.sipreguntaBtn.setVisible(True)
        self.menu_principal.nopreguntaBtn.setVisible(True)
        self.menu_principal.comenzarBtn.setVisible(False)
        self.adivinador = Adivinador()
        pregunta = self.adivinador.dame_pregunta(self.bosque)
        self.menu_principal.preguntasLb.setText("<html><head/><body><b><p align=\"center\"><H1> {} </H1></p></b><br/></p></body></html>".format(pregunta))
        self.menu_principal.sipreguntaBtn.clicked.connect(self.respuesta_afirmativa)
        self.menu_principal.nopreguntaBtn.clicked.connect(self.respuesta_negativa)
        self.menu_principal.siprofesorBtn.clicked.connect(self.acertaste)
        self.menu_principal.noprofesorBtn.clicked.connect(self.aprender)

    def respuesta_afirmativa(self):
        self.adivinador.respuesta(1,self.menu_principal.preguntasLb.text(), self.bosque)
        self.proxima_pregunta()

    def respuesta_negativa(self):
        self.adivinador.respuesta(0,self.menu_principal.preguntasLb.text(),self.bosque)
        self.proxima_pregunta()

    def proxima_pregunta(self):
        pregunta = self.adivinador.dame_pregunta(self.bosque)
        if pregunta == None:
            self.menu_principal.sipreguntaBtn.setVisible(False)
            self.menu_principal.nopreguntaBtn.setVisible(False)
            self.menu_principal.siprofesorBtn.setVisible(True)
            self.menu_principal.noprofesorBtn.setVisible(True)
            path = os.path.abspath("controladores/imagenes/Tu profesor es.png")
            myPixmap = QPixmap(path)
            self.menu_principal.preguntasLb.setPixmap(myPixmap)
            nombre_profesor = self.adivinador.dame_nombre_profesor(self.bosque)
            self.menu_principal.fotoLb.setText("<html><head/><body><b><p align=\"center\"><H1>¿Pensaste en {}? </H1></p></b><br/></p></body></html>".format(nombre_profesor))
        else:
            self.menu_principal.preguntasLb.setText("<html><head/><body><b><p align=\"center\"><H1> {} </H1></p></b><br/></p></body></html>".format(pregunta))


    def acertaste(self):
        #falta guardar el profe y la muestra
        path = os.path.abspath("controladores/imagenes/gane.png")
        myPixmap = QPixmap(path)
        self.menu_principal.preguntasLb.setPixmap(myPixmap)
        self.menu_principal.fotoLb.setText(
            "<html><head/><body><b><p align=\"center\"><H1> ¡Gané! Gracias por Jugar </H1></p></b><br/></p></body></html>")
        self.menu_principal.siprofesorBtn.setVisible(False)
        self.menu_principal.noprofesorBtn.setVisible(False)

    def aprender(self):
        ventana = ControladorEleccionProfesor(self.adivinador.profesor_incognito)
        ventana.exec_()
