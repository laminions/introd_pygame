# importamos la libreria pygame
import pygame
import sys
import math


# inicializamos los modulos de la librería
pygame.init()

# Establecer dimensiones de la ventana
ventana = pygame.display.set_mode((400,400))

# establecer titulo de la ventana
pygame.display.set_caption("Dibujar formas básicas")

# definición colores
negro = (0,0,0)
rojo = (255,0,0)
azul = (0,0,255)
naranja = (255,165,0)
verde = (0,255,0)
rosado = (255,192,203)
amarillo = (255,255,0)
blanco = ( 255,255,255)
cian = (0,255,255)

# variables auxiliares
PI = math.pi

# Objeto para la gestión del tiempo
clock = pygame.time.Clock()

# bucle principal del juego
while True:
    # Maximo de fotogramas por segundo
    clock.tick(50)

    for event in pygame.event.get():
        # Al hacer click sobre el boton de cerrar la ventana el juego termina
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(negro)

    # ------------------------------
    # Dibujar formas con modulo draw
    # ------------------------------

    # linesas rectas continuas
    pygame.draw.line(ventana,rojo, (0,0), (400,400), 5)
    pygame.draw.line(ventana,rojo, (0,400), (400,0), 5)

    # lineas resctas descontinuas
    puntos_1 = [(0,0), (50,100), (100,50), (250,200), (400,400)]
    puntos_2 = [(200,0), (400,200), (200,400), (0,200)]
    pygame.draw.lines(ventana,azul,False, puntos_1)
    pygame.draw.lines(ventana,naranja, True,puntos_2)

    # rectangulo relleno 
    pygame.draw.rect(ventana,rosado, (150,150,50,50))

    # rectangulo sin relleno
    pygame.draw.rect(ventana,verde, ((200,200), (50,50)), 3)

    # poligono
    puntos_3 = [(100,200), (200,300), (100,400), (0,300)]
    pygame.draw.polygon(ventana, amarillo, puntos_3,3)

    # estrella
    puntos_4 = [(0,200), (150,150), (200,0), (250,150), (400,200), (250,250), (200,400), (150,250)]
    #pygame.draw.polygon(ventana, cian, puntos_4)

    # circulo
    pygame.draw.circle(ventana, blanco, (300,300), 100,0)

    #Elipse
    pygame.draw.ellipse(ventana,naranja, (200,250,200,100),3)
    pygame.draw.ellipse(ventana,naranja, (250,200,100,200),3)

    #Arcos
    pygame.draw.arc(ventana, cian, (200,0,200,200),PI/4, 7*PI/4,100 )

    #texto
    fuente_arial = pygame.font.SysFont("Arial", 35, 1, 1)
    texto = fuente_arial.render("heidy acosta", 1,blanco)
    ventana.blit(texto, (0,50))

    # actualizar visualización de la ventana
    pygame.display.flip()