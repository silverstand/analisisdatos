# %%
import numpy as np

# Primer nivel, 2 elementos en ancho
arr_1d = np.array(
    [1, 2]
)
arr_1d

# Segundo nivel, 2 elementos en ancho por 2 de alto,
# 4 elementos en total
arr_2d = np.array([
    [1, 2], 
    [3, 4]
])
arr_2d

# Tercer nivel, 2 elementos en ancho por 2 de alto 
# por 2 de profundidad, 8 elementos en total
arr_3d = np.array([
    [
        [1, 2], 
        [3, 4]
    ], 
    [
        [5, 6], 
        [7, 8]
    ]
])
arr_3d

# %%
# Cuarto nivel, 2 elementos en ancho por 2 de alto 
# por 2 de profundidad por 2 más, 16 en total
arr_4d = np.array([
    [
        [
            [1, 2], 
            [3, 4]
        ], 
        [
            [5, 6], 
            [7, 8]
        ]
    ], 
    [
        [
            [9, 10], 
            [11, 12]
        ], 
        [
            [13, 14],
            [15, 16]
        ]
    ]
])
arr_4d

# %%
# Array 3d de ceros 2x2x2
arr_3d = np.zeros([2,2,2])
arr_3d
# %%
arr_2d = np.arange(9).reshape(3,3)
arr_2d 

# %%
# Esto no funcionará: 9 != 3x3x3
arr_3d = np.arange(9).reshape(3,3,3)
arr_3d 


# %%
# Esto sí que funcionará: 27 == 3x3x3
arr_3d = np.arange(27).reshape(3,3,3)
arr_3d 


# %%
# Array 4d de unos 2x2x2x2
arr_4d = np.ones([2,2,2,2])
arr_4d


# %%
