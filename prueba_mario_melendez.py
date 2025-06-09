

cantidad_prestados=0
titulo_libro=""
dias_prestamo_mas=0
dias_prestamo_menos=0

try:
    cantidad_libros=int(input("ingrese la cantidad de libros prestados 📚 \n")) # se le pide al usuario que ingrese la cantidad de libros.
except ValueError as NameError:
        print(f" ⚠️ ingrese solo numeros enteros ⚠️ {NameError}") #si el usuario digita cualquier otra tecla que no sea un numero entero , se le informa al usuario , mostrandole el error.





for cantidad_prestados in range(cantidad_libros): # el for recorre la cantidad de numeros ingresados por el usuario.
    try:
        titulo_libro=input("ingrese el nombre del titulo del libro:\n ")  #se pide que ingrese el nombre del libro.
        cantidad_libros+=1
    
        dias_prestamo=int(input(f"ingrese  los dias de prestamo para el libro {titulo_libro}: \n ")) # se pide que ingrese los dias de prestamo.
        if dias_prestamo > 15:
         dias_prestamo_mas+=1
         print("prestamo por mas de  15 dias.")
        if dias_prestamo <= 15:
          dias_prestamo_menos+=1
          print("prestamo por 15 dias o menos")
          

          
    except ValueError as NameError: #si el usuario digita cualquier otra tecla que no sea un numero entero , se le informa al usuario , mostrandole el error.
        print(f" ⚠️ Opción no válida ⚠️ ingrese solo numeros enteros porfavor. \n {NameError}")
print(f"""Se registraron {dias_prestamo_mas} libros  con préstamo mayor a 15 días 
          Se registraron {dias_prestamo_menos} libros con préstamo de 15 días o menos.""") # se muestra una salida con la cantidad de libros respectivamente.
             

        
     
 




