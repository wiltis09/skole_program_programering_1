def rounded_rectangle_with_text(t, width, height, radius, text, fill_color="lightblue", text_color="black"):
    diameter = radius * 2
    
    # Calculate starting point so the box is centered on the turtle's position
    t.penup()
    start_x, start_y = t.pos()
    t.goto(start_x - width / 2 + radius, start_y - height / 2)
    t.pendown()

    # Draw the filled rounded rectangle
    t.color(text_color, fill_color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width - diameter)
        t.circle(radius, 90)
        t.forward(height - diameter)
        t.circle(radius, 90)
    t.end_fill()

    # Move to the center to write the text
    t.penup()
    # Move back to the original starting position
    t.goto(start_x, start_y)
    
    # Write the text
    # Adjust y-position slightly to account for the font baseline
    font_size = int(min(width, height) * 0.2)
    t.write(text, align="center", font=("Arial", font_size, "bold"))
    
    # Return the turtle to its original position
    t.setheading(0)
    t.goto(start_x, start_y)
    t.pendown()
    

import turtle
screen = turtle.Screen()
screen.title("Rullet Spela")

t = turtle.Turtle()
t.speed(1)
t.pensize(3)
t.color("blue")


t.begin_fill( )
    
rounded_rectangle_with_text(t, 100, 59, 20, "blue")

t.end_fill()

turtle.done()