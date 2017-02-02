from sklearn import tree

def predecir_profesor(Profesor):
    features = {
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
    }

    celia = [features['largo'], features['mujer'], features['tercero'], features['alto'], features['practica'],
             features['fundamentos'], features['segundo_cuatri']]
    celia1 = [features['largo'], features['mujer'], features['quinto'], features['alto'], features['practica'],
              features['toma de decisiones'], features['segundo_cuatri']]

    diegof = [features['corto'], features['hombre'], features['primero'], features['bajo'], features['practica'],
              features['algoritmica I'], features['segundo_cuatri']]
    diegof1 = [features['corto'], features['hombre'], features['segundo'], features['bajo'], features['practica'],
               features['algortmica II'], features['primer_cuatri']]
    diegof2 = [features['corto'], features['hombre'], features['tercero'], features['bajo'], features['teoria'],
               features['laboratorio'], features['primer_cuatri']]
    diegof3 = [features['corto'], features['hombre'], features['quinto'], features['bajo'], features['teoria'],
               features['taller tecnologias'], features['primer_cuatri']]

    diegov = [features['corto'], features['hombre'], features['tercero'], features['alto'], features['practica'],
              features['desarrollo'], features['segundo_cuatri']]
    diegov1 = [features['corto'], features['hombre'], features['cuarto'], features['alto'], features['practica'],
               features['ing III'], features['segundo_cuatri']]

    gloria = [features['largo'], features['mujer'], features['tercero'], features['bajo'], features['teoria'],
              features['fundamentos'], features['segundo_cuatri']]
    gloria1 = [features['largo'], features['mujer'], features['tercero'], features['bajo'], features['teoria'],
               features['desarrollo'], features['segundo_cuatri']]
    gloria2 = [features['largo'], features['mujer'], features['cuarto'], features['bajo'], features['practica'],
               features['paradigmas'], features['primer_cuatri']]
    gloria3 = [features['largo'], features['mujer'], features['cuarto'], features['bajo'], features['teoria'],
               features['ing III'], features['segundo_cuatri']]

    marcelog = [features['corto'], features['hombre'], features['segundo'], features['bajo'], features['practica'],
                features['arquitectura'], features['primer_cuatri']]
    marcelog1 = [features['corto'], features['hombre'], features['segundo'], features['bajo'], features['teoria'],
                 features['concurrencia'], features['segundo_cuatri']]
    marcelog2 = [features['corto'], features['hombre'], features['tercero'], features['bajo'], features['teoria'],
                 features['sistemas_operativos'], features['primer_cuatri']]

    marcelos = [features['largo'], features['hombre'], features['primero'], features['alto'], features['practica'],
                features['epa'], features['primer_cuatri']]
    marcelos1 = [features['largo'], features['hombre'], features['segundo'], features['alto'], features['practica'],
                 features['base'], features['segundo_cuatri']]
    marcelos2 = [features['largo'], features['hombre'], features['tercero'], features['alto'], features['practica'],
                 features['laboratorio'], features['primer_cuatri']]

    marta = [features['largo'], features['mujer'], features['segundo'], features['bajo'], features['teoria'],
             features['algortmica II'], features['primer_cuatri']]
    marta1 = [features['largo'], features['mujer'], features['tercero'], features['bajo'], features['teoria'],
              features['ing I'], features['primer_cuatri']]
    marta2 = [features['largo'], features['mujer'], features['tercero'], features['bajo'], features['teoria'],
              features['ing II'], features['segundo_cuatri']]
    marta3 = [features['largo'], features['mujer'], features['quinto'], features['bajo'], features['teoria'],
              features['administracion'], features['primer_cuatri']]

    nahuel = [features['corto'], features['hombre'], features['segundo'], features['alto'], features['practica'],
              features['concurrencia'], features['segundo_cuatri']]
    nahuel1 = [features['corto'], features['hombre'], features['tercero'], features['alto'], features['practica'],
               features['sistemas_operativos'], features['primer_cuatri']]
    nahuel2 = [features['corto'], features['hombre'], features['cuarto'], features['alto'], features['practica'],
               features['seguridad'], features['segundo_cuatri']]
    nahuel3 = [features['corto'], features['hombre'], features['cuarto'], features['alto'], features['teoria'],
               features['seguridad'], features['segundo_cuatri']]

    ricardo = [features['corto'], features['hombre'], features['primero'], features['bajo'], features['teoria'],
               features['elementos'], features['primer_cuatri']]
    ricardo1 = [features['corto'], features['hombre'], features['cuarto'], features['bajo'], features['teoria'],
                features['Redes'], features['primer_cuatri']]
    ricardo2 = [features['corto'], features['hombre'], features['cuarto'], features['bajo'], features['teoria'],
                features['distribuidos'], features['segundo_cuatri']]

    seba = [features['corto'], features['hombre'], features['tercero'], features['bajo'], features['practica'],
            features['ing I'], features['primer_cuatri']]
    seba1 = [features['corto'], features['hombre'], features['tercero'], features['bajo'], features['practica'],
             features['ing II'], features['segundo_cuatri']]
    seba2 = [features['corto'], features['hombre'], features['quinto'], features['bajo'], features['practica'],
             features['web'], features['primer_cuatri']]
    seba3 = [features['corto'], features['hombre'], features['quinto'], features['bajo'], features['practica'],
             features['taller tecnologias'], features['primer_cuatri']]

    datos = [celia, celia1,
             diegof, diegof1, diegof2, diegof3,
             diegov, diegov1,
             gloria, gloria1, gloria2, gloria3,
             marcelog, marcelog1, marcelog2,
             marcelos, marcelos1, marcelos2,
             marta, marta1, marta2, marta3,
             nahuel, nahuel1, nahuel2, nahuel3,
             ricardo, ricardo1, ricardo2,
             seba, seba1, seba2, seba3]

    profesores = ['celia', 'celia',
                  'diegof', 'diegof', 'diegof', 'diegof',
                  'diegov', 'diegov',
                  'gloria', 'gloria', 'gloria', 'gloria',
                  'marcelog', 'marcelog', 'marcelog',
                  'marcelos', 'marcelos', 'marcelos',
                  'marta', 'marta', 'marta', 'marta',
                  'nahuel', 'nahuel', 'nahuel', 'nahuel',
                  'ricardo', 'ricardo', 'ricardo',
                  'seba', 'seba', 'seba', 'seba']

    clf = tree.DecisionTreeClassifier(class_weight='balanced')
    clf = clf.fit(datos, profesores)
    resultado = clf.predict([[Profesor.pelo, Profesor.sexo, Profesor.materia, Profesor.estatura, Profesor.cargo, Profesor.materia, Profesor.cuatrimestre]])
    return resultado[0]
