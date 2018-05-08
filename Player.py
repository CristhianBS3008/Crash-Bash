import pygame


class Player():
    def __init__(self, fileName, nRows, nCols, posicion):
        # (Nombre del Archivo, Filas del SPrite, Columnas del Sprite, posición)
        self.pos = 0    # Posición inicial en Sprite "0"
        self.imgFuente = pygame.image.load(fileName)
        playerWidth = self.imgFuente.get_size()[0]/nRows
        playerHeight = self.imgFuente.get_size()[1]/nCols

        self.playerRects = []  # Posiciones exactas para recortar el SPrite
        for i in range(4):
            for j in range(4):
                self.playerRects.append((j*playerWidth, i*playerHeight, playerWidth, playerHeight))

        self.imagen = self.imgFuente.subsurface(self.playerRects[self.pos])
        # Estableciendo el centro de un rectángulo como posición de la imagen
        self.recImagen = self.imagen.get_rect()
        self.recImagen.center = posicion

    def cut_image(self, pos):
        self.pos = pos
        self.imagen = self.imgFuente.subsurface(self.playerRects[self.pos])
        self.recImagen = self.imagen.get_rect()

    def get_frame(self, key, pos):
        if key == "DOWN":
            self.cut_image(pos)
            self.pos += 1
            if self.pos == 3:
                self.pos = 0
        if key == "LEFT":
            self.pos = pos
            self.cut_image(pos)
            self.pos += 1
            if self.pos == 7:
                self.pos = 4
        if key == "RIGHT":
            self.cut_image(pos)
            self.pos += 1
            if self.pos == 11:
                self.pos = 8
        if key == "UP":
            self.cut_image(pos)
            self.pos += 1
            if self.pos == 15:
                self.pos = 12

        return self.pos
