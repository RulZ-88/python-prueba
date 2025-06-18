
#saludo inicial
print("""
****************************************
* Bienvenido al programa para calcular *
*     el subsidio de arriendo.         *
****************************************
      
SIGA LAS SIGUIENTES INTRUCCIONES :
      INGRESE EL NUMERO ENTERO DE LA OPCION SEGUN SU CASO:
""")

bono=0
bono_adulto=0

# se pide datos al usuario
quintil=int(input("ingrese su quintil (numero del 1 al 5)😊 : \n"))
empleo=int(input("(ingrese 1) si esta empleado 😀 --- (ingrese 2) si esta desempleado ☹️ : \n"))
edad=int(input("ingrese su edad porfavor 👴: \n"))

# se hace la comparacion logica para entregar un resultado.
if quintil == 1 or quintil ==2 and empleo== 1:
    sub=280_000
    bono=60_000
    bono_adulto=40_000
    valor_final1= (sub + bono )

    if edad > 65:
        valor_final2= (sub + bono+ bono_adulto)
                
        print(f"El valor del subsidio de arriendo es :{valor_final2}")
    else:    
 
     print(f"El valor del subsidio de arriendo es :{valor_final1}")

elif quintil == 1 or quintil == 2 and empleo == 2:
    sub=350_000
    bono=60_000
    bono_adulto=40_000
    valor_final1= (sub + bono )

    if edad > 65:
        valor_final2= (sub + bono+ bono_adulto)
                
        print(f"El valor del subsidio de arriendo es :{valor_final2}")
    else:    
 
     print(f"El valor del subsidio de arriendo es :{valor_final1}")

elif quintil == 3 and empleo == 1:
    sub=200_000
    bono_adulto=40_000
    valor_final1= (sub )

    if edad > 65:
        valor_final2= (sub + bono_adulto)
                
        print(f"El valor del subsidio de arriendo es :{valor_final2}")
    else:    
 
     print(f"El valor del subsidio de arriendo es :{valor_final1}")


elif quintil == 3 and empleo == 2:
    bono_adulto=40_000
    sub=250_000
    valor_final1= (sub )

    if edad > 65:
        valor_final2= (sub + bono_adulto)
                
        print(f"El valor del subsidio de arriendo es :{valor_final2}")
    else:    
 
     print(f"El valor del subsidio de arriendo es :{valor_final1}")

elif quintil == 4 and empleo == 2:
    bono_adulto=35_000
    sub=250_000
    valor_final1= (sub )

    if edad > 65:
        valor_final2= (sub + bono_adulto)
                
        print(f"El valor del subsidio de arriendo es :{valor_final2}")
    else:    
 
     print(f"El valor del subsidio de arriendo es :{valor_final1}")




    
    

    





