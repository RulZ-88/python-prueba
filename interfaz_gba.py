import pygame
import sys

# Inicializar pygame
pygame.init()

# Configurar ventana
ANCHO = 600
ALTO = 400
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi Juego GBA Style")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    ventana.fill(NEGRO) 


    pygame.display.update()
