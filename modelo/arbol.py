from sklearn import tree
import numpy as np
from sklearn.tree import _tree
import pydotplus

class Arbol(tree.DecisionTreeClassifier):

    def __init__(self):
        super(Arbol, self).__init__(criterion='entropy')
        self.nombres_caracteristicas=['Corte de Pelo','Sexo','Año de Enseñanza','Estatura','Cargo en la Materia','Materia','Cuatrimestre de Clase']
        self.profesores=['Celia Cintas', 'Diego Firmenich', 'Diego Van Haaster', 'Gloria Bianchi', 'Marcelo Gomez',
                         'Marcelo Santander', 'Marta Saenz', 'Nahuel Defosse', 'Ricardo Lopez', 'Sebastian Schanz']
    """FEATURES:
    'primer_cuatri': 1,
    'segundo_cuatri': 2,
    'corto': 0,
    'largo': 1,
    'hombre': 0,
    'mujer': 1,
    'primero': 1,
    'segundo': 2,
    'tercero': 3,
    'cuarto': 4,
    'quinto': 5,
    'bajo': 0,
    'alto': 1,
    'practica': 0,
    'teoria': 1,
    'epa': 0,
    'elementos': 1,
    'algoritmica I': 2,
    'algortmica II': 3,
    'arquitectura': 4,
    'base': 5,
    'concurrencia': 6,
    'laboratorio': 7,
    'sistemas_operativos': 8,
    'ing I': 9,
    'desarrollo': 10,
    'fundamentos': 11,
    'ing II': 12,
    'Redes': 13,
    'paradigmas': 14,
    'seguridad': 15,
    'ing III': 16,
    'distribuidos': 17,
    'administracion': 18,
    'web': 19,
    'taller tecnologias': 20,
    'toma de decisiones': 21
    """
    materias = [
        'Expresión de Problemas y Algorítmos',
        'Elementos de Informática',
        'Algoritmica y Programación I',
        'Algoritmica y Programación II',
        'Arquitectura de las Computadoras',
        'Base de Datos I',
        'Introcucción a la Concurrencia',
        'Laboratorio de Programación y Lenguajes',
        'Sistemas Operativos',
        'Ingenieria de Software I - T',
        'Desarrollo de Softwate',
        'Fundamentos Teóricos de Informática',
        'Ingenieria de Software II - T',
        'Redes y Transmisión de Datos',
        'Paradigmas y Lenguajes de Programación - T',
        'Administración de Redes y Seguridad',
        'Ingeniería de Software III - T ',
        'Sistemas Distribuidos',
        'Administración de Proyectos',
        'Aplicaciones Web',
        'Taller de nuevas Tecnologías',
        'Sistemas de Soporte para la Toma de Decisiones'
    ]

    materia_año = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5]

    def entrenar(self):
        self.muestras = np.loadtxt('muestras.txt')
        archivo_porfesores = open('profesores.txt','r')
        profesores = []
        linea = archivo_porfesores.readline()
        while linea != "":
            linea = linea.replace("\n",'')
            profesores.append(linea)
            linea = archivo_porfesores.readline()
        archivo_porfesores.close()
        return self.fit(self.muestras, profesores)

    def predecir_profesor(self, Profesor):

        resultado = self.predict([[Profesor.pelo, Profesor.sexo, Profesor.año, Profesor.estatura, Profesor.cargo, Profesor.materia, Profesor.cuatrimestre]])
        return resultado[0]

    def dibujar_arbol(self):
        dot_data = tree.export_graphviz(self, out_file=None,
                                        feature_names=self.nombres_caracteristicas,
                                        class_names=self.profesores,
                                        filled=True, rounded=True,
                                        special_characters=True)
        graph = pydotplus.graph_from_dot_data(dot_data)
        graph.write_pdf("profesores.pdf")
