import numpy as np

# Indexacion de un solo elemento
x = np.arange(10)
print(x)

# Extraccion de elementos en forma ascendente
print(x[2]) # Resultado: 2

# Extraccion de elementos en forma descendente
print(x[-2]) # Resultado: 8

# Convertir un arreglo dimensional en un arreglo bidimensional
y = x.reshape(2, 5)
print(y)

# Extraccion del elemento con indice 1 en renglon e indice 3 en columna
print(y[1, 3]) # Resultado: 8

# Alternativa de extraccion del elemento con indice 1 en renglon e indice 3 en columna
print(y[1][3]) # Resultado: 8

# Extraccion del elemento con indice 1 en renglon y primer elemento en forma descendente
print(y[1][-1]) # Resultado 9

# Extraccion del renglon completo con indice 0 (al no especificar indice de columna)
print(y[0]) # Resultado: [0,1,2,3,4]

# Cortes en arreglos
z = np.array([0,1,2,3,4,5,6,7,8,9])
'''
[1:7:2] --> start:stop:step
start: indice de donde se empieza a contar (1)
stop: indice donde se detiene el conteo (el ultimo numero no se cuenta, en el ejemplo es el 7)
step: numero de elementos que se van a saltar (en el ejemplo es de 2 en 2)

Como resultado nos dice que comience en el 1, se detenga antes del 7 y que cuente de 2 en 2
'''
print(z[1:7:2]) # Resultado: [1,3,5] "start:stop:step"

# Cortes del arreglo de adelante hacia atras, considerando dos elementos
print(z[-2:10]) # Resultado: [8,9]

# Corte del arreglo de adelante hacia atras, iniciando tres posiciones a partir del final
# y retrocediendo hasta tener como limite el numero 3
print(z[-3:3:-1]) # Resultado: [7,6,5,4]

# Definicion de un nuevo arreglo
# Creacion de un arreglo en forma descendente - Del 10 al 1 (sin incluirlo) - con decrementos de 1
a = np.arange(10, 1, -1)
print(a) # Resultado: [10,9,8,7,6,5,4,3,2]


# Extraccion de elementos especificos del arreglo
extraccion = a[np.array([3,3,1,8])] # Resultado: [7,7,9,2]
print(extraccion)

# Extraccion de elementos con indices 3, 3, -1 (descendente) y 8
extraccion2 = a[np.array([3, 3, -3, 8])]
print(extraccion2) # Resultado: [7,7,4,2]

# Extraccion basada en pares
b = np.arange(35).reshape(5, 7)
print(b)

# Extraccion de coordenadas
extraccion3 = b[np.array([0,2,4]), np.array([0,1,2])]
print(extraccion3) # Resultado: [0, 15, 30]

'''UNION DE ARREGLOS'''
arr = np.concatenate(([1,2,3], [4,5,6]))
print(arr) # Resultado: [1,2,3,4,5,6]

# Apilado vertical de vectores
arr2 = np.stack(([1,2,3], [4,5,6]))
print(arr2) # Resultado: [[1,2,3], [4,5,6]]

# Concatenacion de matrices
mat_1 = np.array(([1,2,3], [4,5,6]))
mat_2 = np.array(([1,1,1], [2,2,2]))
concat_mats = np.concatenate((mat_1, mat_2), axis=0)
print(concat_mats)

concat_mats2 = np.concatenate((mat_1, mat_2), axis=1)
print(concat_mats2)

concat_mats3 = np.concatenate((mat_1, mat_2), axis=None)
print(concat_mats3)