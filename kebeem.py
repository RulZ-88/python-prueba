import pandas as pd
import glob
import os


carpeta = 'C:\\Users\\black\\Desktop\\exels prueba'
  
archivos = glob.glob(os.path.join(carpeta, '*.xlsx'))


dataframes = []

for archivo in archivos:
    df = pd.read_excel(archivo)
    dataframes.append(df)


df_final = pd.concat(dataframes, ignore_index=True)


df_final.to_excel('C:\\Users\\black\\Desktop\\exels prueba\\resultado_final.xlsx', index=False)

import pandas as pd

# Abrir el archivo
df = pd.read_excel('C:\\Users\\black\\Desktop\\resultado_final.xlsx')

