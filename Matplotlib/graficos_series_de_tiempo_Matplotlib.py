'''
Para generar los graficos o que desplegue la ventana tienes que descargar las siguientes librerias

Primero activamos el entorno:
'''

#.\.venv\Scripts\Activate.ps1

'''
Despues instalamos la libreria
python -m pip install matplotlib

'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Descargamos el CSV para obtener la informacion
#https://datahub.io/core/co2-ppm#data

df = pd.read_csv("Matplotlib/co2-mm-mlo.csv")

# Filtrar desde 2015 usando la columna Date decimal
fechas = df[df["Date"] >= 2015]

'''
fig, ax = plt.subplots()
ax.plot(fechas["Date"], fechas["Average"])
ax.set_title("CO₂ desde 2015")
ax.set_xticks([]) # Con esto eliminamos las labels de los datos inferiores
plt.xlabel("Datos mensuales: 2015-01-01 -- 2018-09-01")
plt.ylabel("CO₂ promedio")
'''
#plt.show()

#--------------------------------------
# Creacion de una funcion que grafica series de tiempo
def grafica_series_tiempo(ejes, x, y, color, etiqueta_x, etiqueta_y):
    ejes.plot(x, y, color=color)
    ejes.set_xlabel(etiqueta_x)
    ejes.set_ylabel(etiqueta_y, color=color)
    ejes.tick_params('y', colors=color)

fig, ax = plt.subplots()
grafica_series_tiempo(ax, fechas["Date"], fechas["Average"], 'blue',"Datos mensuales: 2015-01-01 - 2018-09-01", 'CO2 Average')

ax2 = ax.twinx() # Aqui hacemos que dentro del mismo grafico agreguemos otra informacion para mostrar dos graficos

grafica_series_tiempo(ax2, fechas["Date"], fechas["Trend"], 'red', '', 'CO2 Trend')
ax.set_xticks([])
plt.show()