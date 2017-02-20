from sklearn import tree
import numpy as np
import json

class Arbol(tree.DecisionTreeClassifier):

    def __init__(self):
        super(Arbol, self).__init__(criterion='entropy')
        archivo_jason = open('datos.json', 'r')
        datos_jason = json.load(archivo_jason)
        self.nombres_caracteristicas=datos_jason['Caracteristicas']
        self.profesores=datos_jason['Profesores']
        self.materias = datos_jason['Materias']
        self.materia_año = datos_jason['Año de la Materia']

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
