import turtle

turtle.hideturtle()
turtle.speed(0)
turtle.goto(0,0)

colors=['brown','red','magenta','blue','green','orange']

for i in range(36):
    
    index=i//6
    turtle.pencolor(colors[index])
    turtle.circle(100)
    turtle.left(10)

turtle.exitonclick()
