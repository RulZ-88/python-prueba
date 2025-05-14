
print("bienvenido al programa para revisar las vacaciones" )

nombre_usuario= input("ingrese su nombre \n")
clave_usuario= int(input("ingrese su clave de usuario \n "))
antiguedad_usuario=float(input("ingrese su antiguedad \n"))

if clave_usuario == 1 :
    if antiguedad_usuario >= 1 and antiguedad_usuario <2:
        print(f"al usuario {nombre_usuario} le corresponden 7 dias de vacaciones. ")
    elif antiguedad_usuario >=3 and antiguedad_usuario <6:
        print(f"al usuario {nombre_usuario} le corresponden 10 dias de vacaciones. ")
    elif antiguedad_usuario >= 7 and antiguedad_usuario <10:
        print(f"al usuario {nombre_usuario} le corresponden 15 dias de vacaciones. ")
    elif antiguedad_usuario >= 12:
        print(f"al usuario {nombre_usuario} le corresponden 20 dias de vacaciones. ")
    else:
        antiguedad_usuario < 1
        print("ud no tiene derecho a vacaciones")

        

        
    
    










    
      
