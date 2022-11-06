import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, other):
        return Points(self.x - other.x)

    def dot(self, no):
        return self.absolute

    def cross(self):
        return self.absolute
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

points = [[0, 4, 5], [1, 7, 6], [0, 5, 9], [1, 7, 2]]
a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
x = (b - a).cross(c - b)
y = (c - b).cross(d - c)
angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

print("%.2f" % math.degrees(angle))