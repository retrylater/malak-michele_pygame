import pygame

class Nonna:
    def __init__(self, pos = []):        #a cosa serve platofrm e screen? l'ho tolto poi vediamo
        #self.screen = screen
        #self.platform = platform
        immagine_originale = pygame.image.load("nonna.jpeg")
        nuova_larghezza = 70
        nuova_altezza = 70
        self.image = pygame.transform.scale(immagine_originale, (nuova_larghezza, nuova_altezza))
        self.rect = self.image.get_rect()
        self.x = pos[0]
        self.y = pos[1] 

#bisogna capire come modificare la rect 
        self.vx = 8
        self.vy = 8
        #self.g= 0.5 #cos'è?
         
    
    