import pygame

pygame.init()

WIDTH, HEIGHT = 640, 480
ventana = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Ejemplo 3")

ball = pygame.image.load("imagen/Pokeball.png")
ball= pygame.transform.scale(ball,(40,40))
paddle=pygame.image.load("imagen/barra.png")
paddle= pygame.transform.scale(paddle,(80,29))


ballrect = ball.get_rect()
paddlerect=paddle.get_rect()

speed =[4,4]

ballrect.move_ip(0,0)
paddlerect.move_ip(320,450)
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys= pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddlerect.left > 0:
        paddlerect=paddlerect.move(-5,0)
    if keys[pygame.K_RIGHT] and paddlerect.right < ventana.get_width():
        paddlerect = paddlerect.move(5, 0)
    #Compruebo si hay colision
    if paddlerect.colliderect(ballrect):
        speed[1]=-speed[1]

    ballrect=ballrect.move(speed)

    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]

    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speed[1] = -speed[1]

    ventana.fill((0,0,0))
    ventana.blit(ball,ballrect)
    ventana.blit(paddle, paddlerect)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()