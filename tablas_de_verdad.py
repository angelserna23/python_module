a = -5
b = 4

# El valor de a  es menor que el valor de b
print(a < b) #TRUE

# El valor de a es mayor que el valor de b
print(a > b) #FALSE

a == -5 # El valor de a es igual al valor -5
print(a == -5) #TRUE

a != -5 # El valor de a es diferente al valor -5
print(a != -5) #FALSE

#----------------------------------------------
##Manejo de conjunciones (AND)
a = -5
b = 4

print(a < 0 and b > 0) #TRUE & TRUE --> TRUE
print(a > 0 and b > 0) #FALSE & TRUE --> FALSE
print(a > 0 and b < 0) #FALSE & FALSE --> FALSE

#----------------------------------------------
##Manejo de DISYUNCIONES (OR)
a = -5
b = 4

print(a < 0 or b > 0) #TRUE & TRUE --> TRUE    
print(a > 0 or b > 0) #FALSE & TRUE --> TRUE
print(a > 0 or b < 0) #FALSE & FALSE --> FALSE

#----------------------------------------------
##Operador de negacion (NOT)
a = -5
b = 4
print(not a > 0) #TRUE

#----------------------------------------------
##Operador de disyuncion opuesta (NOR --> NOT OR)
a = -5
b = 4

print(not (a < 0 or b > 0)) # FALSE
print(not (a > 0 or b < 0)) # TRUE

#----------------------------------------------
##Casos especiales
a = -5
b = 4

a =+ 5 # a = a + 5
print(a < 0) # a = 0 --> FALSE

#----------------------------------------------
b % 3 # Equivalente a: b = b % 3
print(b) # b = 1

#----------------------------------------------
c = 5
c //= 2 # Equivalente a tomar la parte enterda de la division: c = c // 2
print(c) # c = 2

#----------------------------------------------
a = 4
b = 5
print(a is b) # FALSE --> a y b no son el mismo objeto
print(a is not b) # TRUE --> a y b no son el mismo objeto

#----------------------------------------------
text1 = "Hola"
text2 = "Hola"
text3 = "hola"

print(text1 is text2) # TRUE --> text1 y text2 son el mismo objeto
print(text1 is text3) # FALSE --> text1 y text3 no son el mismo

#----------------------------------------------
conjunto = [1, 2, 3, 4, 5]
print(3 in conjunto) # TRUE --> 3 #checar si el 3 esta en la lista conjunto
print(6 in conjunto) # FALSE --> 6 no es un elemento de la lista conjunto

#----------------------------------------------
texto = "Hola Mundo"
print("Hola" in texto) # TRUE --> "Hola" es una subcadena de texto
print("hola" in texto) # FALSE --> "hola" no es una subcadena de texto
