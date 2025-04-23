# Resolución del ejercicio 5

- El/los parques con más cantidad de árboles.
- El/los parques con los árboles más altos en promedio.
- El/los parques con más variedad de especies.
- La especie que más ejemplares tiene en la ciudad.
- La razón entre especies exóticas y autóctonas.

Vemos que vamos a necesitar una función que de cual/es parques o especies tienen la mayor magnitud en algunas de las propiedades de los arboles. Creamos la función ***cual_tiene_max(cant_por_key)***, la cual tiene como input un diccionario el cual tiene en sus values una cantidad asignada para cada key, y retorna una lista con las keys que tienen la cantidad maxima.

```python
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
```

## **El/los parques con más cantidad de árboles**

Para obtener el/los parques con más cantidad de árboles, creo una función ***cant_arboles_por_parque(nombre_archivo)***: 

```python
def cant_arboles_por_parque(nombre_archivo):
    '''
    Devuelve la cantidad de arboles que hay en cada 
    parque
    '''
    
    file = open(nombre_archivo) # abre el archivo csv
    rows = csv.reader(file)     # lee las filas del cs
    headers = next(rows)        # lee la primer fila y pasa a la siguiente
    idx_espacio_ve = headers.index('espacio_ve')  # almaceno el indice donde en las filas se encuentra el nombre del parque
    data = {}
    for row in rows:
        parque = row[idx_espacio_ve]
        if parque != 'S/D':     # no tiene en consideración los arboles que no tienen definido a que parque pertenecen
            if data.get(parque):
                data[parque] += 1 # cuenta un arbol más
            else:
                data[parque] = 1 # si nunca conto un arbol de un parque, inicializa en 1
    return data
```

Esta función devuelve un diccionario con la cantidad de arboles que hay en cada parque. Luego para saber cual es el que tiene más arboles, realizo:

```python
# obtengo la cantidad de arboles por parque
cant_arboles_x_parque = cant_arboles_por_parque(nombre_archivo)
# 
parq_max_arboles = cual_tiene_max(cant_arboles_x_parque)
print(parq_max_arboles)
```

Donde el resultado cuando el nombre del archivo  "arbolado-en-espacios-verdes.csv”, el cual será el mismo para todos los ejercicios siguientes, es:

```bash
['INDOAMERICANO']
```

donde ‘INDOAMERICANO’ es el nombre del parque con más arboles.

## El/los parques con los árboles más altos en promedio.

Para este caso creo una función que devuelve todas las alturas promedios de cada parque.

```python
def altura_promedio_cada_parque(nombre_archivo):
    '''
    Devuelve la altura promedio de arboles de cada parque
    '''
    file = open(nombre_archivo)
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
		            # hago la suma de todas las alturas en el diccionario
                data[parque] += float(altura)
            else:
                data[parque] = float(altura)
    # obtengo la cantidad de arboles de cada parque
    cant_arb = cant_arboles_por_parque(nombre_archivo)
    # con la cantidad de arboles de cada parque, divido la sumatoria de las alturas y obtengo el promedio
    for parque, cant in cant_arb.items():
			  # redondeo a 2 decimales el promedio obtenido para cada parque
        data[parque] = round(data[parque]/cant,2)
    return data
```

Una vez obtenidos los promedios de altura de cada parque, obtengo cual es el que tiene el promedio máximo:

```python
altura_prom_x_parque = altura_promedio_cada_parque(nombre_archivo)
parq_max_altura_prom = cual_tiene_max(altura_prom_x_parque)
print(parq_max_altura_prom)
```

El resultado fue:

```python
['INFANTE DON ENRIQUE EL NAVEGANTE""']
```

## El/los parques con más variedad de especies.

Creo una función para contar cuantas variedades de especie hay en cada parque:

```python
def variedades_cada_parque(nombre_archivo):
    '''
    Devuelve la cantidad de especies que tiene cada parque.
    '''
    file = open(nombre_archivo)
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
		            # si el parque todavía no fue agregado a data se inicia una lista la variedad de esa especie
                data[parque] = [variedad]
            else:
		            # si el parque si existe, y esa especie no esta en la lista, se agrega
                if variedad not in data[parque]:
                    data[parque].append(variedad)+
    # se modifica el diccionario data
    # se cambia la lista de especies, por la longitud de esa lista
    # la longitud representa la cantidad de especies diferentes que hay en ese parque
    for k, v in data.items():
        data[k] = len(v)
    return data
```

Una vez contada la variedad de especies en cada parque, obtengo que parque contiene la máxima cantidad de variedades:

```python
variedades_x_parque = variedades_cada_parque(nombre_archivo)
parq_con_max_cant_var = cual_tiene_max(variedades_x_parque)
print(parq_con_max_cant_var)
```

El resultado fue:

```python
['EL ROSEDAL (Sector dentro de Plaza HOLANDA)']
```

## La especie que más ejemplares tiene en la ciudad.

Creo una función que devuelve la cantidad de cada especie que hay en la ciudad.

```python
def cant_especies_ciudad(nombre_archivo):
    '''
    Devuelve la cantidad de cada especie de la ciudad indicada
    '''
    file = open(nombre_archivo)
    rows = csv.reader(file)
    headers = next(rows)
    idx_variedad = headers.index('nombre_cie')
    data = {}
    for row in rows:
        especie = row[idx_variedad]
        if data.get(especie):
	        # suma 1 si la especie ya esta en el diccionario
            data[especie] += 1
        else:
	        # si no existe en data, crea key = especie, y comienza a contar en 1
            data[especie] = 1
    return data
```

Una vez contada la cantidad de arboles de cada especie, obtengo cual es la que tiene mas cantidad de arboles en la ciudad.

```python
cant_espe = cant_especies_ciudad(nombre_archivo)
especie_max = cual_tiene_max(cant_espe)
print(especie_max)
```

El resultado fue:

```python
['Eucalyptus sp.']
```

## La razón entre especies exóticas y autóctonas.

Creo una función que devuelve la cantidad de especies que hay de cada origen.

```python
def cant_especies_por_origen(nombre_archivo):
    '''
    Devuelve la cantidad de especies que hay de cada origen.
    Tener en cuenta que se contabilizan las especies, no los arboles.
    '''
    file = open(nombre_archivo)
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
```

Una vez obtenidos los resultados, divido la cantidad de arboles de origen exótico por la cantidad de nativos o autóctonos, es decir, calculo la razón entre las nombradas: 

```python
cant_origen = cant_especies_por_origen(nombre_archivo)
razon_exot_autoc = cant_origen["Exótico"]/cant_origen["Nativo/Autóctono"]
print(f"Razon entre especies exóticas y autóctonas = {razon_exot_autoc:.2f}")
```

El resultado fue:

```python
Razon entre especies exóticas y autóctonas = 3.62
```