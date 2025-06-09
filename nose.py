caracteres = "a1b3"
final = ""
for i in caracteres:
    try:
        if i.isalpha():
            final += str(caracteres.index(i))
        if i.isnumeric():
            final += i
    except ValueError:
        print("Error de índice")
    except Exception as ex:
        print("Otro Error")
print(final)
