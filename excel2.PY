import pandas as pd

# Cargar el Excel
ruta = 'C:\\Users\\black\\Desktop\\exels prueba\\resultado_final.xlsx'
df = pd.read_excel(ruta)

# Crear la nueva fila completa
nueva_fila = {
    'Nombre': 'Mario',
    'Edad': 33,
    'Correo': 'sin_dato@correo.com',
    'MARIO': 'Apellido Melendez Edad 33'
}

# Agregarla al DataFrame
df = pd.concat([df, pd.DataFrame([nueva_fila])], ignore_index=True)

# Guardar el archivo actualizado
df.to_excel(ruta, index=False)

print("✅ Fila agregada correctamente.")
