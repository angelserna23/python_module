'''
La recursividad consiste en funciones que se llaman a si mismas, evitando el uso
de bucles y otros iteradores

Las llamadas recursivas suelen ser muy utiles en casos muy puntuales, pero debido
a su gran factibilidad de caer en interacion infinitas, deben extramarse las medidas
preventivas adecuadas.
'''

def imprimir(x):
    if x > 0:
        imprimir(x - 1)
        print(x)

imprimir(3)

#------------------------------------------
# Suma de una lista sin recursividad
def suma(lista):
    suma = 0
    for i in range(0, len(lista)):
        suma += lista[i]
    return suma
print(suma([1, 2, 3, 4, 5]))

# Suma de una lista con recursividad
def suma_recursiva(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + suma_recursiva(lista[1:])

print(suma_recursiva([1, 2, 3, 4, 5])) 

#------------------------------------------
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(10))

#------------------------------------------
# Cuidado con el uso de recursividad:
# print(factorial(4200)) # Esto puede causar un error de desbordamiento de pila (stack overflow)
