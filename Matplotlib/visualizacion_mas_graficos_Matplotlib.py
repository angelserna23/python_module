import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

meses = pd.DataFrame(np.array(["1","2","3","4","5","6","7","8","9","10","11","12"]), columns=["Meses"])

temperaturas = pd.DataFrame(np.array([20.3,22.5,18.6,21.2,23.3,23.6,
                                       26.4,28.5,25.1,23.3,22.1,21.9]), columns=["Temperaturas"])

temperaturas_x = pd.DataFrame(np.array([18.3,20.5,16.6,19.2,21.3,21.6,
                                        23.4,26.5,23.1,21.3,20.1,19.9]), columns=["Temperaturas"])

#(2, 1) -> Esto nos separa los graficos en dos
#sharey=True -> Permite compartir la misma escala en los dos graficos

fig, ax = plt.subplots(3, 2, sharex=True, sharey=True)
ax[0, 0].plot(meses["Meses"], temperaturas["Temperaturas"], color="r")
ax[0, 1].plot(meses["Meses"], temperaturas_x["Temperaturas"], color="g")
ax[0, 0].set_ylabel("Temperatura")
ax[0, 0].set_xlabel("Global")
ax[0, 1].set_xlabel("Cd. X")
plt.show() # Esto muestra el grafico