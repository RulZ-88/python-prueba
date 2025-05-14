numero1= int(input("ingrese el primer numero"))
numero2= int(input("ingrese el segundo numero"))
numero3= int(input("ingrese el tercer numero"))

numero_mas_largo= numero1

if numero2 > numero_mas_largo:
   numero_mas_largo=numero2
if numero3 > numero_mas_largo:
   numero_mas_largo=numero3

print("el numero mas largo es " , numero_mas_largo)