from numpy import sin, cos, pi, sqrt
from math import atan2

def copo_vonkoch(canvas, lado, n):
    x_offset = 150  
    y_offset = -170
    x_vertice1 = x_offset
    y_vertice1 = 300 + y_offset

    x_vertice2 = x_vertice1 - lado
    y_vertice2 = y_vertice1

    x_vertice3 = x_vertice1 - lado / 2
    y_vertice3 = y_vertice1 - sqrt(lado ** 2 - (lado / 2) ** 2)

    vonkoch(canvas, x_vertice1, y_vertice1, x_vertice2, y_vertice2, n)
    vonkoch(canvas, x_vertice2, y_vertice2, x_vertice3, y_vertice3, n)
    vonkoch(canvas, x_vertice3, y_vertice3, x_vertice1, y_vertice1, n)

def vonkoch(canvas, xi, yi, xf, yf, n):
    if n == 0:
        canvas.create_line(xi, yi, xf, yf)
    else:
        x1 = xi + (xf - xi) / 3.0
        y1 = yi + (yf - yi) / 3.0

        x3 = xf - (xf - xi) / 3.0
        y3 = yf - (yf - yi) / 3.0

        dx = x3 - x1
        dy = y3 - y1
        r = sqrt(dx ** 2 + dy ** 2)
        a = atan2(dy, dx)
        x2 = x1 + r * cos(a - pi / 3)
        y2 = y1 + r * sin(a - pi / 3)

        vonkoch(canvas, xi, yi, x1, y1, n - 1)
        vonkoch(canvas, x1, y1, x2, y2, n - 1)
        vonkoch(canvas, x2, y2, x3, y3, n - 1)
        vonkoch(canvas, x3, y3, xf, yf, n - 1)
