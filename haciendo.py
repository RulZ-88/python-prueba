


        
def codigo_confirmacion_fortificados(codigo):
    errores = []

    if len(codigo) < 6:
        errores.append("el código debe tener al menos 6 caracteres")
    if not any(c.isdigit() for c in codigo):
        errores.append("el código debe contener al menos un número")
    if not any(c.isupper() for c in codigo):
        errores.append("el código debe contener al menos una letra mayúscula")
    if any(c.isspace() for c in codigo):
        errores.append("el código no debe contener espacios")

    if errores:
        print("Código de confirmación inválido:")
        for error in errores:
            print(f" - {error}")
        return False
    return True


def codigo_confi_ilu(codigo):
     
     errores=[]

     if len(codigo) < 5:
          errores.append("el codigo debe tener almenos 5 caracteres")
     if not sum(1 for c in codigo if c.isupper()) >= 3:
          errores.append("el codigo debe tener almenos 3 letras mayuscula")
     if not any (c.isdigit()for c in codigo):
          errores.append("el codigo debe tener almenos 1 numero ")
     if  any(c.isspace() for c in codigo):
          errores.append("el codigo no puede tener espacios ")
     
     if errores:
          print("codigo de confirmacion invalido")

          for error in errores:
               print(f"-{error}")
          return False
     return True



def comprar_forti():
     global entradas_forti

     if not entradas_forti > 0:
          print("no hay stock de entradas ")
          return
          
     
     nombre_user =input("ingrese el nombre:  ")   #nombre usuario
     
     
     if nombre_user in usuarios_forti :
          print("el usuario ya compro entrada")
          return
     
     
     while True:
         
         tipo = input("Ingrese tipo de entrada (G/V):  ").upper()  #tipo entrada
         if tipo not in ["G","V"]:
                print("tipo de entrada invalido digite '(G) o (V)' ")
         else:
             break
     
     
     while True:
          codigo = input("ingrese el codigo de confirmacion:   ")   #codigo confirmacion
          if codigo_confirmacion_fortificados(codigo):
              print("Su compra para la entrada de los fortificados a sido con exito")
              usuarios_forti.append(nombre_user)
              entradas_forti -= 1
              break
         
    
     


def comprar_ilu():

     global entradas_ilu

     if not entradas_ilu > 0:
          print("entradas para los iluminados agotadas")
          return
     




     nombre_user =input("ingrese el nombre:  ").lower

     if nombre_user in usuarios_ilu:
          print("el nombre de usuario ya compro entradas")
          return
     
     while True:
          tipo= input("ingrese su tipo de entrada   ").upper()
          

          if tipo not in ["CV","PAL"]:
               print("el tipo esta mal ingresado")
          else:
               break

     while True:
          codigo= input("ingrese el codigo de confirmacion")

          if codigo_confi_ilu(codigo):
               print("Su compra a sido exitosa para los iluminados ")
               usuarios_ilu.append(nombre_user)
               entradas_ilu -= 1
               break
          

def stock_entradas():

 print(f"entradas para los fortificados :{entradas_forti} \n" )

 print(f"entradas para los ilumidados : {entradas_ilu} ")
       
 




     



     
entradas_forti = 500
entradas_ilu = 500

usuarios_forti=[]
usuarios_ilu =[]


while True:
    print("""
         TOTEM AUTOSERVICIO CONCIERTOS ROCK AND CHILE
1.- Comprar entrada a “los Fortificados”.
2.- Comprar entrada a “los Iluminados”.
3.- Stock de entradas para ambos conciertos.
4.- Salir.
 
          
          
          """)
    
    opcion_user =input("ingrese su opcion:   ")
    
    if opcion_user == "1":
         comprar_forti()
         
    elif opcion_user == "2":
         comprar_ilu()
         
          
    elif opcion_user == "3":
         stock_entradas()

    elif opcion_user  == "4":
         print("gracias por usar el sistema de entradas")
         break
         
         
          
   
     









                


        
    
    
    
    
