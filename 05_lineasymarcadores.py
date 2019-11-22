# %%
# Personalizamos las líneas
import numpy as np
import matplotlib.pyplot as plt

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
mapeado = range(len(meses))

plt.plot(np.random.randint(100, size=[6]),
         label="Pedro", color="red", ls="-", lw="3")
plt.plot(np.random.randint(100, size=[6]),
         label="Marta", color="#0000ff", ls="--", lw="4")
plt.plot(np.random.randint(100, size=[6]),
         label="Ana", color="green", ls="-.", lw="4")
plt.xticks(mapeado, meses)
plt.legend()
plt.show()

# %%
# %%
# Personalizamos los marcadores

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
mapeado = range(len(meses))

plt.plot(np.random.randint(100, size=[6]),
         marker="o", markersize="8", markeredgewidth="2",
         markerfacecolor="green", markeredgecolor="white")
plt.plot(np.random.randint(100, size=[6]),
         marker="*", markersize="10", markeredgewidth="2",
         markerfacecolor="red", markeredgecolor="white")
plt.plot(np.random.randint(100, size=[6]),
         marker="D", markersize="5", markeredgewidth="2",
         markerfacecolor="orange", markeredgecolor="white")
plt.xticks(mapeado, meses)
plt.legend()
plt.show()

# %%
