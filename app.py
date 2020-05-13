import turtle
import winsound



win = turtle.Screen()
win.setup(width=800, height=500)
win.bgcolor("black")
win.title("*************************************      The game show    ******                                   ")
win.tracer(0)

# score record
score1: int=0
score2: int=0

# player information

scoreboard = turtle.Turtle()
scoreboard.color("white")
scoreboard.penup()
scoreboard.fillcolor("blue")
scoreboard.hideturtle()
scoreboard.goto(0, 220)
scoreboard.write("player_1 = 0   player_2 = 0", align="center", font=("courier", 20, "normal"))


# paddle A
pong1 = turtle.Turtle()
pong1.color("red")
pong1.speed(0)
pong1.shape("square")
pong1.shapesize(stretch_wid=5, stretch_len=1)
pong1.penup()
pong1.goto(-350, 0)


# paddle B
pong2 = turtle.Turtle()
pong2.color("red")
pong2.speed(0)
pong2.shape("square")
pong2.shapesize(stretch_wid=5, stretch_len=1)
pong2.penup()
pong2.goto(+350, 0)

# ball

ball = turtle.Turtle()
ball.color("white")
ball.speed(0)
ball.shape("circle")
ball.penup()
ball.dx = 0.2
ball.dy = 0.2


def move_up():
    y = pong1.ycor()
    if(y>180):
        y = 180
    y = y+20
    pong1.sety(y)


def move_down():
    y = pong1.ycor()
    if(y<-180):
        y = -180

    y = y-20
    pong1.sety(y)


def move_down1():
     y1 = pong2.ycor()
     if (y1< -180):
         y1 = -180
     y1 = y1 - 20
     pong2.sety(y1)


def move_up1():
    y1 = pong2.ycor()
    if (y1>180):
        y1 = 180
    y1 = y1+20
    pong2.sety(y1)


win.listen()
win.onkeypress(move_up, "w")
win.onkeypress(move_down, "s")
win.onkeypress(move_up1, "Up")
win.onkeypress(move_down1, "Down")

# main loop
while True:
    win.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 240:
        ball.sety(240)
        ball.dy = ball.dy * -1
        #winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

       # scoreboard.write("player_1 = score1 player_2 = 0", align="center", font=("courier", 20, "normal"))

    if ball.ycor() < -240:
        ball.sety(-240)
        ball.dy = ball.dy * -1
        #winsound.PlaySound("bounce.wav",winsound.SND_LOOP)
    if ball.xcor() > 390:
        ball.setx(0)
        ball.dx = ball.dx * -1
        score1=score1+1
        scoreboard.clear()
        scoreboard.write("player_1={},player_2={}".format(score1,score2), align="center", font=("courier", 20, "normal"))

    if ball.xcor() < -390:
        ball.setx(0)
        ball.dx = ball.dx * -1
        score2 = score2+1
        scoreboard.clear()
        scoreboard.write("player_1={},player_2={}".format(score1, score2), align="center", font=("Arial",20,"normal"))


    if ball.xcor() > 330 and (ball.ycor() < pong2.ycor() + 50) and (ball.ycor() > pong2.ycor() - 50):
        ball.setx(330)
        ball.dx *= -1

    if ball.xcor() < -330 and (ball.ycor() < pong1.ycor() + 50) and (ball.ycor() > pong1.ycor() - 50):
        ball.setx(-330)
        ball.dx *= -1

