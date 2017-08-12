from sklearn.ensemble import RandomForestClassifier
import numpy as np
import json

class Bosque(RandomForestClassifier):

    def __init__(self):
        super(Bosque, self).__init__(criterion='entropy',n_estimators=100)
        archivo_jason = open('datos.json', 'r')
        datos_jason = json.load(archivo_jason)
        self.nombres_caracteristicas=datos_jason['Caracteristicas']
        self.profesores=datos_jason['Profesores']
        self.materias = datos_jason['Materias']
        self.materia_año = datos_jason['Año de la Materia']
        archivo_jason.close()

    def entrenar(self):
        self.muestras = np.loadtxt('muestras_train.txt')
        archivo_porfesores = open('profesores_train.txt','r')
        profesores = []
        linea = archivo_porfesores.readline()
        #PODEMOS USAR UN FOR (QUEDA MAS LIMPIO)
        while linea != "":
            linea = linea.replace("\n",'')
            profesores.append(linea)
            linea = archivo_porfesores.readline()
        archivo_porfesores.close()
        return self.fit(self.muestras, profesores)

    def testear(self):
        self.muestras = np.loadtxt('muestras_test.txt')
        archivo_porfesores = open('profesores_test.txt','r')
        profesores = []
        linea = archivo_porfesores.readline()
        #PODEMOS USAR UN FOR (QUEDA MAS LIMPIO)
        while linea != "":
            linea = linea.replace("\n",'')
            profesores.append(linea)
            linea = archivo_porfesores.readline()
        archivo_porfesores.close()
        return self.score(self.muestras, profesores)

    def predecir_profesor(self, Profesor):
        resultado = self.predict([[Profesor.pelo, Profesor.sexo, Profesor.año, Profesor.estatura, Profesor.cargo, Profesor.materia, Profesor.cuatrimestre]])
        return resultado[0]