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


#-----------------------------------
arreglo = [9,41,12,3,74,15]
numero_mayor = 0
index = 0

for numero in arreglo:
    if numero > arreglo[index]:
        numero_mayor = numero
    else:
        numero_mayor = numero_mayor
    index =+ 1

print(f"El numero mayor del arreglo es: {numero_mayor}")

#--------------------------
frutas = ['manzana','fresa','cereza']
for fruta in frutas:
    print(fruta)
    
    if fruta == "fresa":
        break

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Proceso terminado")

#---------------------------------
base = {'Jose': 85,'Angela': 92,'Miguel': 75,'Ana': 98}
nombre = input("Ingrese el nombre del estudiante que quiera consultar: ")

for estudiante in base:
    if estudiante == nombre:
        print(f"Calificacion: {base[estudiante]}")
        break
else:
    "No se encontrol el estudiante"

#--------------------------------
frutas = ['manzanas','fresa','cereza']
adjetivos = ['roja','grande','deliciosa']

for fruta in frutas:
    for tipo in adjetivos:
        print(fruta, tipo)

#---------------------------------
lista = [10,20,30,40]
for numero in reversed(lista):
    print(numero)


#------------Ejercicio-------------
tablas = int(input("# Numero de tablas a calcular:"))
for i in range(1, tablas + 1):
    print("Tabla de multiplicar del: ", i)
    contador = 1

    while contador < 11:
        print(i * contador, end = ' ') # end --> genera un espacio entre lineas
        contador += 1
    print("\n") #genera un salto de pagina de las lineas