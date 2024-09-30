from turtle import *
start_pos = pos()
angle = 100
while True:
    forward(100)
    right(angle) 
    if pos() == start_pos:
        break