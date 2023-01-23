"""
    BATALLA DE NAVES

    - 2 Naves
    - 2 Campos
    - Cada nave se controla con keys diferentes
    - Cada Jugador dispara con una tecla

"""

import time
import turtle


delay=0.1
wn= turtle.Screen()
wn.title("Naves")
wn.bgcolor("Black")
wn.setup(width=600,height=600)
wn.tracer(0)

nave1 = turtle.Turtle()
nave1.speed(0)
nave1.shape("square")
nave1.color("white")
nave1.penup()
nave1.goto(-150,0)
nave1.direction="stop"


nave2 = turtle.Turtle()
nave2.speed(0)
nave2.shape("square")
nave2.color("white")
nave2.penup()
nave2.goto(150,0)
nave2.direction="stop"

campo = turtle.Turtle()
campo.speed(0)
campo.shape("square")
campo.color("white")
campo.penup()
campo.goto(0,0)
campo.shapesize(31,0.02,1)
campo.direction="stop"

# Bala nave 1
bala1= turtle.Turtle()
bala1.speed(0)
bala1.shape("square")
bala1.color("blue")
bala1.penup()
bala1.shapesize(0.3,0.6,1)
bala1.goto(1000,1000)

# Bala nave 2
bala2= turtle.Turtle()
bala2.speed(0)
bala2.shape("square")
bala2.color("red")
bala2.penup()
bala2.shapesize(0.3,0.6,1)
bala2.goto(-1000,-1000)

# Score
scoreNave1=0
scoreNave2=0
texto = turtle.Turtle()
texto.speed(0)
texto.shape("square")
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0, 250)
texto.write(f"Nave 1 : {scoreNave1}                       Nave 2: {scoreNave2}",
            align="center",font=("candara", 24, "bold"))

VELNAVE=10
VELBALA=10
# Mov nave1
def arribaNave1():
    y = nave1.ycor()
    nave1.sety(y + VELNAVE)
def abajoNave1():
    y = nave1.ycor()
    nave1.sety(y - VELNAVE)
def derechaNave1():
    x= nave1.xcor()
    nave1.setx(x - VELNAVE)
def izquierdaNave1():
    x = nave1.xcor()
    nave1.setx(x + VELNAVE)


# Mov nave2
def arribaNave2():
    y = nave2.ycor()
    nave2.sety(y + VELNAVE)
def abajoNave2():
    y = nave2.ycor()
    nave2.sety(y - VELNAVE)
def derechaNave2():
    x= nave2.xcor()
    nave2.setx(x + VELNAVE)
def izquierdaNave2():
    x = nave2.xcor()
    nave2.setx(x - VELNAVE)

def balaNave1():
    y=nave1.ycor()
    x=nave1.xcor()
    # La bala
    bala1.goto(x,y)


def balaNave2():
    y = nave2.ycor()
    x = nave2.xcor()
    # La bala
    bala2.goto(x, y)



wn.listen()
wn.onkeypress(arribaNave1,"w")
wn.onkeypress(abajoNave1,"s")
wn.onkeypress(derechaNave1,"a")
wn.onkeypress(izquierdaNave1,"d")
wn.onkeypress(arribaNave2,"Up")
wn.onkeypress(abajoNave2,"Down")
wn.onkeypress(derechaNave2,"Right")
wn.onkeypress(izquierdaNave2,"Left")
wn.onkeypress(balaNave1,"space")
wn.onkeypress(balaNave2,"KP_Enter")
wn.onkeypress(balaNave2,"0")
while True:
    wn.update()
    if bala1.xcor()<300:
        x=bala1.xcor()
        bala1.setx(x+VELBALA)
    if bala2.xcor() > -310:
        x = bala2.xcor()
        bala2.setx(x - VELBALA)
    if bala1.distance(nave2)<10:
        scoreNave1+=10
        texto.clear()
        texto.write(f"Nave 1 : {scoreNave1}                       Nave 2: {scoreNave2}",
                    align="center", font=("candara", 24, "bold"))
    if bala2.distance(nave1) < 10:
        scoreNave2 += 10
        texto.clear()
        texto.write(f"Nave 1 : {scoreNave1}                       Nave 2: {scoreNave2}",
            align="center",font=("candara", 24, "bold"))

    time.sleep(delay)


