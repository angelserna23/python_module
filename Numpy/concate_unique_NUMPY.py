import numpy as np

# Concatenar arreglos
x = np.array([1,2,3])
y = np.array([1,5,6])
concat = np.concatenate((x, y))
#print(concat) # Resultado: [1,2,3,4,5,6]

# Concatenar con arreglos bidimensionales
a = np.array([[1,2,3,4],
              [5,6,7,8]])

b = np.array([[9,10,11,12],
              [13,14,15,16]])

concat2 = np.concatenate((a, b), axis=0) # Concatenar por filas
#print(concat2)

concat3 = np.concatenate((a, b), axis=1) # Concatenar por columnas
#print(concat3)


#------------------------------------------------------------
# Arreglo de valores unicos

x = np.array([1,2,3])
y = np.array([1,5,6])
concat = np.concatenate((x, y))

unique_values = np.unique(concat)
#print(unique_values) # Resultado: [1,2,3,4,5,6]
