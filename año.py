
año = int(input("Introduce un año: "))

if año < 1582:
	print("No esta dentro del período del calendario Gregoriano")
elif año % 4 !=0:
		print("es un año comun")
elif año % 100 !=0:
	print("es un año bisiesto")
elif año % 400 !=0:
	print("es un año comun")
		
 
else:
	print(" es un año bisiesto")

  