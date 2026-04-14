#Una lista se usa con []

amigos = ["Pedro","Juan","Jose"]
print(amigos)

elementos = ["rojo",15,[2,9,8]] #Podemos guardar listas dentro de otras listas
print(elementos)

print(amigos[1]) #Podemos mandar a llamar cada elemento por separado mediante su index

amigos_cercanos = amigos
amigos_cercanos[2] = "Jesus" #Podemos reemplazar valores de las listas llamando a su index y poniendo el nuevo valor
print(amigos_cercanos)

'''Uso de len en listas'''
longitud = len(amigos)
print(longitud)

#--------------------

a = [1,2,3]
b = [4,5,6]
c = a + b #Podemos hacer tambien concatenar listas

print(c)

print(c[1:3])

print(c[2:])

'''Uso de funcion type'''
#La funcion type nos sirve para identificar que tipo de variable es

print(type(c))

'''Uso de funcion dir'''

print(dir(c))

#-------------------------
listado = list()
print(listado)

'''Uso de funcion append'''
#Nos sirve para agregar datos a una lista
listado.append("libro")
listado.append(100)

print(listado)

'''Uso de funcion sort'''
#Nos sirve para organizar una lista por orden alfabetico

amigos.sort()
print(amigos)

'''Uso de funcion max'''
#Nos sirve para encontrar el valor max de una lista
print(max(c))

'''Uso de funcion sum'''
#Nos sirve para sumar todos los elemenots de una lista
print(sum(c))

amigos = "Jose Claudia Ramiro"
lista_amigos = amigos.split()

print(lista_amigos)