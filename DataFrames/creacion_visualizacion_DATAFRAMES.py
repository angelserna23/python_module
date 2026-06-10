'''
¿Que es un archivo .CSV?

CSV = "Comma-Separated Values" (Archivo de valores separados por coma)

Diseñado para un manejo optimo en DataFrames, la mayoria de los programas de bases de datos
y hojas de calculo pueden usarlos y/o crearlos

Debido a la flexibilidad de su formato pueden guardar grandes bases de datos en poco espacion en disco
'''

# Opcion 1
import pandas as pd
iris = pd.read_csv("iris.csv")
#print(iris)

#Solo extraer ciertas columnas de nuestro archivo CSV
iris_petal = iris[["petal.length", "petal.width"]]
#print(iris_petal)

#Exportar un archivo CSV
iris_petal.to_csv("Iris_petal.csv") #Automaticamente nos genera un archivo CSV

#------------------------
#Generacion de un histograma en base a nuestros archivos CSV

'''
Para generar los graficos o que desplegue la ventana tienes que descargar las siguientes librerias

Primero activamos el entorno:
.\.venv\Scripts\Activate.ps1

Despues instalamos la libreria
python -m pip install matplotlib

'''
import matplotlib.pyplot as plt

#iris["sepal.length"].hist()
#plt.show()


#-------------------
subintervalos = int(round(len(iris) ** 0.5,0))

#iris["sepal.length"].hist(bins=subintervalos)
#plt.show()

#-------------------
iris_tipo = iris.groupby("variety")["petal.length"].mean()
#print(iris_tipo)

#-------------------
#Grafico de barras
iris_tipo.plot(kind="bar")
plt.show()