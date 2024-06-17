import turtle

def dibujar_sierpinski(t, puntos, nivel):
    if nivel == 0:
        t.up()
        t.goto(puntos[0][0], puntos[0][1])
        t.down()
        t.goto(puntos[1][0], puntos[1][1])
        t.goto(puntos[2][0], puntos[2][1])
        t.goto(puntos[0][0], puntos[0][1])
    else:
        dibujar_sierpinski(t, [puntos[0],
                        punto_medio(puntos[0], puntos[1]),
                        punto_medio(puntos[0], puntos[2])],
                   nivel-1)
        dibujar_sierpinski(t, [puntos[1],
                        punto_medio(puntos[0], puntos[1]),
                        punto_medio(puntos[1], puntos[2])],
                   nivel-1)
        dibujar_sierpinski(t, [puntos[2],
                        punto_medio(puntos[2], puntos[1]),
                        punto_medio(puntos[0], puntos[2])],
                   nivel-1)

def punto_medio(p1, p2):
    return [(p1[0]+p2[0]) / 2, (p1[1]+p2[1]) / 2]

mi_tortuga = turtle.Turtle()
mi_tortuga.pensize(5) #grosor xd
mis_puntos = [[-100, -50], [0, 100], [100, -50]]


dibujar_sierpinski(mi_tortuga, mis_puntos, 3) # nivelcito
turtle.done()