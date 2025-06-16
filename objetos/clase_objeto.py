class Auto:
    def __init__(self, color, velocidad):
        self.color = color
        self.velocidad = velocidad

    def acelerar(self):
        print("El auto acelera")

# Crear un objeto
mi_auto = Auto("Rojo", 100)

# Acceder a atributos y métodos
print(mi_auto.color)      # Rojo
print(mi_auto.velocidad)  # 100
mi_auto.acelerar()        # El auto acelera
