'''
Simulador de batalla entre dos Pokémon.
autor: Mario Meléndez I.

'''
from random import randint
import pygame

pygame.mixer.init()
pygame.mixer.music.load("cancion_poke.mp3")  
pygame.mixer.music.play(-1)
print(
    
   """\033[91m
         Bienvenido al simulador de batalla Pokémon 
            puedes elegir entre 4 tipos de Pokémon
             1) fuego 2)agua 3)planta 4)tierra
""")
input("jugador 1 , elije tu tipo de pokémon : \n")