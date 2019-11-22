# %%
import numpy as np
import matplotlib.pyplot as plt

ahorros = np.random.randint(100, size=[6])
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
mapeado = range(len(meses))

plt.plot(ahorros)           # Añadimos el gráfico
plt.xticks(mapeado, meses)  # Mapeamos los valores horizontales
plt.show()                  # Finalmente lo mostramos

# %%
x = np.arange(6)
y = np.random.randint(20, size=[6])

plt.plot(x, y)
plt.show()

# %%
#Graficos invertidos
plt.plot(y, x)
plt.show()

# %%
# Eje X aleatorio
# %%
x = np.random.randint(20, size=[6])
y = np.random.randint(20, size=[6])

plt.plot(x, y)
plt.show()

# %%
