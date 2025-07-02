import random
import time

# Emoticonos
emojis = {
    "warrior": "🗡️",
    "mage": "🔥",
    "healer": "💖",
    "rogue": "🗡️😈",
    "enemy": "👾",
    "attack": "⚔️",
    "heal": "💊",
    "magic": "✨",
    "dead": "💀",
    "hp": "❤️"
}

# Definición de clases de personajes
characters = {
    "1": {
        "name": "Guerrero",
        "emoji": emojis["warrior"],
        "hp": 100,
        "attack": 15,
        "special": "Golpe Poderoso"
    },
    "2": {
        "name": "Mago",
        "emoji": emojis["mage"],
        "hp": 70,
        "attack": 10,
        "special": "Bola de Fuego"
    },
    "3": {
        "name": "Sanador",
        "emoji": emojis["healer"],
        "hp": 80,
        "attack": 8,
        "special": "Curación"
    },
    "4": {
        "name": "Pícaro",
        "emoji": emojis["rogue"],
        "hp": 90,
        "attack": 12,
        "special": "Ataque Crítico"
    }
}

# Enemigo simple
enemy = {
    "name": "Goblin",
    "emoji": emojis["enemy"],
    "hp": 60,
    "attack": 10
}

def slow_print(text, delay=0.03):
    for c in text:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()

def choose_character():
    print("¡Elige tu personaje!\n")
    for key, char in characters.items():
        print(f"{key}. {char['name']} {char['emoji']} HP: {char['hp']} | Ataque: {char['attack']} | Especial: {char['special']}")

    while True:
        choice = input("\nIntroduce el número de tu elección: ")

        if choice in characters:
            return characters[choice]
        else:
            print("⚠️ Por favor, elige uno de los números mostrados (1, 2, 3 o 4).")


def battle(player):
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

    # Resultado del combate
    if player_hp > 0:
        slow_print(f"\n¡Has vencido al {enemy['name']}! {emojis['enemy']} {emojis['dead']}")
    else:
        slow_print(f"\nHas sido derrotado... {emojis['dead']}")

def main():
    slow_print("🎮 Bienvenido a TEXT RPG 🏰\n")
    player = choose_character()
    slow_print(f"\n¡Has elegido ser un {player['name']}! {player['emoji']}\n")
    battle(player)

if __name__ == "__main__":
    main()
