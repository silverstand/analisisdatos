# %%
# Dibujos con subgráficos
import numpy as np
import matplotlib.pyplot as plt

plt.subplot(1, 3, 1)  # Tabla 1x3 y dibujaremos en la celda 1
plt.plot(np.random.randint(100, size=[6]), label="Pedro", color="green")
plt.ylim(0, 100)
plt.legend()

plt.subplot(1, 3, 2)  # Tabla 1x3 y dibujaremos en la celda 2
plt.plot(np.random.randint(100, size=[6]), label="Marta", color="red")
plt.ylim(0, 100)
plt.legend()

plt.subplot(1, 3, 3)  # Tabla 1x3 y dibujaremos en la celda 3
plt.plot(np.random.randint(100, size=[6]), label="Ana", color="cyan")
plt.ylim(0, 100)
plt.legend()

plt.show()  # Dibujamos el conjunto

# %%
# Dibujando 9 subgráficos
for i in range(9):
    plt.subplot(3, 3, i+1)  # Tabla 3x3
    plt.plot(np.random.randint(100, size=[6]))
    plt.plot(np.random.randint(100, size=[6]))
    plt.ylim(0, 100)

plt.show()

# %%
