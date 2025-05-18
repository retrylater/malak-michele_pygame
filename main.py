import pygame
from pygame.locals import *
from player import Nonna
from asteroide import Asteroide
import random

pygame.init()
tempo_inizio = pygame.time.get_ticks()

pygame.key.set_repeat(10,10)
sfondo = pygame.image.load('sfondo_spaziale.png')

esplosione_base = pygame.image.load("esplosione.png")
altezza_esplosione = 80
larghezza_esplosione = 80
esplosione = pygame.transform.scale(esplosione_base, (larghezza_esplosione, altezza_esplosione))

gameover_base = pygame.image.load('game over.png')
altezza_gameover = 400
larghezza_gameover = 600
gameover = pygame.transform.scale(gameover_base, (larghezza_gameover, altezza_gameover))


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Nonna Rampage(Spaziale)")
clock = pygame.time.Clock()
fps = 60
nonna = Nonna((150, 300))
asteroide = Asteroide()
asteroidi = []
type(asteroidi) == Asteroide
running = True

intervallo_gener = 400  
generazione_a = pygame.USEREVENT + 1
pygame.time.set_timer(generazione_a, intervallo_gener)

mask_nonna = pygame.mask.from_surface(nonna.image)

def disegna_oggetti():
    screen.blit(sfondo, (0,0))
    screen.blit(nonna.image, (nonna.x, nonna.y))
    for a in asteroidi:
        a.disegna(screen)

def aggiorna():
    pygame.display.update()
    clock.tick(fps)

gioco_attivo = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if gioco_attivo:
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_w):
                nonna.y -= nonna.vy
            if nonna.y <= 0:
                nonna.y += nonna.vy
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_s):
                nonna.y += nonna.vy
            if nonna.y >= 530:
                nonna.y -= nonna.vy
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_a):
                nonna.x -= nonna.vx
            if nonna.x <= -10:
                nonna.x += nonna.vx
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_d):
                nonna.x += nonna.vx
            if nonna.x >= 745:
                nonna.x -= nonna.vx

            if event.type == generazione_a:
                nuovo = Asteroide()
                asteroidi.append(nuovo)
    
    pos_nonna = [nonna.x, nonna.y]
    if gioco_attivo:
        tempo_corrente = pygame.time.get_ticks()
        punteggio = (tempo_corrente - tempo_inizio) // 100
        for a in asteroidi:
            a.aggiorna_a()
        asteroidi = [a for a in asteroidi if not a.fuori_schermo()]

        collisione = False

        for a in asteroidi:
            if a.collisione(pos_nonna, mask_nonna):
                collisione = True
                tempo_collisione = pygame.time.get_ticks()
                gioco_attivo = False
                break

    disegna_oggetti()

    font = pygame.font.SysFont(None, 50)
    testo_punteggio = font.render(f"Punteggio: {str(punteggio).zfill(4)}", True, (255, 255, 255))
    screen.blit(testo_punteggio, (10, 10))

    if collisione:
        punteggio_finale = punteggio
        screen.blit(esplosione, (pos_nonna[0], pos_nonna[1]))
        screen.blit(gameover, (100, 100))

    aggiorna()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()