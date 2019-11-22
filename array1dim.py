# %%
import numpy as np

arr = np.arange(0, 50, 5)
arr

# %%
arr[0]

# %%
arr[4]

# %%
# El -1 hace referencia a la ultima posicion de la coleccion.
arr[-1]

# %%
arr[0] = 99
arr

# %%
# Slicing
arr[:]

# %%
# Los 3 primeros elementos
arr[:3]

# %%
# Para modificar un rango de forma masiva
arr[1:-1] = 50
arr

# %%
# Reiniciamos el array a como estaba
arr = np.arange(0, 50, 5)

# Extraemos una subarray
sub_arr = arr[0:4]
sub_arr

# %%
sub_arr[:] = 50

sub_arr

# %%
arr

# %%
# Metodo Copy, para hacer una copia del array
arr = np.arange(0, 50, 5)

cop_arr = arr.copy()

cop_arr

# %%
# Modificamos la copia
cop_arr[:] = 50

cop_arr

# %%
# El original deberia estar intacto
arr

# %%
