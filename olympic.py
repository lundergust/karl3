def olympic():
    import turtle
    import math
    turtle.showturtle()
    radius = turtle.numinput('','Enter radius: ')
    radius = int(radius)

    # Circle 1
    turtle.circle(radius)

# Circle 2
    turtle.penup()
    turtle.left(90)
    turtle.forward(radius)
    turtle.forward(radius)
    turtle.left(90)
    spacing_x = 2*radius + radius/5
    turtle.forward(spacing_x)
    turtle.pendown()
    turtle.circle(radius)

# Circle 3
    turtle.penup()
    turtle.forward(spacing_x)
    turtle.pendown()
    turtle.circle(radius)

# Circle 4
    turtle.penup()
    turtle.left(90)
    turtle.forward(radius)
    turtle.left(90)
    spacing_secondary = radius + radius/10
    turtle.forward(spacing_secondary)
    turtle.left(180)
    turtle.pendown()
    turtle.circle(radius)

# Circle 5
    turtle.penup()
    turtle.left(180)
    turtle.forward(spacing_x)
    turtle.left(180)
    turtle.pendown()
    turtle.circle(radius)
