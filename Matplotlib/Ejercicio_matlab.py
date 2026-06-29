import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Matplotlib/titanic.csv")


#print(df)

conteo_clases = df["Pclass"].value_counts().sort_index()
fig, ax = plt.subplots()
bar = ax.bar(conteo_clases.index, conteo_clases.values)

plt.xlabel("Clase de pasajero")
plt.ylabel("Numero de pasajeros")
plt.title("Numero de pasajeros por clase")
plt.show()
