import turtle
import time
def brick():
    # Setup screen
    screen = turtle.Screen()
    screen.title("Brick Breaker")
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.tracer(0)

    # Paddle
    paddle = turtle.Turtle()
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=1, stretch_len=5)
    paddle.penup()
    paddle.goto(0, -250)

    # Ball
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("red")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 3  # Increased speed
    ball.dy = 3

    # Bricks
    bricks = []
    colors = ["red", "orange", "yellow", "green", "blue"]

    y_pos = 250
    for color in colors:
        for x in range(-350, 400, 70):
            brick = turtle.Turtle()
            brick.shape("square")
            brick.color(color)
            brick.shapesize(stretch_wid=1, stretch_len=3)
            brick.penup()
            brick.goto(x, y_pos)
            bricks.append(brick)
        y_pos -= 30

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
    def paddle_left():
        x = paddle.xcor()
        if x > -350:
            paddle.setx(x - 30)

    def paddle_right():
        x = paddle.xcor()
        if x < 350:
            paddle.setx(x + 30)

    # Keyboard bindings
    screen.listen()
    screen.onkey(paddle_left, "Left")
    screen.onkey(paddle_right, "Right")

    # Main game loop
    game_running = True
    while game_running:
        screen.update()

        # Move ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Wall collisions
        if ball.xcor() > 390:
            ball.setx(390)
            ball.dx *= -1

        if ball.xcor() < -390:
            ball.setx(-390)
            ball.dx *= -1

        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        # Paddle collision
        if (ball.ycor() < -240 and ball.ycor() > -250) and (paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50):
            ball.sety(-240)
            ball.dy *= -1

        # Brick collision
        for brick in bricks:
            if abs(ball.xcor() - brick.xcor()) < 40 and abs(ball.ycor() - brick.ycor()) < 20:
                brick.goto(1000, 1000)  # Move brick out of screen
                bricks.remove(brick)
                ball.dy *= -1
                score += 10
                pen.clear()
                pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
                print("Current Score:", score)  # Print score to terminal
                break

        # Bottom collision (missed ball)
        if ball.ycor() < -300:
            pen.clear()
            pen.goto(0, 0)
            pen.write("Game Over!\nFinal Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
            print("Game Over! Final Score:", score)  # Print final score
            screen.update()
            time.sleep(3)
            game_running = False

        # Check if all bricks cleared
        if len(bricks) == 0:
            pen.clear()
            pen.goto(0, 0)
            pen.write("You Win!\nFinal Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
            print("You Win! Final Score:", score)  # Print final score
            screen.update()
            time.sleep(3)
            game_running = False

        time.sleep(0.01)

    # Clean exit after loop ends
    screen.bye()
brick()
