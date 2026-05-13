# Crear una ciudad de hierro o parque de atraaciones usando los elementos graficos vistos con pygame (lineas, rectangulos, cuadrados, poligonos, circulos, elipses, arcos y textos) en donde los personajes son pacmans.

import pygame
import math

# Inicializar pygame
pygame.init()

# Ventana
ANCHO = 900
ALTO = 650

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Parque de Atracciones")

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 150, 255)
VERDE = (0, 200, 0)
ROJO = (255, 0, 0)
AMARILLO = (255, 255, 0)
NARANJA = (255, 140, 0)
MORADO = (180, 0, 255)
GRIS = (120, 120, 120)
CELESTE = (0, 255, 255)

# Fuentes
fuente_titulo = pygame.font.SysFont("Arial", 38, bold=True)
fuente_nombre = pygame.font.SysFont("Arial", 25)

# Posición Pacman
x = 100

# Reloj
clock = pygame.time.Clock()

# Bucle principal
ejecutando = True

while ejecutando:

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Fondo
    pantalla.fill((20, 20, 50))

    # Césped
    pygame.draw.rect(pantalla, VERDE, (0, 500, 900, 150))

    # Camino
    pygame.draw.rect(pantalla, GRIS, (0, 470, 900, 40))

    # ----------------------------
    # Texto superior
    # ----------------------------
    titulo = fuente_titulo.render(
        "PARQUE DE ATRACCIONES",
        True,
        BLANCO
    )

    pantalla.blit(titulo, (220, 20))

    # ----------------------------
    # Rueda de la fortuna
    # ----------------------------
    centro = (700, 250)

    pygame.draw.circle(pantalla, BLANCO, centro, 100, 4)

    for angulo in range(0, 360, 45):

        x1 = centro[0] + 100 * math.cos(math.radians(angulo))
        y1 = centro[1] + 100 * math.sin(math.radians(angulo))

        pygame.draw.line(
            pantalla,
            BLANCO,
            centro,
            (x1, y1),
            2
        )

        pygame.draw.rect(
            pantalla,
            CELESTE,
            (x1 - 10, y1 - 10, 25, 25)
        )

    pygame.draw.line(pantalla, GRIS, (660, 470), centro, 8)
    pygame.draw.line(pantalla, GRIS, (740, 470), centro, 8)

    pygame.draw.arc(
        pantalla,
        ROJO,
        (250, 240, 250, 160),
        math.radians(0),
        math.radians(180),
        5
    )



    # Entrada
    pygame.draw.rect(
        pantalla,
        MORADO,
        (405, 390, 50, 60)
    )




    # ----------------------------
    # Pacman
    # ----------------------------
    pygame.draw.circle(
        pantalla,
        AMARILLO,
        (x, 400),
        25
    )

    pygame.draw.polygon(
        pantalla,
        NEGRO,
        [
            (x, 440),
            (x + 25, 425),
            (x + 25, 455)
        ]
    )

    pygame.draw.circle(
        pantalla,
        NEGRO,
        (x, 430),
        4
    )

    # Movimiento
    x += 3

    if x > 950:
        x = -50

    # ----------------------------
    # Texto inferior
    # ----------------------------
    nombre = fuente_nombre.render(
        "HEIDY ACOSTA",
        True,
        BLANCO
    )

    pantalla.blit(nombre, (360, 610))

    # Actualizar
    pygame.display.update()

    clock.tick(60)

pygame.quit()