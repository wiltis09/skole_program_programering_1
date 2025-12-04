from turtle import*
from time import*
import random

def fly(x,y):
    pu()
    goto(x,y)
    pd()
    return()

def Ram (x,y,r):
    pu()
    goto(0,y+r+5)
    pd()
    pensize(5)
    color("gold")
    circle(r)
    return

def Kvad():
    pensize(5)
    color("gold","white")
    pu()
    begin_fill()
    goto(-50,0)
    pd()
    goto(50,0)
    goto(50,80)
    goto(-50,80)
    goto(-50,0)
    end_fill()
    pu()
    return()

def Tur():
    Kvad()
    pu()
    goto(0,0)
    pd()
    color("black")
    write("?", font=('Courier',50, 'bold'), align='center')
    t = random.randrange(0,37,1)
    T = random.randrange(1,4,1)
    t2 = t + T*37
    print(t2)
    
    pu()
    goto(5,125)
    setheading(180)
    circle(180,180/37)
    pd()
    color("white")
    shape("circle")
    h = stamp()
    clearstamp(h)
    for i in range(t2):
            pu()
            circle(120,360/37)
            pd()
            sleep(.1)
            
    
    pu()
    Kvad()
    goto(0,0)
    pd()
    color("black")
    write(roll[t], font=('Courier',50, 'bold'), align='center')
    
def Ram2(x,y,r,d):
    setheading(180)
    pu()
    goto(x,y+r+5)
    pensize(3)
    
    pd()
    for j in range(0,160,4):
        for i in range(d-1):
            if i % 2 == 0:
                color("red")
            else:
                color("black")
                
            circle(r+j,360/d)
        color("green")
        circle(r+j,360/d)
    
        return()
        

def Delar(x,y,r,d):
    setheading(180)
    global roll
    pu()
    goto(x,y+r-5)
    circle(r,180/d)
    pd()
    color("white")
    style = ('Courier', 12, 'bold')
    write(roll[0], font=style, align='center')
    pensize(1)
    for i in range(d-1):
        pu()
        circle(r,360/d)
        pd()
        write(roll[i+1], font=style, align='center')
        #write(d-1-i)

def P(x,y):
    if x < -180 and x> -340 :
        Tur()
    if x < 330 and x > 180:
        clear()
        quit()
        done()
        
    return

speed(10000000)
tracer(25)
#ht()
goto(0,5)
dot(460,"chocolate")

roll =[26,3,35,12,28,7,29,18,22,9,31,14,20,1,33,16,24,5,10,23,8,30,11,36,13,27,6,34,17,25,2,21,4,19,15,32,0]

for i in range (105,190,2):
    Ram2(0,0,i,37)
for i in (230,195,140,102):
    Ram(0,0,i)
  
done()
"""
Delar(0,0,165,37)
fly(260,-150)
dot(80,"red")
color("black")
style = ('Courier', 12, 'bold')
write("Slut", font=style, align='center')
fly(-260,-150)
dot(80,"green")
color("black")
style = ('Courier', 12, 'bold')
write("Nästa", font=style, align='center')
Tur()

onscreenclick(P)
done()
"""
