import time
import turtle
import random

# Configuramos la ventana

wn= turtle.Screen()
wn.title("Juego de Pong")
wn.bgcolor("black")
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

manzana= turtle.Turtle()
manzana.speed(0)
manzana.shape("circle")
manzana.color("red")
# Para no dejar estela
manzana.penup()
manzana.goto(random.randint(-290,290),random.randint(-290,290))
manzana.direction="stop"

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
    mov()
    Posponer=0.1
    time.sleep(Posponer)