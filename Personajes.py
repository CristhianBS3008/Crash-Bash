# -*- coding: utf-8 -*-
import pygame

class Personaje(pygame.sprite.Sprite):
    def __init__(self, fileName, nRows, nCols, position, velocidad):
        self.velocidad = velocidad
        self.sheet = pygame.image.load(fileName)
        playerWidth = self.sheet.get_size()[0]/nCols
        playerHeight = self.sheet.get_size()[1]/nRows
        playerRects = []
        for i in range(nRows):
            for j in range(nCols):
                playerRects.append((j*playerWidth,i*playerHeight, playerWidth, playerHeight))

        self.sheet.set_clip(pygame.Rect(0, 0, 52, 76))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.left_states = { 0: playerRects[4], 1: playerRects[5], 2: playerRects[7] }
        self.right_states = { 0: playerRects[8], 1: playerRects[9], 2: playerRects[11] }
        self.up_states = { 0: playerRects[12], 1: playerRects[13], 2: playerRects[15] }
        self.down_states = { 0: playerRects[0], 1: playerRects[1], 2: playerRects[3] }

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction):
        if direction == 'left':
            self.clip(self.left_states)
            self.rect.x -= self.velocidad
        if direction == 'right':
            self.clip(self.right_states)
            self.rect.x += self.velocidad
        if direction == 'up':
            self.clip(self.up_states)
            self.rect.y -= self.velocidad
        if direction == 'down':
            self.clip(self.down_states)
            self.rect.y += self.velocidad

        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])
        if direction == 'stand_up':
            self.clip(self.up_states[0])
        if direction == 'stand_down':
            self.clip(self.down_states[0])

        self.image = self.sheet.subsurface(self.sheet.get_clip())

    def handle_event(self, event):

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                self.update('left')
            if event.key == pygame.K_RIGHT:
                self.update('right')
            if event.key == pygame.K_UP:
                self.update('up')
            if event.key == pygame.K_DOWN:
                self.update('down')

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                self.update('stand_left')
            if event.key == pygame.K_RIGHT:
                self.update('stand_right')
            if event.key == pygame.K_UP:
                self.update('stand_up')
            if event.key == pygame.K_DOWN:
                self.update('stand_down')
