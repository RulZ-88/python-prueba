


usuario=input("ingresa una palabra")
user_word=usuario
# y asignarlo a la variable user_word.


for letras in user_word:
    # Completa el cuerpo del bucle for.
    if letras in ( "a","e","i","o","u"):
        continue 
    print(letras)


user_word = input("Ingresa una palabra: ")
user_word = user_word.upper()

word_without_vowels = ""

for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        word_without_vowels += letter  # Concatenamos la letra no-vocal

print(word_without_vowels)
