

def aplicar_descuento(monto,porcentaje_descuento):
    return monto - (porcentaje_descuento/100)*monto

carrera=3_300_000
while True:
    entrada = input("Introduce tu ingreso anual: ")
    try:
        ingreso = float(entrada)
        break  # Salimos del bucle si todo fue bien
    except ValueError:
        print("⚠️ Error: por favor, ingrese solo números.")


if  ingreso <= 300_000:
    carrera = aplicar_descuento(carrera,20)
    quintil=1 
    porcentaje=20
  
elif ingreso <= 800_000:
    carrera = aplicar_descuento(carrera,10)
    quintil=2
    porcentaje=10
  

elif ingreso <= 1_600_000:
    carrera = aplicar_descuento(carrera,5)
    quintil=3
    porcentaje=5
  
    
elif ingreso <= 2_300_000:
  carrera = aplicar_descuento(carrera,0)
  quintil=4
  porcentaje=0
    
else :
    carrera=aplicar_descuento(carrera,0)
    quintil=5
    porcentaje=0
    
print(f"""señor usuario , su grupo familiar se encuentra en el : {quintil}
     por lo cual se le hace un descuento del : {porcentaje}%
     Total a pagar de la carrera con  el descuento : {carrera}""")
    




