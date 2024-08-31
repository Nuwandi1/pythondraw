import turtle
turtle.bgcolor("black")
squary =turtle.Turtle()
squary.speed(40)
for i in range (160):
    for color in ["red","blue","yellow"]:
        squary.pencolor(color)
        squary.forward(i)
        squary.left(60)
        squary.right(12)