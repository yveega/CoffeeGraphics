from tkinter import *
import math
from Turtle3D import *
import random

LINES = []
CAMERA = Turtle3D(LINES, position=(-15, 0, 4))
CAMERA.pen = False
SCREEN_DIST = 0.8

W, H = 1000, 570
SIZE = 150

root = Tk()
canv = Canvas(root, width=W, height=H, background="black")
t = Turtle3D(LINES, position=(0, 0, 0), face=(1, 0, 0), up=(0, 0, 1))

surf_angle = math.acos(1/3) / math.pi * 180

COLOR1, COLOR2 = (255, 255, 0), (180, 120, 0)

rolling_angle = 0
k_length = 1.4


def tree(n, a, angle1, angle2, angle3, n_max):
    t.set_gradient(COLOR1, COLOR2, n / n_max)
    if n <= 2:
        t.forward(a)
    else:
        t.forward(a)
        pos, face, up = t.pos.copy(), t.face.copy(), t.up.copy()
        t.rotate_right(angle1)
        t.roll_left(rolling_angle)
        tree(n - 1, a / k_length, angle1, angle2, angle3, n_max)
        t.pos, t.face, t.up = pos, face, up
        t.roll_left(120)
        t.rotate_right(angle2)
        t.roll_left(rolling_angle)
        tree(n - 2, a / k_length, angle1, angle2, angle3, n_max)
        t.pos, t.face, t.up = pos, face, up
        t.roll_left(240)
        t.rotate_right(angle3)
        t.roll_left(rolling_angle)
        tree(n - 3, a / k_length, angle1, angle2, angle3, n_max)


def random_tree(pos: Vector3, height):
    global rolling_angle
    t.pen = False
    t.pen = True
    t.pos = pos
    t.face = Vector3(0, 0, 1)
    t.up = Vector3(0, 1, 0)
    t.pen = True
    rolling_angle = random.randint(-23, 23)
    tree(12, height, random.randint(30, 60), random.randint(30, 60), random.randint(30, 60), 12)


def tetraedr(a):
    for _ in range(3):
        t.roll_right(surf_angle)
        t.rotate_left(60)
        t.forward(a)
        t.pen = False
        t.forward(-a)
        t.pen = True
        t.rotate_right(60)
        t.roll_left(surf_angle)
        t.forward(a)
        t.rotate_left(120)


def serpinkiy(n, a, k_color, max_k):
    if n == 0:
        t.set_gradient(COLOR1, COLOR2, k_color / max_k)
        tetraedr(a)
    else:
        for _ in range(3):
            serpinkiy(n - 1, a / 2, k_color, max_k)
            t.pen = False
            t.forward(a)
            t.pen = True
            t.rotate_left(120)
        t.roll_right(surf_angle)
        t.rotate_left(60)
        t.pen = False
        t.forward(a / 2)
        t.pen = True
        t.roll_left(180)
        serpinkiy(n - 1, a / 2, k_color - 1, max_k)
        t.roll_left(180)
        t.pen = False
        t.forward(-a / 2)
        t.rotate_right(60)
        t.roll_left(surf_angle)
        t.pen = True


def draw_all():
    for line in LINES:
        line.drow_projection(canv, CAMERA, SCREEN_DIST)


MOUSE_LAST_COORDS = (0, 0)
CAMERA_RADIUS = abs(CAMERA.pos.x)


def update_screen():
    canv.delete("all")
    draw_all()
    root.update()


def on_mouse_move(event):
    global MOUSE_LAST_COORDS
    if not event.state & 0x0100:
        MOUSE_LAST_COORDS = (0, 0)
    elif MOUSE_LAST_COORDS == (0, 0):
        MOUSE_LAST_COORDS = (event.x, event.y)
    else:
        CAMERA.forward(CAMERA_RADIUS)
        CAMERA.rotate_right((event.x - MOUSE_LAST_COORDS[0]) / 2)
        CAMERA.roll_left(90)
        CAMERA.rotate_left((event.y - MOUSE_LAST_COORDS[1]) / 2)
        CAMERA.roll_right(90)
        CAMERA.forward(-CAMERA_RADIUS)
        MOUSE_LAST_COORDS = (event.x, event.y)

        update_screen()


def on_mouse_wheel_fd(event):
    CAMERA.forward(event.num / 10)

    update_screen()


def on_mouse_wheel_bd(event):
    CAMERA.forward(-event.num / 10)

    update_screen()


t.pen = False
t.forward(50)
t.rotate_left(150)
t.pen = True
serpinkiy(5, 53, 5, 5)

start_v1 = Vector3(8, -6, 0)
start_v2 = Vector3(8, 9, 0)
iter_v = Vector3(-4.2, 0, 0)
t.width = 2
for i in range(5):
    COLOR1 = (random.randint(150, 255), random.randint(50, 100), random.randint(150, 255))
    COLOR2 = (255 - COLOR1[0], COLOR1[1] / 2, 255 - COLOR1[2])
    random_tree(start_v1 + iter_v * i, 2)
    random_tree(start_v2 + iter_v * i, 2)

draw_all()

canv.bind("<Motion>", on_mouse_move)
canv.bind("<Button-4>", on_mouse_wheel_fd)
canv.bind("<Button-5>", on_mouse_wheel_bd)
canv.pack()
root.mainloop()
