'''
¿Que es un DATA FRAME?
Es una esctructura de datos con dos dimensiones en la cula se puede guardar datos de distintos tipos
(como caracteres, enteros, valores de punto flotante, factores y mas) en columnas, de manera a como se realiza
en una hoja de calculo.

¿Que librerias se usan?
->La libreria PANDAS es una libreria de Python especializada en el manejo y analisis de estructuras de datos.
Las principales caracteristicas de esta libreria son:
- Permite leer y escribir facilmente ficheros en formato CSV, Excel y base de datos SQL.
- Ofrece metodos para reordenar, dividir, y combinar conjuntos de datos de manera eficiente.

-> La libreria NUMPY es una libreria de Python especializada en el calculo numerico y el analsis de datos, 
especialmente para un gran volumen de datos.
- Incorpora una nueva clase de objetos llamados "arrays" (arreglos) que permite representar colecciones de datos
de un mismo tipo en varios dimensiones, y funciones muy eficientes para su manipulacion.
'''
#Ejercicio 1: Crear un DataFrame a partir de un diccionario de listas

#------------------------------------------------------
# Antes de comenzar debemos de verificar que tengamos instalado Python en nuestro equipo
# - Para verificarlo, abrimos la terminal y escribimos el siguiente comando:
# python --version

#------------------------------------------------------
# En caso de no tenerlo instalado, debemos de descargarlo desde la pagina oficial de Python: 
# https://www.python.org/downloads/

#------------------------------------------------------
# Creamos el entorno virtual
# python -m venv .venv

# Ejecutamos el siguiente comando en la terminal para permitir la ejecucion de scripts de PowerShell:
#Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

#------------------------------------------------------
# Despues debemos de activar el entorno de trabajo en la terminal:
# .\.venv\Scripts\Activate.ps1

#------------------------------------------------------
# Instalamos la libreria de numpy
#pip install numpy

#------------------------------------------------------
#Despues mandamos a llamar a la libreria numpy
#import numpy
import numpy as np # Podemos colocarle un alias
#Creamos un arreglo
arreglo = np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(arreglo)

#------------------------------------------------------
#Instalamos la libreria de pandas
#pip install pandas
#pip install pandas-stubs

#------------------------------------------------------
#Despues mandamos a llamar a la libreria pandas
import pandas as pd
df = pd.DataFrame(arreglo)
#print(df)

#------------------------------------------------------
# Modificacion de las columnas del DataFrame
'''
data --> La infomacion que se va a guardar en el DataFrame, puede ser un arreglo, una lista, un diccionario, etc.
index --> Es el indice de las filas del DataFrame, es decir, el nombre que se
columns --> Es el nombre de las columnas del DataFrame
'''
df = pd.DataFrame(data = arreglo, index = ['A','B','C'], columns=['D','E','F'])
#print(df)

#------------------------------------------------------
#Seccion superior (ENCABEZADO)
#print(df.head(2)) # Nos muestra las primeras 2 filas del DataFrame

#-------------------------------------------------------
#Informacion de cada columna
#print(df.info()) # Nos muestra el tipo de dato de cada columna, el numero de filas, etc.

#------------------------------------------------------
#Dimensiones del DataFrame
#print(df.shape) # Nos muestra el numero de filas y columnas del DataFrame

#------------------------------------------------------
#Calculo de estadisticas generales de la tabla
#print(df.describe())# Nos muestra estadisticas generales de cada columna del DataFrame, como la media, la desviacion estandar, el valor minimo, el valor maximo, etc.

#------------------------------------------------------
#Nombre de las columnas del DataFrame
#print(df.columns) # Nos muestra el nombre de las columnas del DataFrame

#------------------------------------------------------
#Nombre de las filas del DataFrame
#print(df.index) # Nos muestra el nombre de las filas del DataFrame

#------------------------------------------------------
#Adicion de un nuevo renglon al DataFrame
df.loc['G'] = [10, 11, 12]
#print(df)

#------------------------------------------------------
#Adicion de una nueva columna al DataFrame
df['H'] = [17,16,15,14]
#print(df)

#------------------------------------------------------
#Seleccion de columnas del DataFrame
df2 = df[["E","F"]]
#print(df2)

#------------------------------------------------------
#Seleccion de filas del DataFrame
df3 = df.iloc[0:2]
#print(df3)

#------------------------------------------------------
#Cambio de nombre de todas las columnas del DataFrame
df.columns = ['Columna1','Columna2','Columna3','Columna4']
#print(df)

#------------------------------------------------------
#Cambio de nombre de una sola columna del DataFrame
df.rename(columns = {'Columna1': 'Column1', 'Columna2': 'Column2'}, inplace = True)
#print(df)

#------------------------------------------------------
#Cambio de nombres en renlones
df.rename(index = {"A": "Dato1", "B": "Dato2"}, inplace=True)
#print(df)

#------------------------------------------------------
#Ordenamiento de DataFrame
df = df.sort_values("Columna4", ascending=True)
#print(df)

#------------------------------------------------------
#Verficacion de condiciones en elementos
validacion = df[df["Column2"] > 5] # Nos muestra un booleano indicando si cada elemento de la columna cumple con la condicion
#print(validacion)

condicion1 = df["Column1"] > 1
condicion2 = df["Column2"] < 12

validacion2 = df[condicion1 & condicion2]
#print(validacion2)

#------------------------------------------------------
# Ejercicio 1
arreglo = np.array([
    ["Bella","Labrador","Cafe",56,24, "2013-07-01"],
    ["Charlie","Poodle","Negro",43,24, "2016-09-16"],
    ["Lucy","Chow Chow","Cafe",46,24, "2014-08-25"],
    ["Cooper","Schnauzer","Gris",49,17, "2011-12-11"],
    ["Bernie","San Bernardo","Blanco",77,74, "2018-02-27"]
    ])
#print(arreglo)

df = pd.DataFrame(data = arreglo, columns = ['Nombre','Raza','Color','Altura_cm','Peso_kg','Fecha_Nac'])
#print(df)

# Inciso 1
df2 = df[df["Fecha_Nac"] < "2015-01-01"]
#print(df2)

#Inciso 2
df["Altura_cm"] = df["Altura_cm"].astype(int)
df3 = df[df["Altura_cm"] > 50]
#print(df3)

#Inciso 3
df["IMM"] = df["Peso_kg"].astype(int) / (df["Altura_cm"].astype(int) / 100) ** 2
#print(df)

#Otras manipulaciones
# Exrtraccion de las columnas Nombre, Raza e IMM
df4 = df[["Nombre","Raza","IMM"]]
df4 = df4.sort_values("IMM", ascending=True)
print(df4)