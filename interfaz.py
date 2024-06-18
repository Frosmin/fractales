import tkinter as tk
from turtle import TurtleScreen, RawTurtle
from copoNieve import copo_vonkoch
import math

def dibujar_sierpinski(t, puntos, nivel):
    if nivel == 0:
        t.up()
        t.goto(puntos[0][0], puntos[0][1])
        t.down()
        t.begin_fill()
        t.goto(puntos[1][0], puntos[1][1])
        t.goto(puntos[2][0], puntos[2][1])
        t.goto(puntos[0][0], puntos[0][1])
        t.end_fill()
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
    return [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2]

root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

ts = TurtleScreen(canvas)
mi_tortuga = RawTurtle(ts)

def iniciar_dibujo():
    nivel = int(nivel_entrada.get())
    mi_tortuga.clear()
    root.update()
    width = root.winfo_width()
    height = root.winfo_height() - boton_iniciar.winfo_height() - nivel_label.winfo_height()

    if figura_var.get() == "Triángulo de Sierpinski":
        mis_puntos = [[-width / 2, -height / 2], [0, height / 2], [width / 2, -height / 2]]
        dibujar_sierpinski(mi_tortuga, mis_puntos, nivel)
    elif figura_var.get() == "Copo de nieve de Koch":
        canvas.delete("all")
        lado = min(width, height) * 0.6  # Ajustar el tamaño del lado del triángulo al 60% del tamaño más pequeño
        copo_vonkoch(canvas, lado, nivel)

nivel_label = tk.Label(root, text="Nivel", font=("Arial", 20))
nivel_label.pack(side=tk.LEFT)

nivel_entrada = tk.Entry(root)
nivel_entrada.pack(side=tk.LEFT, padx=10, pady=10)

figura_var = tk.StringVar(value="Triángulo de Sierpinski")
figura_menu = tk.OptionMenu(root, figura_var, "Triángulo de Sierpinski", "Copo de nieve de Koch")
figura_menu.pack(side=tk.LEFT, padx=10, pady=10)

boton_iniciar = tk.Button(root, text="Iniciar", command=iniciar_dibujo, font=("Arial", 20))
boton_iniciar.pack()

root.mainloop()
