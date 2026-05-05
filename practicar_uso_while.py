n = int(input("Capture el valor de n: "))
suma = 0
i = 1

while i <= n:
    suma += i
    i += 1
print("La suma es: ", suma)

#--------------------------------
lista = ["a","b","c"]
while lista:
    print(lista.pop(-1)) # Imprime el último elemento de la lista y lo elimina
print(lista)

#--------------------------------
#Uso de while en una sola linea
n = 5
while n > 0: n -= 1; print(n)

#--------------------------------
numeros = (1,2,3,4,5,6,7,8,9)
valores = len(numeros)
impares = 0
pares = 0
contador = 1

while contador <= valores:
    if numeros[contador - 1] % 2 == 0:
        pares += 1
    else:
        impares += 1
    contador += 1
print("Numero de valores pares: ", pares)
print("Numero de valores impares: ", impares)

#--------------------------------
x,y = 0,1
print(x)
print(y)

while x + y < 50:
    x = x + y
    print(x)

    y = x + y
    print(y)

#--------------------------------
x, y = 0,1
while y < 50:
    print(y)
    x,y = y, x + y # Asigna el valor de y a x y el valor de x + y a y

