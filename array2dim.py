# %%
import numpy as np

arr_2d = np.array(([0,5,10], [15,20,25], [30,35,40]))

arr_2d

# %%
# Primera fila
arr_2d[0]

# %%
# Primera fila y primera columna
arr_2d[0][0]

# %%
arr_2d[-1][-1]

# %%
arr_2d[-1][0] = 99

arr_2d

# %%
#Slicing
arr_2d[:,:]

# %%
#Subarray de las 2 primeras filas
arr_2d[:2,:]

# %%
#Un array de la primera columna
arr_2d[:,:1]

# %%
#Modificar la segunda columna
arr_2d[:,1:2] = 0

arr_2d

# %%
#Fancy index
arr_2d = np.zeros((5,10))

arr_2d

# %%
# La 3 3-1
arr_2d[2] = 10

arr_2d

# %%
#Primera fila, tercera y ultima
arr_2d[[0,2,-1]] = 99
       
arr_2d

# %%
#Doblando indices
arr_2d[[4,0,1,0,4]]

# %%
for row in arr_2d:
    print(row)

# %%
for i, row in enumerate(arr_2d):
    arr_2d[i] = i
    
arr_2d

# %%
