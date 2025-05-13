import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Nonna Rampage")
clock = pygame.time.Clock()

color = (245, 235, 220)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(color)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()