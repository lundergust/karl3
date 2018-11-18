def randomwalk():
    import random
    import math
    import turtle
    turtle.canvwidth = 100
    turtle.canvheight = 100
    turtle.showturtle()

    steps = 0
    while turtle.xcor() < 100 or turtle.ycor() < 100:
        x = random.uniform(1,4)
        x = float(x)
        xi = x + 0.5
        txi = math.trunc(xi)

        if txi == 1:
            turtle.left(0)
            turtle.forward(20)
            steps += 1
        if txi == 2:
            turtle.left(90)
            turtle.forward(20)
            steps += 1
        if txi == 3:
            turtle.left(180)
            turtle.forward(20)
            steps += 1
        if txi == 4:
            turtle.left(270)
            turtle.forward(20)
            steps += 1

    print("Yay! Drunk turtle reached home after walking {} blocks!".format(steps))



if __name__ == '__main__':
    randomwalk()
