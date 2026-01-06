import random
from turtle import Turtle, Screen

# --- CONSTANTES (Configuración) ---
DOT_SIZE = 20
SPACING = 50
ROWS = 10
COLS = 10
SPEED = "fastest"

# Paleta de colores conseguida con Colorgram
COLORS = [
    (115, 160, 192), (134, 46, 112), (242, 243, 246), (103, 34, 79),
    (200, 121, 179), (163, 62, 43), (18, 25, 48), (122, 121, 127)
]

# --- CÁLCULOS MATEMÁTICOS PARA CENTRAR ---
# El ancho total se basa en los espacios entre puntos (Columnas - 1)
total_width = (COLS - 1) * SPACING
total_height = (ROWS - 1) * SPACING

# El punto de inicio es la mitad negativa del tamaño total
start_x = -(total_width / 2)
start_y = -(total_height / 2)

# --- SETUP ---
timmy = Turtle()
screen = Screen()
screen.colormode(255)

timmy.speed(SPEED)
timmy.penup()
timmy.hideturtle()
timmy.goto(start_x, start_y)

# --- DIBUJO ---

for row in range(ROWS):
    for col in range(COLS):
        # Dibujar punto
        timmy.dot(DOT_SIZE, random.choice(COLORS))
        # Avanzar
        timmy.forward(SPACING)

    # Reset para la siguiente fila
    # Incrementamos Y basados en la fila actual + 1 para no depender de una variable mutable externa
    current_y = start_y + (SPACING * (row + 1))
    timmy.goto(start_x, current_y)

screen.exitonclick()