# -*- coding: utf-8 -*-
import pygame
import Director
import SceneHome

def main():
    director = Director.Director()
    scene = SceneHome.SceneHome(director)
    director.change_scene(scene)
    director.loop()
    pygame.quit()

if __name__ == '__main__':
    pygame.init()
    main()
