from modelo.Profesor import Profesor
from modelo.arbol import predecir_profesor
preuguntas = ["TU PROFESOR TIENE EL PELO LARGO?",
              "TU PROFESOR ES MUJER?",
              "TU PROFESOR ESTÁ EN PRIMER AÑO?",
              "TU PROFESOR ES ALTO?",
              "TU PROFESOR DA CLASES DE TEORIA?",
              "TU PROFESOR ENSEÑA INGENIERIA?",
              "TU PROFESOR ENSEÑA EN EL PRIMER CUATRIMESTRE?"]
profesor_incognito = Profesor()

def dame_pregunta():
    if not hasattr(dame_pregunta, "indice"):
        dame_pregunta.indice = 0
    elif dame_pregunta.indice == 6:
        return None

    pregunta = preuguntas[dame_pregunta.indice]
    dame_pregunta.indice += 1
    return pregunta

def respuesta(numero, pregunta):
    if 'PELO' in pregunta:
        profesor_incognito.set_pelo(numero)
    if 'MUJER' in pregunta:
        profesor_incognito.set_sexo(numero)
    if 'AÑO' in pregunta:
        profesor_incognito.set_año(3)
    if 'ALTO' in pregunta:
        profesor_incognito.set_estatura(numero)
    if 'CLASES' in pregunta:
        profesor_incognito.set_cargo(numero)
    if 'ENSEÑA' in pregunta:
        profesor_incognito.set_materia(numero)
    if 'CUATRIMESTRE' in pregunta:
        profesor_incognito.set_cuatrimestre(numero)

def dame_nombre_profesor():
    return predecir_profesor(profesor_incognito)