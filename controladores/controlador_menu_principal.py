from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from vistas_py.menu_principal import Ui_menu_principal
from controladores.controlador_eleccion_profesores import ControladorEleccionProfesor
from controladores.adivinador import Adivinador
from modelo.arbol import Arbol

class ControladorMenuPrincipal(QMainWindow):
    def __init__(self):
        super(ControladorMenuPrincipal, self).__init__()
        self.menu_principal = Ui_menu_principal()
        self.menu_principal.setupUi(self)
        self.menu_principal.sipreguntaBtn.setVisible(False)
        self.menu_principal.nopreguntaBtn.setVisible(False)
        self.menu_principal.siprofesorBtn.setVisible(False)
        self.menu_principal.noprofesorBtn.setVisible(False)
        str = "<html><head/><body><p align=\"center\">Bienvenido Al Adivinador de Profesores!</p><p align=\"center\">Mi tarea es adivinar el profesor que usted está pensando</p><p align=\"center\">Las opciones son:</p><p align=\"center\">Celia Cintas </p><p align=\"center\">" \
              "Diego Firmenich</p><p align=\"center\">Diego Van Haaster</p><p align=\"center\">Gloria Bianchi</p><p align=\"center\">Marcelo Gomez</p><p align=\"center\">Marcelo Santander</p><p align=\"center\">Marta Sanz</p><p align=\"center\">Nahuel Defossé</p><p align=\"center\"" \
              ">Ricardo López</p><p align=\"center\">Sebastian Schanz</p><p align=\"center\"><br/></p></body></html>"
        self.menu_principal.preguntasLb.setText(str)
        path = "imagenes/DIT.png"
        myPixmap = QPixmap(path)
        self.menu_principal.fotoLb.setPixmap(myPixmap)
        self.arbol = Arbol()
        self.arbol = self.arbol.entrenar()
        self.menu_principal.comenzarBtn.clicked.connect(self.comenzar)
        self.menu_principal.action_arbol_de_Profesores.triggered.connect(self.arbol_de_profesores)

    def comenzar(self):
        path = "imagenes/adivinador.png"
        myPixmap = QPixmap(path)
        self.menu_principal.fotoLb.setPixmap(myPixmap)
        self.menu_principal.sipreguntaBtn.setVisible(True)
        self.menu_principal.nopreguntaBtn.setVisible(True)
        self.menu_principal.comenzarBtn.setVisible(False)
        self.adivinador = Adivinador()
        pregunta = self.adivinador.dame_pregunta(self.arbol)
        self.menu_principal.preguntasLb.setText(pregunta)
        self.menu_principal.sipreguntaBtn.clicked.connect(self.respuesta_afirmativa)
        self.menu_principal.nopreguntaBtn.clicked.connect(self.respuesta_negativa)
        self.menu_principal.siprofesorBtn.clicked.connect(self.acertaste)
        self.menu_principal.noprofesorBtn.clicked.connect(self.aprender)

    def respuesta_afirmativa(self):
        self.adivinador.respuesta(1,self.menu_principal.preguntasLb.text(), self.arbol)
        self.proxima_pregunta()

    def respuesta_negativa(self):
        self.adivinador.respuesta(0,self.menu_principal.preguntasLb.text(),self.arbol)
        self.proxima_pregunta()

    def proxima_pregunta(self):
        pregunta = self.adivinador.dame_pregunta(self.arbol)
        if pregunta == None:
            self.menu_principal.sipreguntaBtn.setVisible(False)
            self.menu_principal.nopreguntaBtn.setVisible(False)
            self.menu_principal.siprofesorBtn.setVisible(True)
            self.menu_principal.noprofesorBtn.setVisible(True)
            myPixmap = QPixmap("imagenes/Tu profesor es.png")
            self.menu_principal.preguntasLb.setPixmap(myPixmap)
            nombre_profesor = self.adivinador.dame_nombre_profesor(self.arbol)
            path = "imagenes/"+nombre_profesor+".png"
            myPixmap = QPixmap(path)
            self.menu_principal.fotoLb.setPixmap(myPixmap)
        else:
            self.menu_principal.preguntasLb.setText(pregunta)

    def arbol_de_profesores(self):
        self.arbol.dibujar_arbol()

    def acertaste(self):
        myPixmap = QPixmap("imagenes/gane.png")
        self.menu_principal.preguntasLb.setPixmap(myPixmap)
        myPixmap = QPixmap("imagenes/gracias.png")
        self.menu_principal.fotoLb.setPixmap(myPixmap)
        self.menu_principal.siprofesorBtn.setVisible(False)
        self.menu_principal.noprofesorBtn.setVisible(False)
        #self.menu_principal.comenzarBtn.setVisible(True)

    def aprender(self):
        ventana = ControladorEleccionProfesor(self.adivinador.profesor_incognito)
        ventana.exec_()