from tkinter import *
from math import *
from random import randint
import time


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
                 r_step=2, b_step=-2, g_step=-3):
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


W = 1000
H = 1000

r_ball = 20
h_ball = 300
g = 1
vx = 8.5
vy = 0
kx = 1
ky = 1
time_tick = 0.03
CC = ColorCube()

root = Tk()
c = Canvas(root, width=W, height=H, bg='black')
c.pack()

A = 50

t = Turtle(c, x=700, y=800, direction=0, draw=True, width=1)


def f(i, a, l, r, i1, color):
    if i == 0:
        t.fd(a)
    else:
        t.set_gradient(Color1, Color2, color/i1)
        t.fd(a)
        x, y = t.x, t.y
        d = t.d
        t.lt(l)
        f(i-1, a/sqrt(2), l, r, i1, color)
        t.goto(x, y)
        t.d = d
        t.rt(r)
        f(i-1, a/sqrt(2), l, r, i1, color+1)


def tree(event):
    right = randint(60, 140)
    left = randint(-20, 20)
    global Color1, Color2
    Color1 = (randint(0, 150), randint(0, 150), randint(0, 150))
    Color2 = (255-Color1[0], 255-Color1[1], 255-Color1[2])
    t.goto(event.x, event.y)
    t.dir(0)
    f(8, A, left, right, 12, 0)
    t.goto(event.x, event.y)
    t.dir(0)
    f(8, A, right, -left, 12, 0)
    root.update()


c.bind('<1>', tree)

X = randint(r_ball, W-r_ball)
Y = h_ball

ball = c.create_oval(X-r_ball, Y-r_ball, X+r_ball, Y+r_ball, fill='green')
f1 = c.create_polygon(X-r_ball, Y-r_ball+4, X+r_ball, Y-r_ball+4, X, Y-r_ball-18, fill='red')
f2 = c.create_oval(X-r_ball-2, Y-r_ball, X+r_ball+2, Y-r_ball+7, fill='white')
f3 = c.create_oval(X-3, Y-r_ball-21, X+3, Y-r_ball-15, fill='white')

for i in range(13):
    right = randint(60, 140)
    left = randint(-20, 20)
    Color1 = (randint(0, 150), randint(0, 150), randint(0, 150))
    Color2 = (255 - Color1[0], 255 - Color1[1], 255 - Color1[2])
    x_tree = randint(1, 9)
    y_tree = randint(2, 9)
    x_tree *= 100
    y_tree *= 100
    t.goto(x_tree, y_tree)
    t.dir(0)
    f(8, A, left, right, 12, 0)
    t.goto(x_tree, y_tree)
    t.dir(0)
    f(8, A, right, -left, 12, 0)

while True:
    c.move(ball, vx, vy)
    c.move(f1, vx, vy)
    c.move(f2, vx, vy)
    c.move(f3, vx, vy)
    c.create_oval(X-3, Y-3, X+3, Y+3, fill=CC())
    CC.change_color()
    X += vx
    Y += vy
    root.update()
    time.sleep(time_tick)

    if X <= r_ball:
        vx = abs(vx)*kx
    elif X >= W-r_ball:
        vx = -abs(vx)*kx
    if Y >= H-r_ball:
        ky = 0.85 + randint(0, 30)/100
        vy = -abs(vy)*ky-g
    vy += g

root.mainloop()
