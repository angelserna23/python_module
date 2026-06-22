# Liga de ejemplo
#https://forum.easydatatransform.com/t/olympic-medals-table-csv/289

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Matplotlib/olympic-medals.csv")
#print(df)

# Renombrar los indices de los paises (le quitamos la numeracion de filas)
df = pd.read_csv("Matplotlib/olympic-medals.csv", index_col=0)
#print(df)

# Asignamos los top 10 con medallas
medallas = df.head(10)
#print(medallas)

# Revisar con un grafico de barras la distribucion de medallas
'''
fig, ax = plt.subplots()
ax.bar(medallas.index, medallas["Gold"])
ax.set_xticklabels(medallas.index, rotation=90) # Rotar los titulos a 90° para que quepan en el grafico
ax.set_ylabel("Numero de medallas")
ax.legend(["Gold"])
plt.show()
'''

# Agregar las medallas de de plata "stackeadas"  encima de las de de oro
'''
fig, ax = plt.subplots()
ax.bar(medallas.index, medallas["Gold"]) # Barra de oros
ax.bar(medallas.index, medallas["Silver"], bottom=medallas["Gold"]) 
ax.set_xticklabels(medallas.index, rotation=90)
ax.set_ylabel("Numero de medallas")
ax.legend(["Gold","Silver"])
plt.show()
'''
# Barra de bronce encima de las de plata y oro
'''
fig, ax = plt.subplots()
ax.bar(medallas.index, medallas["Gold"]) # Barra de oros
ax.bar(medallas.index, medallas["Silver"], bottom=medallas["Gold"]) # Barra de plata encima de las de oro
ax.bar(medallas.index, medallas["Bronze"], bottom=medallas["Gold"] + medallas["Silver"]) # Barra de bronce encima de las de plata
ax.set_xticklabels(medallas.index, rotation=90)
ax.set_ylabel("Numero de medallas")
ax.legend(["Gold","Silver","Bronze"])
plt.show()
'''

# Creacion de un histograma de oro
'''
fig, ax = plt.subplots()
ax.hist(df["Gold"], bins=[0,5,10,15,20,25,30,35,40], histtype="step")
plt.show()
'''
# Creacion de dos histogramas en un solo grafico (Oro + Plata)
# bins --> sirve para determinar el salto entre cada grafico para que no se vean tantos numeros
# histtype="step" --> quitar el color de adentro de la grafica para que solo queden las lineas

'''
fig, ax = plt.subplots()
ax.hist(df["Gold"], bins=[0,5,10,15,20,25,30,35,40], histtype="step")
ax.hist(df["Silver"], bins=[0,5,10,15,20,25,30,35,40], histtype="step")
ax.set_xlabel("# de medallas")
ax.set_ylabel("# de observaciones")
ax.legend(["Gold","Silver"])
plt.show()
'''

# Creacion de diagramas de caja
'''
fig, ax = plt.subplots()
ax.boxplot([df["Gold"], df["Silver"]])
ax.set_xticklabels(["Oro","Plata"])
ax.set_ylabel("# de medallas")
plt.show()
'''

# Creacion de graficos de dispersion
'''
fig, ax = plt.subplots()
ax.scatter(df["Gold"], df["Silver"])
ax.set_xlabel("# de medallas de oro")
ax.set_ylabel("# de medallas de plata")
plt.show()
'''

# Creacion de graficos de dispersion multiples
'''
fig, ax = plt.subplots()
ax.scatter(df["Gold"], df["Silver"], color="red", label="Plata")
ax.scatter(df["Gold"], df["Bronze"], color="blue", label="Bronce")
ax.set_xlabel("# de medallas de oro")
ax.set_ylabel("# de medallas")
ax.legend()
plt.show()
'''

# Creacion de graficos de dispersion con degradado en color
df = pd.read_csv("Matplotlib/olympic-medals.csv")
#print(df)

fig, ax = plt.subplots()
ax.scatter(df["Gold"], df["Silver"], c= df.index)
ax.set_xlabel("# de medallas de oro")
ax.set_ylabel("# de medallas de plata")
plt.show()