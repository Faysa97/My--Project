import turtle
git remote add origin https://github.com/Faysa97/pyhton.git
git branch -M main
git push -u origin main
turtle.bgcolor("black")
turtle.pensize(3)

def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)
        

turtle.speed()
turtle.color("red", "pink")

turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
curve()

turtle.left(120)
curve()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()