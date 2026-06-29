import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
Para generar los graficos o que desplegue la ventana tienes que descargar las siguientes librerias

Primero activamos el entorno:
'''

#.\.venv\Scripts\Activate.ps1

'''
Despues instalamos la libreria
python -m pip install matplotlib

'''

'''
fig -> Es el objeto que representa la figura o ventana donde se dibuja el grafico
ax -> Es el objeto que representa el area del grafico, es decir, el espacion donde se dibuja el grafico
'''
#fig, ax = plt.subplots()
#plt.show() # Esto muestra el grafico

#--------------------------------------------------

# Adicion de datos al eje x (meses)
meses = pd.DataFrame(np.array(["Ene","Feb","Mar","Abr","May","Jun","Jul","Aug","Sep",
                               "Oct","Nov","Dic"]), columns=["Meses"])
#print(meses)

# Adicion de datos al eje y (temperaturas promedio por mes en °C)
temperaturas = pd.DataFrame(np.array([20.3,22.5,18.6,21.2,23.3,23.6,
                                       26.4,28.5,25.1,23.3,22.1,21.9]), columns=["Temperaturas"])

#print(temperaturas)


#fig, ax = plt.subplots()
#ax.plot(meses["Meses"], temperaturas["Temperaturas"])
#plt.show() # Esto muestra el grafico

#--------------------------------------------------
# Creacion de DataFrame para temperaturas promedio por mes en °C en la ciudad "X"
temperaturas_x = pd.DataFrame(np.array([18.3,20.5,16.6,19.2,21.3,21.6,
                                        23.4,26.5,23.1,21.3,20.1,19.9]), columns=["Temperaturas"])
#print(temperaturas_x)


# Definimos titulos de los ejes
fig, ax = plt.subplots()
#---------- Modificar el grafico a conveniencia
ax.plot(meses["Meses"], temperaturas["Temperaturas"], color="r") # Color ROJO
ax.plot(meses["Meses"], temperaturas_x["Temperaturas"], color="g") # Color VERDE
ax.set_xlabel("Mes del año") # Aqui definimos nombre para el eje x
ax.set_ylabel("Grados Centigrados") # Aqui definimos nombre para el eje y

plt.show() # Esto muestra el grafico

'''
fig (Figure) → es toda la imagen o ventana completa.
ax (Axes) → es la gráfica que va dentro de esa ventana.

fig, ax = plt.subplots()

Resultado:
+---------------------+
|       fig           |
|  +---------------+  |
|  |      ax       |  |
|  |   gráfica     |  |
|  +---------------+  |
+---------------------+

¿Cómo saber qué poner dentro de ax?

Depende del tipo de gráfica:
Línea	ax.plot(x, y)
Barras	ax.bar(x, y)
Histograma	ax.hist(x)
Dispersión	ax.scatter(x, y)
Pastel	ax.pie(valores)
Caja   ax.boxplot(datos)

Regla rápida
Si el gráfico compara dos variables → normalmente usas x y y.
Si el gráfico muestra la distribución de una sola variable → solo usas una columna.


Gráfica         Variables
Histograma	        1
Boxplot	            1
Barras	            2
Línea	            2
Scatter	            2

Regla de oro para Matplotlib

Antes de escribir el código, responde estas preguntas:

¿Qué quiero mostrar?
Distribución → Histograma o Boxplot
Comparación → Barras
Evolución en el tiempo → Línea
Relación entre variables → Scatter

¿Necesito resumir o agrupar datos primero?
Sí → groupby, count, value_counts, mean, etc, sum.
No → usar columnas directamente.
'''


