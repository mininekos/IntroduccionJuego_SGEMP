import time
import turtle
import random


score=0
delay=0.1

# Configuramos la ventana
wn= turtle.Screen()
wn.title("Serpiente🐍")
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0)

# Cabeza de serpiente

cabeza= turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("white")
# Para no dejar estela
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction="stop"

# La manzana
manzana= turtle.Turtle()
manzana.speed(0)
manzana.shape("circle")
manzana.color("red")
manzana.penup()
manzana.goto(random.randint(-280,280),random.randint(-280,280))

# El cuerpo de la serpiente
segmentos=[]

def arriba():
    if cabeza.direction != "down":
        cabeza.direction = "up"
def abajo():
    if cabeza.direction != "up":
        cabeza.direction = "down"
def derecha():
    if cabeza.direction != "left":
        cabeza.direction = "right"
def izquierda():
    if cabeza.direction != "right":
        cabeza.direction = "left"

def mov():
    if cabeza.direction == "up":
        y=cabeza.ycor()
        cabeza.sety(y+20)
    if cabeza.direction == "down":
        y=cabeza.ycor()
        cabeza.sety(y-20)
    if cabeza.direction == "right":
        x=cabeza.xcor()
        cabeza.setx(x+20)
    if cabeza.direction == "left":
        x=cabeza.xcor()
        cabeza.setx(x-20)

wn.listen()
wn.onkeypress(arriba,"Up")
wn.onkeypress(abajo,"Down")
wn.onkeypress(derecha,"Right")
wn.onkeypress(izquierda,"Left")
while True:
    wn.update()

    if cabeza.distance(manzana)< 20:
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        manzana.goto(x,y)

        nuevo_segmento=turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("blue")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

    totalSeg=len(segmentos)
    for index in range(totalSeg -1,0,-1):
        x=segmentos[index-1].xcor()
        y=segmentos[index-1].ycor()
        segmentos[index].goto(x,y)

    if totalSeg > 0:
        x=cabeza.xcor()
        y=cabeza.ycor()
        segmentos[0].goto(x,y)

    if cabeza.ycor()>280 or cabeza.ycor()<-280 or cabeza.xcor()>280 or cabeza.xcor()<-280 :


        cabeza.goto(0,0)
        cabeza.direction="stop"
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        manzana.goto(x, y)
        for segmento in segmentos:
            segmento.reset()
        segmentos.clear()


    mov()
    time.sleep(delay)