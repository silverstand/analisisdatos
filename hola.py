# %%
import numpy as np
array = np.array([1, 2, 3, 4, 5])

# %%
array

# %% [markdown]
# # Esto es un título
# ## Esto es un subtítulo
# Esto es un parágrafo con __negritas__ y _cursivas_.

# %%
import numpy as np
import pandas as pd

tabla = pd.DataFrame(
    np.random.randint(
        0, 100, size=(4, 3)
    ),
    columns=['Pepe', 'María', 'Juan']
)

tabla

# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

tabla = pd.DataFrame(
    np.random.randint(
        0, 100, size=(4, 3)
    ),
    columns=['Pepe', 'María', 'Juan']
)

tabla.plot()
plt.show()

# %%
