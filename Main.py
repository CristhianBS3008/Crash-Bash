# -*- coding: utf-8 -*-
import pygame
import Player

num_casillas_col = 7
num_casillas_fil = 7
dim_mapa_x = 500
dim_mapa_y = 500
DIMENSIONES = (dim_mapa_x, dim_mapa_y)
LARGO = 60  # Constantes para cada retícula del mapa
ALTO = 60
MARGEN = 10

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
hecho = False  # Bucle Pygame

grid = []  # Creamos matriz 7x7 para pintar
# '0' -> sin pintar, '1' -> pintado
for fila in range(num_casillas_fil):
    grid.append([])
    for columna in range(num_casillas_col):
        grid[fila].append(0)

posPlayer = []  # Creamos matriz 7x7 para las posiciones del personaje
for fila in range(num_casillas_fil):
    posPlayer.append([])
    valorY = MARGEN + (ALTO / 2) + (ALTO + MARGEN) * fila
    for columna in range(num_casillas_col):
        valorX = MARGEN + (LARGO / 2) + (LARGO + MARGEN) * columna
        valor = (valorY, valorX)
        posPlayer[fila].append(valor)


def DrawScene():
    reloj.tick(40)
    pantalla.fill(NEGRO)
    # Creamos el escenario con la matriz creada anteriormente
    for fila in range(num_casillas_fil):
        for columna in range(num_casillas_col):
            color = BLANCO
            pygame.draw.rect(pantalla, color, [
                             (MARGEN+LARGO) * columna + MARGEN, (MARGEN+ALTO)
                             * fila + MARGEN, LARGO, ALTO])


def DrawMove(key, pos, x, y):
    DrawScene()
    # Creamos la subimagen con su respectivo Sprite según el pos
    personaje.recImagen.center = (x, y)
    pantalla.blit(personaje.imagen, personaje.recImagen)
    pygame.display.flip()


def moving(key, posInicio, posFinal):
    velocidad = 6   # Controla la velocidad de movimiento del personaje

    if key == "LEFT":
        pos = 4     # Primera Posición del Sprite moviéndose a la izq
        while posInicio[1] > posFinal[1]:  # Solo se toma en cuenta [1] -> col
            posInicio[1] -= velocidad
            pos = personaje.get_frame(key, pos)  # Retorna el pos del sgt Sprite
            DrawMove(key, pos, posInicio[1], posInicio[0])
            # PosInicio[1] son las columnas que corresponde a X en un rectángulo
            # PosInicio[0] son las filas que corresponde a Y en un rectángulo
    elif key == "RIGHT":
        pos = 8
        while posInicio[1] < posFinal[1]:
            posInicio[1] += velocidad
            pos = personaje.get_frame(key, pos)  # Retorna el pos del sgt Sprite
            DrawMove(key, pos, posInicio[1], posInicio[0])
    elif key == "UP":
        pos = 12
        while posInicio[0] > posFinal[0]:
            posInicio[0] -= velocidad
            pos = personaje.get_frame(key, pos)  # Retorna el pos del sgt Sprite
            DrawMove(key, pos, posInicio[1], posInicio[0])
    elif key == "DOWN":
        pos = 0
        while posInicio[0] < posFinal[0]:
            posInicio[0] += velocidad
            pos = personaje.get_frame(key, pos)  # Retorna el pos del sgt Sprite
            DrawMove(key, pos, posInicio[1], posInicio[0])


# PROGRAMA PRINCIPAL
posX = 0    # Inicializamos la posición del personaje
posY = 0    # posX -> posicion en columnas | posY -> posicion en filas
# Instanciamos un objeto de la clase Player
personaje = Player.Player('kate.png', 4, 4, posPlayer[posX][posY])

pygame.init()  # Iniciamos Pygame
pantalla = pygame.display.set_mode(DIMENSIONES)
pygame.display.set_caption("CRASH BASH")
reloj = pygame.time.Clock()

while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True
        if evento.type == pygame.KEYDOWN:
            posInicio = list(posPlayer[posX][posY])  # Guardamos la pos actual
            if evento.key == pygame.K_LEFT:
                posY -= 1
                key = "LEFT"
            if evento.key == pygame.K_RIGHT:
                posY += 1
                key = "RIGHT"
            if evento.key == pygame.K_UP:
                posX -= 1
                key = "UP"
            if evento.key == pygame.K_DOWN:
                posX += 1
                key = "DOWN"

            if posY < 0:
                posY = 0
            if posX < 0:
                posX = 0
            if posY > num_casillas_col - 1:
                posY = num_casillas_col - 1
            if posX > num_casillas_fil - 1:
                posX = num_casillas_fil - 1

            posFinal = list(posPlayer[posX][posY])  # Guardamos la sgt pos
            moving(key, posInicio, posFinal)

    DrawScene()
    pantalla.blit(personaje.imagen, personaje.recImagen)
    pygame.display.flip()

pygame.quit()
