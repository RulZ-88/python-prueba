import pandas as pd
import glob
import os

# Ruta donde están tus archivos Excel
carpeta = 'ruta/a/tu/carpeta'  # por ejemplo: './datos_excel/'
archivos = glob.glob(os.path.join(carpeta, '*.xlsx'))

# Lista para guardar los DataFrames
dataframes = []

for archivo in archivos:
    df = pd.read_excel(archivo)
    dataframes.append(df)

# Concatenar todos los archivos en uno solo
df_final = pd.concat(dataframes, ignore_index=True)

# Guardar el archivo final
df_final.to_excel('resultado_final.xlsx', index=False)





import pandas as pd
import glob
import os
#- `pandas as pd`: importa la librería `pandas`, que es muy poderosa para manejar datos en tablas (como Excel, CSV, etc.).
#- `glob`: permite encontrar archivos según patrones (por ejemplo: `*.xlsx`).
#- `os`: permite interactuar con el sistema de archivos (rutas, carpetas, etc.).





# Carpeta donde están los archivos Excel
carpeta = 'C:/ruta/a/tu/carpeta/'  # reemplaza esto por tu ruta real
archivos = glob.glob(os.path.join(carpeta, '*.xlsx'))
# `os.path.join(...)` construye correctamente una ruta (evita errores de `/` y `\`).
# `glob.glob(...)` busca todos los archivos que terminen en `.xlsx` dentro de esa carpeta.
# **Resultado**: `archivos` es una **lista** con las rutas de todos los Excel encontrados.

#Ejemplo:
#['C:/Users/black/Documentos/excels/file1.xlsx', 'file2.xlsx', ...]



# Lista para guardar cada archivo leído
dataframes = []

for archivo in archivos:
    df = pd.read_excel(archivo)
    dataframes.append(df)

#Recorre uno a uno los archivos Excel encontrados.
#pd.read_excel(archivo) lee el archivo y lo convierte en un DataFrame (df), que es como una tabla en memoria.
#dataframes.append(df) guarda cada DataFrame en la lista dataframes.





# Unir todos los DataFrames en uno solo
df_unido = pd.concat(dataframes, ignore_index=True)
#Guarda la tabla completa unida en un nuevo archivo Excel llamado compilado.xlsx.
#index=False: evita que se agregue una columna extra con el índice (número de fila).



# Guardar el resultado en un nuevo archivo
df_unido.to_excel('compilado.xlsx', index=False)
print("Archivos unidos correctamente.")


