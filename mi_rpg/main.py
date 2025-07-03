import random
import time
import threading
import tkinter as tk
import json
import os

# Emoticonos
emojis = {
    "warrior": "💪🗡️",
    "mage": "🧙🔥",
    "healer": "💖😇",
    "rogue": "🗡️😈",
    "enemy": "👾",
    "attack": "⚔️",
    "heal": "💊",
    "magic": "✨",
    "dead": "💀",
    "hp": "❤️"
}

# Clases de personajes
characters = {
    "1": {"name": "Guerrero", "emoji": emojis["warrior"], "hp": 100, "attack": 15, "special": "Golpe Poderoso"},
    "2": {"name": "Mago", "emoji": emojis["mage"], "hp": 70, "attack": 10, "special": "Bola de Fuego"},
    "3": {"name": "Sanador", "emoji": emojis["healer"], "hp": 80, "attack": 8, "special": "Curación"},
    "4": {"name": "Pícaro", "emoji": emojis["rogue"], "hp": 90, "attack": 12, "special": "Ataque Crítico"}
}

# Enemigo
enemy = {"name": "Goblin", "emoji": emojis["enemy"], "hp": 60, "attack": 10}

# Variables globales
player = None
player_hp = 0
save_file = "savegame.json"

# Guardar/Cargar
def save_game():
    if player:
        with open(save_file, "w") as f:
            json.dump({"player": player, "hp": player_hp, "enemy": enemy}, f)
        print("\n💾 Juego guardado.")

def load_game():
    global player, player_hp, enemy
    if os.path.exists(save_file):
        with open(save_file, "r") as f:
            data = json.load(f)
            player = data["player"]
            player_hp = data["hp"]
            enemy = data["enemy"]
        print("\n✅ Juego cargado.")
    else:
        print("\n⚠️ No hay partida guardada.")

# Ventana de botones (solo guardar/cargar)
def abrir_ventana_botones_en_segundo_plano():
    def lanzar_ventana():
        root = tk.Tk()
        root.title("Opciones")
        root.configure(bg="black")
        root.geometry("200x80")

        btn_guardar = tk.Button(root, text="Guardar", command=save_game)
        btn_guardar.pack(pady=5)

        btn_cargar = tk.Button(root, text="Cargar", command=load_game)
        btn_cargar.pack(pady=5)

        root.mainloop()

    hilo = threading.Thread(target=lanzar_ventana, daemon=True)
    hilo.start()

# Impresión lenta
def slow_print(text, delay=0.05):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()

# Selección de personaje
def choose_character():
    print("¡Elige tu personaje!\n")
    for key, char in characters.items():
        print(f"{key}. {char['name']} {char['emoji']} HP: {char['hp']} | Ataque: {char['attack']} | Especial: {char['special']}")
    while True:
        choice = input("\nIntroduce el número de tu elección: ")
        if choice in characters:
            return characters[choice]
        print("⚠️ Por favor, elige uno de los números mostrados (1, 2, 3 o 4).")

# Combate
def battle(player):
    global player_hp
    print(f"\n¡Un {enemy['name']} {enemy['emoji']} aparece!")
    player_hp = player["hp"]
    enemy_hp = enemy["hp"]

    while player_hp > 0 and enemy_hp > 0:
        print(f"\nTu HP: {player_hp} {emojis['hp']} | HP del enemigo: {enemy_hp} {emojis['hp']}")
        print("1. Ataque normal ⚔️")
        print(f"2. {player['special']} ✨")
        action = input("¿Qué quieres hacer? ")

        if action == "1":
            dmg = random.randint(player["attack"] - 3, player["attack"] + 3)
            slow_print(f"\n¡Atacas al enemigo! {emojis['attack']} Causas {dmg} de daño.")
            enemy_hp -= dmg
        elif action == "2":
            if player["name"] == "Sanador":
                heal = random.randint(15, 25)
                player_hp += heal
                slow_print(f"\nUsas {player['special']} {emojis['heal']} y recuperas {heal} HP.")
            else:
                dmg = random.randint(player["attack"] + 5, player["attack"] + 15)
                slow_print(f"\nUsas {player['special']} {emojis['magic']} y causas {dmg} de daño mágico.")
                enemy_hp -= dmg
        else:
            slow_print("No entiendo esa opción. Pierdes el turno.")

        if enemy_hp > 0:
            enemy_dmg = random.randint(enemy["attack"] - 2, enemy["attack"] + 2)
            slow_print(f"\n{enemy['name']} te ataca {emojis['attack']} y te causa {enemy_dmg} de daño.")
            player_hp -= enemy_dmg

    if player_hp > 0:
        slow_print(f"\n¡Has vencido al {enemy['name']}! {emojis['enemy']} {emojis['dead']}")
    else:
        slow_print(f"\nHas sido derrotado... {emojis['dead']}")

# Juego principal
def main():
    slow_print("🎮 '🏰 The Cursed Castle 🏰 '\n")
    global player
    player = choose_character()
    slow_print(f"\n¡Has elegido ser un {player['name']}! {player['emoji']}\n")
    battle(player)

if __name__ == "__main__":
    abrir_ventana_botones_en_segundo_plano()  # Solo guardar/cargar
    main()
