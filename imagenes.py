import pygame, sys

pygame.init()

pantalla = pygame.display.set_mode((370,442))
pygame.display.set_caption("mario bros")
NEGRO = (0,0,0)
pantalla.fill(NEGRO)

# cargar imagen
mario = pygame.image.load("Assets/images/mario03.png").convert()
# ubicar la imagen en la ventana
pantalla.blit(mario, (5,5))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.flip()
