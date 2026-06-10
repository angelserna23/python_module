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

df = pd.DataFrame(data = arreglo, columns = ["Nombre","Raza","Color","Altura_cm","Peso_kg","Fecha_nac"])
df["Altura_cm"] = df["Altura_cm"].astype(int)
df["Peso_kg"] = df["Peso_kg"].astype(int)

#print(df)

#------------------------------------------------------
#Informacion de las columnas
#print(df.columns)

#------------------------------------------------------
#Informacion sobre los renglones del DataFrame
#print(df.index)

#------------------------------------------------------
#Para establecer una columna como indices (titulos de renglon)
df_ind = df.set_index("Nombre")
#print(df_ind)

#------------------------------------------------------
#Para deshacer la asignacion de indices
df_ind = df_ind.reset_index()
#print(df_ind)

#------------------------------------------------------
#Para remover indices y columnas con informacion de indices
df_ind = df_ind.reset_index(drop=True)
#print(df_ind)

#------------------------------------------------------
#Ventajas de usar indices
# Opcion 1: Busqueda de nombre en base original
#print(df[df["Nombre"].isin(["Bernie", "Max"])])

# Opcion 2: Busqueda de nombres en base con indices de nombres
df_ind = df.set_index("Nombre")
#print(df_ind.loc[["Bernie","Max"]])

#------------------------------------------------------
#Generacion de indices multiples (Indices jerarquicos)
df_ind2 = df.set_index(["Raza","Color"])
#print(df_ind2)

#------------------------------------------------------
#Consultar sobre una caracteristica
#print(df_ind2.loc[["Schnauzer","Poodle"]])

#------------------------------------------------------
#Consultar sobre dos caracteristicas (con tuplas)
#print(df_ind2.loc[[("Schnauzer","Gris"), ("Poodle","Negro")]])

#------------------------------------------------------
#Ordenamiento por primer indice de referencia
#print(df_ind2.sort_index())

#------------------------------------------------------
#Ordenamiento por mas de un indice
#print(df_ind2.sort_index(level=["Color","Raza"], ascending= [True, False]))

#------------------------------------------------------
#Extraccion de los primeros 3 registros
#print(df[:3])

#------------------------------------------------------
#Extraccion de los registros de indice 2 a 4
#print(df[2:5])

#------------------------------------------------------
#Extraccion alternativa de extraer todo el DataFrame
#print(df[:])

#------------------------------------------------------
#Extraccion de DataFrames con indices jerarquicos
df_ind2 = df.set_index(["Raza","Color"])
#print(df_ind2)

#------------------------------------------------------
df_ind2 = df_ind2.sort_index(level="Raza", ascending=True)
#print(df_ind2)

#Extraccion correcta
#print(df_ind2.loc["Chow Chow":"Labrador"])

#------------------------------------------------------
#Para cortar partes de un DataFrame con indices multiples usamos tuplas
#print(df_ind2.loc[("Chow Chow","Cafe"):("Schnauzer","Gris")])

#------------------------------------------------------
#Corte de columnas en DataFrame
df_ind3 = df_ind2.loc[:,"Nombre":"Peso_kg"]
#print(df_ind3)

#------------------------------------------------------
#Extraccion simultanea de ciertos renglones y ciertas columnas
df_ind4 = df_ind2.loc[("Chow Chow","Cafe"):("Schnauzer","Gris"),"Nombre":"Peso_kg"]
#print(df_ind4)

#------------------------------------------------------
#Extraccion simultanea de renglones y columnas
# Opcion alternativa por numero de renglon y numero de columna
#print(df_ind4.iloc[1:3,0:1])

#------------------------------------------------------
#Creacion de la tabla pivote
df_altura_por_raza_color = df.pivot_table("Altura_cm", index = "Raza", columns="Color")
#print(df_altura_por_raza_color)

#------------------------------------------------------
#Extraccion de registros
#print(df_altura_por_raza_color.loc["Labrador":"San Bernardo"])

#------------------------------------------------------
#Calculo de promedios para TODOS los renglones {por columna}
print(df_altura_por_raza_color.mean(axis = "index"))


#------------------------------------------------------
#Calculo de promedios para TODAS las columnas {por renglon}
print(df_altura_por_raza_color.mean(axis = "columns"))