from sklearn.ensemble import RandomForestClassifier
import numpy as np
import itertools
import json
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import ExtraTreesClassifier

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Matriz de Confusion',
                          cmap=plt.cm.Blues):
        """
        This function prints and plots the confusion matrix.
        Normalization can be applied by setting `normalize=True`.
        """

        plt.imshow(cm, interpolation='nearest', cmap=cmap)
        plt.title(title)
        plt.colorbar()
        
        
        tick_marks = np.arange(len(classes))
        plt.xticks(tick_marks, classes, rotation=90)
        plt.yticks(tick_marks, classes)

        fmt = '.2f' if normalize else 'd'
        thresh = cm.max() / 2.
        for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
            plt.text(j, i, format(cm[i, j], fmt),
                    horizontalalignment="center",
                    color="white" if cm[i, j] > thresh else "black")

        plt.ylabel('Profesores Verdaderos')
        plt.xlabel('Profesores Predecidos')
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
        model = ExtraTreesClassifier()
        #Ajustamos el modelo
        model.fit(Xtrain,ytrain)
        #Pedimos que nos muestre la importancia de cada variable
        lista_caracteristicas = ['pelo','Sexo','Año','Estatura','Cargo','Materia','Cuatrimestre']
        print("Importancia de las Caracteristicas en la clasificacion:")
        print("Caracteristica - Porcentaje")
        for i in range(0,7): 
            print("{},{}%".format(lista_caracteristicas[i], round(model.feature_importances_[i]*100,2)))
        for x,y in zip(ytest, ypred):
            print("{}-{}".format(x,y))
        
        profesores_predecidos = ypred.tolist()
        profesores_de_test = ytest.tolist()

        total_profesores = profesores_predecidos + profesores_de_test

        profesores_labels = []
        for profesor in total_profesores:
            if profesor not in profesores_labels:
                profesores_labels.append(profesor)

        mat = confusion_matrix(ytest, ypred,profesores_labels)
        plt.figure()
        plot_confusion_matrix(mat, classes=profesores_labels,
                      title='Matriz de Confusion')
        plt.show()

