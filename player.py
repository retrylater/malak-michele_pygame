import pygame

class Nonna:
    def __init__(self, pos = []):       
        immagine_originale = pygame.image.load("nonna_trasparente.png")
        nuova_larghezza = 70
        nuova_altezza = 70
        self.image = pygame.transform.scale(immagine_originale, (nuova_larghezza, nuova_altezza))
        self.rect = self.image.get_rect()
        self.x = pos[0]
        self.y = pos[1] 
        self.vx = 3
        self.vy = 3

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.rect.x = self.x
        self.rect.y = self.y


    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
        
    
    