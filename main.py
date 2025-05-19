import pygame
from pygame.locals import *
from player import Nonna
from asteroide import Asteroide
from orologio import Orologio
from pillola import Pillola
import random

pygame.init()
tempo_inizio = pygame.time.get_ticks()

pygame.key.set_repeat(10,10)
sfondo = pygame.image.load('sfondo_spaziale.png')

rallentamento_base = pygame.image.load('rallentamento.png')
altezza_rallentamento = 400
larghezza_rallentamento = 600
rallentamento_image = pygame.transform.scale(rallentamento_base, (larghezza_rallentamento, altezza_rallentamento))

invincibile_base = pygame.image.load('invincibile.png')
altezza_invincibile = 400
larghezza_invincibile = 600
invincibile_image = pygame.transform.scale(invincibile_base, (larghezza_invincibile, altezza_invincibile))

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
orologi = []
nonna = Nonna((150, 300))
asteroide = Asteroide()
asteroidi = []
pillole = []
running = True

tempo_invincibile_inizio = 0
durata_invincibilita = 3000  
intervallo_generazione_p = 15000
generazione_p = pygame.USEREVENT + 3
pygame.time.set_timer(generazione_p, intervallo_generazione_p)

intervallo_generazione_a = 600  
generazione_a = pygame.USEREVENT + 1
pygame.time.set_timer(generazione_a, intervallo_generazione_a)

intervallo_generazione_o = 10000  
generazione_o = pygame.USEREVENT + 2
pygame.time.set_timer(generazione_o, intervallo_generazione_o)
tempo_rallentamento_inizio = 0
tempo_rallentamento_fine = 5000

mostra_scritta_invincibile = False
tempo_scritta_invincibile = 0

mostra_scritta_rallentamento = False
tempo_scritta_rallentamento = 0

durata_scritta = 1000


def disegna_oggetti(Rallentamento):
    screen.blit(sfondo, (0,0))
    screen.blit(nonna.image, (nonna.x, nonna.y))
    for a in asteroidi:
        a.disegna_a(screen)
    for o in orologi:
        o.disegna_o(screen)
    for p in pillole:
        p.disegna_p(screen)

def aggiorna():
    pygame.display.update()
    clock.tick(fps)

gioco_attivo = True
Rallentamento = False
Invincibile = False

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if gioco_attivo:
            if Rallentamento:
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_w):
                    nonna.y -= (nonna.vy/2)
                if nonna.y <= 0:
                    nonna.y += nonna.vy
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_s):
                    nonna.y += (nonna.vy/2)
                if nonna.y >= 530:
                    nonna.y -= nonna.vy
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_a):
                    nonna.x -= (nonna.vx/2)
                if nonna.x <= -10:
                    nonna.x += nonna.vx
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_d):
                    nonna.x += (nonna.vx/2)
                if nonna.x >= 745:
                    nonna.x -= nonna.vx
            if not Rallentamento:
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
                nuovo_a = Asteroide()
                asteroidi.append(nuovo_a)
            if event.type == generazione_o:
                nuovo_o = Orologio()
                orologi.append(nuovo_o)
            if event.type == generazione_p:
                nuova_p = Pillola()
                pillole.append(nuova_p)
                
    pos_nonna = [nonna.x, nonna.y]
    if gioco_attivo:
        tempo_corrente = pygame.time.get_ticks()
        punteggio = (tempo_corrente - tempo_inizio) // 100
        for a in asteroidi:
            a.aggiorna_a(Rallentamento)
        asteroidi = [a for a in asteroidi if not a.fuori_schermo_a()]
        for o in orologi:
            o.aggiorna_o()
        orologi = [o for o in orologi if not o.fuori_schermo_o()]
        for p in pillole:
            p.aggiorna_p()
        pillole = [p for p in pillole if not p.fuori_schermo_p()]
            

        collisione_a = False

        for p in pillole:
            if p.collide_p(pos_nonna, nonna.mask):
                Invincibile = True
                tempo_invincibile_inizio = pygame.time.get_ticks()
                mostra_scritta_invincibile = True
                tempo_scritta_invincibile = pygame.time.get_ticks()
                pillole.remove(p)
                break

        for a in asteroidi:
            if a.collide_a(pos_nonna, nonna.mask):
                if not Invincibile:
                    collisione_a = True
                    tempo_collisione = pygame.time.get_ticks()
                    gioco_attivo = False
                    break

        for o in orologi:
            if o.collide_o(pos_nonna, nonna.mask):
                tempo_rallentamento_inizio = pygame.time.get_ticks()
                Rallentamento = True
                mostra_scritta_rallentamento = True
                tempo_scritta_rallentamento = pygame.time.get_ticks()   
                orologi.remove(o)
                break

        

    disegna_oggetti(Rallentamento)

    font = pygame.font.SysFont(None, 50)
    testo_punteggio = font.render(f"Punteggio: {punteggio:04d}", True, (255, 255, 255))
    screen.blit(testo_punteggio, (10, 10))

    if collisione_a:
        punteggio_finale = punteggio
        screen.blit(esplosione, (pos_nonna[0], pos_nonna[1]))
        screen.blit(gameover, (100, 100))
    
    if Rallentamento:
        current_time = pygame.time.get_ticks()
        if current_time - tempo_rallentamento_inizio > tempo_rallentamento_fine:
            Rallentamento = False

    if Invincibile:
        current_time = pygame.time.get_ticks()
        if current_time - tempo_invincibile_inizio > durata_invincibilita:
            Invincibile = False

    if mostra_scritta_invincibile:
        if pygame.time.get_ticks() - tempo_scritta_invincibile < durata_scritta:
            screen.blit(invincibile_image, (0,0))
        else:
            mostra_scritta_invincibile = False

    if mostra_scritta_rallentamento:
        if pygame.time.get_ticks() - tempo_scritta_rallentamento < durata_scritta:
            screen.blit(rallentamento_image, (0,0))
        else:
            mostra_scritta_rallentamento = False

    aggiorna()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()