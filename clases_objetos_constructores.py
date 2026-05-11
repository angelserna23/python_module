'''
Que es una clase?
- Los atributos son las variables que pertencen a una clase
- Los atributos son siempre publicos y se puede acceder a ellos mediante el punto (.)

- Los metodos son las funciones que pertenecen a una clase
- Los metodos son siempre publicos y se puede acceder a ellos mediante el punto (.)
'''

#Creacion de una nueva clase
class Mi_clase:
    x = 0
    y = 0
    pass

#Creacion de un nuevo objeto a partir de la clase
objeto = Mi_clase
objeto.x = 5
objeto.y = 10

print(objeto.x)
print(objeto.y)

#--------------------------------------------
#Creacion de una nueva clase con atributos iniciales
class Mi_clase2:
    x = 5
    y = 10

objeto2 = Mi_clase2
print(objeto2.x)
print(objeto2.y)

#--------------------------------------------
#Definicion de un metodo para una clase
class Aviso:
    def saludar(self):
        print("¡Hola, mundo!")

objeto3 = Aviso() #Se tiene que colocar los parentsis cuando tengamos un metodo en la clase
objeto3.saludar() 

#--------------------------------------------
#Definicion de una clase para almacenar los datos de estudiantes
class Estudiante:
    def aprobado(self):
        if self.calif >= 60:
            if self.calif >= 60:
                return True
            else:
                return False
estudiante1 = Estudiante()
estudiante1.nombre = "Juan"
estudiante1.calif = 80
aprobo1 = estudiante1.aprobado()
print(f"{estudiante1.nombre}: {aprobo1}")

estudiante2 = Estudiante()
estudiante2.nombre = "Araceli"
estudiante2.calif = 50
aprobo2 = estudiante2.aprobado()
print(f"{estudiante2.nombre}: {aprobo2}")

#--------------------------------------------
#Manejo de un constructor
class Estudiante2:
    def __init__(self, nombre, calif):
        self.nombre = nombre
        self.calif = calif
        
    def aprobado(self):
        if self.calif >= 60:
            return True
        else:
            return False
estudiante3 = Estudiante2("Maria", 90)
aprobo3 = estudiante3.aprobado()
print(f"{estudiante3.nombre}: {aprobo3}")

