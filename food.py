from turtle import Turtle
import random

random_color = ["azure", "CadetBlue1", "cyan", "coral", "DarkOrange", "DeepSkyBlue", "DarkGoldenrod1", "DarkSeaGreen1",
                "green", "lawngreen", "gold1", "LightPink", "honeydew", "hotpink"]

class Food(Turtle):
    # inherit Turtle superclass for the Food class
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(random_color))
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.color(random.choice(random_color))
        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)
