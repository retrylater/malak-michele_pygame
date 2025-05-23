import pygame

class Restart():
    def __init__(self):
        self.altezza = 80
        self.larghezza = 180
        self.pos = [310, 450]
        self.colore = (0, 125, 125)
        self.surface = pygame.Surface((self.larghezza, self.altezza))
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.larghezza, self.altezza)

    def schiacciato(self, pos_mouse):
        if self.rect.collidepoint(pos_mouse):
            return True
        else:
            return False

    def disegna(self, screen):
        pygame.draw.rect(screen, self.colore, self.rect)
        font = pygame.font.Font(None, 60)
        imgtext_i = font.render('RESTART', True, (0, 0, 0))
        imgtext_f = pygame.transform.scale(imgtext_i, (150, 60))
        screen.blit(imgtext_f, (325, 460))
        
