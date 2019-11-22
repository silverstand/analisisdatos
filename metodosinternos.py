# %%
import numpy as np

# Generamos un array de 2*3 con números aleatorios
arr = np.arange(1,7).reshape(2,3)
arr

# %%
# Sumatorio
arr.sum()


# %%
# Media
arr.mean()

# %%
# Desviación estándard
arr.std()

# %%
# Varianza
arr.var()

# %%
# Ordenar un array
arr = np.random.randint(-10,10,[3,3])
arr

# %%
# Ordenar elementos automáticamente (se ordenan en horizontal y se actualiza el array)
arr.sort()
arr

# %%
# Ordenar verticalmente utilizando el eje 0
arr.sort(0)
arr

# %%
