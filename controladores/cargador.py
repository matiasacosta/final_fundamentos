import json

archivo_jason=open('datos.json', 'r')

datos_jason=json.load(archivo_jason)

print(datos_jason)

print (datos_jason['Año de la Materia'])