# imports
import random
import numpy as np

# funciones
def crear_album(n):
    return np.zeros(n)
def album_incompleto(A):
    if 0 in A:
        return True
    else:
        return False
def comprar_figu(figus_total):
    figu = random.randint(0, figus_total-1)
    return figu
def cuantas_figus(n):
    album = crear_album(n)
    compras = 0
    while album_incompleto(album):
        figu = comprar_figu(n)
        album[figu] += 1
        compras += 1
    return compras
def experimento_figus(n_repeticiones, figus_total):
    data = []
    for i in range(n_repeticiones):
        data.append(cuantas_figus(figus_total))
    return np.sum(data)/n_repeticiones
def comprar_paquete(figus_total, figus_paquete):
    paquete = []
    for i in range(figus_paquete):
        paquete.append(comprar_figu(figus_total))
    return paquete
def cuantos_paquetes(n_album, n_paquete):
    album = np.zeros(n_album)
    compras = 0
    while album_incompleto(album):
        paquete = comprar_paquete(n_album, n_paquete)
        compras += 1
        for figu in paquete:
            album[figu] += 1
    return compras
        
if __name__=="__main__":

    from utilities import *

    print_ejercicio(5)
    n_repeticiones = 1000
    figus_total = 6
    data = []
    for _ in range(n_repeticiones):
        data.append(cuantas_figus(figus_total))
    media = np.sum(data)/n_repeticiones
    print(f"Compra promedio de figuritas para un album de {figus_total} figuritas = {media}")


    print_ejercicio(6)
    n_repeticiones = 100
    figus_total = 860
    media = experimento_figus(n_repeticiones, figus_total)
    print(f"Compra promedio de figuritas para un album de {figus_total} figuritas = {media}")

    
    print_ejercicio(10)
    tamaño_album = 860
    n_repeticiones = 100
    data = []
    for _ in range(n_repeticiones):
        data.append(cuantos_paquetes(tamaño_album, 5))
    media = np.sum(data)/n_repeticiones
    print(f"Compra promedio de paquetes para un album de {tamaño_album} = {media}")