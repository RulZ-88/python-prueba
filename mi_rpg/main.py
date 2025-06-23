import pygame
import sys

# Inicializar pygame
pygame.init()

# Dimensiones de la pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mini RPG")

# Cargar imágenes
player_sheet = pygame.image.load("sprites/player.png").convert_alpha()
tileset = pygame.image.load("sprites/tileset.png").convert_alpha()
npc_sheet = pygame.image.load("sprites/npc.png").convert_alpha()

# Extraer un solo tile para el fondo (por ejemplo, esquina superior izquierda)
tile = tileset.subsurface((0, 0, 32, 32))  # Ajusta si necesitas otro

# Extraer frames del jugador (3 frames horizontales de 32x32 píxeles)
frames = []
for i in range(3):
    frame = player_sheet.subsurface((i * 32, 0, 32, 32))
    frames.append(frame)

# Extraer un NPC específico (esquina superior izquierda)
npc = npc_sheet.subsurface((0, 0, 32, 32))  # Ajusta si necesitas otro NPC

# Posiciones y variables del jugador
x, y = ANCHO // 2, ALTO // 2
vel = 3
frame_idx = 0
frame_timer = 0

clock = pygame.time.Clock()

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento del jugador
    keys = pygame.key.get_pressed()
    dx = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel
    dy = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * vel
    x += dx
    y += dy

    # Animación del jugador
    if dx != 0 or dy != 0:
        frame_timer += 1
        if frame_timer >= 10:
            frame_timer = 0
            frame_idx = (frame_idx + 1) % len(frames)
    else:
        frame_idx = 1  # Frame "idle"

    # Dibujar fondo con tiles
    pantalla.fill((0, 0, 0))  # Opcional: limpiar fondo negro antes de blitear tiles
    for i in range(0, ANCHO, 32):
        for j in range(0, ALTO, 32):
            pantalla.blit(tile, (i, j))

    # Dibujar NPC
    pantalla.blit(npc, (100, 100))

    # Dibujar jugador
    pantalla.blit(frames[frame_idx], (x, y))

    # Actualizar pantalla
    pygame.display.update()
    clock.tick(60)
