import turtle

wn = turtle.Screen()
wn.title("Pong Game by Adina S")
wn.bgcolor("black")
wn.setup(width=800, height=600) #x(-400;400) y(-400;400)
wn.tracer(0)

#Left platfrom
platform_a = turtle.Turtle()
platform_a.speed(0)
platform_a.shape("square")
platform_a.color("white")
platform_a.shapesize(stretch_wid=5, stretch_len=1)
platform_a.penup()
platform_a.goto(-350, 0)


#Right platfrom
platform_b = turtle.Turtle()
platform_b.speed(0)
platform_b.shape("square")
platform_b.color("white")
platform_b.shapesize(stretch_wid=5, stretch_len=1)
platform_b.penup()
platform_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0
ball.dy = 0

#Score data
score_board = turtle.Turtle()
score_board.speed(0)
score_board.color("white")
score_board.penup()
score_board.hideturtle()
score_board.goto(0, 260)
score_board.write("Player 1: 0  	Player 2: 0", align="center", font=("Arial", 24, "normal"))

#score
score_a = 0
score_b = 0
winner = "Player"

#End game function
def endGame():
    end_title = turtle.Turtle()
    end_title.speed(0)
    end_title.color("red")
    end_title.goto(0,3)
    end_title.penup()
    end_title.hideturtle()
    if score_a > score_b:
        winner = "PLAYER 1 WON"
    if score_a < score_b:
        winner = "PLAYER 2 WON"
    if score_a == score_b:
        winner = "DRAW"
    end_title.write(winner, align="center", font=("Arial", 40, "normal"))

#Functions
def platfrom_a_up():
    y = platform_a.ycor()
    y += 30
    platform_a.sety(y)
    if platform_a.ycor() > 390:
        platform_a.sety(-370)

def platfrom_a_down():
    y = platform_a.ycor()
    y -= 30
    platform_a.sety(y)
    if platform_a.ycor() < -390:
        platform_a.sety(370)

def platfrom_b_up():
    y = platform_b.ycor()
    y += 30
    platform_b.sety(y)
    if platform_b.ycor() > 390:
        platform_b.sety(-370)

def platfrom_b_down():
    y = platform_b.ycor()
    y -= 30
    platform_b.sety(y)
    if platform_b.ycor() < -390:
        platform_b.sety(370)

#Keyboard binding
wn.listen()
wn.onkeypress(platfrom_a_up, "w")
wn.onkeypress(platfrom_a_down, "s")
wn.onkeypress(platfrom_b_up, "Up")
wn.onkeypress(platfrom_b_down, "Down")

#Game starting count
timer = turtle.Turtle()
timer.penup()
timer.goto(0,4)
timer.hideturtle()
timer.color("red")

def countdown(count):
    timer.clear()
    if count > 0:
        timer.write(count, align="center", font=("Arial", 40, "normal"))
        wn.ontimer(lambda: countdown(count - 1), 1000)
    else:
        timer.write("START!", align="center", font=("Arial", 40, "normal"))
        wn.ontimer(timer.clear, 400)
        ball.dx = 2 #moves for 2 pixels
        ball.dy = 2

countdown(3)
while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #reverses the direction of the ball

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        if ball.dx > 0:
            ball.dx += 0.5
        else:
            ball.dx -= 0.5
        ball.dx *= -1
        score_a += 1
        score_board.clear()
        score_board .write(f"Player 1: {score_a}	 Player 2: {score_b}", align="center", font=("Arial", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        if ball.dx > 0:
            ball.dx += 0.5
        else:
            ball.dx -= 0.5
        ball.dx *= -1
        score_b += 1
        score_board.clear()
        score_board .write(f"Player 1: {score_a} 	Player 2: {score_b}", align="center", font=("Arial", 24, "normal"))

    #Platform and Ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < platform_b.ycor() + 50 and ball.ycor() > platform_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1


    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < platform_a.ycor() + 50 and ball.ycor() > platform_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

    if score_a == 3 or score_b == 3:
        ball.dx = 0
        ball.dy = 0
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        endGame()

