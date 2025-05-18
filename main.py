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
asteroide = Asteroide()
asteroidi = []
type(asteroidi) == Asteroide
running = True

intervallo_gener = 1000  
generazione_a = pygame.USEREVENT + 1
pygame.time.set_timer(generazione_a, intervallo_gener)

def disegna_oggetti():
    screen.blit(sfondo, (0,0))
    screen.blit(nonna.image, (nonna.x, nonna.y))
    for a in asteroidi:
        a.disegna(screen)

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
        if event.type == generazione_a:
            nuovo = Asteroide()
            asteroidi.append(nuovo) 

    for a in asteroidi:
        a.aggiorna_a()
    asteroidi = [a for a in asteroidi if not a.fuori_schermo()]

    disegna_oggetti()

    aggiorna()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()