from sklearn.ensemble import RandomForestClassifier
import numpy as np
import json
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

class Bosque(RandomForestClassifier):

    def __init__(self):
        super(Bosque, self).__init__(criterion='entropy',n_estimators=100)
        with open(os.path.abspath('modelo/datos.json'), 'r',encoding='utf-8') as archivo_jason:
            datos_jason = json.load(archivo_jason)
            self.nombres_caracteristicas=datos_jason['Caracteristicas']
            self.profesores=datos_jason['Profesores']
            self.materias = datos_jason['Materias']
            self.materia_año = datos_jason['Año de la Materia']

    def entrenar(self):
        path = os.path.abspath('modelo/muestras.csv')
        df = pd.read_csv(path, sep=',', header=None)
        array_atributos = df[df.columns[0:7]].values
        array_profesores = df[df.columns[7]].values
        return self.fit(array_atributos, array_profesores)
        


    def predecir_profesor(self, Profesor):
        resultado = self.predict([[Profesor.pelo, Profesor.sexo, Profesor.año, Profesor.estatura, Profesor.cargo, Profesor.materia, Profesor.cuatrimestre]])
        return resultado[0]

    def prueba_reporte(self):
        path = os.path.abspath('modelo/muestras.csv')
        df = pd.read_csv(path, sep=',', header=None)
        array_atributos = df[df.columns[0:7]].values
        array_profesores = df[df.columns[7]].values
        Xtrain, Xtest, ytrain, ytest = train_test_split(array_atributos, array_profesores,random_state=0,train_size=0.70,test_size=0.30)
        self.fit(Xtrain, ytrain)
        ypred = self.predict(Xtest)
        print(metrics.classification_report(ypred, ytest))
        mat = confusion_matrix(ytest, ypred)
        sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False)
        plt.xlabel('true label')
        plt.ylabel('predicted label')
        plt.show()
