from modelo.Profesor import Profesor

class Adivinador():

    def __init__(self):
        self.indice_pregunta = 0
        self.indice_materia = 0
        self.profesor_incognito = Profesor()
           
    preuguntas = [
        "¿Tiene el pelo largo?",
        "¿Es mujer?",
        "¿Da clases Teóricas?",
        "¿Da su matéria en el segundo cuatrimestre?",
        "¿Es alto?",
        "¿Da clases en primer año?",
        "¿Da clases en segundo año?",
        "¿Da clases en tercer año?",
        "¿Da clases en cuarto año?",
        "¿Da clases en quinto año?",
        "¿ Está en la catedra de "
    ]
    
    def dame_pregunta(self,arbol):
        if self.indice_materia == 22:
            return None

        pregunta = self.preuguntas[self.indice_pregunta]
        if self.indice_pregunta == 10:
            while not (arbol.materia_año[self.indice_materia] == self.profesor_incognito.año):
                self.indice_materia += 1
            pregunta = pregunta + arbol.materias[self.indice_materia] + " ?"
            self.indice_materia += 1
        else:
            self.indice_pregunta += 1
        return pregunta

    def respuesta(self, numero, pregunta, arbol):
        if 'pelo' in pregunta:
            self.profesor_incognito.set_pelo(numero)
        if 'mujer' in pregunta:
            self.profesor_incognito.set_sexo(numero)
        if 'Teóricas' in pregunta:
            self.profesor_incognito.set_cargo(numero)
        if 'cuatrimestre' in pregunta:
            self.profesor_incognito.set_cuatrimestre(numero)
        if 'alto' in pregunta:
            self.profesor_incognito.set_estatura(numero)
        if 'año' in pregunta:
            if numero != 0:
                self.indice_pregunta = 10
                if 'primer' in pregunta:
                    self.profesor_incognito.set_año(1)
                if 'segundo' in pregunta:
                    self.profesor_incognito.set_año(2)
                if 'tercer' in pregunta:
                    self.profesor_incognito.set_año(3)
                if 'cuarto' in pregunta:
                    self.profesor_incognito.set_año(4)
                if 'quinto' in pregunta:
                    self.profesor_incognito.set_año(5)
        if 'catedra' in pregunta:
            if numero != 0:
                self.indice_materia = 22
                if arbol.materias[0] in pregunta:
                    self.profesor_incognito.set_materia(0)
                if arbol.materias[1] in pregunta:
                    self.profesor_incognito.set_materia(1)
                if arbol.materias[2] in pregunta:
                    self.profesor_incognito.set_materia(2)
                if arbol.materias[3] in pregunta:
                    self.profesor_incognito.set_materia(3)
                if arbol.materias[4] in pregunta:
                    self.profesor_incognito.set_materia(4)
                if arbol.materias[5] in pregunta:
                    self.profesor_incognito.set_materia(5)
                if arbol.materias[6] in pregunta:
                    self.profesor_incognito.set_materia(6)
                if arbol.materias[7] in pregunta:
                    self.profesor_incognito.set_materia(7)
                if arbol.materias[8] in pregunta:
                    self.profesor_incognito.set_materia(8)
                if arbol.materias[9] in pregunta:
                    self.profesor_incognito.set_materia(9)
                if arbol.materias[10] in pregunta:
                    self.profesor_incognito.set_materia(10)
                if arbol.materias[11] in pregunta:
                    self.profesor_incognito.set_materia(11)
                if arbol.materias[12] in pregunta:
                    self.profesor_incognito.set_materia(12)
                if arbol.materias[13] in pregunta:
                    self.profesor_incognito.set_materia(13)
                if arbol.materias[14] in pregunta:
                    self.profesor_incognito.set_materia(14)
                if arbol.materias[15] in pregunta:
                    self.profesor_incognito.set_materia(15)
                if arbol.materias[16] in pregunta:
                    self.profesor_incognito.set_materia(16)
                if arbol.materias[17] in pregunta:
                    self.profesor_incognito.set_materia(17)
                if arbol.materias[18] in pregunta:
                    self.profesor_incognito.set_materia(18)
                if arbol.materias[19] in pregunta:
                    self.profesor_incognito.set_materia(19)
                if arbol.materias[20] in pregunta:
                    self.profesor_incognito.set_materia(20)
                if arbol.materias[21] in pregunta:
                    self.profesor_incognito.set_materia(21)
    
    def dame_nombre_profesor(self, arbol):
        return arbol.predecir_profesor(self.profesor_incognito)