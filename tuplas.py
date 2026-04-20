'''
Es un tipo de secuencia que trabaja de manera similar a una 
lista pero en la cual no se puede alterar su contenido. Usamos
parentesis para definirla

Por dicha razo se dice que las tuplas son "inmutables"

Son mas eficientes que las listas en terminos de memoria y rendimiento
'''

x = ('Jose', 'Manuel', 'Alberto')
#print(x[2]) #Alberto

y = (1,4,6)
#print(max(y)) # 6

z = 'ABC'
#print(z[2]) # Error ya que no llega tan lejos

#print(dir(y)) #Nos lanza todas las opciones que tiene esta variable


(x, y) = (4, "Alberto")
#print(x) # 4

diccionario = dict()
diccionario['Alberto'] = 25
diccionario['Pedro'] = 30

#print(diccionario) # {'Alberto': 25, 'Pedro': 30}

tuplas = diccionario.items()
#print(tuplas)

d = {'d': 10, 'b': 15, 'g': 25}
tuplas = sorted(d.items())
print(tuplas)