#import colorgram
#
#rgb_colors = []
#colors = colorgram.extract('image.jpg', 30)
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)
#
#print(rgb_colors)
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(236, 34, 108), (151, 25, 63), (240, 74, 34), (7, 148, 94), (230, 169, 41), (179, 159, 46), (44, 191, 232), (26, 125, 193), (84, 24, 86), (126, 192, 77), (253, 223, 0), (245, 220, 41), (183, 37, 102), (215, 60, 23), (62, 174, 101), (210, 131, 167), (163, 25, 21), (4, 112, 47), (237, 162, 194), (28, 180, 218), (245, 166, 156), (161, 213, 179), (137, 211, 231), (112, 2, 1), (71, 138, 186), (165, 196, 219)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



















screen = turtle_module.Screen()
screen.exitonclick()