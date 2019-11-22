# %%
import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
arr

# %%
# Tranpuesta
arr.T


# %%
# Tranpuesta de la transpuesta
arr.T.T


# %%
# Intercambiar las filas por las columnas
arr.swapaxes(0,1)
arr.swapaxes(1,0) # Es lo mismo

# %%
# Creamos un array 3d
arr_3d = np.arange(8).reshape(2,2,2)
arr_3d


# %%

# Buscamos el array transpuesto
arr_3d.T

# %%
#Intercambiar ejes con swapases
arr_3d.swapaxes(0,2)

# %%
arr_3d.swapaxes(0,1)

# %%
