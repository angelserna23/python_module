'''
Que es una funcion?
Una funcion represnta un subrutina que dado uno o mas parametros
de entrada devuelve un resultado como salida.

La creacion de funciones en Python tiene un doble prposito:
1. Divir y organizar el codigo en partes mas sencillas
2. Encapsular el codigo que se repite a lo largo de un programa para ser reutilizado

Estructura de una funcion en Python:
def nombre_de_la_funcion(parametros):
    # cuerpo de la funcion
    return resultado

def --> palabra reservada para definir una funcion
nombre_de_la_funcion --> es el identificador
parametros --> lista de parametros (opcional)
cuerpo de la funcion --> bloque de codigo que se ejecuta cuando se llama a la funcion
return --> palabra reservada para devolver un resultado (opcional)

'''

def saludo():
    print("Hola, bienvenido a Python!")

saludo() # Llamada a la funcion

#------------------------
def saludo_nombre(nombre):
    print("Hola " + nombre)
saludo_nombre("Juan") # Llamada a la funcion con argumento

#------------------------
#Area de un circulo
def circulo_area(radio):
    area = 3.1416 * radio ** 2
    return area
mi_area = circulo_area(2)
print("El area del circulo es: " + str(mi_area))

#------------------------
#Funcion con varios parametros
def producto(x1,x2):
    return x1 * x2

resultado = producto(3,4)
print("El producto es: " + str(resultado))

#------------------------
#Funcion con valores predeterminados
def suma(a, b=3):
    return a + b
resultado1 = suma(5) # b toma el valor predeterminado de 3
print("La suma es: " + str(resultado1))

#------------------------
def duplica(numero):
    x = numero * 2
    return x
print(duplica(4)) # Llamada a la funcion con argumento 4

#------------------------
def mi_funcion(*amigos):
    print("Mi mejor amigo es: " + amigos[2])
mi_funcion("Pedro","Juan","Linus","Jose") # Llamada a la funcion con varios argumentos

#------------------------
def chicos(chico1, chico2, chico3):
    print("El niño mas joven es: " + chico3)
chicos(chico3 = "Emilio", chico1 = "Tobias", chico2 = "Armando")

#------------------------
#El doble asterisco (**) se utiliza para pasar un numero variable de argumentos con nombre a una funcion.
def apellido(**chico):
    print("El apellido es: " + chico["apellido"])

apellido(npila = "Juan", apellido = "Suarez", edad = 15)

#------------------------
def pais(country = "Mexico"):
    print("Soy de " + country)
pais("Argentina")
pais()

#------------------------
#Uso de instruccion pass
def funcion_vacia():
    pass
funcion_vacia() # Llamada a la funcion vacia, no hace nada pero no genera error

#------------------------
#Pase de listas en funciones
def lista_comida(comida):
    for i in comida:
        print(i)

frutas = ["manzana","fresa","sandia"]
lista_comida(frutas)