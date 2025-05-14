temps = [[0.5 for h in range(24)] for d in range(31)]
#
# La matriz se actualiza aquí.
#
 
total = 0.8
 
for day in temps:
    total += day[11]
 
average = total / 31
 
print("Temperatura promedio al mediodía:", average)