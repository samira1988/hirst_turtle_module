colors = [(45, 112, 157), (113, 150, 203), (212, 123, 164), (16, 128, 96), (172, 44, 88), (1, 177, 143), (153, 18, 54), (224, 201, 117), (225, 76, 115), (163, 166, 35), (28, 35, 84), (227, 86, 43), (42, 166, 208), (120, 172, 116), (119, 102, 158), (215, 64, 33), (237, 244, 241), (39, 52, 100), (76, 21, 45), (229, 169, 188), (14, 99, 71), (31, 61, 56), (8, 92, 107), (222, 177, 169), (181, 188, 208), (171, 203, 193)]
import turtle as t
from turtle import Screen
import random
t.colormode(255)
screen = Screen()
screen.screensize(1500, 1500)
timmy = t.Turtle()
timmy.hideturtle()
timmy.penup()
timmy.goto(-200,-100)
for i in range(10):
   timmy.goto(-300, -200 + (50* i))
   for _ in range(10):
      timmy.dot(10, random.choice(colors))
      timmy.forward(50)





screen.exitonclick()