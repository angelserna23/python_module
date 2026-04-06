# Ejemplo de asignaciones
'''
Las variables se quedan guardadas con el nombre que asignamos de lado izquierdo

'''
x = 2
print(x)

#Aqui reasginamos a x para que sea asi -> 2 = 2 + 3
## SUMA
x = x + 3
print(x) # Resultado -> 5

## POTENCIA
y = x ** 2
print(y) # Resultado -> 25

## RESIDUO
'''
El residuo funciona como una division pero toma el sobrante:

 23 / 5 = 4.6 (Malo)

 20 / 5 = 4 (Lo que nos sobra es 3)

 Este "3" es nuestro sobrante o residuo y es lo que obtenemos con esta operacion
'''
z = 23 % 5 
print(z) # Resultado -> 3


## OPERACIONES VARIAS
'''
Aqui se toma como la jerarquia de operaciones en donde comenzamos 
    1.- Parentesis
    2.- Potencias
    3.- Multiplicaciones, Divisiones y Residuos
    4.- Sumas y Restas
    5.- De izquierda a derecha
'''
x = 1 + 2 + 3 * 5  / 2

print(x) # Resultado -> 10.5

y = 1 + 2 ** 3 / 4 * 5

print(y) # Resultado -> 11

w = (1+2) ** 3 / 4 * 5

print(w) # Resultado -> 33.75

'''----------------Funcion------------------'''
# TYPE
tipo = type(w)
print(tipo) # Resultado -> float
texto = "Hola"

tipo2 = (type(texto))
print(tipo2) # Resultado -> str

x = 4
tipo3 = type(x)
print(tipo3) # Resultado -> int

a = 10
b = 15
c = a / b

tipo4 = type(c)
print(tipo4) # Resultado -> float

'''----------------Cadenas de texto------------------'''
texto2 = "Hola " +  "mundo"
print(texto2) # Resultado -> "Hola mundo"

'''------------------Convertir variables a int, float, str------------------'''
a = 10
b = 15
c = a / b

convert_int = int(c)
print(convert_int) # Resultado -> 0

convert_float = float(a)
print(convert_float) # Resultado -> 10.0

'''----------------Preguntar a usuario------------------'''
nombre = input("Como te llamas: ")
print("Hola ", nombre,", bienvenido") # Resultado -> Hola Angel, bienvenido

edad = input("Ingresa tu edad: ")
resultado = int(edad) * 2 # Siempre tenemos que convertir a enteros o flotantes el numero
print("Tu edad multiplicada por 2 es:", resultado) # Resultado -> Tu edad multiplicada por dos es 4
