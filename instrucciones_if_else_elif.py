#--------------------------------------------------------
# Instrucciones if, else
x = 4

if x > 2:
    print("Grande")
else:
    print("Pequeño")
print("Terminado 1")

#--------------------------------------------------------
# Instrucciones if, elif, else

x = 2

if x < 2:
    print("x = ", x)
    print("Pequeño")
elif x < 10:
    print("x = ", x)
    print("Mediano")
else:
    print("x = ", x)
    print("Grande")
print("\nTerminado 2")

'''
El comando \n nos sirve para imprimir un salto de línea, 
es decir, para dejar una línea en blanco entre el mensaje "Terminado 1" y "Terminado 2". 
Esto hace que la salida sea más legible al separar visualmente los resultados de las dos 
partes del código.
'''

#--------------------------------------------------------
x = int(input(("Introduce un número: ")))
print("x = ", x)

if x < 2:
    print("Pequeño")
elif x < 10:
    print("Mediano")
else:
    print("Grande")
print("\nTerminado 3")

#--------------------------------------------------------
x = int(input(("Introduce un número: ")))
print("x = ", x)

if x < 2:print("Pequeño")
elif x < 10:print("Mediano")
elif x < 29:print("Grande")
else:print("Gigante")
print("\nTerminado 4")

#--------------------------------------------------------
a = 3
b = 5
print("A") if a > b else print("B")

#--------------------------------------------------------
a = 3
b = 5
print("A es mayor que B") if a > b else print("=") if a == b else print("B es mayor que A")

#--------------------------------------------------------
# Instruccion de pass en python
a = 33
b = 200

if b > a:
    pass