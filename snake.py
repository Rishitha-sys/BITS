import turtle
import time
import random

def snake():
        # Setup screen
        screen = turtle.Screen()
        screen.title("Simple Snake Game")
        screen.bgcolor("black")
        screen.setup(width=600, height=600)
        screen.tracer(0)

        # Snake head
        head = turtle.Turtle()
        head.shape("square")
        head.color("white")
        head.penup()
        head.goto(0, 0)
        head.direction = "stop"

        # Snake food
        food = turtle.Turtle()
        food.shape("circle")
        food.color("red")
        food.penup()
        food.goto(0, 100)

        segments = []

        # Score
        score = 0
        pen = turtle.Turtle()
        pen.speed(0)
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 260)
        pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))

        # Functions
        def go_up():
            if head.direction != "down":
                head.direction = "up"

        def go_down():
            if head.direction != "up":
                head.direction = "down"

        def go_left():
            if head.direction != "right":
                head.direction = "left"

        def go_right():
            if head.direction != "left":
                head.direction = "right"

        def move():
            if head.direction == "up":
                y = head.ycor()
                head.sety(y + 20)

            if head.direction == "down":
                y = head.ycor()
                head.sety(y - 20)

            if head.direction == "left":
                x = head.xcor()
                head.setx(x - 20)

            if head.direction == "right":
                x = head.xcor()
                head.setx(x + 20)

        # Keyboard bindings (Arrow keys)
        screen.listen()
        screen.onkey(go_up, "Up")
        screen.onkey(go_down, "Down")
        screen.onkey(go_left, "Left")
        screen.onkey(go_right, "Right")

        # Main game loop
        while True:
            screen.update()

            # Check for collision with border
            if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
                time.sleep(1)
                print("Game Over! Final Score:", score)
                turtle.bye()
                break

            # Check for collision with food
            if head.distance(food) < 20:
                x = random.randint(-280, 280)
                y = random.randint(-280, 280)
                food.goto(x, y)

                new_segment = turtle.Turtle()
                new_segment.shape("square")
                new_segment.color("grey")
                new_segment.penup()
                segments.append(new_segment)

                score += 10
                pen.clear()
                pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

            # Move segments
            for index in range(len(segments) - 1, 0, -1):
                x = segments[index - 1].xcor()
                y = segments[index - 1].ycor()
                segments[index].goto(x, y)

            if len(segments) > 0:
                x = head.xcor()
                y = head.ycor()
                segments[0].goto(x, y)

            move()

            # Check for collision with self
            for segment in segments:
                if segment.distance(head) < 20:
                    time.sleep(1)
                    print("Game Over! Final Score:", score)
                    turtle.bye()
                    exit()

            time.sleep(0.1)

        # Keeps window open (actually never reached now)
        turtle.done()

snake()










