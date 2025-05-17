import pygame
from pygame.locals import *
from player import Nonna
from asteroide import Asteroide
import random

pygame.init()
pygame.key.set_repeat(10,10)
sfondo = pygame.image.load('sfondo_spaziale.png')
gameover = pygame.image.load('game over.png')
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Nonna Rampage")
clock = pygame.time.Clock()
fps = 60
nonna = Nonna((150, 300))
asteroide = Asteroide((140, 200))
asteroidi = []
running = True

def disegna_oggetti():
    screen.blit(sfondo, (0,0))
    screen.blit(nonna.image, (nonna.x, nonna.y))
    screen.blit(asteroide.image,(asteroide.x, asteroide.y))

def aggiorna():
    pygame.display.update()
    clock.tick(fps)


while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_w):
            nonna.y -= nonna.vy
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_s):
            nonna.y += nonna.vy
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_a):
            nonna.x -= nonna.vx
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_d):
            nonna.x += nonna.vx
             
    # for _ in range(1):               
    #     x = 800                       # volevo generare più asteroidi alla voltasolo che me ne escono troppi, dobbiamo pensare a generare un tot asteroidi ogni tot tempo
    #     y = random.randint(0, 550)
    #     asteroidi.append(Asteroide((x, y)))

    # for asteroide in asteroidi:
    asteroide.aggiorna()

    disegna_oggetti()
    # for asteroide in asteroidi:
    asteroide.disegna(screen)

    aggiorna()
 
    pygame.display.flip()
    clock.tick(60)

pygame.quit()