from tkinter import *
from Turtle3D import *

LINES = []
CAMERA = Turtle3D(LINES, position=(-9, 0, 4))
CAMERA.pen = False
SCREEN_DIST = 1.5

W, H = 1000, 570
SIZE = 150

root = Tk()
canv = Canvas(root, width=W, height=H, background="black")
sc_angle1 = Scale(root, from_=-180, to=180, orient=HORIZONTAL, length=W)
sc_angle2 = Scale(root, from_=-180, to=180, orient=HORIZONTAL, length=W)
sc_angle3 = Scale(root, from_=-180, to=180, orient=HORIZONTAL, length=W)



def draw_all():
    for line in LINES:
        line.drow_projection(canv, CAMERA, SCREEN_DIST)


t = Turtle3D(LINES, position=(0, 0, 0), face=(0, 0, 1), up=(1, 0, 0))

def coord_arrows():
    t.forward(5)
    t.goto(0, 0, 0)
    t.rotate_left(90)
    t.forward(5)
    t.goto(0, 0, 0)
    t.roll_left(90)
    t.rotate_right(90)
    t.roll_right(90)
    t.forward(5)
    t.goto(0, 0, 0)


def spiral():
    t.goto(0, 0, 0)
    t.roll_left(45)
    for i in range(400):
        t.forward(0.2)
        t.roll_left(1)
        t.rotate_left(7)
        t.roll_right(2)


COLOR1, COLOR2 = (0, 0, 255), (255, 0, 0)


def tree(n, a, angle1, angle2, angle3, n_max):
    t.set_gradient(COLOR1, COLOR2, n / n_max)
    if n <= 2:
        t.forward(a)
    else:
        t.forward(a)
        pos, face, up = t.pos.copy(), t.face.copy(), t.up.copy()
        t.rotate_right(angle1)
        t.roll_left(10)
        tree(n - 1, a / 1.4, angle1, angle2, angle3, n_max)
        t.pos, t.face, t.up = pos, face, up
        t.roll_left(120)
        t.rotate_right(angle2)
        t.roll_left(10)
        tree(n - 2, a / 1.4, angle1, angle2, angle3, n_max)
        t.pos, t.face, t.up = pos, face, up
        t.roll_left(240)
        t.rotate_right(angle3)
        t.roll_left(10)
        tree(n - 3, a / 1.4, angle1, angle2, angle3, n_max)


def tree2(n, a, branches, angle, n_max):
    t.set_gradient(COLOR1, COLOR2, n / n_max)
    if n == 0:
        t.forward(a)
    else:
        t.forward(a)
        pos, face, up = t.pos.copy(), t.face.copy(), t.up.copy()
        angle_roll = 360 / branches
        for i in range(branches):
            t.roll_left(angle_roll * i)
            t.rotate_left(angle)
            tree2(n - 1, a / 1.4, branches, angle, n_max)
            t.pos, t.face, t.up = pos, face, up


def dragon(n, a, dir=1):
    if n == 0:
        t.forward(a)
    else:
        t.rotate_left(45 * dir)
        dragon(n - 1, a / 1.4, dir)
        t.rotate_right(90 * dir)
        dragon(n - 1, a / 1.4, -dir)
        t.rotate_left(45 * dir)


def koha(n, a):
    if n == 0:
        t.forward(a)
    else:
        t.roll_right(60)
        koha(n - 1, a / 3)
        t.rotate_left(60)
        koha(n - 1, a / 3)
        t.rotate_right(120)
        koha(n - 1, a / 3)
        t.rotate_left(60)
        koha(n - 1, a / 3)
        t.roll_left(60)

tree(12, 3, 15, 120, 70, 12)
# dragon(10, 5)
# tree2(4, 3, 5, 58, 7)
# koha(4, 6)
# spiral()

draw_all()

radius = 9

def camera_roll(event):
    while True:
        canv.delete("all")
        CAMERA.forward(radius)
        CAMERA.rotate_left(1)
        CAMERA.forward(-radius)
        CAMERA.roll_left(1)

        t.goto(0, 0, 0)
        t.face = Vector3(0, 0, 1)
        t.up = Vector3(1, 0, 0)
        LINES.clear()
        tree(13, 3.5, sc_angle1.get(), sc_angle2.get(), sc_angle3.get(), 13)

        draw_all()
        root.update()


canv.bind('<Button-1>', camera_roll)
canv.pack()
sc_angle1.pack()
sc_angle2.pack()
sc_angle3.pack()
root.mainloop()
