from tkinter import *
import Turtle_Kolya as TT

r = Tk()
c = Canvas(r, width=2500, height=1000, bg="black")
CC = TT.ColorCube(r_step=0.4, g_step=-0.2, b_step=-0.3)
t = TT.Turtle(c, x=200, y=800, color=CC(), draw=True)

c.pack()


def dekahex2(n):
    n = round(n)
    lc = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    return lc[(n % 255) // 16] + lc[n % 16]


def f(i, a, n=True):
    if i == 0:
        t.fd(a)
    else:
        if n:
            t.rt(45)
            f(i-1, a)
            t.lt(90)
            f(i-1, a, False)
            t.rt(45)
        else:
            t.lt(45)
            f(i-1, a)
            t.rt(90)
            f(i-1, a, False)
            t.lt(45)
    if i == 6:
        CC.change_color()
        t.color = CC()
    if i == 16:
        r.update()


f(19, 0.8)
t.goto(700, 700)
del CC
CC = TT.ColorCube(r_step=-0.1, g_step=0.3, b_step=0.4)
t.color = CC()
f(19, 0.8)
t.goto(1300, 750)
del CC
CC = TT.ColorCube(r_step=0.3, g_step=0.4, b_step=-0.2)
t.color = CC()
f(19, 0.8)

r.mainloop()
