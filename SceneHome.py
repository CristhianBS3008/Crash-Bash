import pygame
import Scene

class SceneHome(Scene.Scene):
    """Escena inicial del juego, esta es la primera que se carga cuando inicia"""

    def __init__(self, director):
        Scene.Scene.__init__(self, director)
        self.pantalla = director.screen

        self.NEGRO = (0, 0, 0)
        self.BLANCO = (255, 255, 255)

        self.LARGO = 60
        self.ALTO = 60
        self.MARGEN = 10

        self.grid = []
        for fila in range(7):
            self.grid.append([])
            for columna in range(7):
                self.grid[fila].append(0)

    def on_update(self):
        pass

    def on_event(self):
        pass

    def on_draw(self, screen):
        self.pantalla.fill(self.NEGRO)

        for fila in range(7):
            for columna in range(7):
                color = self.BLANCO
                pygame.draw.rect(self.pantalla, color,[(self.MARGEN+self.LARGO) * columna + self.MARGEN,(self.MARGEN+self.ALTO) * fila + self.MARGEN,self.LARGO,self.ALTO] )
