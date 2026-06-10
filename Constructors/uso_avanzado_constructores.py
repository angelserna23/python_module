'''
Tipos de constructores:
-Constructores predeterminados: 
    El constructor predeterminado es un constructor simple que no
    acepta ningun argumento. Su definicion tiene solo un argument que es una referente a la isntancia
    que se esta construyendo
'''

class Expertos:
    def __init__(self):
        self.text = "Sesion experta"
    
    def imprime_texto(self):
        print(self.text)

elemento = Expertos()
elemento.imprime_texto()

#--------------------------------
'''
-Constructores parametrizados:
    Es aquel constructor con parametros que toma su primer argumento como una referencia
    a la instancia que se esta construyendo conocida como self y el resto de los argumentos
    son proporcionados por el programador.
'''
class Adicion:
    def __init__(self, primero, segundo):
        self.primero = primero
        self.segundo = segundo
    
    def calcula(self):
        self.respuesta = self.primero + self.segundo
    
    def mostrar(self):
        print(f"Primer numero = {str(self.primero)}")
        print(f"Segundo numero = {str(self.segundo)}")
        print(f"Respuesta = {str(self.respuesta)}")

elemento2 = Adicion(5, 10)
elemento2.calcula()
elemento2.mostrar()

#--------------------------------
'''
-Herencias:
    La herencia simple tiene lugar cuando una clase hija hereda los atributos y metodos
    de una unica clase padre
'''
class Estudiante(object): #Clase padre
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre
    
class Derecho(Estudiante): #Clase hija
    def presentarse(self):
        print(f"Soy {self.nombre} y tengo {self.edad} años")

Manuel = Derecho(20, "Manuel")
Manuel.presentarse()

#--------------------------------
'''
-Herencia multiple:
    Los casos de herencia multiple en Python se dan cuando una clase secundaria o hija
    hereda atributos y metodos de mas de una clase principal o padre. Basta con separar
    con una coma ambas clases principales a la hora de crear la clase secundaria
'''
# Ejemplo de herencia multiple
class Estudiante2(object): #Clase padre 1
    def __init__(self, edad, nombre):
        self.edad = edad
        self.nombre = nombre

class Instituto(object): #Clase padre 2
    def presentarinstituto(self):
        print("Estudio en el instituto de leyes")

class Derecho2(Estudiante2, Instituto): #Clase hija
    def presentarse(self):
        print(f"Soy {self.nombre} y tengo {self.edad} años y estudio derecho")

Manuel2 = Derecho2(20, "Manuel Contreras")
Manuel2.presentarse()
Manuel2.presentarinstituto()

#--------------------------------}
# Ejercicio 
class Figura(object): #Clase padre
    def area(self):
        pass

class Circulo(Figura): #Clase hija 1
    '''Objeto de tipo Circulo'''
    def __init__(self, radio = 0):
        self.radio = radio
    
    def area(self):
        return 3.14 * (self.radio ** 2)

class Triangulo(Figura): #Clase hija 2
    '''Objeto de tipo Triangulo'''
    def __init__(self, base = 0, altura = 0):
        self.base = base
        self.altura = altura
    
    def area(self):
        return (self.base * self.altura) / 2

c = Circulo(5)
print(c.area())

t = Triangulo(3, 5)
print(t.area())