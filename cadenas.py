nombre = "Angel"
nombre2 = "Serna"
nombre3 = nombre + " " + nombre2

print(nombre3)

print(nombre[1])

print(nombre[0])

print(nombre3[0:9])

print(nombre3[0:])

print(nombre3[:])

'''Uso de la funcion len'''
print(len(nombre3))

'''Uso de la funcion .lower '''
print(nombre3.lower())

'''Uso de la funcion .upper'''
print(nombre3.upper())

'''Uso de la funcion dir'''
print(dir(nombre3))


#---------------------------------
texto = "Hola amigo"
textomodif = texto.replace("amigo", "amiga")
print(textomodif)

'''Uso de funcion de quitar espacios'''
texto = "    Hola amigo     "
textofix = texto.lstrip()
print(textofix)

'''Uso de funcion para quitar espacios de lado derecho'''
texto = "    Hola amigo      "
textfixright = texto.rstrip()
print(textfixright)

'''Uso de funcion para quitar espacios de lado izquierdo'''
texto = "    Hola amigo      "
textfixleft = texto.strip()
print(textfixleft)
