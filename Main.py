# -*- coding: utf-8 -*-
import pygame
import player

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

hecho = False

LARGO = 60
ALTO = 60
MARGEN = 10

grid = []
for fila in range(7):
    grid.append([])
    for columna in range(7):
        grid[fila].append(0)

pygame.init()

dimensiones = (500,500)
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("CRASH BASH")
reloj = pygame.time.Clock()
velocidad = 7
personaje = player.Kate((0, 0), 7)


while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            hecho = True

    pantalla.fill(NEGRO)

    for fila in range(7):
        for columna in range(7):
            color = BLANCO
            pygame.draw.rect(pantalla, color,[(MARGEN+LARGO) * columna + MARGEN,(MARGEN+ALTO) * fila + MARGEN,LARGO,ALTO] )

    personaje.handle_event(evento)
    pantalla.blit(personaje.image, personaje.rect)

    pygame.display.flip()
    reloj.tick(40)

pygame.quit()
