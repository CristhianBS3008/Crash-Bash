import pygame

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


while not hecho:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            print("El usuario solicito salir.")
            hecho = True

    pantalla.fill(NEGRO)

    for fila in range(7):
        for columna in range(7):
            color = BLANCO
            pygame.draw.rect(pantalla, color,[(MARGEN+LARGO) * columna + MARGEN,(MARGEN+ALTO) * fila + MARGEN,LARGO,ALTO] )

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
