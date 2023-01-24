import pygame
import random

pygame.init()

#Matriz de todas las figuras
figuras = [
        [[1, 2, 5, 6]], #Cuadrao
        [[1, 5, 9, 13], [4, 5, 6, 7]],#Palo
        # [[4, 5, 9, 10], [2, 6, 5, 9]],# Z
        # [[6, 7, 9, 10], [1, 5, 6, 10]],# Z invertida
        # [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],# Mini T
        # [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],# L
        # [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],# L invertida
    ]
#Colores posibles
coloresFiguras = [(0, 255, 0), (255, 0, 0), (0, 255, 255),
                  (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]

WIDTHPANTALLA, HEIGHTPANTALLA = 600, 600
WIDTHTABLERO, HEIGHTTABLERO = 300, 600
SEPARACION=30
Score=0
ventana = pygame.display.set_mode((WIDTHPANTALLA,HEIGHTPANTALLA))


#Titulo
pygame.display.set_caption("Tetris")

#Clase completa de la figura

class Figura:
    # Inicializo la figura
    def __init__(self, x, y,numRandom):
        self.x = x
        self.y = y
        self.rotacion = 0
        self.forma = numRandom
        self.color = numRandom

    def pintar(self):
        return figuras[self.forma][self.rotacion]

    def girar(self):
        self.rotacion = (self.rotacion + 1) % len(figuras[self.type])
class Tetris:
    level = 2
    state = "start"
    tablero = []
    height = 0
    width = 0
    x = 100
    y = 60
    zoom = 20
    figura = None

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.tablero = []
        self.score = 0
        self.state = "start"
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.tablero.append(new_line)

    def nuevaFigura(self):
        self.figura = Figura(3, 0,random.randint(0,len(figuras)-1))

    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figura.pintar():
                    if i + self.figura.y > self.height - 1 or \
                            j + self.figura.x > self.width - 1 or \
                            j + self.figura.x < 0 or \
                            self.tablero[i + self.figura.y][j + self.figura.x] > 0:
                        intersection = True
        return intersection

    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.tablero[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.tablero[i1][j] = self.tablero[i1 - 1][j]
        self.score += lines ** 2

    def go_space(self):
        while not self.intersects():
            self.figura.y += 1
        self.figura.y -= 1
        self.freeze()

    def go_down(self):
        self.figura.y += 1
        if self.intersects():
            self.figura.y -= 1
            self.freeze()

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figura.pintar():
                    self.tablero[i + self.figura.y][j + self.figura.x] = self.figura.color
        self.break_lines()
        self.nuevaFigura()
        if self.intersects():
            self.state = "gameover"

    def go_side(self, dx):
        old_x = self.figura.x
        self.figura.x += dx
        if self.intersects():
            self.figura.x = old_x

    def girar(self):
        posicionAnterior = self.figura.rotacion
        self.figura.girar()
        if self.intersects():
            self.figura.rotacion = posicionAnterior
# Crear tablero
def crearTablero(ventana):
    color_tablero=(128,128,128)
    pygame.draw.rect(ventana, (255, 255, 255), pygame.Rect(0,0,WIDTHTABLERO,HEIGHTTABLERO))
    # Pinto las lineas verticales
    for i in range(11):
        x = SEPARACION * i
        pygame.draw.line(
            ventana, color_tablero, (x, 0), (x, HEIGHTTABLERO)
        )
        # Pinto las lineas horizontal
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
        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_UP:
                # girar
                input()
            if event.key== pygame.K_LEFT:
                # mover izquierda
                input()
            if event.key== pygame.K_RIGHT:
                # mover derecha
                input()
            if event.key== pygame.K_DOWN:
                # bajar la pieza
                input()


    ventana.fill((0,0,0))
    crearTablero(ventana)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()