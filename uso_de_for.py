#Uso de for
numeros = [6,5,3,8,4,2,5,4,11]
suma = 0

for valor in numeros:
    suma = suma + valor
#print("La suma es: ", suma)

#---------------------------------------------
#Uso de f para concatenar texto con variables
numeros = [6,5,3,8,4,2,5,4,11]
suma = 0

for valor in numeros:
    suma = suma + valor
#print(f"La suma es: {suma}")

#---------------------------------------------
frutas = ["manzana","fresa","cereza"]
for fruta in frutas:
    print(fruta)

#---------------------------------------------
for letra in "Python":
    print(letra)

#---------------------------------------------
total = 0
for i in 5,7,11,13:
    #print(i)
    total += i # El uso del operador += sirve para sumar el valor de i a total.
#print(f"Total: {total}")

#---------------------------------------------
for x in range(6):
    print(x)

for x in range(2,10):
    print(x)

#---------------------------------------------
for x in range(2,10,3): 
    '''
    Aqui lo que hace es que va iterando en el rango de 2 a 10, pero va saltando de 3 en 3, 
    es decir, va a imprimir 2, luego salta a 5, luego a 8, y así sucesivamente 
    hasta llegar a 10.
    '''
    print(x)

for x in range(6):
    print(x)
else:
    print("Proceso terminado")
    