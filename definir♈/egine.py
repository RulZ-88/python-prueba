import random
import math

class Enemigo:
    def __init__(self):
        self.x = random.random() * 800
        self.y = random.random() * 600

    def mover(self):
        self.x += random.uniform(-1, 1)
        self.y += random.uniform(-1, 1)

    def colisiona_con_jugador(self, jugador_x, jugador_y):
        distancia = math.hypot(self.x - jugador_x, self.y - jugador_y)
        return distancia < 20

enemigos = [Enemigo() for _ in range(1000)]

for frame in range(60):  # Simulamos 1 segundo (60 FPS)
    for enemigo in enemigos:
        enemigo.mover()
        if enemigo.colisiona_con_jugador(400, 300):
            print("¡Enemigo disparando!")
