"""Planets.py: To simulate the movement of the first six planets 
               in the solar systerm. 

__author__ = "Xiang Yifan"
__pkuid__  = "1800011820"
__email__  = "1800011820@pku.edu.cn"
"""

import turtle
import math

turtle.setup(width=550,height=600, startx=700, starty=0)
bg = turtle.bgcolor('black')
sun = turtle.Turtle()
sun.shape('circle')
sun.color('yellow')

planet1 = turtle.Turtle()
planet2 = turtle.Turtle()
planet3 = turtle.Turtle()
planet4 = turtle.Turtle()
planet5 = turtle.Turtle()
planet6 = turtle.Turtle()

planet1.speed(0)
planet2.speed(0)
planet3.speed(0)
planet4.speed(0)
planet5.speed(0)
planet6.speed(0)

planet1.color('blue')
planet2.color('red')
planet3.color('violet')
planet4.color('green')
planet5.color('cyan')
planet6.color('white')

planet1.shape('circle')
planet2.shape('circle')
planet3.shape('circle')
planet4.shape('circle')
planet5.shape('circle')
planet6.shape('circle')

planet1.ht()
planet2.ht()
planet3.ht()
planet4.ht()
planet5.ht()
planet6.ht()

planet1.up()
planet2.up()
planet3.up()
planet4.up()
planet5.up()
planet6.up()

planet1.setposition(-40,60)
planet2.setposition(-60,100)
planet3.setposition(-120,200)
planet4.setposition(-150,260)
planet5.setposition(-180,340)
planet6.setposition(-200,480)

planet1.down()
planet2.down()
planet3.down()
planet4.down()
planet5.down()
planet6.down()

planet1.st()
planet2.st()
planet3.st()
planet4.st()
planet5.st()
planet6.st()

planet1.speed(1)
planet2.speed(1)
planet3.speed(1)
planet4.speed(1)
planet5.speed(1)
planet6.speed(1)

t = 0
i = 1

while i != 0:
   
    t += 1
    
   
    a1 = 80*math.sin(math.radians(3*t))
    a2 = 60*math.cos(math.radians(3*t))
    planet1.goto(a1-40,a2)

    a1 = 130*math.sin(math.radians(2*t))
    a2 = 100*math.cos(math.radians(2*t))
    planet2.goto(a1-60,a2)

    a1 = 240*math.sin(math.radians(1.2*t))
    a2 = 200*math.cos(math.radians(1.2*t))
    planet3.goto(a1-120,a2)

    a1 = 340*math.sin(math.radians(0.9*t))
    a2 = 260*math.cos(math.radians(0.9*t))
    planet4.goto(a1-150,a2)

    a1 = 440*math.sin(math.radians(0.5*t))
    a2 = 340*math.cos(math.radians(0.5*t))
    planet5.goto(a1-180,a2)

    a1 = 580*math.sin(math.radians(0.25*t))
    a2 = 480*math.cos(math.radians(0.25*t))
    planet6.goto(a1-200,a2)

    
