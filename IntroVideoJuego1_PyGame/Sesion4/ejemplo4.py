import pygame
from random import *

pygame.init()

WIDTH, HEIGHT = 640, 480
ventana = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Ejemplo 4")

ball = pygame.image.load("imagen/Pokeball.png")
ball= pygame.transform.scale(ball,(40,40))
paddle=pygame.image.load("imagen/barra.png")
paddle= pygame.transform.scale(paddle,(80,29))


ballrect = ball.get_rect()
paddlerect=paddle.get_rect()

speed =[randint(3,6), randint(3,6)]
ballrect.move_ip(0,0)
paddlerect.move_ip(WIDTH/2,450)


fuente = pygame.font.Font(None,36)

texto=fuente.render("Game Over",True,(125,125,125))
texto_rect=texto.get_rect()
textoX=ventana.get_width()/2-texto_rect.width/2
textoY=ventana.get_height()/2-texto_rect.height/2

perder=False


run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys= pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddlerect.left > 0 and not perder:
        paddlerect=paddlerect.move(-5,0)
    if keys[pygame.K_RIGHT] and paddlerect.right < ventana.get_width() and perder==False:
        paddlerect = paddlerect.move(5, 0)
    #Compruebo si hay colision
    if paddlerect.colliderect(ballrect):
        # if paddlerect.midleft:
        #     speed[0] = - randint(3, 6)
        # if paddlerect.midright:
        #     speed[0] = randint(3, 6)
        speed[1]= - randint(3,6)
        speed[0]= randint(3,6)


    ballrect=ballrect.move(speed)

    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]

    if ballrect.top < 0:
        speed[1] = -speed[1]

    if ballrect.bottom > ventana.get_height():
        perder=True
        speed[0]=0
        speed[1]=0


    ventana.fill((0,0,0))
    ventana.blit(ball,ballrect)
    ventana.blit(paddle, paddlerect)
    if perder:
        ventana.blit(texto, [textoX,textoY])
        if keys[pygame.K_SPACE]:
            perder = False
            ballrect = ball.get_rect()
            paddlerect = paddle.get_rect()
            speed = [randint(3, 6), randint(3, 6)]
            ballrect.move_ip(0, 0)
            paddlerect.move_ip(WIDTH / 2, 450)
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()