# %%
import numpy as np
import matplotlib.pyplot as plt

ahorros = np.random.randint(100, size=[6])
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
mapeado = range(len(meses))

plt.plot(ahorros)                         # Añadimos el gráfico
plt.xticks(mapeado, meses)                # Mapeamos los valores horizontales
plt.xlim(2, 4)                            # Configuramos el límite horizontal
plt.title("Ahorros del primer semestre")  # Configuramos el título
plt.xlabel("Meses")                       # Configuramos la etiqueta del eje X
plt.ylabel("Cantidad en €")               # Configuramos la etiqueta del eje Y
plt.show()                                # Finalmente lo mostramos

# %%
# Mostramos una leyenda
plt.plot(ahorros)                         # Añadimos el gráfico
plt.xticks(mapeado, meses)                # Mapeamos los valores horizontales
plt.xlim(2, 4)                            # Configuramos el límite horizontal
plt.title("Ahorros del primer semestre")  # Configuramos el título
plt.xlabel("Meses")                       # Configuramos la etiqueta del eje X
plt.ylabel("Cantidad en €")               # Configuramos la etiqueta del eje Y
plt.legend(loc=4)                         # Mostramos la leyenda
plt.show()                                # Finalmente lo mostramos

# %%
# Mostramos una leyenda con un texto
plt.plot(ahorros, label="Evolución")      # Añadimos el gráfico con un texto
plt.xticks(mapeado, meses)                # Mapeamos los valores horizontales
plt.xlim(2, 4)                            # Configuramos el límite horizontal
plt.title("Ahorros del primer semestre")  # Configuramos el título
plt.xlabel("Meses")                       # Configuramos la etiqueta del eje X
plt.ylabel("Cantidad en €")               # Configuramos la etiqueta del eje Y
plt.legend()                              # Mostramos la leyenda automáticamente
plt.show()                                # Finalmente lo mostramos

# %%
# Mostramos los ahorros de tres personas diferentes
import numpy as np
import matplotlib.pyplot as plt

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
mapeado = range(len(meses))

plt.plot(np.random.randint(100, size=[6]), label="Pedro")
plt.plot(np.random.randint(100, size=[6]), label="Marta")
plt.plot(np.random.randint(100, size=[6]), label="Ana")
plt.xticks(mapeado, meses)
plt.xlim(2, 4)
plt.title("Ahorros del primer semestre")
plt.xlabel("Meses")
plt.ylabel("Cantidad en €")
plt.legend()
plt.show()

# %%
# Tablas de multiplicar del 1 al 10
for t in range(1, 11):
    plt.plot(
        range(1, 11),                   # Eje X
        [t * n for n in range(1, 11)],  # Eje Y
        label=f"Tabla del {t}"          # Leyenda
    )
plt.title('Tablas')
plt.xlabel('Número')
plt.ylabel('Resultado')
plt.legend()
plt.show()

# %%
