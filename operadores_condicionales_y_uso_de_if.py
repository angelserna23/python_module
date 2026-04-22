a = 33
b = 200

if b > a:
    print("b es mayor que a")

if 'f' in "fool":
    print('1')
    print('2')
    print('3')

#------------------------------------------------------
if 'f' in 'fool': print('4'); print('5'); print('6')

#------------------------------------------------------
i = 15
if i > 10: print("i es mayor que 10")

#------------------------------------------------------
a = 200
b = 33
c = 500

if a > b and c > a:
    print("Ambas condiciones son verdaderas")

if a > b or c > a:
    print("Al menos una de las condiciones es verdadera")

x = 5

#------------------------------------------------------
if x < 10:
    print("Pequeño")
if x > 20:
    print("Grande")   
print("Fin")

#------------------------------------------------------
x = 5
if x == 5:
    print("Igual a 5") # --> True
if x > 5:
    print("Mayor que 4") # --> True
if x >= 5:
    print("Mayor o igual a 5") # --> True
if x < 6:
    print("Menor que 6") # --> True
if x != 6:
    print("Diferente de 6") # --> True

#------------------------------------------------------
x = int(input("Dame un numero:"))

if float(x) > 1:
    print("Mayor que 1")

    if float(x) < 100:
        print("Menor a 100")
print("Fin del proceso")

#------------------------------------------------------
