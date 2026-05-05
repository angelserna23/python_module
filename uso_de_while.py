#El uso de while se utiliza para ciclos cuando no sabemos cuando van a terminar.

n = 4

while n > 0:
    print(n)
    n -= 1
print("Fin")

n = 1
while n > 1:
    print("Uno")
    print("Dos")
print("Fin")

#---------------------------------
'''
Uso de break --> se sale del ciclo while
Uso de continue --> se brinca las instrucciones restantes y regresa al principio del ciclo while
'''

while True:
    linea = input("Escibe un texto: ")

    if linea == "Fin":
        break
    print(linea)
print("Proceso terminado")

#---------------------------------

while True:
    linea = input("Escribe un texto: ")
    if linea[0] == "#":
        continue
    if linea == "Fin":
        break
    print(linea)
print("Proceso terminado")

#---------------------------------
i = 1
while i < 6:
    print(i)
    i += 1