import copy 
#
# EJERCICIO 1
#
def invertir_lista(lista):
    new = []
    for i in range(len(lista)):
        new.append(lista[-i-1])
    return new
        


print(invertir_lista([1,2,3,4,5]))
print(invertir_lista(['Bogotá', 'Rosario', 'San Fernando', 'San Miguel']))

#
# EJERCICIO 2
#
def collatz(nro):
    pasos = 0
    while nro!=1:
        pasos += 1
        if nro%2==0:
            nro = nro/2
        else:
            nro = nro*3+1
    return pasos

nro = 100
pasos = collatz(nro)
print(f"Se requieren {pasos} pasos de collatz si lo aplicamos al número {nro}")

#
# EJERCICIO 3
#
def contar_definiciones(d):
    new = {}
    for k, v in d.items():
        new[k] = len(v)
    return new

def cantidad_de_claves_letra(d, l):
    contador = 0
    for k in d:
        if l == k[0]:
            contador += 1
    return contador

dic = {"holi": [1,2,3], "chauchis": [5,6], "lola": [1,1,1], "lincoln":[3,4,2], "Humahuaca": [2]}
resultado = contar_definiciones(dic)
print(resultado)

letra = "h"   # ¿Debería contar aunque sea mayúscula ?
cant_de_l = cantidad_de_claves_letra(dic, letra)
print(cant_de_l)

#
# EJERCICIO 4
#

def propagar(fosf):     

    fosf_prop = fosf.copy()
    for i, f in enumerate(fosf):
        if f == 1:
            # reviso el de la izquierda si esta nuevo si no estoy en el extremo izquierdo (i=0)
            if i != 0:
                if fosf[i-1] == 0:
                    fosf[i-1] = 1
            # reviso la derecha si no estoy en el extremo derecho
            if i != len(fosf) - 1:
                if fosf[i+1] == 0:
                    fosf[i+1] = 1
        else:
            continue
    return fosf


fosforos = [ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]

print(propagar(fosforos))



