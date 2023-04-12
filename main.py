from turtle import Turtle, Screen, colormode
from random import choice

# TODO make painting 10x10 dots, dot size = 20, spacing between dots = 50

color_list = [(209, 165, 125), (140, 49, 106), (164, 169, 38), (244, 80, 57), (229, 116, 164), (3, 143, 56), (215, 234, 231), (241, 65, 140), (1, 143, 184), (162, 55, 52), (50, 203, 226), (254, 230, 0), (21, 166, 126), (248, 222, 227), (212, 234, 238), (243, 223, 51), (27, 196, 219), (119, 184, 146), (230, 167, 191)]

screen = Screen()
screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)
screen.colormode(255)

tim = Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")

def make_dot_move_fwd():
    tim.dot(20, choice(color_list))
    tim.forward(50)


def move_9x():
    for _ in range(10):
        make_dot_move_fwd()


def u_turn_left():
    tim.left(90)
    make_dot_move_fwd()
    tim.left(90)


def u_turn_right():
    tim.right(90)
    make_dot_move_fwd()
    tim.right(90)

def make_2_lines():
    move_9x()
    u_turn_left()
    move_9x()
    u_turn_right()

for _ in range(5):
    make_2_lines()

screen = Screen()
screen.exitonclick()
