# %%
import numpy as np

# Declaramos un par de arrays de prueba
arr_1 = np.arange(1,6)
arr_2 = np.array([-3,7,3,13,0])

# %%
# Suma
np.add(arr_1, arr_2)

# %%
# Resta
np.subtract(arr_2, arr_1)

# %%
# Raiz cuadrada
np.sqrt(arr_1)

# %%
# Potencia
np.power(arr_1, 2)


# %%
# Signo
np.sign(arr_1)

# %%
# Seno
np.sin(arr_1)

# %%
# CoSeno
np.cos(arr_1)

# %%
# Tangente
np.tan(arr_1)

# %%
# Grados a radianes
np.deg2rad(arr_1)

# %%
# Máximo
np.maximum(arr_1, arr_2)

# %%
# Igual
np.equal(arr_1, arr_2)


# %%
# Mayor
np.greater(arr_1, arr_2)


# %%
# Declaramos un tercer array de prueba
arr_3 = np.array([3.14, 2.57, -6.4, 0.47, 5.5])


# %%
# Valor absoluto
np.fabs(arr_3)

# %%
# Techo (redondeo entero siempre al alza)
np.ceil(arr_3)

# %%
# Suelo (redondeo entero siempre a la baja)
np.floor(arr_3)

# %%
