import turtle as trtl
import random
import time

wn = trtl.Screen()
wall = trtl.Turtle()
wn.bgcolor("grey")

wall.speed(0)
wall.ht()
wall.pensize(1)

# Values (Change if you want)
wall_spacing = 8
wall_amount = 20
wall_angle = 90
gap_size = 25

# Draw Maze (Don't change)
def draw_maze():
    wall.pu()
    wall.goto(0, 0)
    wall.pd()
    wall.clear()
    wall_space = wall_spacing * 2 
    count = 0
    while (count < wall_amount):
        random_length = random.randint(0, (25 + (count*wall_space)))
        wall.forward(25 + (count*wall_space) - random_length)
        wall.pu()
        wall.forward(gap_size)
        wall.pd()
        if count >= 4:
            wall.right(90)
            wall.forward(wall_space * 3.9)
            wall.backward(wall_space * 3.9)
            wall.left(90)
        wall.forward(25 + ((count * wall_space + random_length) - gap_size))
        wall.right(wall_angle)
        
        count += 1

# Player Creation

player = trtl.Turtle()
player.color("red")
player.pu()
player.goto(10, -20)
player.shape("turtle")
player.shapesize(0.7)
player.speed(0)

# Counter Turtle Creation + Score

counter = trtl.Turtle()
inputs = 0

counter.pu()
counter.ht()
counter.speed(0)
counter.goto(-300, 330)
counter.write("Number of Moves: " + str(inputs), True, "left", ("Impact", 30, "bold"))

# yOu WiN!!11!
message = trtl.Turtle()
message.ht()
message.pu()
message.pencolor("white")

def victory_check():
    xcor = player.xcor()
    ycor = player.ycor()
    if (xcor > 350 or xcor < -350 or ycor > 275 or ycor < -350): #set to number * count later
        player.ht()
        wall.clear()
        acid = True
        while acid == True:
            global wn
            counter.clear()
            counter.goto(0, 100)
            counter.write("You Win!", True, align=("center"), font=( "Impact", 46, "normal"))
            wn.bgcolor("red")
            time.sleep(1/30)
            wn.bgcolor("green")
            time.sleep(1/30)
            wn.bgcolor("blue")
            time.sleep(1/30)

# Player Input

def move_up():
    global inputs
    inputs += 1
    counter.clear()
    counter.goto(-300, 330)
    counter.write("Number of Moves: " + str(inputs), True, "left", ("Impact", 30, "normal"))
    player.setheading(90)
    player.forward(3)
    victory_check()

def move_down():
    global inputs
    inputs += 1
    counter.clear()
    counter.goto(-300, 330)
    counter.write("Number of Moves: " + str(inputs), True, "left", ("Impact", 30, "normal"))
    player.setheading(270)
    player.forward(3)
    victory_check()

def move_left():
    global inputs
    inputs += 1
    counter.clear()
    counter.goto(-300, 330)
    counter.write("Number of Moves: " + str(inputs), True, "left", ("Impact", 30, "normal"))
    player.setheading(180)
    player.forward(3)
    victory_check()

def move_right():
    global inputs
    inputs += 1
    counter.clear()
    counter.goto(-300, 330)
    counter.write("Number of Moves: " + str(inputs), True, "left", ("Impact", 30, "normal"))
    player.setheading(0)
    player.forward(3)
    victory_check()

def move_up_fast():
    global inputs
    inputs += 1
    counter.clear()
    counter.goto(-300, 330)
    counter.write("Number of Moves: " + str(inputs), True, "left", ("Impact", 30, "normal"))
    player.setheading(90)
    player.forward(8)
    victory_check()

def move_down_fast():
    global inputs
    inputs += 1
    counter.clear()
    counter.goto(-300, 330)
    counter.write("Number of Moves: " + str(inputs), True, "left", ("Impact", 30, "normal"))
    player.setheading(270)
    player.forward(8)
    victory_check()

def move_left_fast():
    global inputs
    inputs += 1
    counter.clear()
    counter.goto(-300, 330)
    counter.write("Number of Moves: " + str(inputs), True, "left", ("Impact", 30, "normal"))
    player.setheading(180)
    player.forward(8)
    victory_check()

def move_right_fast():
    global inputs
    inputs += 1
    counter.clear()
    counter.goto(-300, 330)
    counter.write("Number of Moves: " + str(inputs), True, "left", ("Impact", 30, "normal"))
    player.setheading(0)
    player.forward(8)
    victory_check()



wn.onkeyrelease(move_up, "w")
wn.onkeyrelease(move_left, "a")
wn.onkeyrelease(move_down, "s")
wn.onkeyrelease(move_right, "d")
wn.onkeyrelease(move_up_fast, "Up")
wn.onkeyrelease(move_left_fast, "Left")
wn.onkeyrelease(move_down_fast, "Down")
wn.onkeyrelease(move_right_fast, "Right")

draw_maze()
wn.listen()
wn.mainloop()