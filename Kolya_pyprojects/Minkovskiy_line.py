from tkinter import *
import Turtle_Kolya as TT

r = Tk()
c = Canvas(r, width=1000, height=1000, bg="black")
c.pack()
t = TT.Turtle(c, x=200, y=200, draw=True)
CC = TT.ColorCube(r_step=0.11, g_step=-0.27, b_step=-0.37)


def f(i, a):
    if i == 0:
        t.fd(a)
        t.color = CC()
        CC.change_color()
    else:
        f(i - 1, a / 4)
        t.lt(90)
        f(i - 1, a / 4)
        t.rt(90)
        f(i - 1, a / 4)
        t.rt(90)
        f(i - 1, a / 4)
        f(i - 1, a / 4)
        t.lt(90)
        f(i - 1, a / 4)
        t.lt(90)
        f(i - 1, a / 4)
        t.rt(90)
        f(i - 1, a / 4)
    if i == 3:
        r.update()


t.dir(90)
t.width = 2
for _ in range(4):
    f(5, 500)
    t.rt(90)
r.mainloop()
