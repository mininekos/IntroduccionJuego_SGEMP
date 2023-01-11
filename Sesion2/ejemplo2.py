import pygame

pygame.init()

WIDTH, HEIGHT = 640, 480
ventana = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Ejemplo 2")
#Crea el objeto pelota
ball = pygame.image.load("./imagen/Pokeball.png")
# ball= pygame.transform.scale(ball(59,33)) no va
#Obtengo el rectangulo del objeto anterior
ballrect = ball.get_rect()
# Inicializo los valores con los que van a mover la pelota.
speed =[4,4]
#Pongo la pelata en el origen de coordenadas
ballrect.move_ip(0,0)
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #Muevo la pelota
    ballrect=ballrect.move(speed)
    # Compruebo si la pelota llega a los limites de la ventana
    # Eje X
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    #Eje Y
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speed[1] = -speed[1]

    ventana.fill((252,243,207))
    ventana.blit(ball,ballrect)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()