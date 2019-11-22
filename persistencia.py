# %%
import numpy as np

arr_1 = np.random.randint(0,4,[3,3])
arr_1

# %%
# Para guardarlo utilizamos la ruta y la extensin .npy
np.save('arr_1.npy', arr_1)

# %%
# Ahora eliminamos el array  para asegurarnos de que ya no existe
del(arr_1)
arr_1

# %%
# Y lo cargamos de nuevo
arr_1 = np.load('arr_1.npy')
arr_1

# %%
arr_2 = np.random.randint(-4,0,[3,3])

# Utilizaremos savez para guardar de forma comprimida con la extensión .npz
# Especificaremos una clave para cada array que queramos guardar
np.savez('arrays.npz', arr_1=arr_1, arr_2=arr_2)

# %%
# Ahora los borramos
del(arr_1)
del(arr_2)

# %%
# Y los cargamos de nuevo
arrays = np.load('arrays.npy')
arrays

# %%
#Recuperar
arrays['arr_1']

arrays['arr_2']

# %%
# Creamos un array de prueba
arr_3 = np.random.randint(-10,10,[3,3])
arr_3

# %%
# Lo guardamos en un fichero de texto, el formato es libre
np.savetxt('arr_3.txt', arr_3)

# %%
# Columnas con ,
np.savetxt('arr_3.txt', arr_3, delimiter=',')

# %%
# Lo borramos
del(arr_3)

# %%
# Lo cargamos indicando el separador (si lo hemos cambiado)
arr_3 = np.loadtxt('arr_3.txt', delimiter=',')
arr_3

# %%
