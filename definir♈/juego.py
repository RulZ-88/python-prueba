import pygame
import sys

# --- Inicialización ---

pygame.init()
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mini RPG")

# --- Carga de sprites ---

player_sheet = pygame.image.load("sprites/player.png").convert_alpha()
tile_image = pygame.image.load("sprites/tileset.png").convert_alpha()
npc_image = pygame.image.load("sprites/npc.png").convert_alpha()

# Extrae frames del jugador (suponiendo 3 frames por fila)
frames = []
for i in range(3):
    frame = player_sheet.subsurface((i*32, 0, 32, 32))
    frames.append(frame)

# --- Variables de juego ---

x, y = ANCHO//2, ALTO//2
vel = 3
frame_idx = 0
frame_timer = 0

# --- Bucle principal ---

clock = pygame.time.Clock()

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # --- Movimiento del jugador ---
    keys = pygame.key.get_pressed()
    dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel
    dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * vel
    x += dx; y += dy

    # --- Animación ---
    if dx != 0 or dy != 0:
        frame_timer += 1
        if frame_timer >= 10:
            frame_timer = 0
            frame_idx = (frame_idx + 1) % len(frames)
    else:
        frame_idx = 1  # frame estático

    # --- Render ---
    pantalla.fill((0, 0, 0))  # fondo negro

    # Dibuja tile de fondo repetido
    for i in range(0, ANCHO, 32):
        for j in range(0, ALTO, 32):
            pantalla.blit(tile_image, (i, j))

    # Dibuja NPC fijo en pantalla
    pantalla.blit(npc_image, (100, 100))

    # Dibuja jugador animado
    pantalla.blit(frames[frame_idx], (x, y))

    pygame.display.update()
    clock.tick(60)
