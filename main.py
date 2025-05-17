import pygame
from pygame.locals import *
from player import Nonna

pygame.init()

sfondo = pygame.image.load('sfondo_spaziale.png')
gameover = pygame.image.load('game over.png')


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Nonna Rampage")
clock = pygame.time.Clock()
fps = 60
nonna = Nonna((150, 300))
running = True

def disegna_oggetti():
    screen.blit(sfondo, (0,0))
    screen.blit(nonna.image, (nonna.x, nonna.y))

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
 

 #non funziona tenendo premuto
    disegna_oggetti()

    aggiorna()


    
    #pygame.display.flip()
    #clock.tick(60)

pygame.quit()