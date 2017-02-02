from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from vistas_py.menu_principal import Ui_menu_principal
from controladores.controlador_eleccion_profesores import ControladorEleccionProfesor
from controladores.preguntas import dame_pregunta , respuesta, dame_nombre_profesor

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
              ">Ricardo Lopez</p><p align=\"center\">Sebastian Schanz</p><p align=\"center\"><br/></p></body></html>"
        self.menu_principal.preguntasLb.setText(str)
        path = "imagenes/ball.jpg"
        myPixmap = QPixmap(path)
        self.menu_principal.fotoLb.setPixmap(myPixmap)
        self.menu_principal.comenzarBtn.clicked.connect(self.comenzar)

    def comenzar(self):
        self.menu_principal.sipreguntaBtn.setVisible(True)
        self.menu_principal.nopreguntaBtn.setVisible(True)
        self.menu_principal.comenzarBtn.setVisible(False)
        pregunta = dame_pregunta()
        self.menu_principal.preguntasLb.setText(pregunta)
        self.menu_principal.sipreguntaBtn.clicked.connect(self.respuesta_afirmativa)
        self.menu_principal.nopreguntaBtn.clicked.connect(self.respuesta_negativa)

    def respuesta_afirmativa(self):
        respuesta(1,self.menu_principal.preguntasLb.text())
        self.proxima_pregunta()

    def respuesta_negativa(self):
        respuesta(0,self.menu_principal.preguntasLb.text())
        self.proxima_pregunta()

    def proxima_pregunta(self):
        pregunta = dame_pregunta()
        if pregunta == None:
            myPixmap = QPixmap("imagenes/fin.png")
            self.menu_principal.preguntasLb.setPixmap(myPixmap)
            self.menu_principal.sipreguntaBtn.setDisabled(True)
            self.menu_principal.nopreguntaBtn.setDisabled(True)
            nombre_profesor = dame_nombre_profesor()
            self.menu_principal.fotoLb.setText(nombre_profesor)
            print(nombre_profesor)
        else:
            self.menu_principal.preguntasLb.setText(pregunta)


"""
    def ranking(self):
        ventana = ControladorRanking()
        ventana.exec_()

    def empezar(self):
        self.facemash.empezarBtn.setDisabled(True)
        profesorA, profesorB = dame_competidores()
        path = str("imagenes/" + profesorA.foto)
        myPixmap = QPixmap(path)
        self.facemash.foto1Lb.setPixmap(myPixmap)
        path = str("imagenes/" + profesorB.foto)
        myPixmap2 = QPixmap(path)
        self.facemash.foto2Lb.setPixmap(myPixmap2)
        #CARGA DE BANDERAS EN LA INTERFAZ
        self.facemash.id1Lb.setVisible(False)
        self.facemash.id2Lb.setVisible(False)
        self.facemash.id1Lb.setText(str(profesorA.id))
        self.facemash.id2Lb.setText(str(profesorB.id))

    def gano_uno(self):
        ganador = int(self.facemash.id1Lb.text())
        perdedor = int(self.facemash.id2Lb.text())
        self.rankear(ganador, perdedor)

    def gano_dos(self):
        ganador = int(self.facemash.id2Lb.text())
        perdedor = int(self.facemash.id1Lb.text())
        self.rankear(ganador, perdedor)

    def rankear(self, ganador_id, perdedor_id):
        guardar_ganador(ganador_id, perdedor_id)
        profesorA, profesorB = dame_competidores()
        if profesorB == None:
            myPixmap = QPixmap("imagenes/fin.png")
            self.facemash.foto1Lb.setPixmap(myPixmap)
            myPixmap2 = QPixmap("imagenes/gracias.png")
            self.facemash.foto2Lb.setPixmap(myPixmap2)
            self.facemash.empezarBtn.setDisabled(False)
            self.facemash.voto1Btn.setDisabled(True)
            self.facemash.voto2btn.setDisabled(True)
        else:
            path = str("imagenes/" + profesorA.foto)
            myPixmap = QPixmap(path)
            self.facemash.foto1Lb.setPixmap(myPixmap)
            path = str("imagenes/" + profesorB.foto)
            myPixmap2 = QPixmap(path)
            self.facemash.foto2Lb.setPixmap(myPixmap2)
            # CARGA DE BANDERAS EN LA INTERFAZ
            self.facemash.id1Lb.setVisible(False)
            self.facemash.id2Lb.setVisible(False)
            self.facemash.id1Lb.setText(str(profesorA.id))
            self.facemash.id2Lb.setText(str(profesorB.id)) """