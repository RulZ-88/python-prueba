import time

texto = """
+================================+
|    ¡ Hola bebé ❤️ !            |
|        me ama?  💕             | 
|  presione 1 para "si" 😘       | 
|  presione 2 para "no" 😭😿     |
|                                 |
+================================ +

"""

for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.020)  # 0.1 segundos entre letras (ajusta el tiempo si quieres más lento)

