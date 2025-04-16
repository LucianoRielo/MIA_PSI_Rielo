import csv
from utilities import *
def arboles_parque(nombre_archivo, nombre_parque):
    file = open(nombre_archivo)
    rows = csv.reader(file)
    headers = next(rows)
    idx_espacio_ve = headers.index('espacio_ve')
    idx_id_arbol = headers.index('id_arbol')
    data_dict = {}
    for row in rows:
        id = row[idx_id_arbol]
        if row[idx_espacio_ve] == nombre_parque:
            data_dict[id] = {}
            for i in range(len(headers)):
                if not i == idx_id_arbol:
                    data_dict[id][headers[i]] = row[i]
    file.close()

    return data_dict

def arbol_mas_popular()


if __name__=="__main__":

    print_ejercicio(1)
    data = arboles_parque("arbolado-en-espacios-verdes.csv", "ARMENIA")

    data_keys = list(data.keys())
    data_values = list(data.values())

    print(f"ID = {data_keys[0]}")
    print(f"DATA = {data_values[0]}\n")

    print(f"ID = {data_keys[1]}")
    print(f"DATA = {data_values[1]}\n")
