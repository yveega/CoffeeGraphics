'''
left click for zoom in 10x
right click for zoom out 10x
counting time about 2 - 3 sec
'''

import numpy as np
from tkinter import *
from PIL import Image, ImageTk


W = 1000
H = 1000
repeat = 124
top_num = 999999999999999
koe = 7
x_center, y_center = (-0.5, 0)
zoom = 1


def draw_fractal(event=0):
    global x_center, y_center, zoom, r
    if event != 0:
        r.destroy()
        x_center = x_center - zoom + event.x / W * 2 * zoom
        y_center = y_center - zoom + event.y / H * 2 * zoom
        if event.num == 3:
            zoom *= 10
        else:
            zoom /= 10

    r = Tk()
    c = Canvas(r, width=W, height=H)

    real = np.array([np.linspace(x_center-zoom, x_center+zoom, W)]*H, dtype='complex128')
    i_arr = np.array([np.linspace(y_center-zoom, y_center+zoom, H)*(0.+1.j)]*W, dtype='complex128')
    i_arr = i_arr.transpose()
    a = real+i_arr

    res = np.zeros((H, W), dtype='int8')
    z = np.zeros((H, W), dtype='complex128')
    mach = np.zeros((H, W), dtype='bool')
    for _ in range(repeat):
        z = z * z + a
        mach += z.real > top_num
        res += mach

    res *= koe
    r_arr = res
    g_arr = res * 2
    b_arr = -res
    colors = np.hstack((r_arr, g_arr, b_arr)).reshape((H, W, 3), order='F')

    im = Image.fromarray(colors, mode='RGB')
    ph_im = ImageTk.PhotoImage(image=im)
    c.create_image(0, 0, image=ph_im, anchor=NW)
    r.bind('<Button-1>', draw_fractal)
    r.bind('<Button-3>', draw_fractal)
    c.pack()
    r.mainloop()


draw_fractal()
