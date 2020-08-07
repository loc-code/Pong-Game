import turtle

wn = turtle.Screen()
wn.title("Loc's Pong Game!")
wn.bgcolor("Black")
wn.setup(width = 900, height = 600)
wn.tracer(0)

# Player A
player_a = turtle.Turtle()
player_a.speed(0)
player_a.shape("square")
player_a.shapesize(stretch_wid = 5, stretch_len = 0.5)
player_a.color("white")
player_a.pesssnup()
player_a.goto(-430, 0)

# Player B
player_b = turtle.Turtle()
player_b.speed(0)
player_b.shape("square")
player_b.shapesize(stretch_wid = 5, stretch_len = 0.5)
player_b.color("white")
player_b.penup()
player_b.goto(422, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.46
ball.dy = -0.46

# Function
def player_a_up():
	y = player_a.ycor()
	y += 25
	player_a.sety(y)

def player_a_down():
	y = player_a.ycor()
	y -= 25
	player_a.sety(y)

def player_b_up():
	y = player_b.ycor()
	y += 20
	player_b.sety(y)

def player_b_down():
	y = player_b.ycor()
	y -= 20
	player_b.sety(y)


# KeyBoard Binding
wn.listen()
wn.onkeypress(player_a_up, "w")
wn.onkeypress(player_a_down, "s")
wn.onkeypress(player_b_up, "Up")
wn.onkeypress(player_b_down, "Down")


# Main Game Loop
while True:
	wn.update()

	#Move The Ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	#Boders checking
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1

	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1

	if ball.xcor() > 426:
		ball.goto(0, 0)
		ball.dx *= -1

	if ball.xcor() < -426:
		ball.goto(0, 0)
		ball.dx *= -1


	if ball.xcor() > 415 and (ball.ycor() < player_b.ycor() + 50 and ball.ycor() > player_b.ycor() - 50):
		ball.dx *= -1

	if ball.xcor() < -415 and (ball.ycor() < player_a.ycor() + 50 and ball.ycor() > player_a.ycor() - 50):
		ball.dx *= -1

