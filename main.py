import pygame 
from pygame import font
import sys
from character import Player
from npc import NPC

pygame.init() 

pygame.display.set_caption("Joginho")
screensize = (800, 600)
screen = pygame.display.set_mode(screensize)
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player1 = Player(3)
all_sprites.add(player1)

"""npc1 = NPC(3)  
all_sprites.add(npc1)"""

myFont = font.SysFont("Calibri", 20)
while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    all_sprites.update()
    all_sprites.draw(screen)

    texto_velocidad = myFont.render(f"Velocidad: {player1.speed}", True, (0,0,255))
    screen.blit(texto_velocidad, (600,50))

    texto_vida = myFont.render(f"Vida: {player1.health}", True, (255,0,0))
    screen.blit(texto_vida, (600,75))

    pygame.display.flip() 

    clock.tick(60) 




"""
Sprite main pj

mapa tiles

camera offset

sistema de combate

hotbar
"""
