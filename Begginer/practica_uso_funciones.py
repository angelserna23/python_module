def tabla_del(numero):
    resultado = []
    for i in range(1, 11): #Se coloca hasta el 11 porque el rango no incluye el número final
        '''
        Append es un método de las listas en Python que se utiliza para agregar un elemento al 
        final de la lista. En este caso, se está agregando el resultado de multiplicar el 
        número dado por i a la lista resultado. Cada vez que se ejecuta el ciclo, 
        se calcula el producto y se agrega a la lista, lo que permite construir la tabla de 
        multiplicar del número especificado.
        '''
        resultado.append(numero * i)
    return resultado
'''
for valor in range(1, 11):
    print(tabla_del(valor))
'''

#-----------------------------------------
def Palindromo(cadena):
    izquierda = 0
    derecha = len(cadena) - 1

    while derecha >= izquierda:
        if not (cadena[izquierda] == cadena[derecha]):
            return False
        izquierda += 1
        derecha -= 1
    return True
print(Palindromo("Rayar"))

#-----------------------------------------
#Version 2
def Palindromo2(cadena):
    izquierda = 0
    derecha = len(cadena) - 1

    while derecha >= izquierda:
        if not (cadena[izquierda].lower() == cadena[derecha].lower()):
            return False
        izquierda += 1
        derecha -= 1
    return True
print(Palindromo2("Rayar"))

#-----------------------------------------
#Funcion lambda
'''
La funcion Lambda es una función anónima, es decir, una función sin nombre, 
que se define utilizando la palabra clave lambda.
'''
def cuadrado(x):
    return x ** 2
print(cuadrado(5))

#Funcion lambda Tipo 2
cuadrado_lambda = lambda x: x ** 2
print(cuadrado_lambda(5))

#Funcion lambda Tipo 3
suma = lambda x, y: x  + y
print(suma(2, 3))

#Funcion lambda Tipo 4
print((lambda x, y: x + y)(2, 3))

#------------------------------------------
def Calcular(x):
    return lambda x: x ** 2
resultado = Calcular(2)
print(f"El doble del numero 15 es: {resultado(15)}")

#------------------------------------------
Inicia_con = lambda texto, x: True if x.startswith(texto) else False
print(Inicia_con("Python","p"))