import turtle

def drawCircle (centerpoint, radius):

    (x,y) = centerpoint
    
    turtle.pencolor("red")

    turtle.up()

    turtle.setpos(x,y)

    turtle.down()

    turtle.circle(radius)

    print ("Radius is", radius)

    print ("The circumference moved is", (2.0 * 3.14 * radius))

drawCircle((20,20), 20)
