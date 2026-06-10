import numpy as np
import pandas as pd

arreglo = np.array([
    ["Bella","Labrador","Cafe",56,24, "2013-07-01"],
    ["Charlie","Poodle","Negro",43,24, "2016-09-16"],
    ["Lucy","Chow Chow","Cafe",46,24, "2014-08-25"],
    ["Cooper","Schnauzer","Gris",49,17, "2011-12-11"],
    ["Bernie","San Bernardo","Blanco",77,74, "2018-02-27"],
    ["Max","Chow Chow","Blanco", 45, 28, "2019-03-27"],
    ["Reed","Schnauzer","Negro", 45, 15, "2017-09-18"]
    ])
#print(arreglo)
df = pd.DataFrame(arreglo, columns=["Nombre","Raza","Color","Altura_cm","Peso_kg","Fecha_nacimiento"])
df["Altura_cm"] = df["Altura_cm"].astype(int)
df["Peso_kg"] = df["Peso_kg"].astype(int)
#print(df)


#------------------------------------------------------
#Calculo de la media
media_peso = df["Peso_kg"].mean()
print("Media del peso:", media_peso)

#-------------------------------------------------------
#Calculo de fecha de nacimiento mas antigua
fecha_antigua = df["Fecha_nacimiento"].min()
print("Fecha de nacimiento más antigua:", fecha_antigua)

#-------------------------------------------------------
#Funcion de agregacion estadistica
def percentil80(columna):
    return columna.quantile(0.8)

agregacion_estadistica = df["Altura_cm"].agg(percentil80)
print("Percentil 80 de la altura:", agregacion_estadistica)

#-------------------------------------------------------
#Agrupacion estadisitica en varias columnas
agrupacion_estadistica = df[["Altura_cm", "Peso_kg"]].agg(percentil80)
print("Percentil 80 de la altura y peso:\n", agrupacion_estadistica)

#-------------------------------------------------------
#Aplicacion de estadisticas multiples
def percentil90(columna):
    return columna.quantile(0.90)
estadisticas_multiples = df["Altura_cm"].agg([percentil80, percentil90])
print("Estadísticas múltiples de la altura:\n", estadisticas_multiples)

#-------------------------------------------------------
print(df["Altura_cm"])

#-------------------------------------------------------
#Suma acumulada de elementos
suma_acumulada = df["Altura_cm"].cumsum()
print("Suma acumulada de la altura:\n", suma_acumulada)

#-------------------------------------------------------
#Suma acumulada de elementos minimos
suma_acumulada_minimos = df["Altura_cm"].cummin()
print("Suma acumulada de los mínimos de la altura:\n", suma_acumulada_minimos)

#-------------------------------------------------------
#Conteo de elementos
conteo_acumulado = df["Raza"].value_counts()
print("Conteo acumulado de razas:\n", conteo_acumulado)

#-------------------------------------------------------
#Proporcion de elementos en porcentaje
proporcion_porcentaje = df["Raza"].value_counts(normalize=True)
print("Proporción de razas en porcentaje:\n", proporcion_porcentaje)

#-------------------------------------------------------
#Resumen de datos por grupo
print(df[df["Color"] == "Blanco"]["Peso_kg"].mean())
print(df[df["Color"] == "Cafe"]["Peso_kg"].mean())
print(df[df["Color"] == "Gris"]["Peso_kg"].mean())
print(df[df["Color"] == "Negro"]["Peso_kg"].mean())

#-------------------------------------------------------
#Resumen de datos por grupo (MEJOR OPCION)
print(df.groupby("Color")["Peso_kg"].mean())

#-------------------------------------------------------
#Agrupacion por color en base a diversas estadisticas
print(df.groupby("Color")["Peso_kg"].agg([min, max, sum]))

#-------------------------------------------------------
#Agrupacion por color y raza en base a la media del peso
print(df.groupby(["Color","Raza"])["Peso_kg"].mean())

#-------------------------------------------------------
#Uso de tablas pivote en python
tabla_pivote = df.pivot_table(values = "Peso_kg", index = "Color", aggfunc = [np.mean, np.median])
print("Tabla pivote de peso por color:\n", tabla_pivote)

#-------------------------------------------------------
#Obtencion de promedios para dos variables
tabla_pivote_dos_variables = df.pivot_table(values = "Peso_kg", index = "Color", columns = "Raza")
print("Tabla pivote de peso por color y raza:\n", tabla_pivote_dos_variables)

tabla_pivote_dos_variables2 = df.pivot_table(values = "Peso_kg", index = "Color", columns = "Raza", fill_value = 0)
print("Tabla pivote de peso por color y raza:\n", tabla_pivote_dos_variables2)

#-------------------------------------------------------
#Obtencion de promedios para dos variables: Mejor #2
tbl_pivote_mas_variables = df.pivot_table(values = "Peso_kg", index = "Color", columns = "Raza", fill_value = 0, margins = True, aggfunc = np.mean)
print("Tabla pivote de peso por color y raza con totales:\n", tbl_pivote_mas_variables)

#-------------------------------------------------------
#Obtencion de medias para dos variables
tbl_pivote = df.pivot_table(values = "Peso_kg", index = "Color", columns = "Raza", fill_value = 0, margins = True, aggfunc = np.median)
print("Tabla pivote de peso por color y raza con totales:\n", tbl_pivote)