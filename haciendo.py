


        
def codigo_confirmacion_fortificados(codigo):
    if (
        len(codigo) >= 6 and
        any(c.isdigit()for c in codigo) and
        any(c.isupper()for c in codigo) and
        not any (c.isspace()for c in codigo)
       ):
         return True
    return False



def comprar_forti(nombre_user):
     global entradas_forti
     if nombre_user in usuarios_forti :
          print("el usuario ya compro entrada")
          return
     
     
     while True:
         
         tipo = input("Ingrese tipo de entrada (G/V):  ").upper()
         if tipo not in ["G","V"]:
                print("tipo de entrada invalido digite '(G) o (V)' ")
         else:
             break
     
     
     while True:
          codigo = input("ingrese el codigo de confirmacion:   ")
          if codigo_confirmacion_fortificados(codigo):
              print(f"Su compra para la entrada de los fortificados a sido con exito")
              usuarios_forti.append(nombre_user)
              entradas_forti -= 1
              break
          else:
               print(" el codigo esta mal ingresado")


     
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
         nombre_user =input("ingrese el nombre:  ")
         comprar_forti(nombre_user)
         
          
          
   
     









                


        
    
    
    
    
