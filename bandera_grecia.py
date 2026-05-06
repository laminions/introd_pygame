# importamos la libreria pygame
import pygame

# inicializamos los modulos de la libreria
pygame.init()

# establecer dimensiones de la ventana
ventana = pygame.display.set_mode((1080,720))

# establecer titulo de la ventana
pygame.display.set_caption("pygame heidy")

blanco = (255,255,255)
azul = (13,94,175)

# creamos una superficie 
superficie_1 = pygame.Surface((1080,750))
superficie_2 = pygame.Surface((1080,80))
superficie_3 = pygame.Surface((1080,80))
superficie_4 = pygame.Surface((680,80))
superficie_5 = pygame.Surface((680,80))
superficie_6 = pygame.Surface((680,80))
superficie_7 = pygame.Surface((160,160))
superficie_8 = pygame.Surface((160,160))
superficie_9 = pygame.Surface((160,160))
superficie_10 = pygame.Surface((160,160))

superficie_1.fill(blanco)
superficie_2.fill(azul)
superficie_3.fill(azul)
superficie_4.fill(azul)
superficie_5.fill(azul)
superficie_6.fill(azul)
superficie_7.fill(azul)
superficie_8.fill(azul)
superficie_9.fill(azul)
superficie_10.fill(azul)


ventana.blit(superficie_1, (0,0))
ventana.blit(superficie_2, (0,640))
ventana.blit(superficie_3, (0,480))
ventana.blit(superficie_4, (400,320))
ventana.blit(superficie_5, (400,160))
ventana.blit(superficie_6, (400,0))
ventana.blit(superficie_7, (0,0))
ventana.blit(superficie_8, (240,0))
ventana.blit(superficie_9, (0,240))
ventana.blit(superficie_10, (240,240))


pygame.display.flip()

# bucle del juego 
while True :
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame.quit()
