# Simple pong Game (NO OOP, Spaghetti code)
# TODO
# Game Over , Restart


# Module for graphics
from difflib import restore
import turtle

# Our window
wn = turtle.Screen()
wn.title("Pong by Bassem")
wn.bgcolor("black")
wn.setup(width=800, height=600)

# Stops the window from updating and it needs to be manually updated
# Speeds up the game quite a bit, if it's not written things will be slower
wn.tracer(0)

# ________________________________________________
# Score___________________________________________
# ________________________________________________

score_a = 0
score_b = 0
restart = bool(0)

# ________________________________________________
# Paddle A_______________________________________
# ________________________________________________

paddle_a = turtle.Turtle()
# Speed of animation (Maximum speed)
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
# Stretch the paddle object
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
# Turtle usually draws a line, to prevent that we use penup
paddle_a.penup()
# Its Transform (Position) in the screen
paddle_a.goto(-350, 0)

# ________________________________________________
# Paddle B_______________________________________
# ________________________________________________

paddle_b = turtle.Turtle()
# Speed of animation (Maximum speed)
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
# Stretch the paddle object
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
# Turtle usually draws a line, to prevent that we use penup
paddle_b.penup()
# Its Transform (Position) in the screen
paddle_b.goto(350, 0)

# ________________________________________________
# Ball_______________________________________
# ________________________________________________

ball = turtle.Turtle()
# Speed of animation (Maximum speed)
ball.speed(0)
ball.shape("square")
ball.color("white")
# Turtle usually draws a line, to prevent that we use penup
ball.penup()
# Its Transform (Position) in the screen
ball.goto(0, 0)

# Ball movement (Delta)
# When the ball moves it moves by 0.1 pixels
if restart != bool(1):
    ball.dx = 0.2
    ball.dy = 0.2

# ________________________________________________
# Pen (UI)________________________________________
# ________________________________________________

pen = turtle.Turtle()

# animation speed
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center",
          font=("Courier", 24, "normal"))

# ________________________________________________
# Functions_______________________________________
# ________________________________________________


def paddle_a_up():
    # To move it we need to know its Y coordinate
    y = paddle_a.ycor()
    # Add 20 pixels to the Y coordinate
    y += 20
    # Update the paddle coordinates
    paddle_a.sety(y)


def paddle_a_down():
    # To move it we need to know its Y coordinate
    y = paddle_a.ycor()
    # Subtract 20 pixels to the Y coordinate
    y -= 20
    # Update the paddle coordinates
    paddle_a.sety(y)


def paddle_b_up():
    # To move it we need to know its Y coordinate
    y = paddle_b.ycor()
    # Add 20 pixels to the Y coordinate
    y += 20
    # Update the paddle coordinates
    paddle_b.sety(y)


def paddle_b_down():
    # To move it we need to know its Y coordinate
    y = paddle_b.ycor()
    # Subtract 20 pixels to the Y coordinate
    y -= 20
    # Update the paddle coordinates
    paddle_b.sety(y)


def gameOver():

    restart = bool(1)
    paddle_a.clear()
    paddle_b.clear()
    ball.clear()

    pen.goto(0, 0)
    pen.color("red")
    pen.write("Game Over", align="center",
              font=("Courier", 54, "normal"))

    pen.goto(0, -50)
    pen.color("white")
    pen.write("Restart", align="center",
              font=("Courier", 24, "normal"))


# ________________________________________________
# Keyboard binding_______________________________________
# ________________________________________________

# In the turtle module. This command tells it to listen dor keyboard input
wn.listen()

# paddle_a
# Excute the function when the "w,s" keys are pressed
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

# paddle_b
# Excute the function when the "Up,Down" keys are pressed
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# ________________________________________________
# Man game loop_______________________________________
# ________________________________________________

while True:

    # Everytime the loop runs it updates the screen
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Top Boorder Check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # Down border check
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Right border check
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))

    # Left border check
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 24, "normal"))

    # Paddle and ball collistion
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    # Paddle and ball collistion
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
