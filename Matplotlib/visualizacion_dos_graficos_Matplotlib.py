import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

meses = pd.DataFrame(np.array(["Ene","Feb","Mar","Abr","May","Jun","Jul","Aug","Sep",
                               "Oct","Nov","Dic"]), columns=["Meses"])

temperaturas = pd.DataFrame(np.array([20.3,22.5,18.6,21.2,23.3,23.6,
                                       26.4,28.5,25.1,23.3,22.1,21.9]), columns=["Temperaturas"])

temperaturas_x = pd.DataFrame(np.array([18.3,20.5,16.6,19.2,21.3,21.6,
                                        23.4,26.5,23.1,21.3,20.1,19.9]), columns=["Temperaturas"])

#(2, 1) -> Esto nos separa los graficos en dos
#sharey=True -> Permite compartir la misma escala en los dos graficos

fig, ax = plt.subplots(2, 1, sharey=True)
ax[0].plot(meses["Meses"], temperaturas["Temperaturas"], color="r")
ax[1].plot(meses["Meses"], temperaturas_x["Temperaturas"], color="g")
ax[1].set_xlabel("Mes del año")
ax[0].set_ylabel("Temperatura Global")
ax[1].set_ylabel("Temperatura Cd.X")

plt.show() # Esto muestra el grafico

