# %%
import numpy as np

# Número decimal entre 0 y 1
np.random.rand()

# %%
# Array 1D de decimales entre 0 y 1
np.random.rand(4)

# %%
# Array 2D de decimales entre 0 y 1
np.random.rand(4,2)

# %%
# Array 3D de decimales entre 0 y N
np.random.uniform(10, size=[2,2,2])


# %%
# Array 4D de decimales entre -N y M
np.random.uniform(-10, 10, size=[2,2,2,2])

# %%
# Número entero entre 0 y N
np.random.randint(10)

# %%
# Array de enteros entre 0 y N
np.random.randint(10, size=[3,2])


# %%
# Array de enteros entre -N y M
np.random.randint(-10, 10, size=[3,2])

# %%
# Array uniforme (con curva gaussiana)
np.random.normal(size=100)

# %%
arr = np.arange(10)

# Desordenar un array (lo cambia)
np.random.shuffle(arr)
arr


# %%
# Generar secuencia permutada a partir de un número
np.random.permutation(10)
arr

# %%
