for i in range(3):         # Bucle exterior
    for j in range(5):     # Bucle interior
        if j == 2:
            continue       # Salta cuando j es 2
        print("i= " , i ,"j=" ,j )