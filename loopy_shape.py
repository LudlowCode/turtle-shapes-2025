from turtle import *
start_pos = pos()
points = 18
counter = 0
angle = 100
while counter < points:
    forward(100)
    right(angle) 
    if pos() == start_pos:
        break
    counter += 1