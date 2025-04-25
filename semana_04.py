import csv
from utilities import *
def arboles_parque(nombre_archivo, nombre_parque):
    """
    Función arboles_parque(nombre_archivo, nombre_parque) que dado el archivo 
    'arbolado-en-espacios-verdes.csv' nos genere una lista con un diccionario 
    para cada árbol (identificado por su id) de ese parque (cada fila del csv) 
    y los nombres de las columnas correspondientes como claves de un diccionario interno.
    """
    file = open(nombre_archivo, encoding='utf-8')
    rows = csv.reader(file)
    headers = next(rows)
    idx_espacio_ve = headers.index('espacio_ve')
    idx_id_arbol = headers.index('id_arbol')
    data = {}
    for row in rows:
        id = row[idx_id_arbol]
        if row[idx_espacio_ve] == nombre_parque:
            data[id] = {}
            for i in range(len(headers)):
                data[id][headers[i]] = row[i]
    file.close()

    return data

def arbol_mas_popular(nombre_parque):
    """
    Crear una función que aprovechando la anterior, 
    nos indique el árbol más popular de ese parque: arbol_mas_popular(nombre_parque).
    """
    data = arboles_parque("arbolado-en-espacios-verdes.csv", nombre_parque)
    contador = {}
    for values in data.values():
        if contador.get(values['nombre_gen']) is None:
            contador[values['nombre_gen']] = 1
        else:
            contador[values['nombre_gen']] += 1
    return max(contador, key=contador.get)  # get es un iterador que recorre los values de cada clave

def n_mas_altos(nombre_parque, n):
    """
    Indica los n árboles más altos de ese parque n_mas_altos(nombre_parque, n).
    """
    data = arboles_parque("arbolado-en-espacios-verdes.csv", nombre_parque)

    arboles_mas_altos = []

    for _ in range(n):
        arbol_max = max(list(data.values()), key=lambda arbol: float(arbol["altura_tot"]))
        arboles_mas_altos.append(arbol_max)
        del data[arbol_max["id_arbol"]]

    return arboles_mas_altos

def altura_promedio(nombre_parque, especie):
    """
    Dado un parque y una especie, indica la altura 
    promedio de esa especie altura_promedio(nombre_parque, especie).
    Se utiliza el 'nombre_ge'n en especie.
    """    
    data = arboles_parque("arbolado-en-espacios-verdes.csv", nombre_parque)

    contador = 0
    altura_total = 0

    for arbol in data.values():
        if arbol["nombre_gen"] == especie:
            contador += 1
            altura_total += float(arbol["altura_tot"])

    return altura_total/contador

def obtener_parques(nombre_archivo):
    '''
    Devuelve una lista con todos los parques existentes.
    '''
    file = open(nombre_archivo, encoding='utf-8')
    rows = csv.reader(file)
    headers = next(rows)
    idx_espacio_ve = headers.index('espacio_ve')
    parques = []
    for arbol in rows:
        if (parque:=arbol[idx_espacio_ve]) not in parques:
            parques.append(parque)
    file.close()
    return parques

def cant_arboles_por_parque(nombre_archivo):
    '''
    Devuelve la cantidad de arboles que hay en cada parque
    '''
    file = open(nombre_archivo, encoding='utf-8')
    rows = csv.reader(file)
    headers = next(rows)
    idx_espacio_ve = headers.index('espacio_ve')
    data = {}
    for row in rows:
        parque = row[idx_espacio_ve]
        if parque != 'S/D':
            if data.get(parque):
                data[parque] += 1
            else:
                data[parque] = 1
    return data

def altura_promedio_cada_parque(nombre_archivo):
    '''
    Devuelve la altura promedio de arboles de cada parque
    '''
    file = open(nombre_archivo, encoding='utf-8')
    rows = csv.reader(file)
    headers = next(rows)
    idx_espacio_ve = headers.index('espacio_ve')
    idx_altura_tot = headers.index('altura_tot')
    data = {}
    for row in rows:
        parque = row[idx_espacio_ve]
        altura = row[idx_altura_tot]
        if parque != 'S/D':
            if data.get(parque):
                data[parque] += float(altura)
            else:
                data[parque] = float(altura)
    cant_arb = cant_arboles_por_parque(nombre_archivo)
    for parque, cant in cant_arb.items():
        data[parque] = round(data[parque]/cant,2)
    return data

def variedades_cada_parque(nombre_archivo):
    '''
    Devuelve la cantidad de especies que tiene cada parque.
    '''
    file = open(nombre_archivo, encoding='utf-8')
    rows = csv.reader(file)
    headers = next(rows)
    idx_espacio_ve = headers.index('espacio_ve')
    idx_variedad = headers.index('nombre_cie')
    data = {}
    for row in rows:
        parque = row[idx_espacio_ve]
        variedad = row[idx_variedad]
        if parque != 'S/D':
            if not data.get(parque):
                data[parque] = [variedad]
            else:
                if variedad not in data[parque]:
                    data[parque].append(variedad)
    for k, v in data.items():
        data[k] = len(v)
    return data
        
def cual_tiene_max(cant_por_key):
    '''
    A partir de un diccionario donde las keys 
    son nombres y los values son la cantidad 
    de cada una de esas keys, retorna cual
    o cuales tienen el maximo valor.
    '''
    data = {"": 0}
    for parq, cant in cant_por_key.items():
        if cant > list(data.values())[0]:
            data = {parq : cant}
        elif cant == list(data.values())[0]:
            data[parq] = cant
    return list(data.keys())

def cant_especies_ciudad(nombre_archivo):
    '''
    Devuelve la cantidad de cada especie de la ciudad indicada
    '''
    file = open(nombre_archivo, encoding='utf-8')
    rows = csv.reader(file)
    headers = next(rows)
    idx_variedad = headers.index('nombre_cie')
    data = {}
    for row in rows:
        especie = row[idx_variedad]
        if data.get(especie):
            data[especie] += 1
        else:
            data[especie] = 1
    return data

def distintos_origenes(nombre_archivo):
    '''
    Permite ver cuales son los distintos origenes para analizar el dataset
    '''
    file = open(nombre_archivo, encoding='utf-8')
    rows = csv.reader(file)
    headers = next(rows)
    idx_origen = headers.index('origen')
    data = []
    for row in rows:
        if (origen:=row[idx_origen]) not in data:
            data.append(origen)
    return data

def cant_especies_por_origen(nombre_archivo):
    '''
    Devuelve la cantidad de especies que hay de cada origen.
    Tener en cuenta que se contabilizan las especies, no los arboles.
    '''
    file = open(nombre_archivo, encoding='utf-8')
    rows = csv.reader(file)
    headers = next(rows)
    idx_origen = headers.index('origen')
    idx_especie = headers.index('nombre_cie')
    especies_contadas = []
    data = {}
    for row in rows:
        origen = row[idx_origen]
        especie = row[idx_especie]
        if especie not in especies_contadas:
            especies_contadas.append(especie)
            if data.get(origen):
                data[origen]+= 1
            else:
                data[origen] = 1
    return data

if __name__=="__main__":

    nombre_archivo = "arbolado-en-espacios-verdes.csv"

    # ejercicio 1
    print_ejercicio(1)
    data = arboles_parque(nombre_archivo, "ARMENIA")

    ids_arboles_armenia = list(data.keys())
    datos_arboles_armenia = list(data.values())

    print(f"ID = {ids_arboles_armenia[-1]}")
    print(f"DATA = {datos_arboles_armenia[-1]}\n")

    # ejercicio 2
    print_ejercicio(2)
    arbol_pop = arbol_mas_popular("ARMENIA")
    print(arbol_pop)

    # ejercicio 3
    print_ejercicio(3)
    arboles_mas_altos = n_mas_altos("ARMENIA", 2)
    print(arboles_mas_altos)

    # ejercicio 4
    print_ejercicio(4)
    altura_prom = altura_promedio("ARMENIA", "Eucalyptus")
    print(altura_prom)

    # ejercicio 5
    print_ejercicio("5 a")
    # a
        # El/los parques con más cantidad de árboles.
    cant_arboles_x_parque = cant_arboles_por_parque(nombre_archivo)
    parq_max_arboles = cual_tiene_max(cant_arboles_x_parque)
    print(parq_max_arboles)

    print_ejercicio("5 b")
    # b
        # El/los parques con los árboles más altos en promedio.
    '''
    Creo una funcion que devuelve todas las alturas
    promedios de cada parque
    '''
    altura_prom_x_parque = altura_promedio_cada_parque(nombre_archivo)
    parq_max_altura_prom = cual_tiene_max(altura_prom_x_parque)
    print(parq_max_altura_prom)

    print_ejercicio("5 c")
    # c
        # El/los parques con más variedad de especies.
    variedades_x_parque = variedades_cada_parque(nombre_archivo)
    parq_con_max_cant_var = cual_tiene_max(variedades_x_parque)
    print(parq_con_max_cant_var)

    print_ejercicio("5 d")
    # d
        # La especie que más ejemplares tiene en la ciudad.
    cant_espe = cant_especies_ciudad(nombre_archivo)
    especie_max = cual_tiene_max(cant_espe)
    print(especie_max)

    print_ejercicio("5 e")
    # e
        # La razón entre especies exóticas y autóctonas.
    # primero reviso cuales son los origenes existentes en el dataset
    print(distintos_origenes(nombre_archivo))
    cant_origen = cant_especies_por_origen(nombre_archivo)
    razon_exot_autoc = cant_origen["Exótico"]/cant_origen["Nativo/Autóctono"]
    print(f"Razon entre especies exóticas y autóctonas = {razon_exot_autoc:.2f}")

    