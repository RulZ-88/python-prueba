import random
import json
import os

# ----------------------
# CLASE PRINCIPAL
# ----------------------
class Personaje:
    def __init__(self, nombre, emoji, hp, ataque, especial):
        self.nombre = nombre
        self.emoji = emoji
        self.hp = hp
        self.hp_max = hp
        self.ataque = ataque
        self.especial = especial
        self.nivel = 1
        self.experiencia = 0
        self.dinero = 50
        self.inventario = []

    def mostrar_info(self):
        print(f"\n{self.nombre} {self.emoji} | Nivel {self.nivel} | HP: {self.hp}/{self.hp_max} \
               | Ataque: {self.ataque} | Exp: {self.experiencia} | 💰: {self.dinero}")

    def recibir_daño(self, cantidad):
        self.hp = max(self.hp - cantidad, 0)
        print(f"{self.nombre} ha recibido {cantidad} de daño. HP actual: {self.hp}")

    def atacar(self, enemigo):
        daño = random.randint(self.ataque - 2, self.ataque + 2)
        print(f"{self.nombre} ataca a {enemigo['nombre']} causando {daño} de daño.")
        enemigo["hp"] = max(enemigo["hp"] - daño, 0)

    def magia(self, enemigo):
        costo = 10
        if self.dinero >= costo:
            daño = random.randint(self.ataque, self.ataque + 10)
            self.dinero -= costo
            print(f"{self.nombre} usa magia y causa {daño} de daño por {costo} monedas.")
            enemigo["hp"] = max(enemigo["hp"] - daño, 0)
        else:
            print("No tienes suficiente dinero para usar magia.")

    def curar(self):
        cura = random.randint(15, 25)
        self.hp = min(self.hp + cura, self.hp_max)
        print(f"{self.nombre} se cura {cura} puntos. HP actual: {self.hp}")

    def ganar_exp(self, cantidad):
        self.experiencia += cantidad
        print(f"🧪 Has ganado {cantidad} de experiencia.")
        while self.experiencia >= self.nivel * 20:
            self.subir_nivel()

    def subir_nivel(self):
        self.experiencia -= self.nivel * 20
        self.nivel += 1
        self.hp_max += 10
        self.hp = self.hp_max
        self.ataque += 2
        print(f"⭐ ¡Has subido al nivel {self.nivel}!")

    def agregar_objeto(self, objeto):
        self.inventario.append(objeto)
        print(f"🎒 Has obtenido: {objeto}")

    def usar_objeto(self):
        if not self.inventario:
            print("El inventario está vacío.")
            return
        print("Objetos disponibles:")
        for i, obj in enumerate(self.inventario, 1):
            print(f"{i}. {obj}")
        choice = input("¿Qué objeto usar? (número): ")
        if choice.isdigit() and 1 <= int(choice) <= len(self.inventario):
            obj = self.inventario.pop(int(choice)-1)
            if obj == "Poción de vida":
                self.curar()
            else:
                print(f"Usaste {obj}, pero no pasó nada.")
        else:
            print("Opción inválida.")

    def mostrar_inventario(self):
        print("🎒 Inventario:", ", ".join(self.inventario) if self.inventario else "Vacío")


# ----------------------
# SELECCIONAR PERSONAJE
# ----------------------
def elegir_personaje():
    personajes = {
        "1": Personaje("Guerrero", "🗡️", 100, 15, "Golpe Poderoso"),
        "2": Personaje("Mago", "🧙", 70, 20, "Bola de fuego"),
        "3": Personaje("Sanador", "💖", 80, 10, "Curación divina"),
        "4": Personaje("Pícaro", "🕶️", 90, 13, "Ataque sigiloso")
    }
    while True:
        print("🧙‍♂️ Elige tu personaje:\n")
        for k, pj in personajes.items():
            print(f"{k}. {pj.nombre} {pj.emoji} | HP: {pj.hp} | Ataque: {pj.ataque}")
        op = input("Número: ")
        if op in personajes:
            return personajes[op]
        print("⚠️ Número inválido (1–4).")

# ----------------------
# HISTORIA
# ----------------------
def contar_historia():
    print("""
     🏰 The Cursed Castle 🏰
Tu aldea fue devastada por Varyan Grinn...
Deberás , recorrer caminos, batallar y fortalecerte para vencerlo
    """)

# ----------------------
# COMBATE
# ----------------------
def combate(jugador, enemigo):
    print(f"\n⚔️ Aparece {enemigo['nombre']} (HP: {enemigo['hp']})")
    while jugador.hp > 0 and enemigo["hp"] > 0:
        jugador.mostrar_info()
        print("\n1. Ataque")
        print("2. Magia (💰10 monedas)")
        print("3. Curar")
        print("4. Usar objeto")
        accion = input("¿Qué haces? ")
        if accion == "1":
            jugador.atacar(enemigo)
        elif accion == "2":
            jugador.magia(enemigo)
        elif accion == "3":
            jugador.curar()
        elif accion == "4":
            jugador.usar_objeto()
        else:
            print("Acción inválida.")

        if enemigo["hp"] > 0:
            dmg = random.randint(enemigo["ataque"] - 2, enemigo["ataque"] + 2)
            jugador.recibir_daño(dmg)
    if jugador.hp <= 0:
        print("💀 Has muerto. Fin de la aventura.")
        exit()
    print(f"✅ Has vencido a {enemigo['nombre']}!")
    jugador.ganar_exp(enemigo["exp"])
    jugador.agregar_objeto(enemigo["drop"])
    jugador.dinero += enemigo["exp"]
    print(f"💰 Ganaste {enemigo['exp']} monedas.")

# ----------------------
# ENEMIGOS
# ----------------------
def crear_enemigo():
    return random.choice([
        {"nombre": "Slime", "hp": 30, "ataque": 5, "exp": 10, "drop": "Poción de vida"},
        {"nombre": "Murciélago", "hp": 40, "ataque": 7, "exp": 12, "drop": "Colmillo negro"},
        {"nombre": "Esqueleto", "hp": 50, "ataque": 9, "exp": 15, "drop": "Poción de vida"}
    ])

# ----------------------
# TIENDA
# ----------------------
def tienda(jugador):
    items = {"1": ("Poción de vida", 20), "2": ("Espada pequeña", 50)}
    print("\n🏪 Bienvenido a la tienda:")
    for k, (name, price) in items.items():
        print(f"{k}. {name} — {price} monedas")
    choice = input("¿Qué compras? ")
    if choice in items:
        name, price = items[choice]
        if jugador.dinero >= price:
            jugador.dinero -= price
            jugador.agregar_objeto(name)
        else:
            print("No tienes suficiente dinero.")
    else:
        print("No compraste nada.")

# ----------------------
# GUARDAR / CARGAR PROGRESO
# ----------------------
SAVE_FILE = "guardar.json"

def guardar(jugador):
    data = jugador.__dict__
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)
    print("💾 Juego guardado.")

def cargar():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE) as f:
            data = json.load(f)
        pj = Personaje(data['nombre'], data['emoji'], data['hp_max'], data['ataque'], data['especial'])
        pj.hp = data['hp']
        pj.nivel = data['nivel']
        pj.experiencia = data['experiencia']
        pj.dinero = data['dinero']
        pj.inventario = data['inventario']
        print("✅ Juego cargado.")
        return pj
    return None

# ----------------------
# JUEGO PRINCIPAL
# ----------------------
def juego():
    contar_historia()
    jugador = cargar() or elegir_personaje()
    jugador.mostrar_info()

    caminos = ["Bosque", "Cueva", "Pueblo"]
    for lugar in caminos:
        print(f"\n🏞️ Llegas al {lugar}.")
        enemigo = crear_enemigo()
        combate(jugador, enemigo)
        tienda(jugador)
        jugador.mostrar_inventario()
        guardar(jugador)

    print("\n🎉 ¡Llegaste al final del camino por ahora! Continúa tu aventura luego.")

# ----------------------
# PUNTO DE ENTRADA
# ----------------------
if __name__ == "__main__":
    juego()



