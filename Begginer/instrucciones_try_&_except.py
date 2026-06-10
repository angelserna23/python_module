cadena1 = "123"
entero = int(cadena1)
#print(entero)

cadena = input("Dame un numero positivo: ")
'''
El uso de try y except es para evitar que el 
programa se detenga por un error, en este caso si el usuario 
ingresa un valor que no se pueda convertir a entero, el programa no se detendrá, 
sino que asignará un valor de -1 a la variable entero.

try: Es el bloque de codigo que se va a intentar ejecutar, si no hay ningun error,
 se ejecuta normalmente, pero si hay un error, se salta al bloque de except.

except: Es el bloque de codigo que se ejecuta si hay un error en el bloque de try, en
 este caso, si el usuario ingresa un valor que no se pueda convertir a entero, se ejecuta el bloque de
 except, asignando un valor de -1 a la variable entera
'''

try: 
    entero = int(cadena)
except:
    entero = -1

if entero > 0:
    print("Valor correcto")
else:
    print("Valor incorrecto")

#-------------------------------------------------------------
#USOS AVANZADOOS DE IF
lluvia = False
print("Vamos a","la playa" if not lluvia else "la biblioteca")

x = y = 40
z = x + 1 if x > y else y + 2
print(z)

x = 3
s = ('abc' if  (x == 1) else
     'def' if (x == 2) else
     'ghi' if (x == 3) else
     'mno')
print(s)

print('Si' if ('jkl' in ['abc','def','ghi','jkl']) else 'No')