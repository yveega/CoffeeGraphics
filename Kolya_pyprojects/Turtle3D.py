import math
from tkinter import *

class Vector3:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    def len(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
    
    def norm(self):
        length = self.len()
        return Vector3(self.x / length, self.y / length, self.z / length)
    
    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)
    
    def __mul__(self, other): # multiplication by scalar or vector multiplication
        if type(other) in {int, float}:
            return Vector3(self.x * other, self.y * other, self.z * other)
        else:
            return Vector3(self.y * other.z - self.z * other.y,
                           self.z * other.x - self.x * other.z,
                           self.x * other.y - self.y * other.x)
    
    def scalar(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cos(self, other):
        self_len = self.len()
        other_len = other.len()
        if self_len == 0 or other_len == 0:
            return 0
        return self.scalar(other) / self.len() / other.len()

    def __str__(self) -> str:
        return "({}, {}, {})".format(self.x, self.y, self.z)
    
    def copy(self):
        return Vector3(self.x, self.y, self.z)
    
    def projection(self, camera, screen_dist):
        towards = self - camera.pos
        proj_ort = towards * camera.face
        cam_left = camera.up * camera.face
        len_proj = proj_ort.len() * screen_dist / camera.face.scalar(towards)
        x = camera.up.cos(proj_ort) * len_proj
        y = cam_left.cos(proj_ort) * len_proj
        return (x, y)


def dekahex2(n):
    n = round(n)
    lc = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    return lc[(n % 256) // 16] + lc[n % 16]


def rgb(red, green, blue):
    return '#' + dekahex2(red) + dekahex2(green) + dekahex2(blue)   


class Turtle3D:
    def __init__(self, lineList, position=(0, 0, 0), face=(1, 0, 0), up=(0, 0, 1)) -> None:
        self.pos = Vector3(*position)
        self.face = Vector3(*face).norm()
        self.up = Vector3(*up).norm()
        self.pen = True
        self.lineList = lineList
        self.color = "red"
    
    def forward(self, points):
        new_pos = self.pos + self.face * points
        if self.pen:
            self.lineList.append(Line(self.pos, new_pos, self.color))
        self.pos = new_pos
    
    def goto(self, x, y, z):
        self.pos = Vector3(x, y, z)

    def rotate_right(self, degrees):
        right_ort = self.face * self.up
        radians = degrees / 180 * math.pi
        self.face = self.face * math.cos(radians) + right_ort * math.sin(radians)
        self.face = self.face.norm()
    
    def rotate_left(self, degrees):
        left_ort = self.up * self.face
        radians = degrees / 180 * math.pi
        self.face = self.face * math.cos(radians) + left_ort * math.sin(radians)
        self.face = self.face.norm()
    
    def roll_right(self, degrees):
        right_ort = self.face * self.up
        radians = degrees / 180 * math.pi
        self.up = self.up * math.cos(radians) + right_ort * math.sin(radians)
        self.up = self.up.norm()
    
    def roll_left(self, degrees):
        left_ort = self.up * self.face
        radians = degrees / 180 * math.pi
        self.up = self.up * math.cos(radians) + left_ort * math.sin(radians)
        self.up = self.up.norm()
    
    def rgb(self, red, green, blue):
        self.color = '#' + dekahex2(red) + dekahex2(green) + dekahex2(blue)

    def set_gradient(self, start_color, end_color, k):
        red = start_color[0] + (end_color[0]-start_color[0]) * k
        green = start_color[1] + (end_color[1]-start_color[1]) * k
        blue = start_color[2] + (end_color[2]-start_color[2]) * k
        self.rgb(red, green, blue)


W, H = 1000, 570
SIZE = 150


class Line:
    def __init__(self, start: Vector3, end: Vector3, color="purple") -> None:
        self.start = start
        self.end = end
        self.color = color
    
    def drow_projection(self, canvas: Canvas, camera: Turtle3D, screen_dist):
        start_x, start_y = self.start.projection(camera, screen_dist)
        end_x, end_y = self.end.projection(camera, screen_dist)
        start_x, start_y = W/2 + start_x * SIZE, H/2 - start_y * SIZE
        end_x, end_y = W/2 + end_x * SIZE, H/2 - end_y * SIZE
        canvas.create_line(start_x, start_y, end_x, end_y, fill=self.color)