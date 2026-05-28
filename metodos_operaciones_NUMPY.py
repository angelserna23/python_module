import numpy as np
#Columnas = areas
#Filas = años
accidentes = np.array([[0,1,1],
                       [1,0,1],
                       [1,3,2],
                       [2,2,0]])

# Inciso a)
total_accidentes = accidentes.sum()
print(total_accidentes) # Resultado: 14

#Inciso b)
accid_areas = accidentes.sum(axis=0)
print(accid_areas) # Resultado = array([4,6,4])

print("Los accidentes del area 1:", accid_areas[0])
print("Los accidentes del area 2:", accid_areas[1])
print("Los accidentes del area 3:", accid_areas[2])

#Inciso c)
accid_anios = accidentes.sum(axis=1)
print(accid_anios)

accid_anios = accidentes.sum(axis=1, keepdims=True)
print(accid_anios)

print("Los accidentes del año 1:", accid_anios[0])
print("Los accidentes del año 2:", accid_anios[1])
print("Los accidentes del año 3:", accid_anios[2])
print("Los accidentes del año 4:", accid_anios[3])

#Inciso d)
maximo = accidentes.max()
minimo = accidentes.min()

print(f"Maximo de accidentes: {maximo}")
print(f"Minimo de accidentes: {minimo}")

#Inciso e)
promedio = accidentes.mean()
print(f"Promedio de accidentes: {promedio}")

#----------------------------------------------------------------------------
'''
Operaciones vectorizadas

- Incluye funciones tales como "sum", "min" y "max
- Permiten realizar operaciones mas rapidamente (en comparacion a su equivalente mediante ciclos en Python)
- Estan soportadas por el lenguaje C
'''

arreglo = np.array([[1,2,3],
                    [4,5,6]])

dimensiones = arreglo.shape
print(f"Renglones: {dimensiones[0]}")
print(f"Columnas: {dimensiones[1]}")
print(f"El primer elemento del arreglo es: {arreglo[0][0]}")

# Ejemplo de un ciclo for en Python
# Inciso a)
import time # Es una libreria que determina el tiempo

inicio = time.time()

arreglo_final = np.zeros((2,3))
for renglon in range(dimensiones[0]):
    for columna in range(dimensiones[1]):
        arreglo_final[renglon][columna] = arreglo_final[renglon][columna] + 3

print(arreglo_final)

fin = time.time()
print(f"Tiempo total de ejecucion (Segundos.) {fin - inicio}")

# Ejemplo de un ciclo con Operaciones Vectorizadas
# Inciso b)
import time
inicio = time.time()

arreglo_final = arreglo + 3
print(arreglo_final)

fin = time.time()

print(f"Tiempo total de ejecucion (Segundos): {fin - inicio}")