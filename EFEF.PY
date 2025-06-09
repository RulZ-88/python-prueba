import pandas as pd
import os

# Ruta del archivo Excel original
ruta_archivo = 'C:\\Users\\black\\Desktop\\exels prueba\\resultado_final.xlsx'

# Verifica si el archivo existe
if os.path.exists(ruta_archivo):
    # Leer el archivo
    df = pd.read_excel(ruta_archivo)

    # Agregar o reemplazar la columna 'MARIO' con el texto deseado
    df['MARIO'] = 'Apellido Melendez Edad 33'

    # Guardar el archivo actualizado
    df.to_excel(ruta_archivo, index=False)

    print("✅ Archivo actualizado correctamente con la columna 'MARIO'.")
else:
    print("❌ El archivo no existe. Revisa la ruta.")
