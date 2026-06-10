elementos = dict()

elementos['dinero'] = 10
elementos['dulces'] = 20
elementos['amigos'] = 5

print(elementos) #{'dinero': 10, 'dulces': 20, 'amigos': 5}

print(elementos['dulces']) #20

# En listas
lista = list()
lista.append(20)

#print(lista) #20

diccionario = {}
diccionario['edad'] = 45

#print(diccionario) #{'edad': 45}

conteo = dict()
nombres = ['pedro','juan','juan', 'ramiro']

# Para cada nombre en la de nombres
# Checar si el nombre ya existe en el direccionario "conteo"
# Si el nombre no esta la lista, inicializar su frecuencia en 1
# En caso contrario (ya esta en la lista), incrementar su frecuencia 

for nombre in nombres:
    if nombre not in conteo:
        conteo[nombre] = 1
    else:
        conteo[nombre] = conteo[nombre] + 1

#print(conteo)

archivo = open("trabalenguas.txt")
#contenido = archivo.read() # Nos sirve para leer lo que esta en un archivo
#print(contenido)

for texto in archivo:
    palabras = texto.split()
    #print(palabras)

conteo2 = dict()

for nombre in palabras:
    if nombre not in conteo2:
        conteo2[nombre] = 1
    else:
        conteo2[nombre] = conteo2[nombre] + 1
print(conteo2)