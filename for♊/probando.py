print(""" Cree su contraseña 🔏
   1. El largo de la contraseña debe ser de mínimo 8 caracteres y máximo 16.
   2. Debe tener al menos un número
   3. Debe tener al menos una letra, no importando si es mayúscula o minúscula.
   4. Debe tener como máximo un caracter especial. La lista de caracteres especiales son: -_*.!?#$%
   5. No puede tener espacios en blanco.
   6. No puede terminar con un caracter especial.
      
""")

contador_num=0
contador_letras=0
contador_especial=0
contador_espacios=0
contador_contraseña=0
try:
  contraseña=int(input("ingrese su contraseña porfavor, con las reglas que se mencionan mas arriba:  "))
  for i in contraseña:
   contador_contraseña+=1
  if i.isnumeric():
    contador_num+=1
  if i.isalpha():
    contador_letras+=1
  if i.isspace():
    contador_espacios+=1
  if i in "-_*.!?#$%":
    contador_especial+=1
  
except ValueError as error:
  print(error)
  exit()
 
 

if contador_contraseña<8 :
  print(" la contraseña debe tener almenos 8 caracteres")
elif contador_contraseña >16:
  print(" la contraseña debe tener maximo 16 caracteres")
elif contador_num <=0:
  print(" la contraseña debe tener almenos un numéro")
elif contador_letras <=0:
  print(" la contraseña debe tener almenos una letra")
elif i in "-_*.!?#$%":
  print("la contraseña no puede terminar en un caracter especial")
elif contador_espacios >0:
  print("la contraseña no puede tener espacios en blancos")
else :
  print("contraseña valida!")

  



