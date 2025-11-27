
import turtle

screen = turtle.Screen()
screen.title("Programmeringsutmaning 1")
screen.bgcolor("white")
turtle.speed(200)
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "gray", "cyan", "magenta", "lime", "navy", "teal", "maroon", "olive", "silver", "gold", "coral", "indigo", "violet", "turquoise"]


def drew_square(max_size=100, move_speed=200, size_step=10):
    turtle.speed(move_speed)
    for size in range(0, max_size, size_step):
        turtle.pencolor(colors[size%6])
        for angel in range(0, 360, 45):
            turtle.right(angel)
            for i in range(4):
                turtle.forward(size)
                turtle.right(90)
                
                
drew_square(300, 500, 10)





turtle.done()
