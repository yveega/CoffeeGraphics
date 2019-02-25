from math import *
from random import randint


def dekahex2(n):
    n = round(n)
    lc = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    return lc[(n % 256) // 16] + lc[n % 16]


def tow(x1, y1, x2, y2):
    return atan((x2 - x1) / (y2 - y1))


def rgb(red, green, blue):
    return '#' + dekahex2(red) + dekahex2(green) + dekahex2(blue)


class Turtle:
    def __init__(self, canvas, x=0, y=0, direction=0, color='black', draw=False, width=1):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.d = (direction - 180) / -180 * pi
        self.color = color
        self.draw = draw
        self.width = width

    def goto(self, x, y, pen=False):
        if pen:
            self.canvas.create_line(self.x, self.y, x, y, fill=self.color, width=self.width)
        self.x = x
        self.y = y

    def fd(self, step):
        xn = self.x + step * sin(self.d)
        yn = self.y + step * cos(self.d)
        if self.draw:
            self.canvas.create_line(self.x, self.y, xn, yn, fill=self.color, width=self.width)
        self.x = xn
        self.y = yn

    def bd(self, step):
        xn = self.x - step * sin(self.d)
        yn = self.y - step * cos(self.d)
        if self.draw:
            self.canvas.create_line(self.x, self.y, xn, yn, fill=self.color, width=self.width)
        self.x = xn
        self.y = yn

    def rt(self, deg):
        self.d -= deg / 180 * pi

    def lt(self, deg):
        self.d += deg / 180 * pi

    def dir(self, deg):
        self.d = (deg - 180) / -180 * pi

    def rgb(self, red, green, blue):
        self.color = '#' + dekahex2(red) + dekahex2(green) + dekahex2(blue)

    def set_gradient(self, start_color, end_color, k):
        red = start_color[0] + (end_color[0]-start_color[0]) * k
        green = start_color[1] + (end_color[1]-start_color[1]) * k
        blue = start_color[2] + (end_color[2]-start_color[2]) * k
        self.rgb(red, green, blue)

    def pu(self):
        self.draw = False

    def pd(self):
        self.draw = True

    def tow(self, x, y):
        self.d = tow(self.x, self.y, x, y)


class ColorCube:
    def __init__(self, r_start=randint(20, 235), g_start=randint(20, 235), b_start=randint(20, 235),
                 r_step=1, b_step=1, g_step=1):
        self.r = r_start
        self.g = g_start
        self.b = b_start
        self.r_step = r_step
        self.g_step = g_step
        self.b_step = b_step

    def __call__(self, *args, **kwargs):
        return rgb(self.r, self.g, self.b)

    def change_color(self):
        if self.r <= abs(self.r_step)+1 or self.r >= 254-abs(self.r_step):
            self.r_step *= -1
        if self.g <= abs(self.g_step)+1 or self.g >= 254-abs(self.g_step):
            self.g_step *= -1
        if self.b <= abs(self.b_step)+1 or self.b >= 254-abs(self.b_step):
            self.b_step *= -1
        self.r += self.r_step
        self.g += self.g_step
        self.b += self.b_step

