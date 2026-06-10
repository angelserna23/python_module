#Ejercicio 1
# Suma de dos numeros complejos
class Complejo:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario
    
    def agregar(self, numero):
        real = self.real + numero.real
        imaginario = self.imaginario + numero.imaginario
        resultado = Complejo(real, imaginario)
        return resultado
    
numero1 = Complejo(2, 3)
numero2 = Complejo(5, 6)

suma = numero1.agregar(numero2)
print(f"Parte real: {suma.real}, suma imaginaria: {suma.imaginario}")

#---------------------------------------------
# Ejercicio 2
# La referencia "self" puede tomar cualquier denominacion
class Persona:
    def __init__(objeto, nombre, edad):
        objeto.nombre = nombre
        objeto.edad = edad
    
    def mensaje(objeto):
        print(f"Hola, mi nombre es {objeto.nombre} y tengo {objeto.edad} años.")

persona1 = Persona("Angel", 25)
persona1.mensaje()

#---------------------------------------------
# Ejercicio 3
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def perim(self):
        operacion = self.lado1 + self.lado2 + self.lado3
        return operacion

triangulo1 = Triangulo(4, 5, 4)
perimetro = triangulo1.perim()
print(f"El perimetro del triangulo es: {perimetro}")

