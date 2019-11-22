# %%
import numpy as np

# Generamos un array con números aleatorios repetidos
arr = np.random.randint(0, 4, 10)
arr

# Aplicamos el filtro unique
np.unique(arr)

# %%
#Filtro in1d
np.in1d([-1, 3, 2], arr)

# %%
# Generamos un array con números aleatorios
arr_1 = np.random.uniform(-5, 5, size=[3,2])
arr_1

# %%
# Creamos un filtro que establece los negativos a 0
arr_2 = np.where(arr_1<0, 0, arr_1)
arr_2


# %%
# Añadimos otro filtro que establece los positivos a 1
arr_2 = np.where(arr_2>0, True, arr_2)
arr_2

# %%
# Comprobar si todos los elementos de un array son True
arr_bool = np.array([True,True,True,False])
arr_bool.all()

# %%
# Comprobar al menos un elemento del array es True
arr_bool = np.array([True,True,True,False])
arr_bool.any()

# %%
# También aplican a un eje en particular
arr_bool = np.array([[True,True],[False,True],[True,True]])
arr_bool

# %%
# Columas verdaderas
arr_bool.all(0)

# %%
# Filas verdaderas
arr_bool.all(1)

# %%
