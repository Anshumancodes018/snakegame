import turtle
import random
import time

delay = 0.1
sc = 0
hs = 0
bodies = []

# Create screen
s1 = turtle.Screen()
s1.title("Snake Game")
s1.bgcolor("black")
s1.setup(width=600, height=600)

# Create head
h1 = turtle.Turtle()
h1.shape("circle")
h1.speed(0)
h1.color("brown")
h1.fillcolor("red")
h1.penup()
h1.goto(0, 0)
h1.direction = "stop"

# Create food
f1 = turtle.Turtle()
f1.speed(0)
f1.shape("square")
f1.color("green")
f1.penup()
f1.goto(0, 100)

# Create scoreboard
sb = turtle.Turtle()
sb.color("white")
sb.ht()
sb.penup()
sb.goto(-270, 260)
sb.write("Score: 0 | Highest score: 0", font=("Arial", 14, "normal"))

# Movement functions
def moveup():
    if h1.direction != "down":
        h1.direction = "up"

def movedown():
    if h1.direction != "up":
        h1.direction = "down"

def moveleft():
    if h1.direction != "right":
        h1.direction = "left"

def moveright():
    if h1.direction != "left":
        h1.direction = "right"

def movestop():
    h1.direction = "stop"

# Move head
def move():
    if h1.direction == "up":
        h1.sety(h1.ycor() + 20)
    if h1.direction == "down":
        h1.sety(h1.ycor() - 20)
    if h1.direction == "left":
        h1.setx(h1.xcor() - 20)
    if h1.direction == "right":
        h1.setx(h1.xcor() + 20)

# Key bindings
s1.listen()
s1.onkey(moveup, "Up")
s1.onkey(movedown, "Down")
s1.onkey(moveleft, "Left")
s1.onkey(moveright, "Right")
s1.onkey(movestop, "space")

# Main game loop
while True:
    s1.update()

    # Border collision
    if h1.xcor() > 290 or h1.xcor() < -290 or h1.ycor() > 290 or h1.ycor() < -290:
        time.sleep(1)
        h1.goto(0, 0)
        h1.direction = "stop"
        for body in bodies:
            body.ht()
        bodies.clear()
        sc = 0
        delay = 0.1
        sb.clear()
        sb.write("Score: 0 | Highest score: {}".format(hs), font=("Arial", 14, "normal"))

    # Collision with food
    if h1.distance(f1) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        f1.goto(x, y)

        # Add body segment
        b1 = turtle.Turtle()
        b1.speed(0)
        b1.shape("square")
        b1.color("red")
        b1.penup()
        bodies.append(b1)

        # Update score
        sc += 10
        if sc > hs:
            hs = sc
        sb.clear()
        sb.write("Score: {} | Highest score: {}".format(sc, hs), font=("Arial", 14, "normal"))
        delay -= 0.001

    # Move body segments
    for i in range(len(bodies)-1, 0, -1):
        x = bodies[i-1].xcor()
        y = bodies[i-1].ycor()
        bodies[i].goto(x, y)
    if len(bodies) > 0:
        bodies[0].goto(h1.xcor(), h1.ycor())

    move()

    # Collision with body
    for b in bodies:
        if b.distance(h1) < 20:
            time.sleep(1)
            h1.goto(0, 0)
            h1.direction = "stop"
            for body in bodies:
                body.ht()
            bodies.clear()
            sc = 0
            delay = 0.1
            sb.clear()
            sb.write("Score: 0 | Highest score: {}".format(hs), font=("Arial", 14, "normal"))

    time.sleep(delay)

s1.mainloop()
