# -*- encoding: utf-8 -*-
import pygame
import sys

class Director:

    def __init__(self):
        DIMENSIONES = (500, 500)
        self.screen = pygame.display.set_mode(DIMENSIONES)
        pygame.display.set_caption("CRASH BASH")
        self.scene = None
        self.quit_flag = False                                                   #Bandera que nos indica si queremos salir
        self.clock = pygame.time.Clock()

    def loop(self):
        "Pone en funcionamiento el juego."

        while not self.quit_flag:
            time = self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()

            # detecta eventos
            #self.scene.on_event()

            # actualiza la escena
            #self.scene.on_update()

            # dibuja la pantalla
            self.scene.on_draw(self.screen)
            pygame.display.flip()

    def change_scene(self, scene):
        "Altera la escena actual."
        self.scene = scene

    def quit(self):                                                             #llamando a este método, saldrá del método loop
        self.quit_flag = True
