import pygame
import numpy as np
import random

pygame.init()

cuadrado=np.array((
    (1, 1),
    (1, 1),
))
palo=np.array((
    (1, 1, 1, 1),
))

WIDTHPANTALLA, HEIGHTPANTALLA = 600, 600
WIDTHTABLERO, HEIGHTTABLERO = 300, 600
SEPARACION=30
Score=0
Figura=random.randint(0,7)
ventana = pygame.display.set_mode((WIDTHPANTALLA,HEIGHTPANTALLA))


#Titulo
pygame.display.set_caption("Tetris")

# Dibujar cuadrado
def dibujarCuadrado():

# Crear tablero
def crearTablero(ventana):
    color_tablero=(50,50,50)
    pygame.draw.rect(ventana, (255, 255, 255), pygame.Rect(0,0,WIDTHTABLERO,HEIGHTTABLERO))
    for i in range(11):
        x = SEPARACION * i
        pygame.draw.line(
            ventana, color_tablero, (x, 0), (x, HEIGHTTABLERO)
        )
        # Horizontal liens.
    for i in range(21):
        y = SEPARACION * i
        pygame.draw.line(
            ventana, color_tablero, (0, y), (WIDTHTABLERO, y)
        )

#Bucle principal

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           exit()

    ventana.fill((0,0,0))
    crearTablero(ventana)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()