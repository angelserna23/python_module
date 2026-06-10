'''
Numpy en el ecosistema de Python
El elemento primordial de trabajo en Numpy es el arreglo

Existen diferentes tipos de arreglos
-Unidimensionales
-Bidimensionales
-Multidimensionales
'''

import numpy as np

lista1 = [1,2,3,4,5]
arreglo1 = np.array(lista1)

#print(type(arreglo1))

#Creacion de un arreglo a partir de una lista de listas
lista2 = [[1,2,3],
          [4,5,6],
          [7,8,9]]
arreglo2 = np.array(lista2)

#Las listas pueden contener diversos tipos de datos
lista = ["a",True,1]

# Los arreglos solo pueden tener un mismo tipo de datos
# Usan menos espacio en memoria
arreglo = np.array(lista)
#print(arreglo) # Convirtio todos los valores a string --> "a","True","1"

#Creacion de arreglos con ceros
arreglo3 = np.zeros((5,4))
#print(arreglo3) #Genera un arreglo de puros 0 de 5 filas y 4 columnas todaas en 0

# Creacion de arreglos con numeros aleatorios uniformes entre 0 y 1
np.random.random((3, 2)) # Genera numeros aleatorios entre 0 y 1  de 3 filas y 2 columnas

# Creacion de arreglos en un rango
np.arange(-2,7) #Crea un arreglo unidimensional de -2 hasta 6
np.arange(5) # Aqui es lo mismo pero utiliza el inicio del arreglo desde 0 y termina en el 4

'''
Creacion de un arreglo Multidimensional
'''

#Primero creamos arreglos bidimensionales
arreglo1 = np.array([[1,2],
                     [5,7]])

arreglo2 = np.array([[8,9],
                     [5,7]])

arreglo3 = np.array([[1,2],
                     [5,7]])


arreglo_3D = np.array([arreglo1, arreglo2, arreglo3])
#print(arreglo_3D)

#Arreglos bidimensionales de 0 
arreglo4 = np.zeros((5,4))
#print(arreglo4)
#print(arreglo4.shape) # Resultado --> (5, 4)

#Conversion de un arreglo multi-dimensional a un uni-dimensional
lista5 = [[1,2,3],
          [4,5,6],
          [7,8,9]]
arreglo5 = np.array(lista5)
arreglo5.flatten()

#Cambio de dimension de un arreglo
arreglo6 = np.array([[1,2],
                     [3,4],
                     [5,6]])
arreglo6.reshape(2, 3) # Rediseña el arreglo a 2 filas y 3 columnas en vez de como estaba

# Nota ---> Tiene que tener las mismas dimensiones para la misma cantidad de elementos cuando queremos diseñarlo

'''
Matrices y tensores en NumPY

- Una matriz tiene dos dimensiones (Bidimensional)
- Un tensor tiene tres o mas dimensiones (Multidimensional)


-------------------
Tipos de datos de Python:
-- int
-- float

Tipos de datos en NumPY:
-- np.int64
-- np.int32
-- np.float64
-- np.float32

'''

# El atributo dtype
ejemplo1 = np.array([1.25, 2.43, 200.88]).dtype
#print(ejemplo1) # Resultado: float64

ejemplo2 = np.array([[1,2,3], [4,5,6]]).dtype
#print(ejemplo2) # Resultado: int64

arreglo_string = np.array(["Introduccion","a","la","programacion"]).dtype
#print(arreglo_string) # Resultado: <U12

# Uso de dtype como argumento
arreglo7 = np.array([1.25, 2.43, 200.88], dtype= np.float32) # Mismo arreglo pero cambiando su type
#print(arreglo7.dtype) # Resultado: float32

# Cambio de tipo de arreglo
arreglo_booleano = np.array([[True, False]], dtype= np.bool_)
#print(arreglo_booleano.dtype) # Resultado: bool

arreglo8 = arreglo_booleano.astype(np.int32)
#print(arreglo8) # Resultado: array([[1, 0]], dtype=int32)

# Homologacion del tipo por jerarquia de los elementos
ejemplo3 = np.array([0, 50, 50.8]).dtype
#print(ejemplo3) # Resultado: float64

ejemplo4 = np.array([False, 42])
print(ejemplo4) # Resultado: array([0, 42]) --> Lo convierte a 0 el False

'''
La jerarquia que va a tomar para convertir los numeros seria la siguiente:

- Primero convierte los BOOLEANOS (bool)
- Despues los ENTEROS (int32 & int64)
- Pasando a los valores FLOTANTES (float32 & float64)
- Para finalizar con los valores de tipo cadena (<U12)

'''