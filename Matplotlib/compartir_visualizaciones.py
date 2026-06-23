# Liga de ejemplo
#https://forum.easydatatransform.com/t/olympic-medals-table-csv/289

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Matplotlib/co2-mm-mlo.csv")
#plt.style.use("ggplot") # Agrega color y diseño al grafico
#plt.style.use("default") # Setea el grafico como la base o default que tiene
#print(df)

fechas = df[df["Date"] >= 2015]

'''
fix, ax = plt.subplots()
ax.plot(fechas["Date"], fechas["Interpolated"])
ax.set_xticks([])
plt.xlabel("Datos mensuales: 2015 - 2018")
plt.ylabel("Emisiones de CO2 promedio")
plt.show()
'''

'''
fig,ax = plt.subplots()
ax.plot(fechas["Date"], fechas["Interpolated"])
ax.set_xticks([])
plt.xlabel("Datos mensuales: 2015 - 2018")
plt.ylabel("Emisiones de CO2 promedio")
plt.show()
'''

#-----------------------------------------------

#Existen diferentes tipos de formatos y colores para manejar el Matplotlib
# Estilo "bmh"
'''
plt.style.use("bmh")
fig,ax = plt.subplots()
ax.plot(fechas["Date"], fechas["Interpolated"])
ax.set_xticks([])
plt.xlabel("Datos mensuales: 2015 - 2018")
plt.ylabel("Emisiones de CO2 promedio")
plt.show()
'''

# Estilo "seaborn"
'''
plt.style.use("seaborn-v0_8-colorblind")
fig,ax = plt.subplots()
ax.plot(fechas["Date"], fechas["Interpolated"])
ax.set_xticks([])
plt.xlabel("Datos mensuales: 2015 - 2018")
plt.ylabel("Emisiones de CO2 promedio")
plt.show()
'''

# Estilo "tableau"
'''
plt.style.use("tableau-colorblind10")
fig,ax = plt.subplots()
ax.plot(fechas["Date"], fechas["Interpolated"])
ax.set_xticks([])
plt.xlabel("Datos mensuales: 2015 - 2018")
plt.ylabel("Emisiones de CO2 promedio")
plt.show()
'''

# Estilo "grayscale"
plt.style.use("grayscale")
fig,ax = plt.subplots()
ax.plot(fechas["Date"], fechas["Interpolated"])
ax.set_xticks([])
plt.xlabel("Datos mensuales: 2015 - 2018")
plt.ylabel("Emisiones de CO2 promedio")
plt.show()

# Guardar los graficos generados como png
#fig.savefig("medallas.png")

# Guardar los graficos con una resolucion especifica (a mayor dpi's mayor calidad)
#fig.savefig("medallas.png", dpi=300)

# Guardar en formato jpg
#fig.savefig("medallas.jpg")

