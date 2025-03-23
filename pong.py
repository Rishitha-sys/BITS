import turtle
import time

def pong():
    screen = turtle.Screen()
    screen.title("One Player Pong")
    screen.bgcolor("black")
    screen.setup(width=600, height=600)
    screen.tracer(0)

    # Paddle
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(-250, 0)

    # Ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("red")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 3
    ball.dy = 3

    # Score
    score = 0
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

    # Paddle movement
    def paddle_up():
        y = paddle.ycor()
        if y < 250:
            paddle.sety(y + 20)

    def paddle_down():
        y = paddle.ycor()
        if y > -240:
            paddle.sety(y - 20)

    # Keyboard bindings
    screen.listen()
    screen.onkey(paddle_up, "Up")
    screen.onkey(paddle_down, "Down")

    # Main game loop
    game_over = False
    while not game_over:
        screen.update()

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Bounce off top and bottom walls
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        # Bounce off right wall
        if ball.xcor() > 290:
            ball.setx(290)
            ball.dx *= -1

        # Bounce off paddle
        if (ball.xcor() < -230 and ball.xcor() > -240) and (paddle.ycor() + 50 > ball.ycor() > paddle.ycor() - 50):
            ball.setx(-230)
            ball.dx *= -1
            score += 1
            pen.clear()
            pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

        # Check if ball missed paddle (goes past left wall)
        if ball.xcor() < -300:
            pen.clear()
            pen.goto(0, 0)
            pen.write("Game Over!\nFinal Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
            print(f"\nGame Over! You scored {score} points.")
            time.sleep(2)
            game_over = True
            turtle.bye()  # Close window

        time.sleep(0.01)  # Control speed
pong()
