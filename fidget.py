import turtle as t
from turtle import *
state = {'turn': 0}
def spinner(): #Art of fidget
    clear()
    angle = state['turn'] / 10
    right(angle)
    forward(100)
    dot(140, 'cyan')
    back(100)
    right(120)
    forward(100)
    dot(140, 'blue')
    back(100)
    right(120)
    forward(100)
    dot(140, 'orange')
    back(100)
    right(120)
    update()

def animate(): #Animations
    if state['turn'] > 0:
        state['turn'] -= 1

    spinner()
    ontimer(animate, 20)

def flick(): #The flick
    state['turn'] += 10

setup(420, 420, 370, 0)
hideturtle()
tracer(False) #The tracer will be "false " so the flick can happen
width(20)
onkey(flick, 'space') #It will flick when I will press the space key 
listen() #Command in freegames
animate() #animate
done() #Complete

