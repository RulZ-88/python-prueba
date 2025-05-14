drawn = [5, 11, 9, 42, 3, 49]
bets = [3, 7, 11, 42, 34, 49]
hits = 0
matching_numbers=[]
for number in bets:
    if number in drawn:
        hits += 1
        matching_numbers.append(number) 
 
print(hits)
print(" los numeros que coinciden son  : " , matching_numbers)

 