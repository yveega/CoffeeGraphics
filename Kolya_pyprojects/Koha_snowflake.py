from tkinter import *
import Turtle_Kolya as TT

r = Tk()
c = Canvas(r, width=1000, height=1000, bg="black")
c.pack()
t = TT.Turtle(c, x=200, y=300, draw=True)
n = 255 / (4**4 * 3)
CC = TT.ColorCube(r_step=n, g_step=-n*2, b_step=-n*3)


def f(i, a):
    if i == 0:
        t.color = CC()
        CC.change_color()
        r.update()
        t.fd(a)
    else:
        f(i-1, a/3)
        t.lt(60)
        f(i-1, a/3)
        t.rt(120)
        f(i-1, a/3)
        t.lt(60)
        f(i-1, a/3)


t.width = 2
t.dir(90)
for _ in range(3):
    f(5, 600)
    t.rt(120)
r.mainloop()
